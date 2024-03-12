# Escribe un bucle for que cuente hasta cinco.
# Cuerpo del bucle: imprime el número del contador y la palabra "Mississippi".
# Cuerpo del bucle - usar: time.sleep (1)

# Importa el módulo time al principio de tu programa.
import time

for i in range(1, 6):
    print(i, "Mississippi")
    time.sleep(1)

# Escribe un bucle while que cuente hasta cinco.
i = 1
while i <= 5:
    print(i, "Mississippi")
    # Cuerpo del bucle - usar: time.sleep (1)
    time.sleep(1)
    i += 1
