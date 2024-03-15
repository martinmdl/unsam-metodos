# input: dos reales a, b tales que a < b y f(a)*f(b) < 0, y un real epsilon > 0
# 9. Método de trisección. Implementar en Python un método para aproximar raíces al estilo de bisección,
# pero que en vez de dividir el intervalo en 2 subintervalos lo divida en 3,
# y en cada iteración elija uno de los 3 subintervalos que contenga una raíz.
# Usar una condición de parada análoga a la del método de bisección.

import math

def f(x):
    return x**3 + x - 10

a, b = [-50, 50]
epsilon = 0.01

# biseccion (metodo de parada: error absoluto)
def triseccion(a, b, epsilon):
    media = 1

    while(b - a >= epsilon):

        tercio = abs(b - a) / 3
        primer_tercio = a + tercio
        segundo_tercio = primer_tercio + tercio

        if(f(primer_tercio) > 0): b = primer_tercio
        else:
            if(f(segundo_tercio) < 0): a = segundo_tercio
            else:
                a = primer_tercio
                b = segundo_tercio
            
    media = (primer_tercio + segundo_tercio) / 2
    return media

raiz = triseccion(a, b, epsilon)
print(f"Raiz: {raiz:.2f}")
print(f"F({raiz:.2f}) = {f(raiz)}")
