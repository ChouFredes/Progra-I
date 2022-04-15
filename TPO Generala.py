import random

completa=[]

def tirarDados():
    tirada=[]
    for i in range(5):        
        n=random.randint(1,6)
        tirada.append(n)
    print("Su mano es:",tirada)
    completa.append(tirada)
    return tirada

def comprobarFull(tirada):
    tirada.sort()
    if tirada[0]==tirada[1] and tirada[2]==tirada[3] and tirada[2]==tirada[4]:
        return True
    if tirada[0]==tirada[1] and tirada[0]==tirada[2] and tirada[3]==tirada[4]:
        return True
    else:
        return False

def comprobarEscalera(tirada):
    tirada.sort()
    if tirada==[1,2,3,4,5] or tirada==[2,3,4,5,6]:
        return True
    else:
        return False

def comprobarPoker(tirada):
    tirada.sort()
    if tirada[0]==tirada[1] and tirada[0]==tirada[2] and tirada[0]==tirada[3] and tirada[0]!=tirada[4]:
        return True
    if tirada[1]==tirada[2] and tirada[1]==tirada[3] and tirada[1]==tirada[4] and tirada[0]!=tirada[1]:
        return True
    else:
        return False
    
def comprobarGenerala(tirada):
    val=False
    for x in range(1,6):
        if tirada.count(x)==5:
            val=True
            break
    return val

def comprobarGenerala2(tirada):
    val=False
    for x in range(1,6):
        if tirada.count(x)==5:
            val=True
            break
    return val

def contarPuntos(puntuacion):
    punt="".join(puntuacion)
    val=punt.isdigit()
    return val

def cambiarDados(dados):
    aux=[]
    camb=int(input("Ingrese el/los dado/s que desea cambiar (-1 para terminar):"))
    aux.append(camb)
    while camb!=-1:
        while aux.count(camb)>1:
            aux.remove(camb)
            camb=int(input("Error, ingrese un dado nuevo (-1 para terminar):"))
        dados[camb]=random.randint(1,6)
        camb=int(input("Ingrese el/los dado/s que desea cambiar (-1 para terminar):"))
        aux.append(camb)
    
    
# Programa principal
puntuacion=["a","a","a","a","a","a","a","a","a","a","a"]
while contarPuntos(puntuacion)==False:
    puntuacionAux=[]
    cont=0
    while cont<3:        
        dados=tirarDados()
        cont=cont+1
        seguir=int(input("Desea finalizar el turno?(1 es si, 0 es no):"))
        if seguir==1:
            break
        else:
            cambiarDados(dados)
            cont=cont+1
            print(dados)
            seguir=int(input("Desea finalizar el turno?(1 es si, 0 es no):"))
            if seguir==1:
                break
            else:
                print(dados)
                cambiarDados(dados)                
                cont=cont+1
    for i in range(1,7):
        c=dados.count(i)
        puntuacionAux.append(c*i)
    if comprobarEscalera(dados)==True:
        puntuacionAux.append(20)
    if comprobarEscalera(dados)==True and cont==1:
        puntuacionAux.append(20)
    if comprobarEscalera(dados)==False:
        puntuacionAux.append(0)
    if comprobarFull(dados)==True:
        puntuacionAux.append(30)
    if comprobarFull(dados)==True and cont==1:
        puntuacionAux.append(35)
    if comprobarFull(dados)==False:
        puntuacionAux.append(0)
    if comprobarPoker(dados)==True:
        puntuacionAux.append(40)
    if comprobarPoker(dados)==True and cont==1:
        puntuacionAux.append(45)
    if comprobarPoker(dados)==False:
        puntuacionAux.append(0)
    if comprobarGenerala(dados)==True:
        puntuacionAux.append(50)
    if comprobarGenerala(dados)==True and cont==1:
        puntuacionAux.append(55)
    if comprobarGenerala(dados)==False:
        puntuacionAux.append(0)
    if puntuacion[9]!="a":
        if comprobarGenerala2(dados)==True:
            puntuacionAux.append(100)
        if comprobarGenerala2(dados)==True and cont==1:
            puntuacionAux.append(105)
        if comprobarGenerala2(dados)==False:
            puntuacionAux.append(0)
    print(puntuacionAux)
     
     
    



