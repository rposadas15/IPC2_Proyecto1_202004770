from xml.dom import minidom
#C:\Users\ronal\Downloads\terrenos.xml
'''def LeerXML(ruta):
    doc = minidom.parse(ruta)
    nombre = doc.getElementsByTagName("terreno")[0]
    print(nombre.firstChild.data)'''

from ListaVertical import ListaVertical
from ListaHorizontal import ListaHorizontal

ListaV = ListaVertical()
ListaH = ListaHorizontal()

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

'''if __name__ == '__main__':
    print("1. Cargar Archivo")
    print("2. Procesar Terreno")
    print("3. Escribir Archivo de Salida")
    print("4. Mostrar Datos del Estudiante")
    print("5. Generar Grafica")
    print("6. Salir")
    numero = int(input("Seleccione una opcion: "))
    while(numero != 6):
        if numero == 1:
            archivo = input('Ingrese la ruta del archivo: ')
        elif numero == 2:                
            print('2')
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
        numero = int(input("Seleccione una opcion: "))'''