grammar gramatica;

options {
  language = Python3;
}

NEWLINE: '\r'? '\n' ; 
NUMERO: '-'?[0-9]+'.'?[0-9]?;
ID: [a-zA-Z0-9];           
WS: [ \t\r\n]+ -> skip;
IMPORT: 'import';
DEF: 'def';
CLASS: 'class';
IF: 'if';
ELSE: 'else';
FOR: 'for';
IN: 'in';
RANGE: 'range';
SELF: 'self';
WHILE: 'while';
TRY: 'try';
EXCEPT: 'except';
RETURN: 'return';
BREAK: 'break';
NEXT: 'next';
INPUT: 'input';
PRINT: 'print';
INT: 'int';
FLOAT: 'float';
BOOLEAN: 'True' | 'False';
STR: 'str';
POW: 'pow';
MATHSQRT: 'mathsqrt';
AND: 'and';
OR: 'or';
NOT: 'not';
ELIF: 'elif';
SUMA: '+';
ASIGNACION: '=';
RESTA: '-';
DIVISION: '/';
MULTIPLICACION: '*';
IGUAL: '==';
DIFERENTE: '!=';
MAYORQUE: '>';
MENORQUE: '<';
MENORIGUAL: '>=';
MAYORIGUAL: '<=';
PUNTO: '.';
COMA: ',';
DOSPUNTOS: ':';
PUNTOCOMA: ';';
COMILLASIMPLE: '\'';
COMILLADOBLE: '"';
PARENTESIS_A: '(';
PARENTESIS_C: ')';
LLAVE_C: '}';
LLAVE_A: '{';
CORCHETE_A: '[';
CORCHETE_C: ']';
MASMAS: '++';
MENOSMENOS: '--';
POTENCIA:'^';
MODULO:'%';


start: sentencias+ ;

sentencias      : printf
                | asignacion
                | condicional
                | ciclo_while
                | expresion
                | funcion
                | llamafuncion 
                | ciclo_for
                | v_input 
                | casteo 
                | graficas 
                | importss 
                | func
                | matriz_operaciones
                | regresion_lineal
                | k_means
                | dbscan
		| mlp
                | NEWLINE
                ;

asignacion: ID ASIGNACION var_casteo? PARENTESIS_A? (expresion | v_input | matriz_operaciones | arange) PARENTESIS_C?
          | ID ASIGNACION ID PARENTESIS_A (parametro | expresion | matriz_operaciones )? PARENTESIS_C 
          ;

v_input: var_casteo? PARENTESIS_A? INPUT PARENTESIS_A expresion? PARENTESIS_C PARENTESIS_C?;

printf: PRINT PARENTESIS_A (expresion  | matriz_operaciones)? PARENTESIS_C;

var_casteo: STR
          | INT
          | FLOAT
          | BOOLEAN
          ;

casteo: var_casteo PARENTESIS_A expresion PARENTESIS_C;

cadena  : COMILLASIMPLE ID+ COMILLASIMPLE
        | COMILLADOBLE ID+ COMILLADOBLE 
        | COMILLADOBLE NUMERO COMILLADOBLE  
        | COMILLASIMPLE NUMERO COMILLASIMPLE 
        ;

funcion: DEF ID PARENTESIS_A parametro? PARENTESIS_C DOSPUNTOS sentencias v_return? sentencias
       | DEF ID PARENTESIS_A PARENTESIS_C DOSPUNTOS sentencias v_return? sentencias
       | DEF ID PARENTESIS_A parametro? PARENTESIS_C DOSPUNTOS sentencias
       | DEF ID PARENTESIS_A PARENTESIS_C DOSPUNTOS sentencias
       ;

v_return: RETURN expresion;

llamafuncion: ID PARENTESIS_A parametro? PARENTESIS_C;

condicional: IF PARENTESIS_A? (parametro|expresion) PARENTESIS_C? DOSPUNTOS sentencias elifBlock? condicional_else? ;

elifBlock:condicional_elif+;

condicional_elif: ELIF PARENTESIS_A? (parametro|expresion) PARENTESIS_C? DOSPUNTOS sentencias ;

condicional_else: ELSE DOSPUNTOS sentencias ;

ciclo_for: FOR ID IN RANGE PARENTESIS_A expresion COMA? expresion? COMA? expresion? PARENTESIS_C DOSPUNTOS sentencias v_return?
          | FOR ID IN expresion DOSPUNTOS sentencias v_return?
          ;

ciclo_while: WHILE PARENTESIS_A? expresion PARENTESIS_C? DOSPUNTOS sentencias+;

parametro: ID COMA? parametro?;

func : ('math'|'np') PUNTO ('sin' | 'cos' | 'tan' | 'arcsin' | 'arccos' | 'arctan') PARENTESIS_A expresion PARENTESIS_C ;

expresion: expresion (SUMA | RESTA | MULTIPLICACION | DIVISION | POTENCIA | MODULO) termino
         | expresion ( MAYORQUE | MENORQUE | MENORIGUAL | MAYORIGUAL | DIFERENTE | IGUAL | ASIGNACION ) termino
         | expresion (OR | AND )termino
         | termino
         | func
         ;

matriz_operaciones: matriz SUMA? matriz?
                  | matriz RESTA matriz
                  | matriz MULTIPLICACION matriz
                  | 'inv' PARENTESIS_A matriz PARENTESIS_C
                  | 'trans' PARENTESIS_A matriz PARENTESIS_C
                  ;

matriz: CORCHETE_A fila_matriz (COMA fila_matriz)* CORCHETE_C;

fila_matriz: CORCHETE_A expresion (COMA expresion)* CORCHETE_C;

importss: IMPORT ('math' | 'matplotlib.pyplot' | 'numpy as np');

termino: NUMERO
       | ID+
       | BOOLEAN
       | cadena
       | lista
       | arreglo
       ;

lista: PARENTESIS_A (NUMERO | ID+ | BOOLEAN | cadena | COMA)+ PARENTESIS_C;

arreglo: CORCHETE_A (NUMERO | ID+ | BOOLEAN | cadena | COMA | arreglo)+ CORCHETE_C;

graficas: ('plot'|'scatter'|'fill_between'|'bar'|'barh'|'hist') PARENTESIS_A x=expresion ',' y=expresion PARENTESIS_C
        | ('pie'|'boxplot') PARENTESIS_A x=expresion  PARENTESIS_C
        | ('grafsen'|'grafcos'|'graftan') PARENTESIS_A (arange|ID+) COMA func PARENTESIS_C
        ;

arange  : 'linspace' PARENTESIS_A expresion COMA expresion '*' 'np' PUNTO 'pi' COMA expresion PARENTESIS_C
        ;

regresion_lineal: 'regresion_lineal' PARENTESIS_A expresion COMA expresion PARENTESIS_C;

k_means: 'kmeans' PARENTESIS_A arreglo COMA arreglo COMA NUMERO PARENTESIS_C;

dbscan: 'dbscan' PARENTESIS_A arreglo COMA arreglo COMA NUMERO COMA NUMERO PARENTESIS_C;

mlp: 'mlp' PARENTESIS_A NUMERO COMA NUMERO COMA NUMERO COMA NUMERO COMA arreglo COMA arreglo PARENTESIS_C;



