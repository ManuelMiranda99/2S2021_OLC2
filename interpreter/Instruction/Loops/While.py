from Abstract.Instruction import *
from Abstract.Return import *

class While(Instruction):

    def __init__(self, condition, instr, line, column):
        Instruction.__init__(self, line, column)
        self.cond = condition
        self.instr = instr
    
    def execute(self, environment):
        cond = self.cond.execute(environment)
        if cond.type != Type.BOOLEAN:
            print("La condicion no es booleana")
            return
        while cond.value:
            element = self.instr.execute(environment)
            cond = self.cond.execute(environment)
            if cond.type != Type.BOOLEAN:
                print("La condicion no es booleana")
                return