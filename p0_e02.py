# 2. Implementar en Python un proceso al estilo del anterior, pero que use dos funciones,
# una f y una g, y que la aplicación iterada sea una vez f, luego g, luego f, luego g,
# y así siguiendo, alternando una con otra, en total las veces que se especifique por el parámetro n,
# y finalmente devuelva el resultado obtenido tras la última aplicación.

# 3. ¿Se le ocurre alguna forma de entender la idea de aplicar una f infinitas veces?
# ¿Cómo se podría definir esa aplicación infinitaria, y de qué dependerá que esté bien definida?

def f(x):
    return x * 2 - 1

def g(x):
    return x * 2 + 3

x = 2
n = 4
i = 0

while(i < n):
    if(i % 2 == 0):
        x = f(x)
    else:
        x = g(x)
    i += 1

print(f"RESULTADO: {x}")