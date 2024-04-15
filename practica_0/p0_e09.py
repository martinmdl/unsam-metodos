# input: dos reales a, b tales que a < b y f(a)*f(b) < 0, y un real epsilon > 0
# 9. Método de trisección. Implementar en Python un método para aproximar raíces al estilo de bisección,
# pero que en vez de dividir el intervalo en 2 subintervalos lo divida en 3,
# y en cada iteración elija uno de los 3 subintervalos que contenga una raíz.
# Usar una condición de parada análoga a la del método de bisección.

import math

def f(x):
    return x**3 + x - 10

def signo(a, b):
    return f(a) * f(b)

def triseccion(a, b, epsilon):
    
    while b - a >= epsilon:

        tercio = abs(b - a) / 3
        primer_tercio = a + tercio
        segundo_tercio = b - tercio

        if signo(a, primer_tercio) <= 0:
            b = primer_tercio

        elif signo(primer_tercio, segundo_tercio) <= 0:
            a = primer_tercio
            b = segundo_tercio
        
        elif signo(segundo_tercio, b) <= 0:
            a = segundo_tercio
            
    return (a + b) / 2

a, b = [1, 4]
epsilon = 0.001

raiz = triseccion(a, b, epsilon)
print(f"Raiz: {raiz:.2f}")
print(f"F({raiz:.2f}) = {f(raiz)}")
