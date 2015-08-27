#ifndef _H_bI
#define _H_bI

#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstdio>
#include <cmath>

#include <direct.h>

using namespace std;

extern int yylex(void);
extern int yyparse(void);
extern char *yytext;
extern int yylineno;
extern void yyerror(const char *msg);
#include "bI.tab.hpp"

#endif //  _H_bI
