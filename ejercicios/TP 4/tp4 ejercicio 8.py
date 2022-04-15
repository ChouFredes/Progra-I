# 8. Escribir una función que reciba como parámetro una cadena de caracteres en la 
# que las palabras se encuentran separadas por uno o más espacios.
# Devolver otra cadena con las palabras ordenadas alfabéticamente, dejando un espacio entre cada una.

cad=str("caca ano pito boludo")
def ordenAlf(cad):
    lista=cad.split()
    lista.sort()
    final=" ".join(lista)
    return final

print(ordenAlf(cad))
