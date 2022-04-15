# 1.Escribir un programa que permita ingresar una cadena de caracteres cualquiera y una secuencia de letras.
# Informar en cuántas palabras aparece la secuencia ingresada, e imprimir dichas palabras.
# Ejemplo:
# ∑Frase: "Esto es una prueba de cadena de caracteres, analizaremos cada palabra si todas las partes concuerdan"
# ∑Secuencia de caracteres: "cda"
# ∑Resultado: La secuencia cda aparece en 3 palabras: cadena, cada, concuerdan.

cad=str(input("Ingrese su cadena de caracteres:"))
letras=str(input("Ingrese su secuencia de letras:"))
while letras=="":
    letras=str(input("Ingrese su secuencia de letras no vacía:"))

def encontrarSecuencia(cad,letras):
    lista=cad.split()
    listaletras=[]
    f=0
    cont=0
    final=[]             
    for secuencia in range(len(letras)):
        listaletras.append(letras[secuencia])
    longSec=len(listaletras)
    for f in range(len(lista)):
        for c in range(len(lista[f])):
            if lista[f][c]==listaletras[cont]:
                cont=cont+1
            if cont==longSec:
                final.append(lista[f])
                cont=0
            if (c+1)==len(lista[f]) and cont!=0:
                cont=0                
    return final

encontradas=encontrarSecuencia(cad,letras)
print("La secuencia se encuentra en",len(encontradas) ,"palabra/s:")
for i in range(len(encontradas)):
    print(encontradas[i],end=", ")
