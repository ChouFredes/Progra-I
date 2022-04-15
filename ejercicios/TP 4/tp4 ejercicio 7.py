# 7. Escribir una función para eliminar una subcadena de una cadena de caracteres, a 
# partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante.
# Escribir también un programa para verificar el comportamiento de la misma. 
# Escribir una función para cada uno de los siguientes casos:

# a. Utilizando rebanadas

cad=str("chocolate")
n1=int(input("Ingrese la posición:"))
n2=int(input("Ingrese la cantidad de valores a extraer:"))

def eliminarCad(cad,n1,n2):
    nf=n1+n2
    final=cad.replace(cad[n1:nf],"")
    return final

a=eliminarCad(cad,n1,n2)
print(a)

# b. Sin utilizar rebanadas

def eliminarCad2(cad,n1,n2):
    final=str()
    nf=n1+n2
    while n1<nf:
        final=cad.replace(cad[n1],"")
    return final

b=eliminarCad2(cad,n1,n2)
print(b)

# mal, copiar cadena hasta el numero inicial y copiar los caracteres desde el lugar que terminan los no entrados