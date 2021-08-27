import xml.etree.ElementTree as ET
from Terreno import Terreno
from Lista import ListaDEnlazada
from MatrizOrtogonal import Matriz
BuscarTerreno = ListaDEnlazada()

#C:\Users\ronal\Downloads\prueba.xml
#C:/Users/ronal/Downloads/terreno.xml
def LeerXML(ruta):
    mytree = ET.parse(ruta)
    myroot = mytree.getroot()
    #print(myroot.tag)
    return myroot

def Posiciones(xml, a):
    Contenido_Matriz = Matriz() 
    for x in xml[a].findall('posicion'):
        Contenido_Matriz.Insertar(x.attrib.get('x'), x.attrib.get('y'), int(x.text))
    #Contenido_Matriz.RecorrerFilas()
    return Contenido_Matriz

gas = 0

def ProcesarTerreno(xml, dato):
    nombres_terrenos = []
    ejeX = []
    ejeY = []
    PosicionI_X = []
    PosicionI_Y = []
    PosicionF_X = []
    PosicionF_Y = []
    global gas    
        
    for x in xml:
        nombres_terrenos.append(x.attrib.get('nombre'))    

    for x in range(len(xml)):
        for j in xml[x].findall('dimension'):
            ejeX.append(int(j.find('n').text))
            ejeY.append(int(j.find('m').text))
        for j in xml[x].findall('posicioninicio'):
            PosicionI_X.append(int(j.find('x').text))
            PosicionI_Y.append(int(j.find('y').text))
        for j in xml[x].findall('posicionfin'):
            PosicionF_X.append(int(j.find('x').text))
            PosicionF_Y.append(int(j.find('y').text))
        #print(nombres_terrenos[x], ejeX[x], ejeY[x], PosicionI_X[x], PosicionI_Y[x], PosicionF_X[x], PosicionF_Y[x])

    #BuscarTerreno = ListaDEnlazada()

    for x in range(len(xml)):        
        pasada = Terreno(nombres_terrenos[x], ejeX[x], ejeY[x], PosicionI_X[x], PosicionI_Y[x], PosicionF_X[x], PosicionF_Y[x], Posiciones(xml, x))
        BuscarTerreno.Insertar(pasada)
    #print(BuscarTerreno.Tamaño)

    aux = BuscarTerreno.Primero
    while aux:
        if aux.data.getNombre() == dato:
            print('------------------------')
            print(' - Calculando Ruta')
            print(' - Calculando Combustible a usar')
            print('')
            if aux.data.getIX() >= aux.data.getFX():
                if aux.data.getIY() > aux.data.getFY(): #Ya
                    #print('arriba y izquierda')
                    a, b , c = aux.data.getPosiciones().RecorridoArI(aux.data.getIX(), aux.data.getIY(), aux.data.getFX(), aux.data.getFY(), gas)
                    print('Llego a la casilla', a, b)
                    print('Combustible usado', c)
                elif aux.data.getIY() < aux.data.getFY(): #Ya
                    #print('abajo y izquierda')                
                    a, b , c = aux.data.getPosiciones().RecorridoAbI(aux.data.getIX(), aux.data.getIY(), aux.data.getFX(), aux.data.getFY(), gas)
                    print('Llego a la casilla', a, b)
                    print('Combustible usado', c)         
            elif aux.data.getIX() < aux.data.getFX():
                if aux.data.getIY() >= aux.data.getFY(): #Ya                
                    #print('arriba y derecha')
                    a, b , c = aux.data.getPosiciones().RecorridoArD(aux.data.getIX(), aux.data.getIY(), aux.data.getFX(), aux.data.getFY(), gas)
                    print('Llego a la casilla', a, b)
                    print('Combustible usado', c)
                elif aux.data.getIY() < aux.data.getFY(): #Ya
                    #print('abajo y derecha')
                    a, b , c = aux.data.getPosiciones().RecorridoAbD(aux.data.getIX(), aux.data.getIY(), aux.data.getFX(), aux.data.getFY(), gas)
                    print('Llego a la casilla', a, b)
                    print('Combustible usado', c)
                    #aux.data.getPosiciones().RecorrerFilas()
            print('------------------------')
            break
        aux = aux.siguiente    

