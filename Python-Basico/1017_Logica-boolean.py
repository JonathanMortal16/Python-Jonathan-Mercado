"""
Operadores relacionales en Python:
== -> Igual que
!= -> Diferente que
<  -> Menor que
>  -> Mayor que
<= -> Menor o igual que
>= -> Mayor o igual que
"""

# Pedir dos números al usuario
valor_1 = int(input("Ingrese el primer número: "))
valor_2 = int(input("Ingrese el segundo número: "))

# Comparaciones básicas entre valor_1 y valor_2
es_igual = valor_1 == valor_2
print("Son iguales: ", es_igual)

es_diferente = valor_1 != valor_2
print("Son diferentes: ", es_diferente)

es_menor = valor_1 < valor_2
print("El primero es menor que el segundo: ", es_menor)

es_mayor = valor_1 > valor_2
print("El primero es mayor que el segundo: ", es_mayor)

es_menor_igual = valor_1 <= valor_2
print("El primero es menor o igual que el segundo: ", es_menor_igual)

es_mayor_igual = valor_1 >= valor_2
print("El primero es mayor o igual que el segundo: ", es_mayor_igual)

# Pedir un tercer número
valor_3 = int(input("Ingrese un tercer número: "))

# Uso de operadores lógicos
condicion_and = valor_1 > valor_2 and valor_2 > valor_3
print("Valor 1 mayor que Valor 2 y Valor 2 mayor que Valor 3: ", condicion_and)

condicion_or = valor_1 == valor_2 or valor_2 < valor_3
print("Valor 1 igual a Valor 2 o Valor 2 menor que Valor 3: ", condicion_or)

# Negación de la última comparación
negacion = not condicion_or
print("Negando el resultado anterior: ", negacion)
