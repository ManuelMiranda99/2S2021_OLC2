from Abstract.Expression import *
from Abstract.Return import *
from Symbol.Generator import Generator
import uuid
class Literal(Expression):

    def __init__(self, value, type, line, column):
        Expression.__init__(self, line, column)
        self.value = value
        self.type = type
    
    def compile(self, env):
        genAux = Generator()
        generator = genAux.getInstance()
        if(self.type == Type.INT or self.type == Type.FLOAT):
            return Return(str(self.value), self.type, False)
        elif self.type == Type.BOOLEAN:
            if self.trueLbl == '':
                self.trueLbl = generator.newLabel()
            if self.falseLbl == '':
                self.falseLbl = generator.newLabel()
            
            if(self.value):
                generator.addGoto(self.trueLbl)
                generator.addComment("GOTO PARA EVITAR ERROR DE GO")
                generator.addGoto(self.falseLbl)
            else:
                generator.addGoto(self.falseLbl)
                generator.addComment("GOTO PARA EVITAR ERROR DE GO")
                generator.addGoto(self.trueLbl)
            
            ret = Return(self.value, self.type, False)
            ret.trueLbl = self.trueLbl
            ret.falseLbl = self.falseLbl

            return ret
        elif self.type == Type.STRING:
            retTemp = generator.addTemp()
            generator.addExp(retTemp, 'H', '', '')

            for char in str(self.value):
                generator.setHeap('H', ord(char))   # heap[H] = NUM;
                generator.nextHeap()                # H = H + 1;

            generator.setHeap('H', '-1')            # FIN DE CADENA
            generator.nextHeap()

            return Return(retTemp, Type.STRING, True)
        else:
            print('Por hacer')