from Abstract.Instruction import *

class Function(Instruction):
    def __init__(self, id, params, instr, line, column):
        Instruction.__init__(self, line, column)
        self.id = id
        self.params = params
        self.instr = instr
    
    def execute(self, environment):
        try:
            environment.saveFunc(self.id, self)
        except:
            print("Error al guardar funcion")