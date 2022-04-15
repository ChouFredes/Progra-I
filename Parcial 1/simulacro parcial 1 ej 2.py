# 2.Escribir funciones que reciban como parámetro una cadena y un carácter, y devuelvan una nueva cadena luego de realizar las siguientes tareas:a
# .Insertar el carácter dado entre cada letra de la cadena. Ejemplo: 'separar' y ',' debería devolver 's,e,p,a,r,a,r'.
# b.Reemplazar todos los espacios por el carácter dado. Ejemplo: 'archivo de texto.txt' y '_' debería devolver 'archivo_de_texto.txt'.
# Escribir también un programa principal para leer los datos a través del teclado, invocar a las funciones y mostrar los valores devueltos.

cad=str(input("Ingrese su cadena:"))
a=str(input("Ingrese el caracter para separar:"))

def juntarCadenas(cad,a):
    lista1=[]
    for i in range(len(cad)):
        lista1.append(cad[i])
    final=a.join(lista1)
    return final

def reemplazarEspacios(cad,a):
    final=cad.replace(" ",a)
    return final


print(juntarCadenas(cad,a))
print(reemplazarEspacios(cad,a))