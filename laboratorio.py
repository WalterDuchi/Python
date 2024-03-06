"""
# ejemplo de inicialización de todos los tipos de elementos en python

# Inicializar variables
# Enteros
a = 1
print("a=", a, type(a))
# Flotantes
b = 1.5
print("b=", b, type(b))
# Cadenas
c = "Hola Mundo"
print("c=", c, type(c))
# Listas
d = [1, 2, 3, 4, 5]
print("d=", d, type(d))
# Tuplas
e = (1, 2, 3, 4, 5)
print("e=", e, type(e))
# Diccionarios
f = {"a": 1, "b": 2, "c": 3}
print("f=", f, type(f))
# Arreglos
g = [1, 2, 3, 4, 5]
print("g=", g, type(g))
# Dataframes
h = {"a": [1, 2, 3, 4, 5], "b": [6, 7, 8, 9, 10]}
print("h=", h, type(h))
# Gráficos
i = ([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
print("i=", i, type(i))
# Mapas de calor
j = h
print("j=", j, type(j))


# Imprimir tipos de variables
print("\nTipos de variables")
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))
print(type(i))
print(type(j))

"""

# Diapositiva 2.4.1.6
a = 3.0
b = 4.0
c = (a**2 + b**2) ** 0.5
print("c=", c)

# Diapositiva 2.4.1.7
juan = 3
maria = 5
adan = 6
print("Juan=", str(juan), "Maria=", str(maria), "Adan=", str(adan))
print("Juan=%d Maria=%d Adan=%d" % (juan, maria, adan))
"""
print("Juan=" + juan.__str__() + " Maria=" + maria.__str__())
"""
print("Juan={}, Maria={}, Adan={}".format(juan, maria, adan))
print(f"Juan={juan} Maria={maria} Adan={adan}")

total_manzanas = juan + maria + adan
print("Total de manzanas=", total_manzanas)

# Diapositiva 2.4.1.9
kilometers = 12.25
miles = 7.38
miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61
print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")

# Diapositiva conversiones
# convertir kg a libras
kg = 10
libras = kg * 2.20462
print(kg, "kilogramos es igual a", round(libras, 2), "libras")

# convertir usd a euros
usd = 100
euros = usd * 0.92  # precio en este preciso momento segun Refinitiv
print(usd, "dolares es igual a", round(euros, 2), "euros")

# convertir meses a hora
meses = 2
horas = meses * 30 * 24
print(meses, "meses es igual a", horas, "horas")

# convertir galones a onzas
galones = 2
onzas = galones * 128
print(galones, "galones es igual a", onzas, "onzas")

# convertir pies a metros
a = float(input("Ingrese un valor para a: "))
b = float(input("Ingrese un valor para b: "))
print("a+b=", a + b)
print("a-b=", a - b)
print("a*b=", a * b)
print("a/b=", a / b)
print("\nEso es todo, amigos!")
