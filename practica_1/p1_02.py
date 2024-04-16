# 2 – Elegir una f del ejercicio anterior tal que pueda usarse bisección, y aproximar una raíz de f 
# con un error tal que tenga los primeros 2 decimales correctos. 

import math as m

def biseccion(a, b, epsilon, f):
    
    while abs(b - a) >= epsilon:

        media = (b + a) / 2
        
        if f(media) >= 0:
            b = media

        elif f(media) < 0:
            a = media

    return media

###########################################
# funcion_B f(x) = x^3 +1 

def funcion_B(x):
    return x**3 + 1

error_epsilon = 0.01 # minimo para obtener 2 decimales correctos

raiz = biseccion(-3, 2, error_epsilon, funcion_B)
print(f"f({raiz:.2f}) = {funcion_B(raiz)}")