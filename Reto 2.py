palabra1 = ""
palabra2 = ""
continuar = ""

while True:
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    print(sorted(palabra1) == sorted(palabra2))

    print("Desea continuar? (s/n): ")
    continuar = input()

    if continuar != "s" and continuar != "S":
        break
