from Abstract.Expression import *
from Abstract.Return import *
from Symbol.Environment import *

class CallFunc(Expression):

    def __init__(self, id, params, line, column):
        Expression.__init__(self, line, column)
        self.id = id
        self.params = params
    