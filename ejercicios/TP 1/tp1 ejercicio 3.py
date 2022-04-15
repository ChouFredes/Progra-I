presio=float(input("Ingrese el precio del boleto:"))
viajes=int(input("Ingrese la cantidad de viajes:"))

if presio<=0:
    presio=int(input("Ingrese un número válido:"))

if viajes<=0:
    viajes=int(input("Ingrese un número válido:"))

final=presio*viajes

if viajes>40:
    print("El precio final es de $", final*0.60)
elif viajes>30:
    print("El precio final es de $", final*0.70)
elif viajes>20:
    print("El precio final es de $", final*0.80)
elif viajes>0:
    print("El precio final es de $", final)