from Abstract.Expression import *
from Abstract.Return import *
from Symbol.Generator import Generator
from enum import Enum
import uuid

class ArithmeticOption(Enum):
    PLUS = 0
    MINUS = 1
    TIMES = 2
    DIV = 3
    POT = 4

class Arithmetic(Expression):
    
    def __init__(self, left, right, type, line, column):
        Expression.__init__(self, line, column)
        self.left = left
        self.right = right
        self.type = type
    
    def compile(self, env):
        genAux = Generator()
        generator = genAux.getInstance()
        leftValue = self.left.compile(env)
        rightValue = self.right.compile(env)

        temp = generator.addTemp()
        op = ''
        if(self.type == ArithmeticOption.PLUS):
            op = '+'
        elif(self.type == ArithmeticOption.MINUS):
            op = '-'
        elif(self.type == ArithmeticOption.TIMES):
            op = '*'
        elif(self.type == ArithmeticOption.DIV):
            op = '/'    
        
        if (self.type == ArithmeticOption.POT):
            generator.fPotencia()
            paramTemp = generator.addTemp()

            generator.addExp(paramTemp, 'P', env.size, '+')
            generator.addExp(paramTemp, paramTemp, '1', '+')
            generator.setStack(paramTemp, leftValue.value)
            
            generator.addExp(paramTemp, paramTemp, '1', '+')
            generator.setStack(paramTemp, rightValue.value)
            
            generator.newEnv(env.size)
            generator.callFun('potencia')

            temp = generator.addTemp()
            generator.getStack(temp, 'P')
            generator.retEnv(env.size)

            return Return(temp, Type.INT, True)
        else:
            generator.addExp(temp, leftValue.value, rightValue.value, op)
            return Return(temp, Type.INT, True)