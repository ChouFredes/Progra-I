# 3. Desarrollar una función que devuelva una cadena de caracteres con el nombre del 
# mes cuyo número se recibe como parámetro. Los nombres de los meses deberán 
# obtenerse de una lista de cadenas de caracteres inicializada dentro de la función. 
# Devolver una cadena vacía si el número de mes es inválido. La detección de meses 
# inválidos deberá realizarse a través de excepciones.

def meses(mes):
    meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    try:
        assert 1<=mes<=12
        fin=mes-1
        print(meses[fin])
    except AssertionError:
        print("")
    except TypeError:
        print("")
    return ""

