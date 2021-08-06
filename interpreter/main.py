from grammar import parse
from Symbol.Environment import *

newEnv = Environment(None)
ast = parse()

try:
    for instr in ast:
        instr.execute(newEnv)
except:
    print("Error al ejecutar instrucciones")