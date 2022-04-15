# Archivo 2: Los campos están separados por el signo #.
# Pérez Juan#20080211#Corrientes 348
# González Ana M#20080115#Juan de Garay 1111 3er piso Dto A

try:
    arch=open("archivo2.txt","rt")
    lista=[]
    for palabra in arch:
        lista.append(palabra)
except OSError as mensaje:
    print("No se puede grabar el archivo:", mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass

try:
    arch=open("archivo2nuevo.txt","wt")
    for i in range(len(lista)):
        cad="".join(lista[i])
        cad=cad.replace("#",";")
        arch.write(cad)
except OSError as mensaje:
    print("No se puede grabar el archivo:", mensaje)
finally:
    try:
        arch.close()
    except NameError:
        pass