def EscribirXML(ruta, dato):
    aux = BuscarTerreno.Primero

    while aux:
        if aux.data.getNombre() == dato:
            print('------------------------')
            print('Se escribio el archivo xml')
            if aux.data.getIX() >= aux.data.getFX():            
                if aux.data.getIY() > aux.data.getFY(): #Ya
                    #print('arriba y izquierda')
                    aux.data.getPosiciones().XMLArI(aux.data.getIX(), aux.data.getIY(), aux.data.getFX(), aux.data.getFY(), gas, ruta, dato)                
                elif aux.data.getIY() < aux.data.getFY(): #Ya
                    #print('abajo y izquierda')                
                    aux.data.getPosiciones().XMLAbI(aux.data.getIX(), aux.data.getIY(), aux.data.getFX(), aux.data.getFY(), gas, ruta, dato)                
            elif aux.data.getIX() < aux.data.getFX():
                if aux.data.getIY() >= aux.data.getFY(): #Ya           
                    #print('arriba y derecha')
                    aux.data.getPosiciones().XMLArD(aux.data.getIX(), aux.data.getIY(), aux.data.getFX(), aux.data.getFY(), gas, ruta, dato)                
                elif aux.data.getIY() < aux.data.getFY(): #Ya
                    #print('abajo y derecha')
                    aux.data.getPosiciones().XMLAbD(aux.data.getIX(), aux.data.getIY(), aux.data.getFX(), aux.data.getFY(), gas, ruta, dato)
            print('------------------------')
            break
        aux = aux.siguiente

def CrearGrafica(nombre): #Ya
    aux = BuscarTerreno.Primero

    while aux:
        if aux.data.getNombre() == nombre:
            print('------------------------')
            print('Grafico Creado Correctamente')
            print('------------------------')
            #aux.data.getPosiciones().RecorrerFilas()
            aux.data.getPosiciones().Grapho(nombre)
            break
        aux = aux.siguiente

if __name__ == '__main__':
    print("1. Cargar Archivo")
    print("2. Procesar Terreno")
    print("3. Escribir Archivo de Salida")
    print("4. Mostrar Datos del Estudiante")
    print("5. Generar Grafica")
    print("6. Salir")
    numero = int(input("Seleccione una opcion: "))
    while(numero != 6):
        if numero == 1:
            global archivo
            archivo = input('Ingrese la ruta del archivo: ')
            LeerXML(archivo)            
        elif numero == 2:
            global nombre_terreno
            nombre_terreno = input('Ingrese el nombre del terreno: ')
            ProcesarTerreno(LeerXML(archivo), nombre_terreno)
        elif numero == 3:
            escribir = input('Ingrese la ruta especificada: ')
            EscribirXML(escribir, nombre_terreno)
        elif numero == 4:
            print('------------------------')
            print(' -Ronaldo Javier Posadas Guerra')
            print(' -202004770')
            print(' -Introduccion a la Programacion y Computacion 2 Seccion A')
            print(' -Ingenieria en Ciencias y Sistemas')
            print(' -4to Semestre')
            print('------------------------')
        elif numero == 5:
            nombre = input('Ingrese el nombre a graficar: ')
            CrearGrafica(nombre)
        else:
            print('---Opcion no Valida, Intente de Nuevo---')
        print("1. Cargar Archivo")
        print("2. Procesar Terreno")
        print("3. Escribir Archivo de Salida")
        print("4. Mostrar Datos del Estudiante")
        print("5. Generar Grafica")
        print("6. Salir")
        numero = int(input("Seleccione una opcion: "))