def sumaIterativa(n):
    suma = 0
    while n > 9:
        suma += n % 10
        n //= 10
    return suma + n

def sumaRecursiva(n):
    if n <= 9:
        return n
    else:
        return sumaRecursiva(n // 10) + n % 10

def main():
    numero = int(input("Ingresa un número: "))

    sumaIterativaResultado = sumaIterativa(numero)
    sumaRecursivaResultado = sumaRecursiva(numero)

    print("Suma iterativa:", sumaIterativaResultado)
    print("Suma recursiva:", sumaRecursivaResultado)

if __name__ == "__main__":
    main()

