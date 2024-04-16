# 1 – Emplear el método de bisección y hacer los primeros 3 pasos, con el fin de aproximar una 
# raíz para cada una de las siguientes funciones, cuando sea posible usarlo. Para las funciones 
# en las cuales no se pueda usar, justificar. 

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
# funcion_A f(x) = √x

def funcion_A(x):
    return m.sqrt(x)

raiz = biseccion(0, 2, 0.001, funcion_A)
print(f"f({raiz:.2f}) = {funcion_A(raiz)}")

###########################################
# funcion_B f(x) = x^3 +1 

def funcion_B(x):
    return x**3 + 1

raiz = biseccion(-3, 2, 0.001, funcion_B)
print(f"f({raiz:.2f}) = {funcion_B(raiz)}")

###########################################
# funcion_C f(x) = x^3 - x + 1 

def funcion_C(x):
    return x**3 - x + 1

raiz = biseccion(-3, 2, 0.001, funcion_C)
print(f"f({raiz:.2f}) = {funcion_C(raiz)}")

###########################################
# funcion_D f(x) = e^(-x) – sen x 
# no sirve porque tiene infinitas raíces

def funcion_D(x):
    return m.exp(-x) - m.sin(x)

raiz = biseccion(-1, 2, 0.001, funcion_D)
print(f"f({raiz:.2f}) = {funcion_D(raiz)}")

###########################################
# funcion_E f(x) = 2/x
# no sirve porque no está definida en 0

def funcion_E(x):
    return 2 / x

raiz = biseccion(-1, 2, 0.001, funcion_E)
print(f"f({raiz:.2f}) = {funcion_E(raiz)}")

###########################################
# funcion_F f(x) = |x + 5| 
# no sirve porque f(a) * f(b) > 0

def funcion_F(x):
    return abs(x + 5)

raiz = biseccion(-6, 0, 0.001, funcion_F)
print(f"f({raiz:.2f}) = {funcion_F(raiz)}")

###########################################
# funcion_G f(x) = 2*x + 3

def funcion_G(x):
    return 2*x + 3

raiz = biseccion(-3, -1, 0.001, funcion_G)
print(f"f({raiz:.2f}) = {funcion_G(raiz)}")





















