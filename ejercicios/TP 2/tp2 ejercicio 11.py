# 11.Resolver el siguiente problema, diseñando las funciones a utilizar:
#  Una clínica necesita un programa para atender a sus pacientes. Cada paciente que 
#  ingresa se anuncia en la recepción indicando su número de afiliado (número entero 
#  de 4 dígitos) y además indica si viene por una urgencia (ingresando un 0) o con 
#  turno (ingresando un 1). Para finalizar se ingresa -1 como número de socio. Luego 
#  se solicita:
#     a. Mostrar un listado de los pacientes atendidos por urgencia y un listado de 
#       los pacientes atendidos por turno en el orden que llegaron a la clínica.
#     b. Realizar la búsqueda de un número de afiliado e informar cuántas veces 
#       fue atendido por turno y cuántas por urgencia. Repetir esta búsqueda hasta que se ingrese -1 como número de afiliado.

listaUrg=[]
listaTurn=[]
cont=0

num=int(input("Ingrese su número de socio (Ingrese 0 para notificar emergencia, 1 para notificar un turno y -1 para finalizar):"))

while num!=-1:
    cont=cont+1
    while num>9999 or num<1000 and num!=0 and num!=1:
        num=int(input("Error. Ingrese su número de socio:"))
    if num==0:
        print("Urgencia notificada.")
        num=int(input("Ingrese su número de socio:"))
        listaUrg.append(num)
    if num==1:
        print("Turno notificado.")
        num=int(input("Ingrese su número de socio:"))
        listaTurn.append(num)
    num=int(input("Ingrese su número de socio (Ingrese 0 para notificar emergencia, 1 para notificar un turno y -1 para finalizar):"))

if cont==0:
    print("Finalizado sin datos.")
else:
    print("La lista de pacientes por emergencia es:", listaUrg)
    print("La lista de pacientes con turno es:",listaTurn)

buscador=int(input("Ingrese un número de socio a buscar (-1 para finalizar):"))

def buscar(num,listaUrg,listaTurn):
    while num!=-1:
        print("Cantidad de veces del paciente en lista de urgencia:", listaUrg.count(num))
        print("Cantidad de veces del paciente en lista por turno:", listaTurn.count(num))
        num=int(input("Ingrese otro número de socio (-1 para finalizar):"))
    return ""

busqueda=buscar(buscador,listaUrg,listaTurn)


        
