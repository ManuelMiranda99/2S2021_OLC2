from Abstract.Instruction import *
from Abstract.Return import *

class While(Instruction):

    def __init__(self, condition, instr, line, column):
        Instruction.__init__(self, line, column)
        self.cond = condition
        self.instr = instr
    