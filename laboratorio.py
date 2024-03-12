user_word = input("Ingrese una palabra: ")

for letter in user_word:
    if letter in "aeiou":
        user_word = user_word.replace(letter, "")
print(user_word)
