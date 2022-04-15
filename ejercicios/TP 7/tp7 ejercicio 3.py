# 3. Escribir una función que devuelva la suma de los N primeros números naturales

def sumarNat(n):
    if n==1:
        return 1
    else:
        return n+sumarNat(n-1)
 
n=int(input("Ingrese un número natural:"))
while n<0:
    n=int(input("Ingrese un número natural:"))
print(sumarNat(n))