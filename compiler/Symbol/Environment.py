from Symbol.Symbol import *

class Environment:
    
    def __init__(self, prev):
        self.prev = prev
        
        # NUEVO
        self.size = 0
        self.breakLbl = ''
        self.continueLbl = ''
        self.returnLbl = ''
        if(prev != None):
            self.size = self.prev.size
            self.breakLbl = self.prev.breakLbl
            self.continueLbl = self.prev.continueLbl
            self.returnLbl = self.prev.returnLbl

        self.variables = {}
        self.functions = {}
        self.structs = {}
    
    def saveVar(self, idVar, symType, inHeap, structType = ""):
        if idVar in self.variables.keys():
            print("Variable ya existe")
        else:
            newSymbol = Symbol(idVar, symType, self.size, self.prev == None, inHeap, structType)
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
        env = self
        while env != None:
            if idFunc in env.functions.keys():
                return env.functions[idFunc]
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