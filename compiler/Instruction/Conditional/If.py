from Abstract.Instruction import *
from Abstract.Return import Type

class If(Instruction):

    def __init__(self, condition, instructions, line, column, elseSt = None):
        Instruction.__init__(self, line, column)
        self.condition = condition
        self.instructions = instructions
        self.elseSt = elseSt