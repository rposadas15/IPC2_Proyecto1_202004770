from Tipos_Nodos import Nodo, NodoEncabezado

class ListaEncabezado:

    def __init__(self, primero = None):
        self.primero = primero

    def setEncabezado(self, Nuevo):
        if self.primero == None:
            self.primero = Nuevo
        elif Nuevo.id < self.primero.id:
            Nuevo.siguiente = self.primero
            self.primero.anterior = Nuevo
            self.primero = Nuevo
        else:
            actual = self.primero
            while actual.siguiente != None:
                if Nuevo.id < actual.siguiente.id:
                    Nuevo.siguiente = actual.siguiente
                    actual.siguiente.anterior = Nuevo
                    Nuevo.anterior = actual
                    actual.siguiente = Nuevo
                    break
                actual = actual.siguiente

            if actual.siguiente == None:
                actual.siguiente = Nuevo
                Nuevo.anterior = actual

    def getEncabezado(self, id):
        actual = self.primero
        while actual != None:
            if actual.id == id:
                return actual
            actual = actual.siguiente
        return None