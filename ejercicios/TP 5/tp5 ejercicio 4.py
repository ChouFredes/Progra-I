# 4. Todo programa Python es susceptible de ser interrumpido mediante la pulsación de 
# las teclas Ctrl-C, lo que genera una excepción del tipo KeyboardInterrupt.
# Realizar un programa para imprimir los números enteros entre 1 y 100000,
# y que solicite confirmación al usuario antes de detenerse cuando se presione Ctrl-C.

while True:
    try:
        for i in range(1,100000):
            print(i)
    except KeyboardInterrupt:
        print("Detención momentánea.")
        a=input("¿Desea finalizar el programa?(S/N):")
        if a.upper()=="S":
            raise
    else:
        break
                
                
