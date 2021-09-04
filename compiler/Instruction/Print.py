from Abstract.Instruction import *
from Abstract.Return import *
from Symbol.Generator import Generator
import uuid

class Print(Instruction):

    def __init__(self, value, line, column, newLine = False):
        Instruction.__init__(self, line, column)
        self.value = value
        self.newLine = newLine
    
    def compile(self, env):
        val = self.value.compile(env)
        genAux = Generator()
        generator = genAux.getInstance()

        if(val.type == Type.INT):
            generator.addPrint("d", val.value)
        else:
            print("POR HACER")