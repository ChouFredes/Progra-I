def diadelasemana(dia,mes,año):    
    if mes < 3:
        mes = mes + 10
        año = año – 1
    else:
        mes = mes – 2
    siglo = año // 100
    año2 = año % 100
    diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

dia=int(input("Ingrese un día:"))
mes=int(input("Ingrese un mes:"))
año=int(input("Ingrese un año:"))

valor=True
if dia<1 or dia>31:
    valor=False
elif mes==2 and dia>28:
    valor=False
elif (mes==4 or mes==6 or mes==9 or mes==11) and dia>30:
    valor=False
elif año<1:
    valor=False

resultado=diadelasemana(dia,mes,año)
print(resultado)