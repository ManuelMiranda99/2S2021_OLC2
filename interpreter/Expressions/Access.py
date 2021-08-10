from Abstract.Expression import *
from Abstract.Return import *

class Access(Expression):

    def __init__(self, id, line, column):
        Expression.__init__(self, line, column)
        self.id = id

    def execute(self, environment):
        value = environment.getVar(self.id)
        if value == None:
            print("Error, no existe la variable")
            return
        return Return(value.value, value.type)