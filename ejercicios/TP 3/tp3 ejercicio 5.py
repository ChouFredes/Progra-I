# 5. Desarrolle un programa que permita realizar reservas en una sala de cine de barrio 
# de N filas con M butacas por cada fila. Las filas se deberán referenciar con las letras desde la A y las butacas con los números desde el 1.

import random

def mostrar_butacas(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end="")
        print()

filasnombres=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

filas=int(input("Ingrese cantidad de filas:"))
while filas>len(filasnombres):
    filas=int(input("Error. Ingrese cantidad válida de filas:"))

butacas=int(input("Ingrese la cantidad de butacas por fila:"))

matriz= [[0] * butacas for i in range(filas)]

print("El estado de la sala de cine es (0 libre, 1 ocupado):")
mostrar_butacas(matriz)
print()

reservafila=input("Ingrese la letra correspondiente a la fila a alquilar:")
reservaasiento=int(input("Ingrese el número de asiento a reservar:"))
while reservaasiento>butacas:
    reservaasiento=int(input("Error. Ingrese el número de asiento a reservar:"))

filasnombres=filasnombres.index(reservafila)
matriz[filasnombres][reservaasiento-1]=1

print("Las butacas luego de la reserva son:")
mostrar_butacas(matriz)
print()

def cargar_sala(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            n=random.randint(0,1)
            matriz[f][c]=n

def butacas_libres(matriz):
    cont=0
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c]==0:
                cont=cont+1
    return cont


