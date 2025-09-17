# MUTABILIDAD, INMUTABILIDAD Y HASHABILIDAD EN PYTHON

# --- OBJETOS MUTABLES ---
# Son los que pueden cambiar su valor después de creados
lista = [10, 30, 40]
print("Lista original:", lista)
lista[0] = 20
print("Lista modificada:", lista)

# Los diccionarios también son mutables
diccionario = {"a": 1, "b": 2}
print("Diccionario original:", diccionario)
diccionario["a"] = 100
print("Diccionario modificado:", diccionario)

print("-" * 40)

# --- OBJETOS INMUTABLES ---
# No pueden cambiar su valor después de creados
tupla = (10, 20, 30, 40)
print("Tupla:", tupla)

numero = 50
print("Número entero:", numero)

# Si intentamos modificar un entero o tupla directamente -> error
# tupla[0] = 100  # Descomenta y verás un TypeError
# numero[0] = 60  # No es posible

print("-" * 40)

# --- OBJETOS HASHABLES ---
# Un objeto hashable:
#   1. Es inmutable
#   2. Tiene un valor de hash constante en tiempo de ejecución
#   3. Puede compararse con otros de su tipo

saludo = "Hola Humano"
print("Cadena:", saludo)
print("Hash del saludo:", hash(saludo))

# Las tuplas también pueden ser hashables
tupla2 = (1, 2, 3)
print("Tupla hashable:", tupla2)
print("Hash de la tupla:", hash(tupla2))

# Ojo: una tupla solo es hashable si TODOS sus elementos son inmutables
# tupla_mala = (1, [2, 3])  # Esto da error porque incluye una lista (mutable)