# 4. Escribir una función que reciba como parámetro un número entero entre 0 y 3999 
# y lo convierta en un número romano, devolviéndolo en una cadena de caracteres. 
# ¿En qué cambiaría la función si el rango de valores fuese diferente?

numero=int(input("Ingrese un número entre 0 y 3999:"))
while numero>3999 or numero<0:
    numero=int(input("Error.Ingrese un número entre 0 y 3999:"))

def numRomano(numero):
    lista=[]
    num=str(numero)
    if len(num)==1:
        for i in range(len(num)):
            if num[i]=="0":
                lista.append()
            elif num[i]=="1":
                lista.append("I")
            elif num[i]=="2":
                lista.append("II")
            elif num[i]=="3":
                lista.append("III")            
            elif num[i]=="4":
                lista.append("IV")
            elif num[i]=="5":
                lista.append("V")
            elif num[i]=="6":
                lista.append("VI")
            elif num[i]=="7":
                lista.append("VII")
            elif num[i]=="8":
                lista.append("VIII")
            elif num[i]=="9":
                lista.append("IX")
    if len(num)==2:
        for i in range(len((num))-1):
            if num[i]=="1":
                lista.append("X")
            elif num[i]=="2":
                lista.append("XX")
            elif num[i]=="3":
                lista.append("XXX")
            elif num[i]=="4":
                lista.append("XL")
            elif num[i]=="5":
                lista.append("L")
            elif num[i]=="6":
                lista.append("LX")
            elif num[i]=="7":
                lista.append("LXX")
            elif num[i]=="8":
                lista.append("LXXX")
            elif num[i]=="9":
                lista.append("XC")
        for i in range(len((num))-1):
            if num[i+1]=="0":
                lista.append()
            elif num[i+1]=="1":
                lista.append("I")
            elif num[i+1]=="2":
                lista.append("II")
            elif num[i+1]=="3":
                lista.append("III")            
            elif num[i+1]=="4":
                lista.append("IV")
            elif num[i+1]=="5":
                lista.append("V")
            elif num[i+1]=="6":
                lista.append("VI")
            elif num[i+1]=="7":
                lista.append("VII")
            elif num[i+1]=="8":
                lista.append("VIII")
            elif num[i+1]=="9":
                lista.append("IX")
    return lista

final=numRomano(numero)
romano="".join(final)
print("Su número convertido a romano es:",romano)
    