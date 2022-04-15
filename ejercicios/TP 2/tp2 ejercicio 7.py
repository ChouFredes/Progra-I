# Ejercicio 7
# Intercalar los elementos de una lista entre los elementos de otra. La intercalación 
# deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará 
# una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3] 
# y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7].

lista1=["8","1","3","4"]
lista2=["5","9","7","11"]

def intercalar(lista2,lista1):
    i=0
    x=0
    while x!=(len(lista2)):
        lista1[i:i]=lista2[x]
        x=x+1
        i=i+2
    return lista1

listafinal=intercalar(lista1,lista2)
print(listafinal)