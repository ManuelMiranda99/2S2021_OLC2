from Abstract.Instruction import *

class Function(Instruction):
    def __init__(self, id, params, instr, line, column):
        Instruction.__init__(self, line, column)
        self.id = id
        self.params = params
        self.instr = instr
    