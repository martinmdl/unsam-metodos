# input: dos reales a, b tales que a < b y f(a)*f(b) < 0, y un real epsilon > 0
# 7. Aplicar el método de bisección para aproximar un x que cumpla cos(x) = -1, con error menor que epsilon = 1/10. Notar que esto sirve para encontrar aproximaciones de pi.

import math

def f(x):
    xrad = math.radians(x)
    return math.cos(xrad)
    # return math.cos(x)

a, b = [0, 540]
epsilon = 1/10
img = -1

# biseccion (metodo de parada: error absoluto)
def biseccion(a, b, epsilon):
    media = 1
    while(b - a >= epsilon):
        media = (a + b) / 2
        if(f(media) > img):
            b = media
        else:
            if(f(media) < img):
                a = media
            else:
                return media
    return media

img_aprox = biseccion(a, b, epsilon)
print(f"Respuesta: {img_aprox:.2f}")
print(f"F({img_aprox:.2f}) = {f(img_aprox)}")

# NO FUNCIONA