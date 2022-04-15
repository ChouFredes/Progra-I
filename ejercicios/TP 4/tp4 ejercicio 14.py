# 14.Se solicita crear un programa para leer direcciones de correo electrónico y verificar 
# si representan una dirección válida. Por ejemplo usuario@dominio.com.ar. Para 
# que una dirección sea considerada válida el nombre de usuario debe poseer solamente caracteres alfanuméricos,
# la dirección contener un solo carácter @, el dominio debe tener al menos un carácter y tiene que finalizar con .com.ar. 
# Repetir el proceso de validación hasta ingresar una cadena vacía.
# Al finalizar mostrar un listado de todos los dominios, sin repetirlos y ordenados alfabéticamente, 
# recordando que las direcciones de mail no son case sensitive.

lista=[]
def comprobarEmail(cad,lista):
     for i in range(1):
         if cad.count("@")==1:
               if cad[-7:]==".com.ar":
                   num=cad.index("@")
                   fin=cad.index(".com.ar")
                   if cad[(num+1):fin]!="":
                       lista.append(cad)
     return lista

cad=str(input("Ingrese su E-Mail:"))
while cad!="":
    final=comprobarEmail(cad,lista)
    cad=str(input("Ingrese su E-Mail:"))

final.sort()
while lista.count(i)>1:
    lista.remove(i)
print(final)