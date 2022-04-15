# 6. Desarrollar una función que extraiga una subcadena de una cadena de caracteres, 
# indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena 
# como valor de retorno. Escribir también un programa para verificar el comportamiento de la misma.
# Ejemplo, dada la cadena "El número de teléfono es 4356-7890" extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres, 
# resultando la subcadena "4356-7890". Escribir una función para cada uno de los siguientes casos:
# a. Utilizando rebanadas
# b. Sin utilizar rebanadas

cad=str("El número de teléfono es 4356-7890")
n1=int(input("Ingrese la posición:"))
n2=int(input("Ingrese la cantidad de valores a extraer:"))

def subcad(cad,n1,n2):
    nf=n1+n2
    final=cad[n1:nf]
    return final

caca=subcad(cad,n1,n2)
print(caca)

def subcad2(cad,n1,n2):
    final=str()
    nf=n1+n2
    while n1<nf:
        final=final+cad[n1]
        n1=n1+1
    return final

caca2=subcad2(cad,n1,n2)
print(caca)
