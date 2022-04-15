# 3. Desarrollar un programa para rellenar una matriz de N x N con números enteros al 
# azar comprendidos en el intervalo [0,N2)
# de tal forma que ningún número se repita. Imprimir la matriz por pantalla.

import random

filas=int(input("Ingrese la cantidad de filas:"))
columnas=int(input("Ingrese la cantidad de columnas:"))

while filas!=columnas or columnas!=filas:
    filas=int(input("Error. Ingrese la cantidad de filas:"))
    columnas=int(input("Ingrese la cantidad de columnas:"))

matriz= [[0] * columnas for i in range(filas)]

def rellenarmatriz(matriz):
    repetidos=[]
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            n=random.randint(0,(filas**2)-1)
            while n in repetidos:
                n=random.randint(0,(filas**2)-1)
            matriz[f][c]=n
            repetidos.append(n)
                  
def imprimirmatriz(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end="")
        print()

rellenarmatriz(matriz)
imprimirmatriz(matriz)