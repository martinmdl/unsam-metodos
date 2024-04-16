# input: dos reales a, b tales que a < b y f(a)*f(b) < 0, y un real epsilon > 0
# 6. Aplicar el método de bisección para hallar una aproximación de un x que cumpla x^2 + x = 12. Calcular luego el valor exacto de otra manera, y comparar.

# ERROR DE CONSIGNA
# 7. Aplicar el método de bisección para aproximar un x que cumpla cos(x) = -1,
# con error menor que epsilon = 1/10. Notar que esto sirve para encontrar aproximaciones de pi.

def f(x):
    return x**2 + x

a, b = [-50, 50]
epsilon = 0.1
img = 12

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

# queda pendiente hallar un x / f(x) = 12 con otro método y comparar