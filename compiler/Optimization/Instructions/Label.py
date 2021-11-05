from Optimization.C3DInstruction import *

class Label(C3DInstruction):

    def __init__(self, id, line, column):
        C3DInstruction.__init__(self, line, column)
        self.id = id
        # Cualquier instrucción que sea el destino de un salto
        # condicional o incondicional es líder
        self.isLeader = True
    
    def getCode(self):
        if self.deleted:
            return ''
        return f'{self.id}:'