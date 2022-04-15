# 9. Desarrollar una función que devuelva una subcadena con los últimos N caracteres 
# de una cadena dada. La cadena y el valor de N se pasan como parámetros.

cad=str(input("Ingrese su cadena:"))
N=int(input("Ingrese el valor numérico:"))

while N>len(cad):
    N=int(input("Error. Ingrese un valor numérico válido:"))

def subcad(cad,N):
    diferencia=len(cad)-N
    lista=[]
    lista.append(cad[diferencia: ])
    return lista

cadenaFinal=subcad(cad,N)
print("Los últimos",N,"valores de su cadena son:",cadenaFinal)