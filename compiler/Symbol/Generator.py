from .Environment import Environment

class Generator:
    generator = None
    def __init__(self):
        # Contadores
        self.countTemp = 0
        self.countLabel = 0
        # Code
        self.code = ''
        self.funcs = ''
        self.natives = ''
        self.inFunc = False
        self.inNatives = False
        # Lista de Temporales
        self.temps = []
        
    def cleanAll(self):
        # Contadores
        self.countTemp = 0
        self.code = ''
        # Lista de Temporales
        self.temps = []
        Generator.generator = Generator()
    
    # CODE
    def getCode(self):
        return f'{self.code}'

    def codeIn(self, code):
        self.code = self.code + code

    def addComment(self, comment):
        self.codeInt(f'/* {comment} */')
    
    def getInstance(self):
        if Generator.generator == None:
            Generator.generator = Generator()
        return Generator.generator

    # Manejo de Temporales
    def addTemp(self):
        temp = f't{self.countTemp}'
        self.countTemp += 1
        self.temps.append(temp)
        return temp

    # EXPRESIONES
    def addExp(self, result, left, right, op):
        self.codeIn(f'{result}={left}{op}{right};\n')
    
    # INSTRUCCIONES
    def addPrint(self, type, value):
        self.codeIn(f'fmt.Printf("%{type}", {value});\n')
    
    def printTrue(self):
        self.addPrint("s", "t")
        self.addPrint("s", "r")
        self.addPrint("s", "u")
        seld.addPrint("s", "e")