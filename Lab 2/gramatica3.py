tokens = (
    "NUMBER",
    "U",
    "DTOKEN",
    "L",
    "RTOKEN",
    "PARDER",
    "PARIZQ",
    "COMMA",
    "SEMICOLON"
)

t_U = r'u'
t_DTOKEN = r'd'
t_L = r'l'
t_RTOKEN = r'r'
t_PARDER = r'\('
t_PARIZQ = r'\)'
t_COMMA = r','
t_SEMICOLON = r';'

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

def p_s(t):
    'S : R'
    t[0] = t[1]
    print("(x: " + str(t[0][0]) + ", y: " + str(t[0][1]) + ")")

def p_r(t):
    'R : COSA_RANDOM PI mov'
    t[0] = [t[2][0], t[2][1]]

def p_cosa_random(t):
    'COSA_RANDOM : U'
    t[0] = "Hola, estoy en la pila"

def p_pi(t):
    'PI : PARDER NUMBER COMMA NUMBER PARIZQ'
    t[0] = [t[2], t[4]]

def p_mov(t):
    '''mov : mov SEMICOLON d
           | d'''
    if len(t) == 2 :
        print(t[-2])
        t[0] = [t[-1][0] + t[1][0], t[-1][1] + t[1][1]]

    else :
        t[0] = [t[1][0] + t[3][0], t[1][1] + t[3][1]]


def p_d(t):
    '''d :   U
        |    DTOKEN
        |    RTOKEN
        |    L'''
    if t[1] == 'u' : t[0] = [0, 1]
    elif t[1] == 'd' : t[0] = [0, -1]
    elif t[1] == 'r' : t[0] = [1, 0]
    elif t[1] == 'l' : t[0] = [-1, 0]

def p_error(t):
    print("Error sintáctico en '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

f = open("./entradaPos.txt", "r")
input = f.read()
parser.parse(input)