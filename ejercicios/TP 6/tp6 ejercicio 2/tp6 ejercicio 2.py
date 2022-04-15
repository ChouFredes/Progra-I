# Escribir un programa que permita grabar un archivo los datos de lluvia caída durante un año.
# Cada línea del archivo se grabará con el siguiente formato:
# <dia>;<mes>;<lluvia caída en mm> por ejemplo 25;5;319
# Los datos se generarán mediante números al azar, asegurándose que las fechas 
# sean válidas. La cantidad de registros también será un número al azar entre 50 y 
# 200. Por último se solicita leer el archivo generado e imprimir un informe en formato matricial donde cada columna represente a un mes y cada fila corresponda a 
# los días del mes. Imprimir además el total de lluvia caída en todo el año

import random

def imprimirmatriz(matriz):
    print("La matriz es la siguiente:")
    for fila in matriz:
        for valor in fila:
            print("\t", valor, end=" ")
        print()

cont=0
try:
    arch=open("lluvia.txt","wt")
    for i in range(random.randint(50,200)):
        mes=random.randint(1,12)
        if mes==2:
            dia=random.randint(1,28)
        elif mes==4 or mes==6 or mes==9 or mes==11:
            dia=random.randint(1,30)
        elif mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
            dia=random.randint(1,31)
        lluvia=random.randint(0,500)
        arch.write(str(dia)+";"+str(mes)+";"+str(lluvia)+"\n")
        cont=cont+lluvia    
except OSError as mensaje:
    print("No se puede grabar el archivo:", mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass

matriz= [[0] * 12 for i in range(31)]

try:
    arch=open("lluvia.txt","rt")
    for linea in arch:
        dia,mes,lluvia=linea.split(";")
        lluvia=lluvia.rstrip("\n")
        matriz[int(dia)-1][int(mes)-1]=lluvia
    imprimirmatriz(matriz)
    print("La cantidad de lluvia caida en el año es:",cont)
except OSError as mensaje:
    print("No se puede grabar el archivo:", mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass