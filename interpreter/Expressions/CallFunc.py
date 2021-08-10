from Abstract.Expression import *
from Symbol.Environment import *

class CallFunc(Expression):

    def __init__(self, id, params, line, column):
        Expression.__init__(self, line, column)
        self.id = id
        self.params = params
    
    def execute(self, environment):
        func = environment.getFunc(self.id)
        if func != None:
            newEnv = Environment(environment.getGlobal())
            for i in range(len(self.params)):
                value = self.params[i].execute(environment)
                newEnv.saveVar(func.params[i].id, value.value, value.type)
            func.instr.execute(newEnv)