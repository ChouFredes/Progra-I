# Cargar una lista con números al azar de cuatro dígitos.
# La cantidad de elementos también será un número al azar de dos dígitos.

import random

def funcion1():
    cant_elementos=random.randint(10,99)
    lista1=[]
    for i in range(cant_elementos):
        lista1.append(random.randint(1000,9999))
    return lista1

lista=funcion1()
print("La lista generada aleatoriamente es:")
print(lista)


#  Calcular y devolver la sumatoria de todos los elementos de la lista anterior.

def funcion2(lista):
    suma=sum(lista)
    return suma

listasumada=funcion2(lista)
print("")
print("La sumatoria de todos los elementos de la lista anterior es:",listasumada)



# Eliminar todas las apariciones de un valor en la lista anterior.
# El valor a eliminar se ingresa desde el teclado y la función lo recibe como parámetro.

def funcion3(lista,n):
    valor=True
    if n not in lista:
        print("El elemento no se encuentra en la lista.")
        valor=False
    else:
        while n in lista:
            lista.remove(n)   
    return lista,valor

print("")
num=int(input("Ingrese un valor a borrar:"))
listaborrar,valor=funcion3(lista,num)
if valor!=False:
    print("")
    print("La lista nueva es:")
    print(lista)
else:
    print()
    
#  Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas 
# auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50]

def funcion4(lista):
    i=0
    x=-1
    valor=False
    if len(lista)%2!=0:
        while lista[i]==lista[x] and i<(len(lista)-1):
            valor=True
            i=i+1
            x=x-1           
    return valor

listacapi=funcion4(lista)
if listacapi==True:
    print("")
    print("La lista es capicúa.")
else:
    print("")
    print("La lista no es capicúa.")
    
    
    