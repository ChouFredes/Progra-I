# Eliminar de una lista de palabras las palabras que se encuentren en una segunda 
# lista. Imprimir la lista original, la lista de palabras a eliminar y la lista resultante.

lista1=["caca","culo","pedo","pis"]
lista2=["culo","caca"]

def borrar(lista1,lista2):
    for i in range(0,len(lista2)):
        if lista2[i] in lista1:
            num=lista1.index(lista2[i])
            lista1.pop(num)
            
    return lista1

lista3=borrar(lista1,lista2)
print(lista3)