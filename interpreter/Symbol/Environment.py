from Symbol.Symbol import *

class Environment:
    
    def __init__(self, prev):
        self.prev = prev
        self.variables = {}
        self.functions = {}
        self.structs = {}
    
    def saveVar(self, idVar, value, typeVar):
        env = self
        newSymbol = Symbol(value, idVar, typeVar)
        while env != None:
            if idVar in env.variables.keys():
                env.variables[idVar] = newSymbol
                return
            env = env.prev
        self.variables[idVar] = newSymbol
    
    def saveVarStruct(self, idVar, attrs, type):
        env = self
        newSymbol = Symbol(None, idVar, Type.STRUCT, type)
        newSymbol.attributes = attrs
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
    
    def saveStruct(self, idStruct, attr):
        if idStruct in self.structs.keys():
            print("Struct repetido")
        else:
            self.structs[idStruct] = attr

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
        
    def getStruct(self, idStruct):
        env = self
        while env != None:
            if idStruct in env.structs.keys():
                return env.structs[idStruct]
            end = end.prev
        return None

    def getGlobal(self):
        env = self
        while env.prev != None:
            env = env.prev
        return env