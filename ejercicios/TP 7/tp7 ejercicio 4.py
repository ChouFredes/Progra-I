# 4. Desarrollar una función que devuelva el producto de dos números enteros por sumas sucesivas.

def productoSus(n,m):
    if m==1:
        return n
    else:
        return n+productoSus(n,m-1)

print(productoSus(5,4))