class Nodo:

    def __init__(self, puntero):
        self.puntero = puntero
        self.siguente = None

    def __str__(self):
        return str(self.puntero)