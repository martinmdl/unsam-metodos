import math as m


# a, b = [1, 4]

# a = abs(a)
# b = abs(b)

# tercio = abs(b) - abs(a) / 3

# print(f"RESULTADO A: {a}")

# print(f"RESULTADO B: {b}")

x = -1

try:
    m.sqrt(x)
except ValueError as e:
    print(f"HOLA = {e}")
else:
    print(f"MOLESTO")
finally:
    print(f"CHAU = {x}")