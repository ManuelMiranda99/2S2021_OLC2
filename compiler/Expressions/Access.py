from Abstract.Expression import *
from Abstract.Return import *

class Access(Expression):

    def __init__(self, id, line, column):
        Expression.__init__(self, line, column)
        self.id = id
