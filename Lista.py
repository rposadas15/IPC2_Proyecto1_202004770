from NodoNormal import NodoNormal

class ListaDEnlazada:

    def __init__(self):
        self.Primero = None
        self.Ultimo = None
        self.Tamaño = 0

    def Insertar(self, data):
        if self.Primero == None:            
            self.Primero = self.Ultimo = NodoNormal(data)
        else:
            aux = self.Ultimo
            self.Ultimo = aux.siguiente = NodoNormal(data)
            self.Ultimo.anterior = aux
        self.Tamaño += 1