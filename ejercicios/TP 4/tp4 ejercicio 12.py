# 12. Escribir un programa para crear una lista por comprensión con los naipes de la baraja española. La lista debe contener cadenas de caracteres.
# Ejemplo: ["1 Oros", "2 Oros"... ]. Imprimir la lista por pantalla.

barajas=["Oros","Bastos","Espadas","Copas"]
lista=[[i,barajas[x]]for i in range(1,13) for x in range(len(barajas))]
print(lista)
