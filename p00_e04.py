# input: dos reales a, b tales que a < b y f(a)*f(b) < 0, y un real epsilon > 0
# 4. Aplicar el método de bisección para hallar una raíz aproximada de la función f(x) = x^3 + x - 5, comenzando con el intervalo [1,2], y el error epsilon = 0.5.

def f(x):
    return x**3 + x - 5

a, b = [1, 2]
epsilon = 0.5 # (epsilon -> 0) => (f(raiz_aprox) -> 0) 

# biseccion (metodo de parada: error absoluto)
def biseccion(a, b, epsilon):
    media = 1
    while(b - a >= epsilon):
        media = (a + b) / 2
        if(f(media) > 0):
            b = media
        else:
            if(f(media) < 0):
                a = media
            else:
                return media
    return media

raiz_aprox = biseccion(a, b, epsilon)
print(f"Respuesta: {raiz_aprox:.2f}")
print(f"F({raiz_aprox:.2f}) = {f(raiz_aprox)}")