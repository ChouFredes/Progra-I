# 5. Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo una frase y un entero N,
# y devuelva otra cadena con las palabras que tengan N o más caracteres de la cadena original.
# Escribir también un programa para verificar el comportamiento de la misma.
# Hacer tres versiones de la función, para cada uno de los siguientes casos:
#    a. Utilizando sólo ciclos normales
#    b. Utilizando listas por comprensión
#    c. Utilizando la función filter

cad=input("Ingrese la cadena con número:")

def filtrar_palabras(cad):
    cad1=str(cad)
    lista=cad1.split(" ")
    x=lista[-1]
    N=int(x)
    listaFinal=[]
    for i in range(len(lista)):
        if len(lista[i])>=N:
            listaFinal.append(lista[i])
    return listaFinal
    
print(filtrar_palabras(cad))