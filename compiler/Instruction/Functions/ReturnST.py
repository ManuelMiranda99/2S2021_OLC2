from Abstract.Expression import *
from Abstract.Return import *

class ReturnST(Expression):

    def __init__(self, expr, line, column):
        Expression.__init__(self, line, column)
        self.expr = expr
    