from Nodo import Nodo
from NodoCabeceraFila import NodoCabeceraFila
from ListaCabeceraFila import ListaCabeceraFila
from NodoCabeceraColumna import NodoCabeceraColumna
from ListaCabeceraColumna import ListaCabeceraColumna

class Matriz:

    def __init__(self):
        self.columnas = ListaCabeceraColumna()
        self.filas = ListaCabeceraFila()

    def Insertar(self, x, y, dato):
        NuevoNodo = Nodo(dato, x, y)
        if self.columnas.Buscar(x) == None:
            self.columnas.Insertar(x)
        if self.filas.Buscar(y) == None:
            self.filas.Insertar(y)
        Bandera1 = NodoCabeceraColumna
        Bandera2 = NodoCabeceraFila
        Bandera1 = self.columnas.Buscar(x)
        Bandera2 = self.filas.Buscar(y)
        Bandera1.columna.Insertar(dato, x, y)
        Bandera2.fila.Insertar(dato, x, y)
        print("Se inserto: ", dato, " en la pos: ", x, ",", y)

    def LlegarDestino():
        return True
    
    '''def Llenar(self, tamañox, tamañoy, gasolina = []):
        a = 0
        for x in range(1, tamañox + 1):
            for j in range(1, tamañoy + 1):
                self.Insertar(x, j, int(gasolina[a]))
                a = a + 1'''