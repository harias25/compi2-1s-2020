import ply.yacc as yacc
from Expresiones.Operacion import Operacion, TIPO_OPERACION
from Expresiones.Primitivo import Primitivo
from Instrucciones.Print import Print

#palabras reservadas
reservadas = {
    'print' : 'IMPRIMIR'
}

#TOKENS
tokens  = [
    'PTCOMA',
    'PARIZQ',
    'PARDER',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'RESTO',
	'DECIMAL',
    'ENTERO'
] + list(reservadas.values())

# Tokens
t_PTCOMA    = r';'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_MAS       = r'\+'
t_MENOS     = r'-'
t_POR       = r'\*'
t_DIVIDIDO  = r'/'
t_RESTO     = r'%'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
     r'[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reservadas.get(t.value.lower(),'ID')    # Check for reserved words
     return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_newline(t):
     r'\n+'
     t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("LEXICO","Error lexico, Caracter "+t.value[0]+" no es valido.",t.lexer.lineno,find_column(t))
    #print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def find_column(token):
    line_start = entrada.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


# Construyendo el analizador léxico
import ply.lex as lex
lexer = lex.lex()

# Asociación de operadores y precedencia
precedence = (
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO','RESTO'),
    ('right','UMENOS'),
)

#********************************************** INICIO DE GRAMATICA  ***********************************

def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

#********************************************** INSTRUCCIONES  ***********************************

def p_instrucciones_lista(t) :
    'instrucciones    : instrucciones instruccion'
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion '
    t[0] = [t[1]]

def p_instruccion(t) :
    '''instruccion      : imprimir_instr 
                        | error '''
    t[0] = t[1]

def p_instruccion_imprimir(t) :
    'imprimir_instr     : IMPRIMIR PARIZQ expresion PARDER PTCOMA'
    t[0] = Print(t[3],t.slice[1].lineno,find_column(t.slice[1]))

def p_expresion(t):
    '''expresion : primitiva 
                 | expresion_unaria
                 | expresion_numerica '''

    t[0] = t[1]

def p_expresion_par(t):
    '''expresion : PARIZQ expresion PARDER '''
    t[0] = t[2]

#********************************************** OPERACIONES ARITMETICAS ***********************************
def p_expresion_numerica(t):
    '''expresion_numerica   :   expresion MAS expresion 
                            |   expresion MENOS expresion 
                            |   expresion POR expresion
                            |   expresion DIVIDIDO expresion
                            |   expresion RESTO expresion'''
                            
    op = Operacion()
    if(t.slice[2].type == 'MAS'):
        op.Operacion(t[1],t[3],TIPO_OPERACION.SUMA,t.slice[2].lineno,1)
    elif(t.slice[2].type == 'MENOS'):
        op.Operacion(t[1],t[3],TIPO_OPERACION.RESTA,t.slice[2].lineno,1)
    elif(t.slice[2].type == 'POR'):
        op.Operacion(t[1],t[3],TIPO_OPERACION.MULTIPLICACION,t.slice[2].lineno,1)
    elif(t.slice[2].type == 'DIVIDIDO'):
        op.Operacion(t[1],t[3],TIPO_OPERACION.DIVISION,t.slice[2].lineno,1) 
    elif(t.slice[2].type == 'RESTO'):
        op.Operacion(t[1],t[3],TIPO_OPERACION.MODULO,t.slice[2].lineno,1)
    t[0] = op

#********************************************** OPERACIONES UNARIAS ***********************************
def p_expresion_unaria(t):
    'expresion_unaria   :   MENOS expresion %prec UMENOS' 
    op = Operacion()
    op.OperacionUnaria(t[2],t.slice[1].lineno,find_column(t.slice[1]))
    t[0] = op

#********************************************** PRIMITIVOS ***********************************
def p_expresion_primitiva(t):
    '''primitiva : ENTERO
                 | DECIMAL '''

    op = Operacion()
    if(t.slice[1].type == 'DECIMAL'):
        op.Primitivo(Primitivo(float(t[1]),t.slice[1].lineno,find_column(t.slice[1])))
    elif(t.slice[1].type == 'ENTERO'):
        op.Primitivo(Primitivo(int(t[1]),t.slice[1].lineno,find_column(t.slice[1])))
    t[0] = op

def p_error(t):
    try:
        print("SINTACTICO","Error sintactico, no se esperaba el valor "+t.value,t.lineno,find_column(t))
    except:
        print("SINTACTICO","Error sintactico",1,1)

parser = yacc.yacc()
entrada = ""
def parse(input) :
    global lexer
    input = input.replace("\r","")
    lexer = lex.lex()
    entrada = input
    return parser.parse(input)