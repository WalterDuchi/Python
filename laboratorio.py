blocks = int(input("Ingrese el número de bloques: "))

altura = 0
i = 1
while i <= blocks:  # Mientras que i sea menor o igual a blocks
    blocks -= i  # Restamos i a blocks
    i += 1  # Aumentamos i en 1
    altura += 1  # Aumentamos la altura en 1

print("La altura de la pirámide:", altura)
