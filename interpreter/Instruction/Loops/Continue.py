from Abstract.Instruction import *
from Abstract.Return import *

class Continue(Instruction):

    def __init__(self, line, column):
        Instruction.__init__(self, line, column)
    
    def execute(self, environment):
        return Return(None, Type.CONTINUEST)