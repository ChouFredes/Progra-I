# 2.Ingresar un número entero correspondiente al ancho de un rombo verificando que sea positivo e impar, volviéndolo a ingresar en caso de error.
# Luego se solicita imprimir dicho rombo con asteriscos en sus bordes y espacios en su interior.

lado=int(input("Ingrese el número de ancho impar(mínimo 3):"))
while lado<3 or lado%2==0:
    lado=int(input("Error. Ingrese el número de ancho impar(mínimo 3):"))

cad1="*".center(lado)
print(cad1)
for i in range((lado-1)//2):
    relleno1="*"+" "*(1+2*i)+"*"
    relleno1cent=relleno1.center(lado)
    print(relleno1cent)
medio=(lado-2)
for i in range(((lado-1)//2)-1):
    relleno2="*"+" "*((medio)-2)+"*"
    relleno2cent=relleno2.center(lado)
    medio=medio-2
    print(relleno2cent)
print(cad1)