# 6. El método index permite buscar un elemento dentro de una lista, devolviendo la 
# posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se 
# produce una excepción de tipo ValueError. Desarrollar un programa que cargue 
# una lista con números enteros ingresados a través del teclado (terminando con -1) 
# y permita que el usuario ingrese el valor de algunos elementos para visualizar la 
# posición que ocupan, utilizando el método index. Si el número no pertenece a la 
# lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el 
# proceso al tercer error detectado. No utilizar el operador in durante la búsqueda.

lista=[]

n=int(input("Ingrese un número:"))
while n!=-1:
    lista.append(n)
    n=int(input("Ingrese otro número:"))

cont=0

while cont<3:
    try:
        a=int(input("Ingrese el número a buscar:"))
        print("Su número está en la posición:",lista.index(a))
        break
    except ValueError:
        cont=cont+1
        print("Error.")

if cont==3:
    print("Se finalizó el programa después de tres errores.")