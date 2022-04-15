# 9. Realizar una función recursiva para imprimir una matriz de M x N.

matriz=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

def imprimirMat(matriz, inicio=0):
    if inicio<len(matriz):
        print(matriz[inicio])
        imprimirMat(matriz, inicio+1)

imprimirMat(matriz)