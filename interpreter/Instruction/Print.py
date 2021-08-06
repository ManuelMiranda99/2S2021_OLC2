from Abstract.Instruction import *

class Print(Instruction):

    def __init__(self, value, line, column, newLine = False):
        Instruction.__init__(self, line, column)
        self.value = value
        self.newLine = newLine
    
    def execute(self, environment):
        value = self.value.execute(environment)
        if self.newLine:
            print(value.value)
        else:
            print(value.value, end="")