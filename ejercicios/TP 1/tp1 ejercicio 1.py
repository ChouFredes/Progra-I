def positivo():
    a=int(input("Ingrese un número:"))
    if a<0:
        a=int(input("Ingrese número válido:"))
    return a

def funcion(a,b,c):
    n=-1
    if a>b:
        if a>c:
            n=a
    if b>a:
        if b>c:
            n=b
    if c>a:
        if c>b:
            n=c
    return n

num1=positivo()
num2=positivo()
num3=positivo()

final=funcion(num1,num2,num3)

if final==-1:
    print("No existe un mayor estricto.")
else:
    print("El número mayor estricto es:",final)