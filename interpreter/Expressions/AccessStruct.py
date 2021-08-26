from Abstract.Expression import *

class AccessStruct(Expression):

    def __init__(self, id, att, line, column):
        Expression.__init__(self, line, column)
        self.id = id
        self.att = att
    
    def execute(self, environment):
        var = None
        if isinstance(self.id, AccessStruct):
            var = self.id.execute(environment)
        else:
            var = environment.getVar(self.id)
        if var.attributes[self.att] != None:
            return var.attributes[self.att]
        else:
            print("No existe ese atributo")