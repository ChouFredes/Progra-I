# 12.Resolver el siguiente problema, utilizando funciones:
# Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se 
# ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de carga. Se solicita:
#   a. Informar para cada socio, cuántas veces ingresó al club (cada socio debe 
#    aparecer una sola vez en el informe).
#   b. Solicitar un número de socio que se dio de baja del club y eliminar todos 
#    sus ingresos. Mostrar los registros de entrada al club antes y después de 
#    eliminarlo. Informar cuántos ingresos se eliminaron.

lista_ingreso=[]

def llenarLista(lista):
    num=int(input("Ingrese su número de socio:")) 
    while num!=0:
        while num<10000 or num>99999:
           num=int(input("Error. Ingrese su número de socio:"))
        lista.append(num)
        num=int(input("Ingrese su número de socio:"))
    return lista

listaFinal=llenarLista(lista_ingreso)
listaNodupli=[]

for i in listaFinal:
    if i not in listaNodupli:
        listaNodupli.append(i)

for i in range(len(listaNodupli)):
    apariciones=listaFinal.count(listaNodupli[i])
    print("El socio", listaNodupli[i],"ingresó",apariciones,"vez/veces.")
    

def borrarSocio(lista,num):
    cont=0
    while num in lista:
        lista.remove(num)
        cont=cont+1
    return lista,cont

borrado=int(input("Ingrese un socio a borrar de la lista:"))
print("La lista de ingreso es:",listaFinal)
if borrado not in listaFinal:
    print("El socio no se encuentra en la lista de entrada.")
else:
    lista2,cont=borrarSocio(listaFinal,borrado)
    print("La nueva lista con el socio borrado es:",lista2)
    print("Se eliminaron:",cont,"ingresos")

