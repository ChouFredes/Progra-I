# 1. Desarrollar una función para ingresar a través del teclado un número natural. La 
# función rechazará cualquier ingreso inválido de datos utilizando excepciones y 
# mostrará la razón exacta del error. Controlar que se ingrese un número, que ese 
# número sea entero y que sea mayor que 0. Devolver el valor ingresado cuando 
# éste sea correcto. Escribir también un programa que permita probar el correcto 
# funcionamiento de la misma.

def numEntero(msj="Ingrese un número natural: "):
    while True:
        try:
            n=int(input(msj))
            assert n.alpha(), "El número debe ser natural."
            assert n>0, "El número debe ser mayor que cero."
            break
        except ValueError:
            print("No se permite ingresar letras.")
        except AssertionError as mensaje:
            print(mensaje)
        except AttributeError:
            print("El número debe ser natural.")
    return n

a=numEntero(msj="Ingrese un número natural: ")
print("Su número es:",a)
