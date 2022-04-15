import random

naranjas=int(input("Ingresar la cantidad de naranjas cosechadas:"))
while naranjas<=0:
    naranjas=int(input("Ingrese un número válido:"))

def calculo_camiones(b):
    cosecha=0
    jugo=0
    num1=0
    for i in range(b):
        num=random.randint(150,350)
        if num>=200 and num<=300:
            cosecha=cosecha+1
            num1=num1+num
        else:
            jugo=jugo+1
    cajones=cosecha//100
    sobrante=cosecha-100*cajones
    return cajones,jugo,sobrante,num1

cajones,jugo,sobrante,peso=calculo_camiones(naranjas)

print("Se puede/n llenar",cajones,"cajon/es.")
print("Hay",jugo,"naranja/s para jugo.")
print("Hay un sobrante de",sobrante,"naranja/s.")

camiones_necesarios=peso//500000
camiones_validos=peso-(camiones_necesarios*500000)
if camiones_validos>=400000:
    camiones_necesarios=camiones_necesarios+1
if camiones_necesarios==0:
    print("La carga no cumple con los requisitos para ser trasladada.")
else:
    print("Se necesitan",camiones_necesarios,"camiones para trasladar la carga.")