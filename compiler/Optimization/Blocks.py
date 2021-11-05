
class Blocks:

    def __init__(self, firstIntr):
        # Primera instruccion del codigo
        self.first = firstIntr
        # Bloques siguientes a este
        self.nexts = []
        self.code = []