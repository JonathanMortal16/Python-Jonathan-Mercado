# Constantes en Python (no existen como tal, pero se usan convenciones)

# Por convención, las constantes se escriben en MAYÚSCULAS
PI = 3.14159
GRAVEDAD = 9.81
VELOCIDAD_LUZ = 299_792_458  # en m/s

def calcular_area_circulo(radio):
    """Calcula el área de un círculo usando la 'constante' PI"""
    return PI * (radio ** 2)

def energia_potencial(masa, altura):
    """Calcula energía potencial usando la 'constante' GRAVEDAD"""
    return masa * GRAVEDAD * altura

def energia_relat(masa):
    """Calcula energía con E = mc^2 usando VELOCIDAD_LUZ"""
    return masa * (VELOCIDAD_LUZ ** 2)

# Ejemplo de uso
print("Área de un círculo de radio 5:", calcular_area_circulo(5))
print("Energía potencial de 10kg a 20m:", energia_potencial(10, 20))
print("Energía relativista de 1kg:", energia_relat(1))