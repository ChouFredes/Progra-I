total1=int(input("Ingrese el total a pagar:"))
recibido=int(input("Ingrese el dinero recibido:"))
total2=recibido-total1

billete500=0
billete100=0
billete50=0
billete20=0
billete10=0
billete5=0
billete1=0


if recibido<total1:
    print("Dinero insuficiente.")
else:
    while total2!=0:
        billete500=total2//500
        total2=total2-500*billete500
        billete100=total2//100
        total2=total2-100*billete100
        billete50=total2//50
        total2=total2-50*billete50
        billete20=total2//20
        total2=total2-20*billete20
        billete10=total2//10
        total2=total2-10*billete10
        billete5=total2//5
        total2=total2-5*billete5
        billete1=total2//1
        total2=total2-1*billete1

    print("Se necesita/n", billete500, "billete/s de $500")
    print("Se necesita/n", billete100, "billete/s de $100")
    print("Se necesita/n", billete50, "billete/s de $50")
    print("Se necesita/n", billete20, "billete/s de $20")
    print("Se necesita/n", billete10, "billete/s de $10")
    print("Se necesita/n", billete5, "billete/s de $5")
    print("Se necesita/n", billete1, "billete/s de $1")


    