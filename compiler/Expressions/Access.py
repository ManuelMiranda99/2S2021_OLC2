from Symbol.Generator import *
from Abstract.Expression import *
from Abstract.Return import *

class Access(Expression):

    def __init__(self, id, line, column):
        Expression.__init__(self, line, column)
        self.id = id

    def compile(self, environment):
        genAux = Generator()
        generator = genAux.getInstance()

        generator.addComment("Compilacion de Acceso")
        
        var = environment.getVar(self.id)
        if(var == None):
            print("Error, no existe la variable")
            return

        # Temporal para guardar variable
        temp = generator.addTemp()

        # Obtencion de posicion de la variable
        tempPos = var.pos
        if(not var.isGlobal):
            tempPos = generator.addTemp()
            generator.addExp(tempPos, 'P', var.pos, "+")
        generator.getStack(temp, tempPos)

        if var.type != Type.BOOLEAN:
            generator.addComment("Fin compilacion acceso")
            generator.addSpace()
            return Return(temp, var.type, True)
        if self.trueLbl == '':
            self.trueLbl = generator.newLabel()
        if self.falseLbl == '':
            self.falseLbl = generator.newLabel()
        
        generator.addIf(temp, '1', '==', self.trueLbl)
        generator.addGoto(self.falseLbl)

        generator.addComment("Fin compilacion acceso")
        generator.addSpace()

        ret = Return(None, Type.BOOLEAN, False)
        ret.trueLbl = self.trueLbl
        ret.falseLbl = self.falseLbl
        return ret