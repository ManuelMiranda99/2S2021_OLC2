# IMPORTS
# Instructions
from Instruction.Statement import *
from Instruction.Print import *
from Instruction.Conditional.If import *

# Expressions
from Expressions.Arithmetic import *
from Expressions.Literal import *
from Expressions.Relational import *

# LEXICAL ANALYSIS
tokens = (
    # NATIVE VALUES
    "INTLITERAL",
    "FLOATLITERAL",
    "STRINGLITERAL",

    # SYMBOLS
    # GENERAL SYMBOLS
    "EQUALS",
    "SEMICOLON",
    "LEPAR",
    "RIPAR",

    # ARITHMETIC SYMBOLS
    "PLUS",
    "MINUS",
    "TIMES",
    "DIV",

    # LOGICAL SYMBOLS
    "AND",
    "OR",
    "NOT",

    # RELATIONAL SYMBOLS
    "GREATER",
    "LESS",
    "GREATEREQUAL",
    "LESSEQUAL",
    "EQUALSEQUALS",
    "DISTINT",

    # RESERVED WORDS
    # GENERAL RW
    "END",
    "TRUE",
    "FALSE",

    # IFELSE SENTENCE
    "IF",
    "ELSE",
    "ELSEIF",

    # NATIVES
    "PRINTLN",
    "PRINT",
)

# TOKENS

# SYMBOLS
# GENERAL SYMBOLS
t_EQUALS                = r'='
t_SEMICOLON             = r';'
t_LEPAR                 = r'\('
t_RIPAR                 = r'\)'

# ARITHMETIC SYMBOLS
t_PLUS                  = r'\+'
t_MINUS                 = r'-'
t_TIMES                 = r'\*'
t_DIV                   = r'/'

# LOGICAL SYMBOLS
t_AND                   = r'&&'
t_OR                    = r'\|\|'
t_NOT                   = r'!'

# RELATIONAL SYMBOLS
t_GREATER               = r'>'
t_LESS                  = r'<'
t_GREATEREQUAL          = r'>='
t_LESSEQUAL             = r'<='
t_EQUALSEQUALS          = r'=='
t_DISTINT               = r'!='

# RESERVED WORDS
# GENERAL RW
t_END                   = r'end'
t_TRUE                  = r'true'
t_FALSE                 = r'false'

# IFELSE SENTENCE
t_IF                    = r'if'
t_ELSE                  = r'else'
t_ELSEIF                = r'elseif'

# NATIVES
t_PRINTLN               = r'println'
t_PRINT                 = r'print'

def t_FLOATLITERAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("ERROR IN PARSE TO FLOAT")
        t.value = 0
    return t

