# 0. Tomar una calculadora de mano (puede ser la de Windows, una TI59, una HP16 u otra).
# Elegir una función existente, por ej. cos, o bien f(x) = x^2 - 1, u otra. Introducir un número x en el display.
# Calcular la función aplicada a ese número que se ve. Aplicar nuevamente la función, y otra vez más, y así siguiendo.
# Probar esto con distintos x. ¿Ocurre algo notable... a veces? (Dependerá de la función elegida, y del x inicialmente elegido.)
# Por ejemplo, sin poner ningún x, pulsar reiteradamente la tecla "coseno".

# 1. Implementar en Python el proceso anterior, que use una función (externa implementada, o bien pasada como parámetro),
# que lea el x como parámetro y un n natural, y luego sobre el ex inicial aplique la f n veces,
# finalmente devolviendo el resultado obtenido tras la última aplicación.

def f(x):
    return x * 2 - 1

x = 2
n = 4
i = 1

while(i <= n):
    res = f(x)
    x = res
    i += 1

print(f"RESULTADO: {x}")