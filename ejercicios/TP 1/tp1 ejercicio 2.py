dia=int(input("Ingrese un día:"))
mes=int(input("Ingrese un mes:"))
año=int(input("Ingrese un año:"))

def diaValido(dia,mes,año):
    valor=True
    if dia<1 or dia>31:
        valor=False
    elif mes<1 or mes>12:
        valor=False
    elif año % 4==0 and año%100!= 0 and mes==2 and dia>=29:
        valor=True
    elif mes==2 and dia>28:
        valor=False
    elif (mes==4 or mes==6 or mes==9 or mes==11) and dia>30:
        valor=False
    return valor

final=diaValido(dia,mes,año)
print(final)
    