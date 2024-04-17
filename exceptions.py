import math as m

x = -1

try: # code that you expect might raise exceptions
    m.sqrt(x)
except ValueError as e: # except blocks to handle different types of exceptions
    print(f"HOLA = {e}")
except ZeroDivisionError as e: # idem
    print(f"HOLA = {e}")
else: # executed only if no exceptions occur
    print(f"MOLESTO")
finally: # always executed (release resources that need to happen even in case of exceptions)
    print(f"CHAU = {x}")






















