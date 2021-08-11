from NodoCabeceraFila import NodoCabeceraFila

class ListaCabeceraFila:

    def __init__(self):
        self.First = None
        self.Ultimo = None
    
    def Insertar(self, ejey):
        NuevoNodo = NodoCabeceraFila(ejey)
        if self.First == None:
            self.First = self.Ultimo = NuevoNodo
        else:
            if NuevoNodo.getY() < self.First.getY():
                self.First.setAnterior(NuevoNodo)
                NuevoNodo.setSiguiente(self.First)
                self.First = NuevoNodo
            elif NuevoNodo.getY() > self.Ultimo.getY():
                self.Ultimo.setSiguiente(NuevoNodo)
                NuevoNodo.setAnterior(self.Ultimo)
                self.Ultimo = NuevoNodo
            '''else:
                Bandera1 = Nodo
                Bandera2 = Nodo
                Bandera1 = self.First
                while Bandera1.getY() < NuevoNodo.getY():
                    Bandera1 = Bandera1.getAbajo()
                Bandera1.getArriba = Bandera2
                Bandera2.setAbajo(NuevoNodo)
                NuevoNodo.setAbajo(Bandera1)
                NuevoNodo.setArriba(Bandera2)
                Bandera1.setArriba(NuevoNodo)'''

    def RecorrerLista(self):
        if self.First != None:
            Bandera1 = NodoCabeceraFila
            Bandera1 = self.First
            while Bandera1 != None:
                print("Y : ", Bandera1.getY())
                Bandera1 = Bandera1.getSiguiente()

    def Buscar(self, posicion):
        if self.First != None:            
            Bandera1 = NodoCabeceraFila
            Bandera1 = self.First
            while Bandera1 != None:
                if(Bandera1.getY() == posicion):
                    return Bandera1
                Bandera1 = Bandera1.getSiguiente()
        return None