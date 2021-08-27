from ..Abstract.Expression import *
from ..Abstract.Return import *
from ..Symbol.Environment import *

class CallFunc(Expression):

    def __init__(self, id, params, line, column):
        Expression.__init__(self, line, column)
        self.id = id
        self.params = params
    
    def execute(self, environment):
        try:
            func = environment.getFunc(self.id)
            if func != None:
                newEnv = Environment(environment.getGlobal())
                for i in range(len(self.params)):
                    value = self.params[i].execute(environment)
                    newEnv.saveVar(func.params[i].id, value.value, value.type)
                ret = func.instr.execute(newEnv)
                if ret != None:
                    if ret["type"] == Type.RETURNST:
                        return ret["value"]
                    else:
                        return ret
            else:
                struct = environment.getStruct(self.id)
                if struct != None:
                    attrs = {}
                    for i in range(len(self.params)):
                        value = self.params[i].execute(environment)
                        attrs.update({
                            struct[i] : value
                        })
                    return Return(attrs, Type.STRUCT, self.id)
        except:
            print("Error en llamada a funcion")