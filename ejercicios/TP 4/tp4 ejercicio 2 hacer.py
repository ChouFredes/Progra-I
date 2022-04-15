# 2. Leer una cadena de caracteres e imprimirla centrada en pantalla. Suponer que la 
# misma tiene 80 columnas.

centrarEntre = lambda string, longitud, relleno=" ": string.center(longitud, relleno)
centrarEntre("titulo", 80)