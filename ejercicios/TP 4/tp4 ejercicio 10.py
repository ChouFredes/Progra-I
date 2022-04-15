# 10. Desarrollar una función para reemplazar todas las apariciones de una palabra por 
# otra en una cadena de caracteres y devolver la cadena obtenida y un entero con la 
# cantidad de reemplazos realizados. Tener en cuenta que sólo deben reemplazarse 
# palabras completas, y no fragmentos de palabras. Escribir también un programa 
# para verificar el comportamiento de la función.

frase=str("Hola gente cómo están tanto tiempo gente")
vieja=str(input("Ingrese palabra a reemplazar:"))
nueva=str(input("Ingrese nueva palabra:"))

def separar(frase,vieja,nueva):
    r=0
    palabras=frase.split()
    for i in range(len(palabras)):
        if palabras[i]==vieja:
            palabras[i]=nueva
            r=r+1
    final=" ".join(palabras)
    return final,r

f,i=separar(frase,vieja,nueva)
print("La frase final es:",f)
print("La palabra se eliminó:",i,"veces.")

