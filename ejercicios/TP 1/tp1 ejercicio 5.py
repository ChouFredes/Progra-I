def asterisco1(a):
    for i in range (a):
        print("**********")
    return ""
    
def asterisco2(a):
    for i in range (a):
        print("**"*(i+1))
    return ""
        

a=int(input("Ingrese número de filas:"))
print(asterisco1(a))

a=int(input("Ingrese número de filas:"))
print(asterisco2(a))
    
    