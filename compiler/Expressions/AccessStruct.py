from Abstract.Expression import *
from Symbol.Generator import *

class AccessStruct(Expression):

    def __init__(self, id, att, line, column):
        Expression.__init__(self, line, column)
        self.id = id
        self.att = att
    
    def compile(self, environment):
        genAux = Generator()
        generator = genAux.getInstance()

        var = environment.getVar(self.id)

        temp = generator.addTemp()

        tempPos = var.pos
        if(not var.isGlobal):
            tempPos = generator.addTemp()
            generator.addExp(tempPos, 'P', var.pos, "+")
        
        generator.getStack(temp, tempPos)
        
        struct = var.structType
        if struct != '':
            struct = environment.getStruct(struct)
            finalAtt = None
            finalAttPos = 0
            for att in struct:
                if att.id == self.att:
                    finalAtt = att
                    break
                finalAttPos = finalAttPos + 1

            tempAux = generator.addTemp()
            retTemp = generator.addTemp()

            generator.addExp(tempAux, temp, finalAttPos, '+')
            generator.getHeap(retTemp, tempAux)

            return Return(retTemp, finalAtt.type, True)