from ListaVertical import ListaVertical

class NodoCabeceraColumna:

    def __init__(self, x):
        self.x = x
        self.siguiente = None
        self.anterior = None
        self.columna = ListaVertical()
    
     #Get
    def getX(self):
        return self.x
    
    def getSiguiente(self):
        return self.siguiente

    #Set
    def setSiguiente(self, siguiente):
        self.siguiente = siguiente

    def setAnterior(self, anterior):
        self.anterior = anterior