from ..Abstract.Return import *

class Symbol:

    def __init__(self, value, symbolID, symbolType, symbolOBJ = ""):
        self.value = value
        self.symbolID = symbolID
        self.type = symbolType
        # Structs
        self.obj = symbolOBJ
        self.attributes = {}