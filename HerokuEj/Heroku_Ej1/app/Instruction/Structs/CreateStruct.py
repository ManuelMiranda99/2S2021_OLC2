from ...Abstract.Instruction import *

class CreateStruct(Instruction):

    def __init__(self, id, attr, line, column):
        Instruction.__init__(self, line, column)
        self.id = id
        self.attr = attr
    
    def execute(self, environment):
        environment.saveStruct(self.id, self.attr)