from Abstract.Instruction import *
from Abstract.Return import *
from Symbol.Environment import *

class Statement(Instruction):

    def __init__(self, instructions, line, column):
        Instruction.__init__(self, line, column)
        self.instructions = instructions
    
    def compile(self, environment):
        for ins in self.instructions:
            ret = ins.compile(environment)
            if ret != None:
                return ret