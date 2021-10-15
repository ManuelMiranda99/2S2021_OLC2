from Abstract.Return import *

class Symbol:

    def __init__(self, symbolID, symbolType, position, globalVar, inHeap, structType = ""):
        self.id = symbolID
        self.type = symbolType
        self.pos = position
        self.isGlobal = globalVar
        self.inHeap = inHeap
        self.structType = structType

        self.value = None