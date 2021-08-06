from Abstract.Expression import *
from Abstract.Return import *

class Literal(Expression):

    def __init__(self, value, type, line, column):
        Expression.__init__(self, line, column)
        self.value = value
        self.type = type
    
    def execute(self, environment):
        if self.type == Type.INT:
            return Return(self.value, Type.INT)
        elif self.type == Type.FLOAT:
            return Return(self.value, Type.FLOAT)
        elif self.type == Type.BOOLEAN:
            return Return(self.value, Type.BOOLEAN)
        else:
            return Return(self.value, Type.STRING)