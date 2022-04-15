# 10. Generar una lista con números al azar entre 1 y 100 y crear una nueva lista con 
# los elementos de la primera que sean impares. El proceso deberá realizarse utilizando listas por comprensión.
# Imprimir las dos listas por pantalla.

import random

lista1=[random.randint(1,100) for i in range(10)]
print(lista1)
lista2=[lista1[i] for i in range(len(lista1)) if lista1[i]%2!=0]
print(lista2)

