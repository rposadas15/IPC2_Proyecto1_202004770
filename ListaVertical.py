from Nodo import Nodo

class ListaVertical:

    def __init__(self):
        self.First = None
        self.Ultimo = None      

    def Insertar(self, data, ejex, ejey):
        NuevoNodo = Nodo(data, ejex, ejey)
        if self.First == None:
            self.First = self.Ultimo = NuevoNodo
        else:
            if NuevoNodo.getY() < self.First.getY():
                self.First.setArriba(NuevoNodo)
                NuevoNodo.setAbajo(self.First)
                self.First = NuevoNodo
            elif NuevoNodo.getY() > self.Ultimo.getY():
                self.Ultimo.setAbajo(NuevoNodo)
                NuevoNodo.setArriba(self.Ultimo)
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
            Bandera1 = Nodo
            Bandera1 = self.First
            while Bandera1 != None:
                print("gasolina: ",Bandera1.dato," x: ",Bandera1.getX(), " y: ", Bandera1.getY())
                Bandera1 = Bandera1.getAbajo()