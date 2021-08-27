from ..Abstract.Expression import *
from ..Abstract.Return import *
from ..Export import output
import uuid

class Literal(Expression):

    def __init__(self, value, type, line, column):
        Expression.__init__(self, line, column)
        self.value = value
        self.type = type
    
    def execute(self, environment):
        return Return(self.value, self.type)

    def getDot(self):
        idNode = 'Literal' + str(uuid.uuid4())
        labelNode = self.value
        output.addNode(idNode, labelNode)

        return idNode