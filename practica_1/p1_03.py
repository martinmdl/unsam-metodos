# 3 – Aproximar una raíz cada una de las funciones del ejercicio 1 usando el método de 
# Newton,anderror posible usarlo. Para las funciones en las cuales no se pueda usar, 
# justificar.

# # Symbolic Differentiation (Derivada Simbólica)
# import sympy as sp
# x = sp.Symbol('x')  # Define x as a symbolic variable
# function = sp.exp(-x) - sp.sin(x)  # Define the function expression
# derivative = function.diff(x)  # Differentiate 'function' with respect to 'x'
# print(derivative)  # Output: (-e^(-x) - cos(x))

# Numerical Approximation Differentiation (Dervidad Numérica Aproximada)
import math as m

error = 0.0001

def fd(x, h, fun):
    return (fun(x + h) - fun(x)) / h

# a -> Xn
# b -> Xn+1
def newton(a, epsilon, f):

    try:
        b = a - f(a) / fd(a, epsilon, f)
    except ValueError:
        print(f"Error de dominio en una raíz o logaritmo:")
    except ZeroDivisionError:
        print(f"División por cero:")
    else:
        while abs(b - a) > epsilon:
            a = b
            try:
                b = b - f(b) / fd(b, epsilon, f)
            except ValueError:
                print(f"Error de dominio en una raíz o un logaritmo:")
                return 1
            except ZeroDivisionError:
                print(f"División por cero:")
                return 1

    return b

###########################################
# funcion_A f(x) = √x

def funcion_A(x):
    return m.sqrt(x)

raiz = newton(5, error, funcion_A)
print(f"f({raiz:.2f}) = {funcion_A(raiz)}")

###########################################
# funcion_B f(x) = x^3 +1 

def funcion_B(x):
    return x**3 + 1

raiz = newton(2, error, funcion_B)
print(f"f({raiz:.2f}) = {funcion_B(raiz)}")

###########################################
# funcion_C f(x) = x^3 - x + 1 

def funcion_C(x):
    return x**3 - x + 1

raiz = newton(2, error, funcion_C)
print(f"f({raiz:.2f}) = {funcion_C(raiz)}")

###########################################
# funcion_D f(x) = e^(-x) – sen x

def funcion_D(x):
    return m.exp(-x) - m.sin(x)

raiz = newton(2, error, funcion_D)
print(f"f({raiz:.2f}) = {funcion_D(raiz)}")

###########################################
# funcion_E f(x) = 2/x

def funcion_E(x):
    return 2 / x

raiz = newton(2, error, funcion_E)
print(f"f({raiz:.2f}) = {funcion_E(raiz)}")

###########################################
# funcion_F f(x) = |x + 5|

def funcion_F(x):
    return abs(x + 5)

raiz = newton(0, error, funcion_F)
print(f"f({raiz:.2f}) = {funcion_F(raiz)}")

###########################################
# funcion_G f(x) = 2*x + 3

def funcion_G(x):
    return 2*x + 3

raiz = newton(1, error, funcion_G)
print(f"f({raiz:.2f}) = {funcion_G(raiz)}")





















