from Abstract.Expression import *
from Abstract.Return import *
from Symbol.Generator import Generator
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

    def compile(self, environment):
        genAux = Generator()
        generator = genAux.getInstance()

        generator.addComment("INICIO EXPRESION RELACIONAL")

        left = self.left.compile(environment)
        right = None

        result = Return(None, Type.BOOLEAN, False)

        if left.type != Type.BOOLEAN:
            right = self.right.compile(environment)
            if (left.type == Type.INT or left.type == Type.FLOAT) and (right.type == Type.INT or right.type == Type.FLOAT):
                self.checkLabels()
                generator.addIf(left.value, right.value, self.getOp(), self.trueLbl)
                generator.addGoto(self.falseLbl)
            elif left.type == Type.STRING and right.type == Type.STRING:
                print("Comparacion de cadenas")     # Únicamente se puede con igualdad o desigualdad
        else:
            gotoRight = generator.newLabel()
            leftTemp = generator.addTemp()

            generator.putLabel(left.trueLbl)
            generator.addExp(leftTemp, '1', '', '')
            generator.addGoto(gotoRight)

            generator.putLabel(left.falseLbl)
            generator.addExp(leftTemp, '0', '', '')

            generator.putLabel(gotoRight)

            right = self.right.compile(environment)
            if right.type != Type.BOOLEAN:
                print("Error, no se pueden comparar")
                return
            gotoEnd = generator.newLabel()
            rightTemp = generator.addTemp()

            generator.putLabel(right.trueLbl)
            
            generator.addExp(rightTemp, '1', '', '')
            generator.addGoto(gotoEnd)

            generator.putLabel(right.falseLbl)
            generator.addExp(rightTemp, '0', '', '')

            generator.putLabel(gotoEnd)

            self.checkLabels()
            generator.addIf(leftTemp, rightTemp, self.getOp(), self.trueLbl)
            generator.addGoto(self.falseLbl)

        generator.addComment("FIN DE EXPRESION RELACIONAL")
        generator.addSpace()
        result.trueLbl = self.trueLbl
        result.falseLbl = self.falseLbl

        return result     
    
    def checkLabels(self):
        genAux = Generator()
        generator = genAux.getInstance()
        if self.trueLbl == '':
            self.trueLbl = generator.newLabel()
        if self.falseLbl == '':
            self.falseLbl = generator.newLabel()

    def getOp(self):
        if self.type == RelationalOption.GREATER:
            return '>'
        elif self.type == RelationalOption.LESS:
            return '<'
        elif self.type == RelationalOption.GREATEREQUAL:
            return '>='
        elif self.type == RelationalOption.LESSEQUAL:
            return '<='
        elif self.type == RelationalOption.EQUALSEQUALS:
            return '=='
        elif self.type == RelationalOption.DISTINT:
            return '!='