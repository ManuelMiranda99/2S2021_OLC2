from Abstract.Return import *

class Symbol:

    def __init__(self, symbolID, symbolType, position, globalVar, inHeap):
        self.id = symbolID
        self.type = symbolType
        self.pos = position
        self.isGlobal = globalVar
        self.inHeap = inHeap

        self.value = None