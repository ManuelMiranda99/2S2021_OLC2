from Symbol import *

class Environment:
    
    def __init__(self, prev):
        self.prev = prev
        self.variables = {}
        self.functions = {}
    
    def saveVar(self, idVar, value, typeVar):
        env = self
        newSymbol = Symbol(value, idVar, typeVar)
        while env != None:
            if idVar in env.variables.keys():
                env.variables[idVar] = newSymbol
                return
            env = env.prev
        self.variables[idVar] = newSymbol
    
    def saveFunc(self, idFunc, function):
        if idFunc in self.functions.keys():
            print("Función repetida")
        else:
            self.functions[idFunc] = function
    
    def getVar(self, idVar):
        env = self
        while env != None:
            if idVar in env.variables.keys():
                return env.variables[idVar]
            env = env.prev
        return None
    
    def getFunc(self, idFunc):
        if idFunc in self.functions.keys():
            return self.functions[idFunc]
        else:
            return None