from ..Abstract.Expression import *
from ..Abstract.Return import *
from ..Export import output
from enum import Enum
import uuid

class ArithmeticOption(Enum):
    PLUS = 0
    MINUS = 1
    TIMES = 2
    DIV = 3

class Arithmetic(Expression):
    
    def __init__(self, left, right, type, line, column):
        Expression.__init__(self, line, column)
        self.left = left
        self.right = right
        self.type = type
    
    def execute(self, environment):
        leftValue = self.left.execute(environment)
        rightValue = self.right.execute(environment)
        
        result = Return(0, Type.INT)

        if self.type == ArithmeticOption.PLUS:
            result.value = leftValue.value + rightValue.value
        elif self.type == ArithmeticOption.MINUS:
            result.value = leftValue.value - rightValue.value
        elif self.type == ArithmeticOption.TIMES:
            result.value = leftValue.value * rightValue.value
        elif self.type == ArithmeticOption.DIV:
            result.value = leftValue.value / rightValue.value
        
        return result
    
    def getDot(self):
        idNode = 'expression' + str(uuid.uuid4())
        labelNode = 'expression'
        output.addNode(idNode, labelNode)

        leftDot = self.left.getDot()
        
        idOperation = self.getDotOp()

        rightDot = self.right.getDot()

        output.addEdges(idNode, leftDot)
        output.addEdges(idNode, idOperation)
        output.addEdges(idNode, rightDot)

        return idNode
    
    def getDotOp(self):
        idOperation = 'Operacion' + str(uuid.uuid4())
        labelOperation = '+'
        if self.type == ArithmeticOption.MINUS:
            labelOperation = '-'
        elif self.type == ArithmeticOption.TIMES:
            labelOperation = '*'
        elif self.type == ArithmeticOption.DIV:
            labelOperation = '/'
        output.addNode(idOperation, labelOperation)
        
        return idOperation