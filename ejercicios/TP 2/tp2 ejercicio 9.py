# 9. Generar e imprimir una lista por comprensión entre A y B con los múltiplos de 7 
# que no sean múltiplos de 5. A y B se ingresar desde el teclado.

A=int(input("Ingrese el primer número:"))
B=int(input("Ingrese el segundo número:"))

while A>B:
    B=int(input("Error. Ingrese el segundo número:"))

lista=[i for i in range(A,B+1) if i%7==0 and i%5!=0]
print(lista)