import xml.etree.ElementTree as ET
from MatrizOrtogonal import Matriz
Contenido_Matriz = Matriz()

#C:\Users\ronal\Downloads\terrenos.xml
#C:/Users/ronal/Downloads/terreno.xml
def LeerXML(ruta):
    mytree = ET.parse(ruta)
    myroot = mytree.getroot()
    #print(myroot.tag)
    return myroot

ejeX = 0
ejeY = 0
nombre_del_terreno = ''
PosicionI_X = 0
PosicionI_Y = 0
PosicionF_X = 0
PosicionF_Y = 0
gas = 0

def ProcesarTerreno(xml, dato):
    global nombre_del_terreno
    global ejeX
    global ejeY
    global PosicionI_X
    global PosicionI_Y
    global PosicionF_X
    global PosicionF_Y
    global gas
    
    for x in range(len(xml)):
        if xml[x].attrib['nombre'] == dato:
            nombre_del_terreno = xml[x].attrib['nombre']            
            for j in xml[x].findall('dimension'):
                ejeX = int(j.find('m').text)
                ejeY = int(j.find('n').text)
            for j in xml[x].findall('posicioninicio'):
                PosicionI_X = int(j.find('x').text)
                PosicionI_Y = int(j.find('y').text)
            for j in xml[x].findall('posicionfin'):
                PosicionF_X = int(j.find('x').text)
                PosicionF_Y = int(j.find('y').text)
            for j in xml[x].findall('posicion'):
                Contenido_Matriz.Insertar(j.attrib['x'], j.attrib['y'],int(j.text))
        #else:
        #    None

    #Contenido_Matriz.NodoInicial(PosicionI_X, PosicionI_Y)
    #Contenido_Matriz.NodoFinal(PosicionF_X, PosicionF_Y)    
    #Contenido_Matriz.RecorrerFilas()
    #Contenido_Matriz.RecorrerColumnas()
    #Contenido_Matriz.Mostrar()
        
    if ejeX > 0:        
        #print('Tamaño ', ejeX, ejeY)
        #print('Inicio ', PosicionI_X, PosicionI_Y)
        #print('Fin ', PosicionF_X, PosicionF_Y)
        print('------------------------')
        print('     Terreno ', nombre_del_terreno, ' encontrado')
        print(' - Calculando Ruta')
        print(' - Calculando Combustible a usar')
        print('')
        if PosicionI_X >= PosicionF_X:            
            if PosicionI_Y > PosicionF_Y: #Ya
                #print('arriba y izquierda')                
                a, b , c = Contenido_Matriz.RecorridoArI(PosicionI_X, PosicionI_Y, PosicionF_X,PosicionF_Y, gas)
                print('Llego a la casilla', a, b)
                print('Combustible usado', c)
            elif PosicionI_Y < PosicionF_Y: #Ya
                #print('abajo y izquierda')                
                a, b , c = Contenido_Matriz.RecorridoAbI(PosicionI_X, PosicionI_Y, PosicionF_X,PosicionF_Y, gas)
                print('Llego a la casilla', a, b)
                print('Combustible usado', c)         
        elif PosicionI_X < PosicionF_X:
            if PosicionI_Y >= PosicionF_Y: #Ya                
                #print('arriba y derecha')
                a, b , c = Contenido_Matriz.RecorridoArD(PosicionI_X, PosicionI_Y, PosicionF_X,PosicionF_Y, gas)
                print('Llego a la casilla', a, b)
                print('Combustible usado', c)
            elif PosicionI_Y < PosicionF_Y: #Ya
                #print('abajo y derecha')
                a, b , c = Contenido_Matriz.RecorridoAbD(PosicionI_X, PosicionI_Y, PosicionF_X,PosicionF_Y, gas)
                print('Llego a la casilla', a, b)
                print('Combustible usado', c)
        print('------------------------')
    else:
        print('Ese terreno no existe')
        #print('Tamaño ', ejeX, ejeY)
        #print('Inicio ', PosicionI_X, PosicionI_Y)
        #print('Fin ', PosicionF_X, PosicionF_Y)

def EscribirXML(ruta):
    if ejeX > 0:
        print('------------------------')
        print('Se escribio el archivo xml')
        if PosicionI_X >= PosicionF_X:            
            if PosicionI_Y > PosicionF_Y: #Ya
                #print('arriba y izquierda')
                Contenido_Matriz.XMLArI(PosicionI_X, PosicionI_Y, PosicionF_X,PosicionF_Y, gas, ruta, nombre_del_terreno)                
            elif PosicionI_Y < PosicionF_Y: #Ya
                #print('abajo y izquierda')                
                Contenido_Matriz.XMLAbI(PosicionI_X, PosicionI_Y, PosicionF_X,PosicionF_Y, gas, ruta, nombre_del_terreno)                
        elif PosicionI_X < PosicionF_X:
            if PosicionI_Y >= PosicionF_Y: #Ya           
                #print('arriba y derecha')
                Contenido_Matriz.XMLArD(PosicionI_X, PosicionI_Y, PosicionF_X,PosicionF_Y, gas, ruta, nombre_del_terreno)                
            elif PosicionI_Y < PosicionF_Y: #Ya
                #print('abajo y derecha')
                Contenido_Matriz.XMLAbD(PosicionI_X, PosicionI_Y, PosicionF_X,PosicionF_Y, gas, ruta, nombre_del_terreno)
        print('------------------------')
    else:
        print('Ese terreno no existe')

def CrearGrafica(nombre): #Pendiente
    Contenido_Matriz.Grapho(nombre)

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
            ejeX = 0
            ejeY = 0
            nombre_del_terreno = ''
            PosicionI_X = 0
            PosicionI_Y = 0
            PosicionF_X = 0
            PosicionF_Y = 0
            gas = 0
            nombre_terreno = input('Ingrese el nombre del terreno: ')
            ProcesarTerreno(LeerXML(archivo), nombre_terreno)
        elif numero == 3:
            escribir = input('Ingrese la ruta especificada: ')
            EscribirXML(escribir)
        elif numero == 4:
            print(' -Ronaldo Javier Posadas Guerra')
            print(' -202004770')
            print(' -Introduccion a la Programacion y Computacion 2 Seccion A')
            print(' -Ingenieria en Ciencias y Sistemas')
            print(' -4to Semestre')
        elif numero == 5:
            nombre = input('Ingrese el nombre a graficar: ')
            CrearGrafica(nombre)
            #print('5')
        else:
            print('---Opcion no Valida, Intente de Nuevo---')
        print("1. Cargar Archivo")
        print("2. Procesar Terreno")
        print("3. Escribir Archivo de Salida")
        print("4. Mostrar Datos del Estudiante")
        print("5. Generar Grafica")
        print("6. Salir")
        numero = int(input("Seleccione una opcion: "))