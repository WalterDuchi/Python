# Función que imprime los primeros 50 números de la serie de Fibonacci
def listaFigonacci():
    a = 0
    print(1, a, sep=": ")
    b = 1
    print(2, b, sep=": ")
    c = a + b
    print(3, c, sep=": ")

    for i in range(4, 51):
        a = b
        b = c
        c = a + b
        print(i, c, sep=": ")


listaFigonacci()
