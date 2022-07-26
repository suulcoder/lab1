/** Grammar from my_class files */
grammar YAPL;

/*
 * Parser Rules
 */

program             : (my_class ';')+ ;

my_class            : 'class' TYPE ('inherits' TYPE)? '{' (feature ';')+ '}' ;

feature             : (ID '(' ( formal ','? )* ')' ':' TYPE '{' expr '}')                       # MethodFeature
                    |  ID ':' TYPE ('<-' expr )?                                                # DeclarationFeature
                    ;

formal              : ID ':' TYPE ;

expr                : ID '<-' expr                                                              # DeclarationExpr
                    | expr '(' (expr ','?)+ ')'                                                 # FunctionExpr
                    | expr  ('@' TYPE)?  '.' ID '(' expr (',' expr)* ')'                        # MethodExpr
                    | 'if' expr 'then' expr 'else' expr 'fi'                                    # ifelseExpr
                    | 'while' expr 'loop' expr 'pool'                                           # whileExpr
                    | '{' (expr ';')+ '}'                                                       # BracketsExpr
                    | 'let' ID ':' TYPE ('<-' expr)? (',' ID ':' TYPE  '<-' expr )* 'in' expr   # LetExpr
                    | 'new' TYPE                                                                # InstanceExpr
                    | 'isvoID' expr                                                             # voidExpr
                    | expr '+' expr                                                             # sumExpr
                    | expr '-' expr                                                             # minusExpr
                    | expr '*' expr                                                             # timesExpr
                    | expr '/' expr                                                             # divideExpr
                    | '~' expr                                                                  # negateExpr
                    | expr '<' expr                                                             # lessThanExpr
                    | expr '<=' expr                                                            # lessThanEqualExpr
                    | expr '=' expr                                                             # equalExpr
                    | 'not' expr                                                                # notExpr
                    | '(' expr ')'                                                              # parensExpr
                    | ID                                                                        # idExpr
                    | INT                                                                       # intExpr
                    | STRING                                                                    # stringExpr
                    | 'true'                                                                    # trueExpr
                    | 'false'                                                                   # falseExpr
                    ;

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

