# 1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar su
# funcionamiento, imprimiendo la matriz luego de invocar a cada función:
# a. Cargar números enteros en una matriz de N x N, ingresando los datos desde 
# teclado.

filas=int(input("Ingrese la cantidad de filas:"))
columnas=int(input("Ingrese la cantidad de columnas:"))
while columnas!=filas:
    columnas=int(input("Error. Ingrese la misma cantidad."))

matriz= [[0] * columnas for i in range(filas)]

def rellenarmatriz(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            n=int(input("Ingrese un número:"))
            matriz[f][c]=n

def imprimirmatriz(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end="")
        print()

rellenarmatriz(matriz)
imprimirmatriz(matriz)
print()

# b. Ordenar en forma ascendente cada una de las filas de la matriz.

def ordenarmatriz(matriz):
    for i in range(len(matriz)):
        matriz[i].sort()

ordenarmatriz(matriz)
imprimirmatriz(matriz)
print()

# c. Intercambiar dos filas, cuyos números se reciben como parámetro.

fila1=int(input("Ingrese la fila a intercambiar:"))
fila2=int(input("Ingrese la otra fila a intercambiar:"))
while fila1>filas or fila2>filas or fila1==fila2:
    fila1=int(input("Error. Ingrese la fila a intercambiar:"))
    fila2=int(input("Ingrese la otra fila a intercambiar:"))

def intercambiarFilas(matriz,fila1,fila2):
    lista1=[]+matriz[fila1-1]
    lista2=[]+matriz[fila2-1]
    for i in range(len(lista1)):
        matriz[fila1-1][i]=lista2[i]
        matriz[fila2-1][i]=lista1[i]
    return matriz

intercambiarFilas(matriz,fila1,fila2)
imprimirmatriz(matriz)
print()

#d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.

columna1=int(input("Ingrese la columna a intercambiar:"))
columna2=int(input("Ingrese la otra columna a intercambiar:"))
while columna1>columnas or columna2>columnas or columna1==columna2:
    columna1=int(input("Error. Ingrese la columna a intercambiar:"))
    columna2=int(input("Ingrese la otra columna a intercambiar:"))

def intercambiarColumnas(matriz,columna1,columna2):
    
    

intercambiarColumnas(matriz,columna1,columna2)
imprimirmatriz(matriz)
print()




