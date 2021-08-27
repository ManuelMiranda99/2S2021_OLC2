from ..Abstract.Instruction import *
from ..Export import output
import uuid

class Print(Instruction):

    def __init__(self, value, line, column, newLine = False):
        Instruction.__init__(self, line, column)
        self.value = value
        self.newLine = newLine
    
    def execute(self, environment):
        value = self.value.execute(environment)
        if self.newLine:
            output.output = output.output + str(value.value) + "\n"
        else:
            output.output = output.output + str(value.value)
    
    def getDot(self):
        idNode = 'Print' + str(uuid.uuid4())
        labelNode = 'print'
        if self.newLine:
            labelNode = 'println'
        output.addNode(idNode, labelNode)
        
        valueDot = self.value.getDot()
        output.addEdges(idNode, valueDot)

        return idNode