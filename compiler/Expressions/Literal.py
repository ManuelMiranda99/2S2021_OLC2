from Abstract.Expression import *
from Abstract.Return import *
import uuid

class Literal(Expression):

    def __init__(self, value, type, line, column):
        Expression.__init__(self, line, column)
        self.value = value
        self.type = type
    
    def compile(self, env):
        if(self.type == Type.INT or self.type == Type.FLOAT):
            return Return(str(self.value), self.type, False)
        else:
            print('Por hacer')