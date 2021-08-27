from NodoPrincipal import Nodo
from NodoEncabezado import NodoEncabezado
from EncabezadosMatriz import ListaEncabezado
import xml.etree.cElementTree as ET
import os

class Matriz:

    def __init__(self):
        self.EncabezadoF = ListaEncabezado()
        self.EncabezadoC = ListaEncabezado()

    def Insertar(self, fila, columna, valor):
        Nuevo = Nodo(fila, columna, valor)
        #Filas
        FILA_E = self.EncabezadoF.getEncabezado(fila)
        if FILA_E == None:
            FILA_E = NodoEncabezado(fila)
            FILA_E.Acceso_Nodo = Nuevo
            self.EncabezadoF.setEncabezado(FILA_E)            
        else:
            if Nuevo.columna < FILA_E.Acceso_Nodo.columna:
                Nuevo.derecha = FILA_E.Acceso_Nodo
                FILA_E.Acceso_Nodo.izquierda = Nuevo
                FILA_E.Acceso_Nodo = Nuevo
            else:
                actual = FILA_E.Acceso_Nodo
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
        COLUMNA_E = self.EncabezadoC.getEncabezado(columna)
        if COLUMNA_E == None:
            COLUMNA_E = NodoEncabezado(columna)
            COLUMNA_E.Acceso_Nodo = Nuevo
            self.EncabezadoC.setEncabezado(COLUMNA_E)            
        else:
            if Nuevo.fila < COLUMNA_E.Acceso_Nodo.fila:
                Nuevo.abajo = COLUMNA_E.Acceso_Nodo
                COLUMNA_E.Acceso_Nodo.arriba = Nuevo
                COLUMNA_E.Acceso_Nodo = Nuevo
            else:
                actual = COLUMNA_E.Acceso_Nodo
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
        FILA_E = self.EncabezadoF.primero        
        while FILA_E != None:
            actual = FILA_E.Acceso_Nodo            
            if int(actual.fila) == IX:                
                while actual != None:                    
                    if int(actual.columna) == IY:
                        return print('Inicio',actual.fila,actual.columna,actual.valor)
                    actual = actual.derecha
            FILA_E = FILA_E.siguiente
        return print('Ese Nodo no Existe')

    def NodoFinal(self, FX, FY):
        FILA_E = self.EncabezadoF.primero        
        while FILA_E != None:
            actual = FILA_E.Acceso_Nodo            
            if int(actual.fila) == FX:                
                while actual != None:                    
                    if int(actual.columna) == FY:
                        return print('Final',actual.fila, actual.columna, actual.valor)
                    actual = actual.derecha
            FILA_E = FILA_E.siguiente
        return print('Ese Nodo no Existe')

    def RecorridoAbD(self, IX, IY, FX, FY, gasolina):
        gasolina = 0
        FILA_E = self.EncabezadoF.primero
        while FILA_E != None:
            actual = FILA_E.Acceso_Nodo
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
            FILA_E = FILA_E.siguiente
        return print('Ese Nodo no Existe')

    def RecorridoAbI(self, IX, IY, FX, FY, gasolina):
        gasolina = 0
        FILA_E = self.EncabezadoF.primero
        while FILA_E != None:
            actual = FILA_E.Acceso_Nodo
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
            FILA_E = FILA_E.siguiente
        return print('Ese Nodo no Existe')

    def RecorridoArD(self, IX, IY, FX, FY, gasolina):
        gasolina = 0
        FILA_E = self.EncabezadoF.primero
        while FILA_E != None:
            actual = FILA_E.Acceso_Nodo
            if int(actual.fila) == IX:
                while actual != None:
                    if int(actual.columna) == IY:
                        while int(actual.columna) >= FY:
                            gasolina += actual.valor                            
                            if int(actual.columna) == FY:
                                gasolina -= actual.valor
                                while int(actual.fila) <= FX:
                                    gasolina += actual.valor
                                    if int(actual.fila) == FX:
                                        return actual.fila, actual.columna, gasolina
                                    actual = actual.abajo
                            actual = actual.izquierda
                    actual = actual.derecha
            FILA_E = FILA_E.siguiente
        return print('Ese Nodo no Existe')
    
    def RecorridoArI(self, IX, IY, FX, FY, gasolina):
        gasolina = 0
        FILA_E = self.EncabezadoF.primero
        while FILA_E != None:
            actual = FILA_E.Acceso_Nodo
            if int(actual.fila) == IX:                
                while actual != None:
                    if int(actual.columna) == IY:
                        while int(actual.columna) >= FY:
                            gasolina += actual.valor                            
                            if int(actual.columna) == FY:
                                gasolina -= actual.valor                                
                                while int(actual.fila) >= FX:
                                    gasolina += actual.valor
                                    if int(actual.fila) == FX:
                                        return actual.fila, actual.columna, gasolina
                                    actual = actual.arriba
                            actual = actual.izquierda
                    actual = actual.derecha
            FILA_E = FILA_E.siguiente
        return print('Ese Nodo no Existe')

    def XMLAbD(self, IX, IY, FX, FY, gasolina, ruta, nombre):
        root = ET.Element("terreno", nombre = str(nombre))
        doc1 = ET.SubElement(root, "posicioninicio")
        nodo1 = ET.SubElement(doc1, "x")
        nodo1.text = str(IX)
        nodo2 = ET.SubElement(doc1, "y")
        nodo2.text = str(IY)
        doc2 = ET.SubElement(root, "posicionfin")
        nodo1 = ET.SubElement(doc2, "x")
        nodo1.text = str(FX)
        nodo2 = ET.SubElement(doc2, "y")
        nodo2.text = str(FY)        

        gasolina = 0
        FILA_E = self.EncabezadoF.primero
        while FILA_E != None:
            actual = FILA_E.Acceso_Nodo
            if int(actual.fila) == IX:
                while actual != None:
                    if int(actual.columna) == IY:
                        while int(actual.columna) <= FY:
                            nodo = ET.SubElement(root, "posicion", x = str(actual.fila), y = str(actual.columna))
                            nodo.text = str(actual.valor)
                            gasolina += actual.valor                           
                            if int(actual.columna) == FY:
                                gasolina -= actual.valor                                
                                while int(actual.fila) <= FX:
                                    nodo = ET.SubElement(root, "posicion", x = str(actual.fila), y = str(actual.columna))
                                    nodo.text = str(actual.valor)
                                    gasolina += actual.valor
                                    if int(actual.fila) == FX:
                                        doc3 = ET.SubElement(root, "combustible")
                                        doc3.text = str(gasolina)
                                        arbol = ET.ElementTree(root)        
                                        arbol.write(ruta)                                        
                                        return True#actual.fila, actual.columna, gasolina
                                    actual = actual.abajo
                            actual = actual.derecha
                    actual = actual.derecha
            FILA_E = FILA_E.siguiente
        return print('Ese Nodo no Existe')

    def XMLAbI(self, IX, IY, FX, FY, gasolina, ruta, nombre):
        root = ET.Element("terreno", nombre = str(nombre))
        doc1 = ET.SubElement(root, "posicioninicio")
        nodo1 = ET.SubElement(doc1, "x")
        nodo1.text = str(IX)
        nodo2 = ET.SubElement(doc1, "y")
        nodo2.text = str(IY)
        doc2 = ET.SubElement(root, "posicionfin")
        nodo1 = ET.SubElement(doc2, "x")
        nodo1.text = str(FX)
        nodo2 = ET.SubElement(doc2, "y")
        nodo2.text = str(FY)

        gasolina = 0
        FILA_E = self.EncabezadoF.primero
        while FILA_E != None:
            actual = FILA_E.Acceso_Nodo
            if int(actual.fila) == IX:                
                while actual != None:
                    if int(actual.columna) == IY:
                        while int(actual.columna) <= FY:
                            nodo = ET.SubElement(root, "posicion", x = str(actual.fila), y = str(actual.columna))
                            nodo.text = str(actual.valor)
                            gasolina += actual.valor                            
                            if int(actual.columna) == FY:
                                gasolina -= actual.valor                                
                                while int(actual.fila) >= FX:
                                    nodo = ET.SubElement(root, "posicion", x = str(actual.fila), y = str(actual.columna))
                                    nodo.text = str(actual.valor)
                                    gasolina += actual.valor
                                    if int(actual.fila) == FX:
                                        doc3 = ET.SubElement(root, "combustible")
                                        doc3.text = str(gasolina)
                                        arbol = ET.ElementTree(root)        
                                        arbol.write(ruta)
                                        return True#actual.fila, actual.columna, gasolina
                                    actual = actual.arriba
                            actual = actual.derecha
                    actual = actual.derecha
            FILA_E = FILA_E.siguiente
        return print('Ese Nodo no Existe')

    def XMLArD(self, IX, IY, FX, FY, gasolina, ruta, nombre):
        root = ET.Element("terreno", nombre = str(nombre))
        doc1 = ET.SubElement(root, "posicioninicio")
        nodo1 = ET.SubElement(doc1, "x")
        nodo1.text = str(IX)
        nodo2 = ET.SubElement(doc1, "y")
        nodo2.text = str(IY)
        doc2 = ET.SubElement(root, "posicionfin")
        nodo1 = ET.SubElement(doc2, "x")
        nodo1.text = str(FX)
        nodo2 = ET.SubElement(doc2, "y")
        nodo2.text = str(FY)

        gasolina = 0
        FILA_E = self.EncabezadoF.primero
        while FILA_E != None:
            actual = FILA_E.Acceso_Nodo
            if int(actual.fila) == IX:
                while actual != None:
                    if int(actual.columna) == IY:
                        while int(actual.columna) >= FY:
                            nodo = ET.SubElement(root, "posicion", x = str(actual.fila), y = str(actual.columna))
                            nodo.text = str(actual.valor)
                            gasolina += actual.valor                            
                            if int(actual.columna) == FY:
                                gasolina -= actual.valor
                                while int(actual.fila) <= FX:
                                    nodo = ET.SubElement(root, "posicion", x = str(actual.fila), y = str(actual.columna))
                                    nodo.text = str(actual.valor)
                                    gasolina += actual.valor
                                    if int(actual.fila) == FX:
                                        doc3 = ET.SubElement(root, "combustible")
                                        doc3.text = str(gasolina)
                                        arbol = ET.ElementTree(root)        
                                        arbol.write(ruta)
                                        return True#actual.fila, actual.columna, gasolina
                                    actual = actual.abajo
                            actual = actual.izquierda
                    actual = actual.derecha
            FILA_E = FILA_E.siguiente
        return print('Ese Nodo no Existe')

    def XMLArI(self, IX, IY, FX, FY, gasolina, ruta, nombre):
        root = ET.Element("terreno", nombre = str(nombre))
        doc1 = ET.SubElement(root, "posicioninicio")
        nodo1 = ET.SubElement(doc1, "x")
        nodo1.text = str(IX)
        nodo2 = ET.SubElement(doc1, "y")
        nodo2.text = str(IY)
        doc2 = ET.SubElement(root, "posicionfin")
        nodo1 = ET.SubElement(doc2, "x")
        nodo1.text = str(FX)
        nodo2 = ET.SubElement(doc2, "y")
        nodo2.text = str(FY)

        gasolina = 0
        FILA_E = self.EncabezadoF.primero
        while FILA_E != None:
            actual = FILA_E.Acceso_Nodo
            if int(actual.fila) == IX:                
                while actual != None:
                    if int(actual.columna) == IY:
                        while int(actual.columna) >= FY:
                            nodo = ET.SubElement(root, "posicion", x = str(actual.fila), y = str(actual.columna))
                            nodo.text = str(actual.valor)
                            gasolina += actual.valor                            
                            if int(actual.columna) == FY:
                                gasolina -= actual.valor                                
                                while int(actual.fila) >= FX:
                                    nodo = ET.SubElement(root, "posicion", x = str(actual.fila), y = str(actual.columna))
                                    nodo.text = str(actual.valor)
                                    gasolina += actual.valor
                                    if int(actual.fila) == FX:
                                        doc3 = ET.SubElement(root, "combustible")
                                        doc3.text = str(gasolina)
                                        arbol = ET.ElementTree(root)        
                                        arbol.write(ruta)
                                        return True#actual.fila, actual.columna, gasolina
                                    actual = actual.arriba
                            actual = actual.izquierda
                    actual = actual.derecha
            FILA_E = FILA_E.siguiente
        return print('Ese Nodo no Existe')
        
    def RecorrerFilas(self):
        FILA_E = self.EncabezadoF.primero

        while FILA_E != None:
            actual = FILA_E.Acceso_Nodo
            print("Fila",str(actual.fila))
            print('Columna Valor')
            while actual != None:
                print(actual.columna,actual.valor)
                actual = actual.derecha
            FILA_E = FILA_E.siguiente
    
    def RecorrerColumnas(self):
        COLUMNA_E = self.EncabezadoC.primero

        while COLUMNA_E != None:
            actual = COLUMNA_E.Acceso_Nodo
            print("Columna",str(actual.columna))
            print('Fila Valor')
            while actual != None:
                print(actual.fila,actual.valor)
                actual = actual.abajo
            COLUMNA_E = COLUMNA_E.siguiente

    def Grapho(self, nombre):        
        archivo = open(nombre + ".dot", "w")
        archivo.write('digraph ' + nombre + ' { ')
        archivo.write(' bgcolor="purple:pink" style=filled \n')
        archivo.write('    subgraph cluster1 {fillcolor="blue:green" style=filled \n')
        archivo.write('     node [shape=circle fillcolor="gold:brown" style=radial gradientangle=180] \n')
        archivo.write('     a0 [label=< \n <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="yellow:violet" gradientangle="315">\n')
        
        FILA_E = self.EncabezadoF.primero
        while FILA_E != None:
            actual = FILA_E.Acceso_Nodo
            archivo.write('<TR>')
            while actual != None:                
                archivo.write("<TD border='3' style='radial' bgcolor='yellow' gradientangle='60'>" + str(actual.valor) + "</TD>")
                actual = actual.derecha
            FILA_E = FILA_E.siguiente
            archivo.write('</TR>')
        
        archivo.write('</TABLE>>]; \na1 [label="'+nombre+'" shape="box"]\n}\n')
        archivo.write('}\n')
        archivo.close()
        os.system('cmd /c "dot.exe -Tpng ' + (nombre + '.dot') + ' -o ' + (nombre + '.png') + '"')        
        os.startfile(nombre + '.png')

    def Mostrar(self):
        FILA_E = self.EncabezadoF.primero
        COLUMNA_E = self.EncabezadoC.primero
        if FILA_E != None and COLUMNA_E != None:
            print('esta llena')