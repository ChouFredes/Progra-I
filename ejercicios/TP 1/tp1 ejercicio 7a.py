def diasiguiente(dia,mes,año):
    dia=dia+1
    if mes==2 and dia==29:
        dia=1
        mes=mes+1
    if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        if dia==32:
          dia=1
          mes=mes+1
    if mes==4 or mes==6 or mes==9 or mes==11:
        if dia==31:
            dia=1
            mes=mes+1
    if mes==13:
         mes=1
         año=año+1
    return (dia,mes,año)

dia=int(input("Ingrese un día:"))
mes=int(input("Ingrese un mes:"))
año=int(input("Ingrese un año:"))
cantidad=int(input("Ingrese la cantidad de días a sumar:"))

valor=True
if dia<1 or dia>31:
    valor=False
elif mes==2 and dia>28:
    valor=False
elif (mes==4 or mes==6 or mes==9 or mes==11) and dia>30:
    valor=False
elif año<1:
    valor=False

if valor==False:
    print("Fecha inválida")
else:
    for i in range(cantidad): 
        dia1,mes1,año1=diasiguiente(dia,mes,año)
        
    print("El día siguiente al indicado es:")
    print("Día:",dia1)
    print("Mes:",mes1)
    print("Año:",año1)