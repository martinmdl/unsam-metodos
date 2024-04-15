# input: dos reales a, b tales que a < b y f(a)*f(b) < 0, y un real epsilon > 0
# 8. Modificar la implementación del método de bisección para que:
# a) haga la menor cantidad posible de evaluaciones de la f en cada iteración
# b) vaya imprimiendo la secuencia de los puntos p que van aproximando a la raíz buscada
# c) que tenga una cota (grande) en la cantidad total de pasos que dará antes de devolver algo
# d) que devuelva, además del p encontrado, la cantidad de pasos que fueron necesarios para llegar a la aproximación buscada

import math

a, b = [-50, 50]
epsilon = 0.1
img = 12

def f(x):
    return x**2 + x

def cant_pasos(a, b, epsilon):
    return math.ceil(math.log2(abs(b - a) / epsilon))

# biseccion (metodo de parada: error absoluto)
def biseccion(a, b, epsilon):
    media = 1
    i = 1
    pasos = 0
    while(b - a >= epsilon):
        media = (a + b) / 2
        print(f"Media {i} = {media:.2f}")
        if(f(media) > img):
            b = media
        else:
            if(f(media) < img):
                a = media
            else:
                return media
        i += 1
        pasos += 1
    return media, pasos

n = cant_pasos(a, b, epsilon)
img_aprox, pasos = biseccion(a, b, epsilon)

print(f"Prediccion cant pasos: {n}")
print(f"Realidad cant pasos: {pasos}")
print(f"Respuesta: {img_aprox:.2f}")
print(f"F({img_aprox:.2f}) = {f(img_aprox)}")