from Nodo import Nodo

class ListaHorizontal:

    def __init__(self):
        self.First = None
        self.Ultimo = None      

    def Insertar(self, data, ejex, ejey):
        NuevoNodo = Nodo(data, ejex, ejey)
        if self.First == None:
            self.First = self.Ultimo = NuevoNodo
        else:
            if NuevoNodo.getX() < self.First.getX():
                self.First.setIzquierda(NuevoNodo)
                NuevoNodo.setDerecha(self.First)
                self.First = NuevoNodo
            elif NuevoNodo.getX() > self.Ultimo.getX():
                self.Ultimo.setDerecha(NuevoNodo)
                NuevoNodo.setIzquierda(self.Ultimo)
                self.Ultimo = NuevoNodo
            '''else:
                Bandera1 = Nodo
                Bandera2 = Nodo
                Bandera1 = self.First
                while Bandera1.getX() < NuevoNodo.getX():
                    Bandera1 = Bandera1.getDerecha()
                Bandera1.getIzquierda = Bandera2
                Bandera2.setDerecha(NuevoNodo)
                NuevoNodo.setDerecha(Bandera1)
                NuevoNodo.setIzquierda(Bandera2)
                Bandera1.setIzquierda(NuevoNodo)'''

    def RecorrerLista(self):
        if self.First != None:
            Bandera1 = Nodo
            Bandera1 = self.First
            while Bandera1 != None:
                print("gasolina: ",Bandera1.dato," x: ",Bandera1.getX(), " y: ", Bandera1.getY())
                Bandera1 = Bandera1.getDerecha()