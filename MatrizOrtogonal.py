from NodoPrincipal import Nodo
from NodoEncabezado import NodoEncabezado
from EncabezadosMatriz import ListaEncabezado

class Matriz:

    def __init__(self):
        self.eFilas = ListaEncabezado()
        self.eColumnas = ListaEncabezado()

    def Insertar(self, fila, columna, valor):
        Nuevo = Nodo(fila, columna, valor)
        #Filas
        eFila = self.eFilas.getEncabezado(fila)
        if eFila == None:
            eFila = NodoEncabezado(fila)
            eFila.Acceso_Nodo = Nuevo
            self.eFilas.setEncabezado(eFila)            
        else:
            if Nuevo.columna < eFila.Acceso_Nodo.columna:
                Nuevo.derecha = eFila.Acceso_Nodo
                eFila.Acceso_Nodo.izquierda = Nuevo
                eFila.Acceso_Nodo = Nuevo
            else:
                actual = eFila.Acceso_Nodo
                while actual.derecha != None:
                    if Nuevo.columna < actual.derecha.columna:
                        Nuevo.derecha = actual.derecha
                        actual.derecha.izquierda = Nuevo
                        Nuevo.izquierda = actual
                        actual.derecha = Nuevo
                        break
                    actual = actual.derecha

                if actual.derecha == None:
                    actual.derecha = Nuevo
                    Nuevo.izquierda = actual
        #Columnas
        eColumna = self.eColumnas.getEncabezado(columna)
        if eColumna == None:
            eColumna = NodoEncabezado(columna)
            eColumna.Acceso_Nodo = Nuevo
            self.eColumnas.setEncabezado(eColumna)            
        else:
            if Nuevo.fila < eColumna.Acceso_Nodo.fila:
                Nuevo.abajo = eColumna.Acceso_Nodo
                eColumna.Acceso_Nodo.arriba = Nuevo
                eColumna.Acceso_Nodo = Nuevo
            else:
                actual = eColumna.Acceso_Nodo
                while actual.abajo != None:                    
                    if Nuevo.fila < actual.abajo.fila:
                        Nuevo.abajo = actual.abajo
                        actual.abajo.arriba = Nuevo
                        Nuevo.arriba = actual
                        actual.abajo = Nuevo
                        break
                    actual = actual.abajo

                if actual.abajo == None:
                    actual.abajo = Nuevo
                    Nuevo.arriba = actual
        #print("Se inserto: ", valor, " en la pos: ", fila, ",", columna)

    def NodoInicial(self, IX, IY):
        eFila = self.eFilas.primero        
        while eFila != None:
            actual = eFila.Acceso_Nodo            
            if int(actual.fila) == IX:                
                while actual != None:                    
                    if int(actual.columna) == IY:
                        return print('Inicio',actual.fila,actual.columna,actual.valor)
                    actual = actual.derecha
            eFila = eFila.siguiente
        return print('Ese Nodo no Existe')

    def NodoFinal(self, FX, FY):
        eFila = self.eFilas.primero        
        while eFila != None:
            actual = eFila.Acceso_Nodo            
            if int(actual.fila) == FX:                
                while actual != None:                    
                    if int(actual.columna) == FY:
                        return print('Final',actual.fila, actual.columna, actual.valor)
                    actual = actual.derecha
            eFila = eFila.siguiente
        return print('Ese Nodo no Existe')

    def RecorridoAD(self, IX, IY, FX, FY, gasolina):
        gasolina = 0
        eFila = self.eFilas.primero
        while eFila != None:
            actual = eFila.Acceso_Nodo
            if int(actual.fila) == IX:
                while actual != None:
                    if int(actual.columna) == IY:
                        while int(actual.columna) <= FY:
                            gasolina += actual.valor                            
                            if int(actual.columna) == FY:
                                gasolina -= actual.valor
                                while int(actual.fila) <= FX:
                                    gasolina += actual.valor
                                    if int(actual.fila) == FX:
                                        return actual.fila, actual.columna, gasolina
                                    actual = actual.abajo
                            actual = actual.derecha
                    actual = actual.derecha
            eFila = eFila.siguiente
        return print('Ese Nodo no Existe')

    def RecorridoAI(self, IX, IY, FX, FY, gasolina):
        gasolina = 0
        eFila = self.eFilas.primero
        while eFila != None:
            actual = eFila.Acceso_Nodo
            if int(actual.fila) == IX:                
                while actual != None:
                    if int(actual.columna) == IY:
                        while int(actual.columna) <= FY:
                            gasolina += actual.valor                            
                            if int(actual.columna) == FY:
                                gasolina -= actual.valor                                
                                while int(actual.fila) >= FX:
                                    gasolina += actual.valor
                                    if int(actual.fila) == FX:
                                        return actual.fila, actual.columna, gasolina
                                    actual = actual.arriba
                            actual = actual.derecha
                    actual = actual.derecha
            eFila = eFila.siguiente
        return print('Ese Nodo no Existe')
        
    def RecorrerFilas(self):
        eFila = self.eFilas.primero

        while eFila != None:
            actual = eFila.Acceso_Nodo
            print("Fila",str(actual.fila))
            print('Columna Valor')
            while actual != None:
                print(actual.columna,actual.valor)
                actual = actual.derecha
            eFila = eFila.siguiente
    
    def RecorrerColumnas(self):
        eColumna = self.eColumnas.primero

        while eColumna != None:
            actual = eColumna.Acceso_Nodo
            print("Columna",str(actual.columna))
            print('Fila Valor')
            while actual != None:
                print(actual.fila,actual.valor)
                actual = actual.abajo
            eColumna = eColumna.siguiente

    def Mostrar(self):
        eFila = self.eFilas.primero
        eColumna = self.eColumnas.primero
        if eFila != None and eColumna != None:
            print('esta llena')