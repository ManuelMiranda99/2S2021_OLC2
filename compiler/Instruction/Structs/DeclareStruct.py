from Abstract.Instruction import *

class DeclareStruct(Instruction):

    def __init__(self, id, type, line, column):
        Instruction.__init__(self, line, column)
        self.id = id
        self.type = type
    