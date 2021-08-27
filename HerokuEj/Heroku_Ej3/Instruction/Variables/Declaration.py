from Abstract.Instruction import *
from Abstract.Return import *

class Declaration(Instruction):

    def __init__(self, id, value, line, column):
        Instruction.__init__(self, line, column)
        self.id = id
        self.value = value
    
    def execute(self, environment):
        value = self.value.execute(environment)
        if value.type == Type.STRUCT: 
            environment.saveVarStruct(self.id, value.value, value.auxType)
        else:
            environment.saveVar(self.id, value.value, value.type)