from Abstract.Expression import *

class AccessStruct(Expression):

    def __init__(self, id, att, line, column):
        Expression.__init__(self, line, column)
        self.id = id
        self.att = att
    