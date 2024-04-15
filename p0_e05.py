# input: dos reales a, b tales que a < b y f(a)*f(b) < 0, y un real epsilon > 0
# 5. Aplicar el método de bisección para hallar una raíz aproximada de la función f(x) = x^3 + x - 10 haciendo 4 pasos.

def f(x):
    return x**3 + x - 10

a, b = [-8, 8]
n = 4 # número de pasos

# biseccion (metodo de parada: número de pasos)
def biseccion(a, b, n):
    media = 1
    for i in range(n):
        media = (a + b) / 2
        if(f(media) > 0):
            b = media
        else:
            if(f(media) < 0):
                a = media
            else:
                return media
    return media

raiz_aprox = biseccion(a, b, n)
print(f"Respuesta: {raiz_aprox}")
print(f"F({raiz_aprox:.2f}) = {f(raiz_aprox)}")