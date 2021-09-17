from Symbol.Symbol import *

class Environment:
    
    def __init__(self, prev):
        self.prev = prev
        
        # NUEVO
        self.size = 0
        if(prev != None):
            self.size = self.prev.size
        
        self.variables = {}
        self.functions = {}
        self.structs = {}
    
    def saveVar(self, idVar, symType, inHeap):
        if idVar in self.variables.keys():
            print("Variable ya existe")
        else:
            newSymbol = Symbol(idVar, symType, self.size, self.prev == None, inHeap)
            self.size += 1
            self.variables[idVar] = newSymbol
        return self.variables[idVar]

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