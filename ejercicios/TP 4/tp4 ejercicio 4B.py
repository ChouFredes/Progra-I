# 4. Escribir una función que reciba como parámetro un número entero entre 0 y 3999 
# y lo convierta en un número romano, devolviéndolo en una cadena de caracteres. 
# ¿En qué cambiaría la función si el rango de valores fuese diferente?

numero=int(input("Ingrese un número entre 0 y 3999:"))
while numero>3999 or numero<0:
    numero=int(input("Error.Ingrese un número entre 0 y 3999:"))

def numRomano(numero):
    enteros=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    romanos=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    final=""
    i=0    
    while numero>0:
        for x in range(numero//enteros[i]):
            final=final+romanos[i]
            numero=numero - enteros[i]
        i=i+1
    return final

final=numRomano(numero)
print("Su número convertido a romano es:",final)