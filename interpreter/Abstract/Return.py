from enum import Enum

class Type(Enum):
    NULL = 0
    INT = 1
    FLOAT = 2
    BOOLEAN = 3
    CHAR = 4
    STRING = 5
    ARRAY = 6
    STRUCT = 7
    UNDEFINED = 8

    RETURNST = 9
    CONTINUEST = 10
    BREAKSTI = 11

class Return:
    def __init__(self, val, retType):
        self.value = val
        self.type = retType