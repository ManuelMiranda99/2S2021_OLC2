from ...Abstract.Instruction import *

class DeclareStruct(Instruction):

    def __init__(self, id, type, line, column):
        Instruction.__init__(self, line, column)
        self.id = id
        self.type = type
    
    def execute(self, environment):
        struct = environment.getStruct(self.type)
        if struct == None:
            print("No existe el type")
            return
        attrs = {}
        for att in struct:
            attrs.update({
                att: 0
            });
        environment.saveVarStruct(self.id, attrs, self.type)