def t_INTLITERAL(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("ERROR IN PARSE TO INT")
        t.value = 0
    return t

def t_STRINGLITERAL(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

t_ignore = " \t"

def t_MLCOMMENT(t):
    r'\#=(.|\n)*?=\#'
    t.lexer.lineno += t.value.count("\n")

def t_OLCOMMENT(t):
    r'\#.*\n'
    t.lexer.lineno += 1

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lexer = lex.lex()

precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'EQUALSEQUALS', 'DISTINT'),
    ('left', 'GREATEREQUAL', 'LESSEQUAL', 'GREATER', 'LESS'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIV'),
    ('right', 'NOT'),
    ('right', 'UMINUS'),
)

# SYNTACTIC ANALYSIS

def p_start(t):
    'start : instructions'
    t[0] = t[1]
    return t[0]

def p_instructions(t):
    '''instructions : instructions instruction
                    | instruction'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[2])
        t[0] = t[1]

def p_instruction(t):
    '''instruction  : printST SEMICOLON
                    | ifST SEMICOLON'''
    t[0] = t[1]

# STATEMENT
def p_statement(t):
    '''statement : instructions'''
    t[0] = Statement(t[1], t.lineno(1), t.lexpos(0))

# PRINT ST
def p_printlnST(t):
    'printST  : PRINTLN LEPAR expression RIPAR'
    t[0] = Print(t[3], t.lineno(1), t.lexpos(0), True)

def p_printST(t):
    'printST  : PRINT LEPAR expression RIPAR'
    t[0] = Print(t[3], t.lineno(1), t.lexpos(0))

# IFST
def p_ifST(t):
    '''ifST : IF expression statement END
            | IF expression statement ELSE statement END
            | IF expression statement elseIfList END'''
    if len(t) == 5:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0))
    elif len(t) == 7:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0), t[5])
    elif len(t) == 6:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0), t[4])

def p_elseIfList(t):
    '''elseIfList   : ELSEIF expression statement
                    | ELSEIF expression statement ELSE statement
                    | ELSEIF expression statement elseIfList'''
    if len(t) == 4:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0))
    elif len(t) == 6:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0), t[5])
    elif len(t) == 5:
        t[0] = If(t[2], t[3], t.lineno(1), t.lexpos(0), t[4])

def p_expression(t):
    '''expression   : MINUS expression %prec UMINUS
                    | NOT expression %prec UMINUS
                    
                    | expression PLUS expression
                    | expression MINUS expression
                    | expression TIMES expression
                    | expression DIV expression

                    | expression GREATER expression
                    | expression LESS expression
                    | expression GREATEREQUAL expression
                    | expression LESSEQUAL expression
                    | expression EQUALSEQUALS expression
                    | expression DISTINT expression
                    
                    | expression OR expression
                    | expression AND expression
                    | finalExp'''
    if len(t) == 2: t[0] = t[1]
    elif len(t) == 3:
        # UMINUS
        t[0] = Arithmetic(Literal(0, Type.INT, t.lineno(1), t.lexpos(0)), t[2], ArithmeticOption.MINUS, t.lineno(1), t.lexpos(0))
    else:
        if t[2] == "+":
            t[0] = Arithmetic(t[1], t[3], ArithmeticOption.PLUS, t.lineno(2), t.lexpos(0))
        elif t[2] == "-":
            t[0] = Arithmetic(t[1], t[3], ArithmeticOption.MINUS, t.lineno(2), t.lexpos(0))
        elif t[2] == "*":
            t[0] = Arithmetic(t[1], t[3], ArithmeticOption.TIMES, t.lineno(2), t.lexpos(0))
        elif t[2] == "/":
            t[0] = Arithmetic(t[1], t[3], ArithmeticOption.DIV, t.lineno(2), t.lexpos(0))
        elif t[2] == ">":
            t[0] = Relational(t[1], t[3], RelationalOption.GREATER, t.lineno(2), t.lexpos(2))
        elif t[2] == "<":
            t[0] = Relational(t[1], t[3], RelationalOption.LESS, t.lineno(2), t.lexpos(2))
        elif t[2] == ">=":
            t[0] = Relational(t[1], t[3], RelationalOption.GREATEREQUAL, t.lineno(2), t.lexpos(2))
        elif t[2] == "<=":
            t[0] = Relational(t[1], t[3], RelationalOption.LESSEQUAL, t.lineno(2), t.lexpos(2))
        elif t[2] == "==":
            t[0] = Relational(t[1], t[3], RelationalOption.EQUALSEQUALS, t.lineno(2), t.lexpos(2))
        elif t[2] == "!=":
            t[0] = Relational(t[1], t[3], RelationalOption.DISTINT, t.lineno(2), t.lexpos(2))
        elif t[2] == "||":
            # OR
            t[0] = 0
        elif t[2] == "&&":
            # AND
            t[0] = 0

def p_finalExp(t):
    '''finalExp : LEPAR expression RIPAR
                | INTLITERAL
                | FLOATLITERAL
                | STRINGLITERAL
                | TRUE
                | FALSE'''
    if len(t) == 2:
        if isinstance(t[1], int):
            t[0] = Literal(int(t[1]), Type.INT, t.lineno(1), t.lexpos(0))
        elif isinstance(t[1], float):
            t[0] = Literal(float(t[1]), Type.FLOAT, t.lineno(1), t.lexpos(0))
        elif isinstance(t[1], str):
            value = str(t[1])
            if "true" in value:
                t[0] = Literal(True, Type.BOOLEAN, t.lineno(1), t.lexpos(0))
            elif "false" in value:
                t[0] = Literal(False, Type.BOOLEAN, t.lineno(1), t.lexpos(0))
            else:
                t[0] = Literal(str(t[1]), Type.STRING, t.lineno(1), t.lexpos(0))
    else:
        t[0] = t[2]

def p_error(t):
    print(t)
    print("Syntactic error in '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()

def parse():
    f = open("./input.jl", "r")
    input = f.read()
    return parser.parse(input)