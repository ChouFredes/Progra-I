# GrabarRangoAlturas() Graba en un archivo las alturas de los atletas de distintas 
# disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una 
# línea distinta. Ejemplo:
# <Deporte 1>
# <altura del atleta 1>
# <altura del atleta 2>

def GrabarRangoAlturas():
    try:
        arch=open("atletas1.txt","wt")
        deporte=input("Ingrese el deporte:(Enter para terminar):")
        while deporte!="":
            arch.write(deporte,)
            arch.write("\n")
            atleta=str(input("Ingrese el atleta:(Enter para terminar):"))
            while atleta!="":
                atleta=str(atleta)
                arch.write(atleta)
                arch.write("\n")
                atleta=str(input("Ingrese el atleta:(Enter para terminar):"))
            deporte=input("Ingrese el deporte:(Enter para terminar):")        
    except OSError as mensaje:
        print("No se puede grabar el archivo:", mensaje)
    finally:
        try:
            arch.close()
        except NameError:
            pass

GrabarRangoAlturas()