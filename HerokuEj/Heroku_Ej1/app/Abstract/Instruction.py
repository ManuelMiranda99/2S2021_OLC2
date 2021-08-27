from abc import ABC, abstractmethod
from ..Symbol.Environment import *

class Instruction(ABC):
    
    def __init__(self, line, column):
        self.line = line
        self.column = column
    
    @abstractmethod
    def execute(self, environment):
        pass
    
    @abstractmethod
    def getDot(self):
        pass
    