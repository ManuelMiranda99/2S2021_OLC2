from Optimization.C3DInstruction import *

class Literal(C3DInstruction):

    def __init__(self, value, line, column, constant = False):
        C3DInstruction.__init__(self, line, column)
        self.value = value
        self.constant = constant
    
    def getCode(self):
        return str(self.value)