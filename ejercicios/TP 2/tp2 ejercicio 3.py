# Crear una lista con los cuadrados de los números entre 1 y N (ambos incluidos), 
# donde N se ingresa desde el teclado. Luego se solicita imprimir los últimos 10 valores de la lista.

def listacuadrado(n):
    lista=[]
    for i in range(1,n+1):
        lista.append(i**2)
    return lista

n=int(input("Ingrese el número final a incluir en la lista cuadrada:"))
lista=listacuadrado(n)
print(lista)

if len(lista)<10:
    print("La lista no tiene 10 valores o más.")
else:
    x=-10
    print("Los últimos 10 valores de la lista son:")
    while x>=-10 and x<=-1:
        print(lista[x], end=", ")
        x=x+1
    


