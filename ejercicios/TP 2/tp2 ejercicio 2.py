import random

# Generar una lista de 50 números aleatorios del 1 al 100.

def punto_a():
    lista=[]
    for i in range(50):
        num=random.randint(1,100)
        lista.append(num)
    return lista

# Recibir una lista como parámetro y devolver True si la misma contiene algún 
# elemento repetido. La función no debe modificar la lista.

def punto_b(lista):
    valor=False
    for i in range(len(lista)):
        c=lista.count(lista[i])
        if c>1:
            valor=True
    return valor

# Recibir una lista como parámetro y devolver una nueva lista con los elementos 
# únicos de la lista original, sin importar el orden.

def punto_c(lista1):
    lista2=[]
    for i in range(len(lista1)):
        c=lista1.count(lista1[i])
        if c<=1:
            lista2.append(lista1[i])
    return lista2

# Programa

lista=punto_a()
print("La lista es:",lista)
repetido=punto_b(lista)
if repetido==True:
    repetido="Si"
else:
    repetido="No"
print("¿Hay números repetidos en la lista?:", repetido)
lista3=punto_c(lista)
print("La nueva lista con elementos únicos es:")
print(lista3)


