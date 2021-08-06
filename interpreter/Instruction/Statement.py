from Abstract.Instruction import *
from Symbol.Environment import *

class Statement(Instruction):

    def __init__(self, instructions, line, column):
        Instruction.__init__(self, line, column)
        self.instructions = instructions
    
    def execute(self, environment):
        newEnv = Environment(environment)
        for ins in self.instructions:
            ins.execute(newEnv)