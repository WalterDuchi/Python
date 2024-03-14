user_word = input("Ingrese una palabra: ")

for letter in user_word:  # recorrer la palabra ingresada
    if letter in "aeiou":  # si la letra es una vocal
        user_word = user_word.replace(
            letter, ""
        )  # reemplazar la vocal por un espacio vacio

# imprimir la palabra sin vocales con mayusculas
print(user_word.upper())
