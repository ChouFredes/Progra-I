# 2. Realizar una función que reciba como parámetros dos cadenas de caracteres conteniendo números reales,
# sume ambos valores y devuelva el resultado como un 
# número real. Devolver -1 si alguna de las cadenas no contiene un número válido, 
# utilizando manejo de excepciones para detectar el error

def cadenas(cad1,cad2):
    try:
        num1=float(cad1)
        num2=float(cad2)
        final=num1+num2
    except ValueError:
        print("-1")
    return ""

cad1=str(input("Ingrese un número real:"))
cad2=str(input("Ingrese otro número real:"))

print(cadenas(cad1,cad2))