palabraSecreta = "chupacabra"

while True:
    palabra = input("Introduce la palabra secreta: ")
    if palabra == palabraSecreta:
        print("¡Felicidades! Has adivinado la palabra secreta.")
        break
    else:
        print("¡Inténtalo de nuevo!")
