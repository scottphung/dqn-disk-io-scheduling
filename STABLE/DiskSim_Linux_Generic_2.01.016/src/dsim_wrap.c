#include "disksim_interface.h"
#include <stdlib.h>
#include <string.h>
#include <diskmodel/dm.h>

static struct disksim_interface *iface = NULL;
static double now = 0.0;
static double next_event = -1.0;   /* -1 means nothing scheduled */
static int    done = 0;
static double done_time = 0.0;

/* Safety valve: DiskSim can spin forever in its event loop (e.g. after a request that
   crosses a track boundary). Each pump loop gives up after this many events. */
static long event_limit = 500000;
void dsim_set_event_limit(long n) { event_limit = n; }

static disksim_interface_callback_t pending_fn = NULL;

/* DiskSim -> us: "call fn at time t" */
static void schedule_cb(disksim_interface_callback_t fn, double t, void *ctx)
{ pending_fn = fn; next_event = t; }
static void deschedule_cb(double t, void *ctx) { next_event = -1.0; }

/* DiskSim -> us: request finished */
static void complete_cb(double t, struct disksim_request *r, void *ctx) {
    done = 1;
    done_time = t;
}

int dsim_init(const char *parfile, const char *outfile) {
    now = 0.0; next_event = -1.0; done = 0;
    iface = disksim_interface_initialize(parfile, outfile,
                                         complete_cb, schedule_cb, deschedule_cb,
                                         NULL, 0, NULL);
    return iface ? 0 : -1;
}

/* Submit one request at the current simulated time. */
void dsim_submit(int devno, unsigned long blkno, int sectors, int is_read) {
    static struct disksim_request r;   /* must outlive the call */
    memset(&r, 0, sizeof r);
    r.start = now;
    r.blkno = blkno;
    r.flags = is_read ? DISKSIM_READ : DISKSIM_WRITE;
    r.devno = devno;
    r.bytecount = sectors;   /* in 512-byte sectors, not bytes */
    done = 0;
    disksim_interface_request_arrive(iface, now, &r);
}

/* Advance simulated time until the outstanding request completes.
   Returns completion time, or -1.0 if the event queue ran dry. */
double dsim_run_until_done(void) {
    long n = 0;
    while (!done) {
        if (next_event < 0) return -1.0;
        if (++n > event_limit) return -2.0;   /* hang guard */
        now = next_event;
        next_event = -1.0;
        disksim_interface_internal_event(iface, now, NULL);
    }
    now = done_time;
    return done_time;
}

/* Process every remaining scheduled event (what syssim_driver does after each
   request). Returns the simulated time of the last event processed. */
double dsim_drain(void) {
    long n = 0;
    while (next_event >= 0) {
        if (++n > event_limit) return -2.0;   /* hang guard */
        now = next_event;
        next_event = -1.0;
        disksim_interface_internal_event(iface, now, NULL);
    }
    return now;
}

double dsim_now(void) { return now; }

/* Let simulated time pass with the disk idle (e.g. waiting for the next arrival). */
int dsim_advance_to(double t) {
    long n = 0;
    while (next_event >= 0 && next_event <= t) {
        if (++n > event_limit) return -1;   /* hang guard */
        now = next_event;
        next_event = -1.0;
        disksim_interface_internal_event(iface, now, NULL);
    }
    if (t > now) now = t;
    return 0;
}

void dsim_shutdown(void) {
    if (iface) {
        disksim_interface_shutdown(iface, now);   /* prints stats */
        disksim_free_disksim(iface);              /* closes outfile etc., frees the instance;
                                                     without it every re-init leaks a descriptor */
    }
    iface = NULL;
}

int dsim_get_pos(int devno, struct disksim_disk_observation *out) {
    return disksim_get_disk_state(iface, devno, now, out);
}

/* ---- geometry helpers so Python can build queue features ---- */

/* Fills cyls/surfaces/sectors_total (dm_sectors) for disk devno. 0 on success. */
int dsim_geometry(int devno, int *cyls, int *surfaces, int *sectors) {
    struct dm_disk_if *d = iface ? disksim_getdiskmodel(iface, devno) : NULL;
    if (!d) return -1;
    *cyls = d->dm_cyls; *surfaces = d->dm_surfaces; *sectors = d->dm_sectors;
    return 0;
}

/* Logical block -> cylinder/head/sector. 0 on success, -1 if lbn doesn't exist. */
int dsim_lbn_to_pbn(int devno, int lbn, int *cyl, int *head, int *sector) {
    struct dm_disk_if *d = iface ? disksim_getdiskmodel(iface, devno) : NULL;
    struct dm_pbn p;
    int remap = 0;
    if (!d) return -1;
    if (d->layout->dm_translate_ltop(d, lbn, MAP_FULL, &p, &remap) == DM_NX) return -1;
    *cyl = p.cyl; *head = p.head; *sector = p.sector;
    return 0;
}
