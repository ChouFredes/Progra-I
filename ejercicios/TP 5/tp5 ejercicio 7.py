# 7. Escribir un programa que juegue con el usuario a adivinar un número. El programa 
# debe generar un número al azar entre 1 y 500 y el usuario debe adivinarlo. Para 
# eso, cada vez que se introduce un valor se muestra un mensaje indicando si el número que tiene que adivinar es mayor o menor que el ingresado.
# Cuando consiga adivinarlo, se debe imprimir en pantalla la cantidad de intentos que le tomó hallar 
# el número. Si el usuario introduce algo que no sea un número se mostrará un 
# mensaje en pantalla y se lo contará como un intento más.

import random

n=random.randint(1,500)
cont=0

while cont<3:
    try:
        adivino=int(input("Ingrese el número para adivinar:"))
        if adivino>n:
            print("El número que ingresó es mayor.")
            cont=cont+1
        if adivino<n:
            print("El número que ingresó es menor.")
            cont=cont+1
        if adivino==n:
            print("Felicitaciones, adivinó el número en",cont,"intentos.")
            break
    except ValueError:
        print("Solo se permite ingresar números enteros. Vuelva a intentarlo.")
        cont=cont+1

if cont==3:
    print("Se le terminaron los intentos.")