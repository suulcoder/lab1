/** Grammar from my_class files */
grammar YAPL;

/*
 * Parser Rules
 */

program             : (my_class ';')+ ;

my_class            : 'class' TYPE ('inherits' TYPE)? '{' (feature ';')+ '}' ;

feature             : (ID '(' ( formal ','? )* ')' ':' TYPE '{' expr '}')                       # MethodFeature
                    |  ID ':' TYPE ('<-' expr )?                                                # AtributeFeature
                    ;

formal              : ID ':' TYPE ;

expr                : call '<-' (expr | call)                                                   # DeclarationExpr
                    | call '(' (parameter ','?)+ ')'                                            # FunctionExpr
                    | 'if' expr 'then' expr 'else' expr 'fi'                                    # ifelseExpr
                    | 'while' expr 'loop' expr 'pool'                                           # whileExpr
                    | '{' (expr ';')+ '}'                                                       # BracketsExpr
                    | 'let' ID ':' TYPE 'in' expr                                               # LetExpr
                    | 'new' TYPE                                                                # InstanceExpr
                    | 'isvoid' expr                                                             # voidExpr
                    | '(' expr ')'                                                              # parensExpr
                    | expr '*' expr                                                             # timesExpr
                    | expr '/' expr                                                             # divideExpr
                    | expr '+' expr                                                             # sumExpr
                    | expr '-' expr                                                             # minusExpr
                    | '~' expr                                                                  # unaryExpr
                    | expr '<' expr                                                             # lessThanExpr
                    | expr '<=' expr                                                            # lessThanEqualExpr
                    | expr '=' expr                                                             # equalExpr
                    | 'not' expr                                                                # notExpr
                    | call                                                                      # idExpr
                    | INT                                                                       # intExpr
                    | STRING                                                                    # stringExpr
                    | 'true'                                                                    # trueExpr
                    | 'false'                                                                   # falseExpr
                    | 'in_string()'                                                             # inStringExpr
                    | 'in_int()'                                                                # inIntExpr
                    | 'in_bool()'                                                               # inBoolExpr
                    | 'out_string(' (call | STRING) ')'                                         # outStringExpr
                    | 'out_int(' (call | INT) ')'                                               # outIntExpr
                    | 'out_bool(' (call | 'true' | 'false') ')'                                 # outBoolExpr
                    ;

call                : ID ('.' ID)* ;

parameter           : expr | call ;

/*
 * Lexer Rules
 */

STRING              : '"' (ESC | ~ ["\\])* '"' ;
fragment ESC        : '\\' (["\\/bfnrt] | UNICODE) ;
fragment UNICODE    : 'u' HEX HEX HEX HEX ;
fragment HEX        : [0-9a-fA-F] ;
INT                 : '0' | [1-9] [0-9]* ;
TYPE                : [A-Z] ([a-zA-Z0-9_])* ;
ID                  : [a-zA-Z] ([a-zA-Z0-9_])* ;
POINT               : '.' ;
UNKNOWN             : . -> skip ;

LINE_COMMENT
                    :   '--' ~[\r\n]* -> skip
                    ;

MULTILINE_COMMENT
                    : '-*' .*? '*-' -> skip
                    ;

