from Abstract.Expression import *
from Abstract.Return import *
from enum import Enum

class RelationalOption(Enum):
    GREATER = 0
    LESS = 1
    GREATEREQUAL = 2
    LESSEQUAL = 3
    EQUALSEQUALS = 4
    DISTINT = 5

class Relational(Expression):
    
    def __init__(self, left, right, type, line, column):
        Expression.__init__(self, line, column)
        self.left = left
        self.right = right
        self.type = type
