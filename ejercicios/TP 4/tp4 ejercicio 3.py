# 3. Los números de claves de dos cajas fuertes están intercalados dentro de un número entero llamado "clave maestra", cuya longitud no se conoce.
# Realizar un programa para obtener ambas claves, donde la primera se construye con los dígitos 
# ubicados en posiciones impares de la clave maestra y la segunda con los dígitos 
# ubicados en posiciones pares. Los dígitos se numeran desde la izquierda. Ejemplo: 
# Si clave maestra fuera 18293, la clave 1 sería 123 y la clave 2 sería 89.

claveM=int(input("Ingrese la clave maestra:"))

def claves(claveM):
    c=str(claveM)
    clave1=[]
    clave2=[]
    for i in range(len(c)):
        if i%2==0:
            clave1.append(c[i])
        else:
            clave2.append(c[i])
    clave1Final="".join(clave1)
    clave2Final="".join(clave2)
    return clave1Final,clave2Final

clave1Final,clave2Final=claves(claveM)
print("La clave número 1 es:", clave1Final)
print("La clave número 2 es:", clave2Final)
