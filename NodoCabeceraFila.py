from ListaHorizontal import ListaHorizontal

class NodoCabeceraFila:

    def __init__(self, y):
        self.y = y
        self.siguiente = None
        self.anterior = None
        self.fila = ListaHorizontal()
    
    #Get
    def getY(self):
        return self.y
    
    def getSiguiente(self):
        return self.siguiente

    #Set
    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def setAnterior(self, anterior):
        self.anterior = anterior