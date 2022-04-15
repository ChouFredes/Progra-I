# Escribir una función que reciba una lista como parámetro y devuelva True si la lista 
# está ordenada en forma ascendente o False en caso contrario. Por ejemplo, 
# ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar 
# además un programa para verificar el comportamiento de la función.

def funcion1(lista):
    valor=False
    lista2=[]+lista
    lista.sort()
    if lista==lista2:
        valor=True
    return valor

lista=["a","b","c","a"]
lista2=funcion1(lista)
print(lista2)
    