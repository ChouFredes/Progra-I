# 1. Escribir una función que devuelva la cantidad de dígitos de un número entero, sin 
# utilizar cadenas de caracteres.

def digitos(n):
    if n<10:
        return 1
    else:
        return 1+digitos(n/10)

print(digitos(n))

