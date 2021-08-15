class Nodo:

    def __init__(self, dato, x, y):
        self.dato = dato
        self.x = x
        self.y = y
        self.derecha = None
        self.izquierda = None
        self.arriba = None
        self.abajo = None
    
    #Get
    def getDato(self):
        return self.dato

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getDerecha(self):
        return self.derecha

    def getIzquierda(self):
        return self.izquierda

    def getArriba(self):
        return self.arriba

    def getAbajo(self):
        return self.abajo
    
    #Set
    def setDerecha(self, derecha):
        self.derecha = derecha

    def setIzquierda(self, izquierda):
        self.izquierda = izquierda

    def setArriba(self, arriba):
        self.arriba = arriba
        
    def setAbajo(self, abajo):
        self.abajo = abajo