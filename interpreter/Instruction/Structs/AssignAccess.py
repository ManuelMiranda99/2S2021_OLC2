from Abstract.Instruction import *

class AssignAccess(Instruction):

    def __init__(self, id, access, expr, line, column):
        Instruction.__init__(self, line, column)
        self.id = id
        self.access = access
        self.expr = expr

    def execute(self, environment):
        value = self.expr.execute(environment)
        symbol = environment.getVar(self.id)
        symbol.attributes[self.access] = value