# Lexical Analysis
tokens = (
    "NUMBER",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIV"
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIV = r'/'

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()

# SYNTACTIC Analysis

def p_init(t):
    'init : suma'
    print("El resultado es: " + str(t[1]))

def p_suma(t):
    '''suma : suma PLUS suma
            | suma MINUS suma
            | mult'''
    if len(t) == 2 : t[0] = t[1]
    elif t[2] == '+' : t[0] = t[1] + t[3]
    elif t[2] == '-' : t[0] = t[1] - t[3]

def p_mult(t):
    '''mult : mult TIMES mult
            | mult DIV mult
            | valo'''
    if len(t) == 2 : t[0] = t[1]
    elif t[2] == '*' : t[0] = t[1] * t[3]
    elif t[2] == '/' : t[0] = t[1] / t[3]

def p_valo(t):
    'valo : NUMBER'
    t[0] = t[1]

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

f = open("./entradaCalc.txt", "r")
input = f.read()
parser.parse(input)