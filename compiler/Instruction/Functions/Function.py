from Abstract.Instruction import *
from Symbol.Generator import *

class Function(Instruction):
    def __init__(self, id, params, type, instr, line, column):
        Instruction.__init__(self, line, column)
        self.id = id
        self.params = params
        self.type = type
        self.instr = instr
    
    def compile(self, environment):
        environment.saveFunc(self.id, self)
        genAux = Generator()
        generator = genAux.getInstance()
        
        newEnv = Environment(environment)

        returnLbl = generator.newLabel()
        newEnv.returnLbl = returnLbl
        newEnv.size = 1

        for param in self.params:
            newEnv.saveVar(param.id, param.type, (param.type == Type.STRING or param.type == Type.STRUCT))
        
        generator.addBeginFunc(self.id)

        try:
            self.instr.compile(newEnv)
        except:
            print(f'Error al compilar instrcciones de {self.id}')
        
        generator.putLabel(returnLbl)
        generator.addEndFunc()
        