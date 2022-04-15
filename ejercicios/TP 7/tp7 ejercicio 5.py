# 5. Realizar una función que devuelva el resto de dos números enteros, utilizando restas sucesivas.

def restaSus(n,m):
    if m>n:
        return 0
    else:
        return restaSus(n,m-1)-1
    
print(restaSus(20,5))