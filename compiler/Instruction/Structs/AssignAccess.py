from Abstract.Instruction import *
from Symbol.Generator import *

class AssignAccess(Instruction):

    def __init__(self, id, access, expr, line, column):
        Instruction.__init__(self, line, column)
        self.id = id
        self.access = access
        self.expr = expr

    def compile(self, environment):
        genAux = Generator()
        generator = genAux.getInstance()

        val = self.expr.compile(environment)

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
                if att.id == self.access:
                    finalAtt = att
                    break
                finalAttPos = finalAttPos + 1
            
            tempAux = generator.addTemp()
            
            generator.addExp(tempAux, temp, finalAttPos, '+')
            generator.setHeap(tempAux, val.value)