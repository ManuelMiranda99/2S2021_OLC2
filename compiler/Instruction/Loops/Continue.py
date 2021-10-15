from Abstract.Instruction import *
from Abstract.Return import *
from Symbol.Generator import *

class Continue(Instruction):

    def __init__(self, line, column):
        Instruction.__init__(self, line, column)
    
    def compile(self, environment):
        if environment.continueLbl == '':
            print("Continue fuera de ciclo")
            return
        genAux = Generator()
        generator = genAux.getInstance()

        generator.addGoto(environment.continueLbl)