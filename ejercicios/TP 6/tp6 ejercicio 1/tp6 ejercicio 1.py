# 1. Desarrollar un programa para eliminar todos los comentarios de un programa escrito en lenguaje Python.
# Tener en cuenta que los comentarios comienzan con el signo #
# (siempre que éste no se encuentre encerrado entre comillas simples o dobles)
# y que también se considera comentario a las cadenas de documentación 
# (docstrings).

cont=0
lista=[]

try:
    arch=open("borrar.txt","rt")
    for linea in arch:
        lu=linea.split()
        if lu[0][0]!="#":
            lista.append(lu)
        cont=cont+1    
except OSError as mensaje:
    print("No se pudo grabar el archivo:", mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass

try:
    arch=open("nueva.txt","wt")
    for i in range(len(lista)):
        cad=" ".join(lista[i])
        arch.writelines(cad)
        arch.write("\n")
except OSError as mensaje:
    print("No se pudo grabar el archivo:", mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass