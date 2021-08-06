c3d = ""
count = 0

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

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIV')
)

def p_expression(t):
    'expression : e'
    global c3d
    print(c3d)

def p_e_suma(t):
    'e : e PLUS e'
    global count
    global c3d
    c3d += "t" + str(count) + " = " + t[1] + " + " + t[3] + "\n"
    t[0] = "t" + str(count)
    count+=1

def p_e_resta(t):
    'e : e MINUS e'
    global count
    global c3d
    c3d += "t" + str(count) + " = " + t[1] + " - " + t[3] + "\n"
    t[0] = "t" + str(count)
    count+=1

def p_e_mult(t):
    'e : e TIMES e'
    global count
    global c3d
    c3d += "t" + str(count) + " = " + t[1] + " * " + t[3] + "\n"
    t[0] = "t" + str(count)
    count+=1

def p_e_div(t):
    'e : e DIV e'
    global count
    global c3d
    c3d += "t" + str(count) + " = " + t[1] + " / " + t[3] + "\n"
    t[0] = "t" + str(count)
    count+=1

def p_e_valor(t):
    'e : NUMBER'
    t[0] = str(t[1])

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

f = open("./entradaCalc.txt", "r")
input = f.read()
parser.parse(input)

'''
    1 + 1 - 2 * 3 / 2

    t0 = 2 * 3
    t1 = t0 / 2
    t2 = 1 + 1
    t3 = t2 - t1
'''