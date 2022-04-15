# 1. Desarrollar una función que determine si una cadena de caracteres es capicúa, sin 
# utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita 
# verificar su funcionamiento.

def esCapi(cad):
    i=0
    x=-1
    valor=False
    while cad[i]==cad[x] and i<(len(cad)-1):
        if cad[i]!=cad[x]:
            valor=False
            break
        else:            
            valor=True
            i=i+1
            x=x-1           
    return valor

cad=input("Ingrese su cadena:")

val=esCapi(cad)
print("¿Cadena capicúa?:",val)
    
        