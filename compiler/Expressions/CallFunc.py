from Abstract.Expression import *
from Abstract.Return import *
from Symbol.Environment import *
from Symbol.Generator import *

class CallFunc(Expression):

    def __init__(self, id, params, line, column):
        Expression.__init__(self, line, column)
        self.id = id
        self.params = params
    
    def compile(self, environment):
        try:
            func = environment.getFunc(self.id)
            if func != None:
                paramValues = []

                genAux = Generator()
                generator = genAux.getInstance()

                size = generator.saveTemps(environment)

                for param in self.params:
                    paramValues.append(param.compile(environment))
                temp = generator.addTemp()

                generator.addExp(temp, 'P', environment.size+1, '+')
                aux = 0
                for param in paramValues:
                    aux = aux +1
                    generator.setStack(temp, param.value)
                    if aux != len(paramValues):
                        generator.addExp(temp, temp, '1', '+')
                
                generator.newEnv(environment.size)
                generator.callFun(self.id)
                generator.getStack(temp, 'P')
                generator.retEnv(environment.size)

                generator.recoverTemps(environment, size)
                
                # TODO: Verificar tipo de la funcion. Boolean es distinto
                return Return(temp, func.type, True)
            else:
                # STRUCT
                struct = environment.getStruct(self.id)
                if struct != None:
                    self.structType = self.id

                    genAux = Generator()
                    generator = genAux.getInstance()

                    returnTemp = generator.addTemp()
                    generator.addExp(returnTemp, 'H', '', '')

                    aux = generator.addTemp()
                    generator.addExp(aux, returnTemp, '', '')

                    generator.addExp('H', 'H', len(struct), '+')

                    for att in self.params:
                        value = att.compile(environment)

                        if value.type != Type.BOOLEAN:
                            generator.setHeap(aux, value.value)
                        else:
                            retLbl = generator.newLabel()
                            
                            generator.putLabel(value.trueLbl)
                            generator.setHeap(aux, '1')
                            generator.addGoto(retLbl)

                            generator.putLabel(value.falseLbl)
                            generator.setHeap(aux, '0')

                            generator.putLabel(retLbl)
                        generator.addExp(aux, aux, '1', '+')
                    
                    return Return(returnTemp, Type.STRUCT, True)
        except:
            print("Error en llamda a funcion")