from Optimization.C3DInstruction import *

class If(C3DInstruction):

    def __init__(self, condition, label, line, column):
        C3DInstruction.__init__(self, line, column)
        self.condition = condition
        self.label = label
    
    def getCode(self):
        return f'if ({self.condition.getCode()}) {{ goto {self.label}; }}'