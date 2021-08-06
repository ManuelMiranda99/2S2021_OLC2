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

    def execute(self, environment):
        leftValue = self.left.execute(environment)
        rightValue = self.right.execute(environment)

        result = Return(False, Type.BOOLEAN)
        
        if self.type == RelationalOption.GREATER:
            result.value = leftValue.value > rightValue.value
        elif self.type == RelationalOption.LESS:
            result.value = leftValue.value < rightValue.value
        elif self.type == RelationalOption.GREATEREQUAL:
            result.value = leftValue.value >= rightValue.value
        elif self.type == RelationalOption.LESSEQUAL:
            result.value = leftValue.value <= rightValue.value
        elif self.type == RelationalOption.EQUALSEQUALS:
            result.value = leftValue.value == rightValue.value
        elif self.type == RelationalOption.DISTINT:
            result.value = leftValue.value != rightValue.value
        
        return result