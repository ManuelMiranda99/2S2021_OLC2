from abc import ABC, abstractmethod
from Symbol.Environment import *

class Expression(ABC):
    
    def __init__(self, line, column):
        self.line = line
        self.column = column
        self.trueLbl = ''
        self.falseLbl = ''
        self.structType = ''
    
    @abstractmethod
    def compile(self, environment):
        pass