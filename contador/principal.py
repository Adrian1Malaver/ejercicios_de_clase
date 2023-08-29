from conteo import *
from abinario import *
from aoctal import *
from ahexadecimal import *

def main():
    print("Elige el sistema de conteo:")
    print("1. Decimal")
    print("2. Binario")
    print("3. Octal")
    print("4. Hexadecimal")
    op = int(input("Selecciona una opción: "))
    
    contar = None
    if op == 1:
        contar = conteo()
    elif op == 2:
        contar = hallarbin()
    elif op == 3:
        contar = hallaroct()
    elif op == 4:
        contar = hallarhex()
    else:
        print("Opción no válida")
        return
    
    while True:
        print(contar.get_value())
        contar.increment()

if __name__ == "__main__":
    main()
