/* A Bison parser, made by GNU Bison 3.8.2.  */

/* Bison interface for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015, 2018-2021 Free Software Foundation,
   Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* DO NOT RELY ON FEATURES THAT ARE NOT DOCUMENTED in the manual,
   especially those whose name start with YY_ or yy_.  They are
   private implementation details that can be changed or removed.  */

#ifndef YY_LIBPARAM_LIBPARAM_TAB_H_INCLUDED
# define YY_LIBPARAM_LIBPARAM_TAB_H_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int libparamdebug;
#endif

/* Token kinds.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    YYEMPTY = -2,
    YYEOF = 0,                     /* "end of file"  */
    YYerror = 256,                 /* error  */
    YYUNDEF = 257,                 /* "invalid token"  */
    LBRACE = 258,                  /* LBRACE  */
    RBRACE = 259,                  /* RBRACE  */
    SEMI = 260,                    /* SEMI  */
    EQUAL = 261,                   /* EQUAL  */
    TRUE = 262,                    /* TRUE  */
    FALSE = 263,                   /* FALSE  */
    DECINT = 264,                  /* DECINT  */
    HEXINT = 265,                  /* HEXINT  */
    FLOAT = 266,                   /* FLOAT  */
    STRING = 267,                  /* STRING  */
    LBRAK = 268,                   /* LBRAK  */
    RBRAK = 269,                   /* RBRAK  */
    COMMA = 270,                   /* COMMA  */
    QU = 271,                      /* QU  */
    COLON = 272,                   /* COLON  */
    NEWLINE = 273,                 /* NEWLINE  */
    SOURCE = 274,                  /* SOURCE  */
    DOTDOT = 275,                  /* DOTDOT  */
    AS = 276,                      /* AS  */
    INSTANTIATE = 277,             /* INSTANTIATE  */
    TOPOLOGY = 278                 /* TOPOLOGY  */
  };
  typedef enum yytokentype yytoken_kind_t;
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
union YYSTYPE
{
#line 56 "libparam.y"

  double d;
  long i;
  char *s;

  struct lp_block *b;
  struct { struct lp_block **b; int blen; } blocks;

  struct lp_param *p;
  struct { struct lp_param **p; int plen; } params;

  struct lp_list *l;

  struct lp_value *v;

  struct { struct lp_topospec *l; int len; } topo;
  struct lp_inst *inst;

#line 106 "libparam.tab.h"

};
typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE libparamlval;


int libparamparse (void);


#endif /* !YY_LIBPARAM_LIBPARAM_TAB_H_INCLUDED  */
