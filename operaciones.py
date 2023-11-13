def sumar(a, b):
    # Comprobar si ambos parámetros son int o float
    if (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return a + b
    else:
        print("Error: Ambos parámetros deben ser int o float")

def restar(a, b):
    # Comprobar si ambos parámetros son int o float
    if (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return a - b
    else:
        print("Error: Ambos parámetros deben ser int o float")

def multiplicar(a, b):
    # Comprobar si ambos parámetros son int o float
    if (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        result = 0
        for i in range(abs(int(b))):
            result += a
        # Ajustar el signo del resultado según el signo de b
        if b < 0:
            result = -result
        return result
    else:
        print("Error: Ambos parámetros deben ser int o float")

# Ejemplos de uso
print(sumar(3, 4.5))         # Imprime: 7.5
print(restar(8, 2))           # Imprime: 6
print(multiplicar(2, 3))      # Imprime: 6
