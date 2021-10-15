from Abstract.Expression import *
from Abstract.Return import *
from Symbol.Generator import *

class ReturnST(Expression):

    def __init__(self, expr, line, column):
        Expression.__init__(self, line, column)
        self.expr = expr
    
    def compile(self, environment):
        if(environment.returnLbl == ''):
            print("Return fuera de funcion")
            return
        genAux = Generator()
        generator = genAux.getInstance()

        value = self.expr.compile(environment)
        if(value.type == Type.BOOLEAN):
            tempLbl = generator.newLabel()
            
            generator.putLabel(value.trueLbl)
            generator.setStack('P', '1')
            generator.addGoto(tempLbl)

            generator.putLabel(value.falseLbl)
            generator.setStack('P', '0')

            generator.putLabel(tempLbl)
        else:
            generator.setStack('P', value.value)
        generator.addGoto(environment.returnLbl)