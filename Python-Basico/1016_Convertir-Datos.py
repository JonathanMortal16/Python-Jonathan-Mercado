# Pedir dos números como texto (string)
valor_a = input("Ingrese el primer número a sumar: ")
valor_b = input("Ingrese el segundo número a sumar: ")

# Realizar la suma (como string se concatenan, no se suman numéricamente)
resultado = valor_a + valor_b
print(f"Tipo de valor_a: {type(valor_a)}")  # Verificar tipo de dato (str)
print(f"Tipo de valor_b: {type(valor_b)}")  # Verificar tipo de dato (str)
print(resultado)                            # Muestra la "suma" (concatenación de cadenas)
print(f"Tipo de resultado: {type(resultado)}")  # Tipo de dato de la suma

print("**Convirtiendo a enteros**")

# Convertir los valores a enteros (int) para sumarlos correctamente
valor_a = int(valor_a)
valor_b = int(valor_b)
resultado = valor_a + valor_b
print(f"Tipo de valor_a: {type(valor_a)}")  # Ahora es int
print(f"Tipo de valor_b: {type(valor_b)}")  # Ahora es int
print(resultado)                            # Muestra la suma correcta
print(f"Tipo de resultado: {type(resultado)}")  # Ahora el resultado es int

# Ejemplo con un entero y un flotante
valor_a = int(input("Ingrese un número entero a sumar: "))
valor_b = float(input("Ingrese un número flotante a sumar: "))
resultado = valor_a + valor_b
print(resultado)                            # Suma entre int + float = float
print(f"Tipo de resultado: {type(resultado)}")  # Tipo float

# Convertir el resultado a entero (pierde la parte decimal)
resultado = int(resultado)
print("**Convertir a entero**")
print(resultado)
print(f"Tipo de resultado: {type(resultado)}")  # Ahora es int

# Convertir el resultado entero a hexadecimal
print("**Convertiendo a otro tipo**")
valor_hex = hex(resultado)
print(valor_hex)                             # Mostrar en formato hexadecimal
print(f"Tipo del cambio: {type(valor_hex)}")  # El tipo es str