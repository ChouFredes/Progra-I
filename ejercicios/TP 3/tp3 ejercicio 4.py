import random

num=int(input("Ingrese el número de fábricas:"))

matriz= [[0] * 6 for i in range(num)]

def rellenarmatriz(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            n=int(random.randint(0,150))
            matriz[f][c]=n
            
def imprimirmatriz(matriz):
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            print("%4d" %matriz[f][c], end="")
        print()
        
print()
rellenarmatriz(matriz)
imprimirmatriz(matriz)
print()

# b. Mostrar la cantidad total de bicicletas fabricadas por cada fábrica.

for i in range(len(matriz)):
    print("En la fábrica", i+1 ,"se fabricaron:",sum(matriz[i]),"bicicletas.")

# c. Cuál es la fábrica que más produjo en un solo día (detallar día y fábrica).

def contarproduccion(matriz):
    cont=0
    fabrica=-1
    dia=-1
    filas=len(matriz)
    columnas=len(matriz[0])
    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c]>cont:
                cont=matriz[f][c]
                fabrica=f
                dia=c
    return cont,fabrica,dia

cont,fabrica,dia=contarproduccion(matriz)
print("La mayor cantidad de producción en un día fue de:",cont)
print("Ocurrió en la fabrica",fabrica+1,"y en el día:",dia)
print()
    
# d. Cuál es el día más productivo, considerando todas las fábricas combinadas.

def diaproductivo(matriz,num):
    cont=0
    contfinal=0
    diafinal=0
    c=0
    for i in range(5):
        while c<num:
            cont=cont+matriz[c][i]
            c=c+1
        if cont>contfinal:
            contfinal=cont
            diafinal=i
            cont=0
        else:
            cont=0
        c=0
    return contfinal,diafinal

total,diamax=diaproductivo(matriz,num)
print("El máximo en un día fue de $",total)
print("Ocurrió en el día:",diamax)
print()

# e. Crear una lista por comprensión que contenga la menor cantidad fabricada 
# por cada fábrica

matrizmenor= [min(matriz[i])*1 for i in range(num)]
print("La menor cantidad fabricada por cada fábrica son de:",matrizmenor)












