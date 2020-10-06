def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    print(n)
    return fibonacci(n - 1)


fibonacci(int(input('Inserta un numero: ')))
