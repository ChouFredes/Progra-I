# 5. La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del 
# módulo math. Escribir un programa que utilice esta función para calcular la raíz 
# cuadrada de un número cualquiera ingresado a través del teclado. El programa 
# debe utilizar manejo de excepciones para evitar errores si se ingresa un número 
# negativo

import math

while True:
    try:
        n=int(input("Ingrese un número para sacar su raiz cuadrada:"))
        assert n>=0
        a=math.sqrt(n)
        print(a)
        break
    except AssertionError:
        print("Error. Ingrese un número positivo o igual a cero.")
    except ValueError:
        print("Error. Ingrese un número.")
