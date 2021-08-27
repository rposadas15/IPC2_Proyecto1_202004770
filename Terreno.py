class Terreno:

    def __init__(self, nombre, tamañox, tamañoy, ix, iy, fx, fy, posiciones):
        self.nombre = nombre
        self.tamañox = tamañox
        self.tamañoy = tamañoy
        self.ix = ix
        self.iy = iy
        self.fx = fx
        self.fy = fy
        self.posiciones = posiciones

    #Get
    def getNombre(self):
        return self.nombre

    def getTamañoX(self):
        return self.tamañox
        
    def getTamañoY(self):
        return self.tamañoy

    def getIX(self):
        return self.ix

    def getIY(self):
        return self.iy

    def getFX(self):
        return self.fx

    def getFY(self):
        return self.fy

    def getPosiciones(self):
        return self.posiciones

    #Set
    def setNombre(self, nombre):
        self.nombre = nombre

    def setTamañoX(self, tamañox):
        self.tamañox = tamañox

    def setTamañoY(self, tamañoy):
        self.tamañoy = tamañoy

    def setIX(self, ix):
        self.ix = ix

    def setIY(self, iy):
        self.iy = iy

    def setFX(self, fx):
        self.fx = fx

    def setFY(self, fy):
        self.fy = fy

    def setPosiciones(self, posiciones):
        self.posiciones = posiciones