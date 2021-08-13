import xml.etree.ElementTree as ET
from Matriz import Matriz
Contenido_Matriz = Matriz()

#C:\Users\ronal\Downloads\terrenos.xml
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

def ProcesarTerreno(xml, dato):
    global nombre_del_terreno
    global ejeX
    global ejeY
    global PosicionI_X
    global PosicionI_Y
    global PosicionF_X
    global PosicionF_Y
    
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
                Contenido_Matriz.Insertar(j.attrib['x'], j.attrib['y'], int(j.text))
        #else:
        #    None

    if ejeX > 0:
        print('Terreno ', nombre_del_terreno, ' encontrado')
        print('Tamaño ', ejeX, ejeY)
        print('Inicio ', PosicionI_X, PosicionI_Y)
        print('Fin ', PosicionF_X, PosicionF_Y)
    else:
        print('Ese terreno no existe')
        print('Tamaño ', ejeX, ejeY)
        print('Inicio ', PosicionI_X, PosicionI_Y)
        print('Fin ', PosicionF_X, PosicionF_Y)

'''from ListaVertical import ListaVertical
from ListaHorizontal import ListaHorizontal
from ListaCabeceraFila import ListaCabeceraFila
from ListaCabeceraColumna import ListaCabeceraColumna
from Matriz import Matriz

ListaV = ListaVertical()
ListaH = ListaHorizontal()
ListaCF = ListaCabeceraFila()
ListaCC = ListaCabeceraColumna()
Fin = Matriz()

print("Vertical")
ListaV.Insertar(1,0,1)
ListaV.Insertar(2,0,2)
ListaV.Insertar(3,0,3)
ListaV.Insertar(4,0,4)
ListaV.Insertar(5,0,5)
ListaV.Insertar(6,0,6)

ListaV.RecorrerLista()

print("Horizontal")
ListaH.Insertar(1,1,0)
ListaH.Insertar(2,2,0)
ListaH.Insertar(3,3,0)
ListaH.Insertar(4,4,0)
ListaH.Insertar(5,5,0)
ListaH.Insertar(6,6,0)

ListaH.RecorrerLista()

print("Lista Cabecera Vertical")
ListaCF.Insertar(1)
ListaCF.Insertar(2)
ListaCF.Insertar(3)
ListaCF.Insertar(4)
ListaCF.Insertar(5)
ListaCF.Insertar(6)

ListaCF.RecorrerLista()

if ListaCF.Buscar(5) != None:
    print('La Cabecera Vertical existe')
else:
    print('La Cabecera Vertical no existe')

print("Lista Cabecera Horizontal")
ListaCC.Insertar(1)
ListaCC.Insertar(2)
ListaCC.Insertar(3)
ListaCC.Insertar(4)
ListaCC.Insertar(5)
ListaCC.Insertar(6)

ListaCC.RecorrerLista()

if ListaCC.Buscar(5) != None:
    print('La Cabecera Horizontal existe')
else:
    print('La Cabecera Horizontal no existe')

print('Matriz Ortogonal')
Fin.Llenar(3,3)'''

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
            PosicionI_X = 0
            PosicionI_Y = 0
            PosicionF_X = 0
            PosicionF_Y = 0
            nombre_terreno = input('Ingrese el nombre del terreno: ')
            ProcesarTerreno(LeerXML(archivo), nombre_terreno)
        elif numero == 3:
            escribir = input('Ingrese la ruta especificada: ')
        elif numero == 4:
            print(' -Ronaldo Javier Posadas Guerra')
            print(' -202004770')
            print(' -Introduccion a la Programacion y Computacion 2 Seccion A')
            print(' -Ingenieria en Ciencias y Sistemas')
            print(' -4to Semestre')
        elif numero == 5:
            print('5')
        else:
            print('---Opcion no Valida, Intente de Nuevo---')
        print("1. Cargar Archivo")
        print("2. Procesar Terreno")
        print("3. Escribir Archivo de Salida")
        print("4. Mostrar Datos del Estudiante")
        print("5. Generar Grafica")
        print("6. Salir")
        numero = int(input("Seleccione una opcion: "))