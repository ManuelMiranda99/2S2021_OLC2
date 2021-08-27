from ...Abstract.Instruction import *
from ...Abstract.Return import Type

class If(Instruction):

    def __init__(self, condition, instructions, line, column, elseSt = None):
        Instruction.__init__(self, line, column)
        self.condition = condition
        self.instructions = instructions
        self.elseSt = elseSt
    
    def execute(self, environment):
        cond = self.condition.execute(environment)
        if cond.type != Type.BOOLEAN:
            print("Condición de tipo no boolean")
            return
        if cond.value:
            return self.instructions.execute(environment)
        elif self.elseSt != None:
            return self.elseSt.execute(environment)