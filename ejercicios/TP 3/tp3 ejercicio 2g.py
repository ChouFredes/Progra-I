n=int(input("Ingrese la cantidad de filas y columnas:"))
matriz= [[0] * n for i in range(n)]

def matrizg(matriz):
    num=1
    i=0
    while i<n/2:
        for c in range(i,n-i):
            matriz[i][c]=num
            num=num+1
        for f in range(i+1,n-i):
            matriz[f][n-i-1]=num
            num=num+1
        for c in range(n-i-2,i-1,-1):
            matriz[n-i-1][c]=num
            num=num+1
        for f in range(n-i-2,i,-1):
            matriz[f][i]=num
            num=num+1
        i=i+1
    
matrizg(matriz)
def imprimirmatriz(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%3d" %matriz[f][c], end="")
        print()

imprimirmatriz(matriz)