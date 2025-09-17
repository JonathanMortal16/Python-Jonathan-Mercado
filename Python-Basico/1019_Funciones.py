"""
Comparador de futbolistas:
- Permite buscar un jugador por nombre (aunque se escriba en mayúsculas/minúsculas o con/sin acentos).
- Muestra sus atributos (pase, tiro, defensa, rol).
- Permite comparar esos atributos con los demás jugadores para ver quién tiene el máximo y mínimo.
- Usa un menú interactivo para elegir qué característica revisar.
"""

from typing import Optional, List, Tuple
import unicodedata

# -------------------- Utilidades --------------------

def normalizar(texto: str) -> str:
    """
    Quita acentos, convierte a minúsculas y elimina espacios innecesarios.
    Esto permite buscar nombres de forma más flexible.
    Ejemplo: "Mbappé", "MBAPPE", "mbappe " → "mbappe"
    """
    nfkd = unicodedata.normalize("NFKD", texto)
    sin_acentos = "".join(c for c in nfkd if not unicodedata.combining(c))
    return sin_acentos.casefold().strip()

def extremos_por_atributo(db: dict, atributo: str) -> Tuple[int, List[str], int, List[str]]:
    """
    Encuentra el valor máximo y mínimo de un atributo (pase, tiro o defensa).
    Retorna: (valor_máximo, lista_jugadores_con_ese_máximo, valor_mínimo, lista_jugadores_con_ese_mínimo).
    Esto permite manejar empates (varios jugadores con el mismo valor).
    """
    # Genera un diccionario con {nombre: valor} solo del atributo elegido
    valores = {nombre: ficha[atributo] for nombre, ficha in db.items()}
    vmax = max(valores.values())   # mayor valor del atributo
    vmin = min(valores.values())   # menor valor del atributo
    n_max = [n for n, v in valores.items() if v == vmax]  # jugadores con el valor máximo
    n_min = [n for n, v in valores.items() if v == vmin]  # jugadores con el valor mínimo
    return vmax, n_max, vmin, n_min

# -------------------- Base de datos --------------------

# Diccionario con futbolistas y sus atributos
FUTBOLISTAS_DB = {
    "Lionel Messi":   {"pase": 95, "tiro": 92, "defensa": 38, "rol": "delantero"},
    "Kevin De Bruyne":{"pase": 94, "tiro": 86, "defensa": 64, "rol": "mediocampista"},
    "Virgil van Dijk":{"pase": 73, "tiro": 60, "defensa": 92, "rol": "defensa"},
    "Kylian Mbappé":  {"pase": 80, "tiro": 91, "defensa": 36, "rol": "delantero"},
    "Luka Modrić":    {"pase": 90, "tiro": 79, "defensa": 72, "rol": "mediocampista"},
}

# Índice de búsqueda (sin acentos ni mayúsculas) → nombre real
NOMBRE_INDEX = {normalizar(nombre): nombre for nombre in FUTBOLISTAS_DB}

# -------------------- Lógica de negocio --------------------

def buscar_jugador(nombre: str) -> Optional[dict]:
    """
    Busca un futbolista por su nombre (en cualquier formato).
    Devuelve sus datos si existe o None si no está en la base.
    """
    can = NOMBRE_INDEX.get(normalizar(nombre))
    return FUTBOLISTAS_DB.get(can) if can else None

def nombre_canonico(nombre: str) -> Optional[str]:
    """
    Devuelve el nombre correcto del jugador tal como aparece en la base.
    Ejemplo: "messi", "MESSI" → "Lionel Messi".
    """
    return NOMBRE_INDEX.get(normalizar(nombre))

def mostrar_datos(nombre: str, datos: dict):
    """Muestra en pantalla los atributos de un futbolista de forma legible."""
    print("\n¡Futbolista encontrado!")
    print(f"Nombre  : {nombre}")
    print(f"Pase    : {datos['pase']}")
    print(f"Tiro    : {datos['tiro']}")
    print(f"Defensa : {datos['defensa']}")
    print(f"Rol     : {datos['rol']}")

def comparar_caracteristica(nombre: str, datos: dict, atributo: str):
    """
    Compara el valor del atributo elegido (pase, tiro o defensa) del jugador
    con el resto de la base de datos.
    Informa si está en el máximo, mínimo o en un nivel intermedio.
    """
    if atributo not in {"pase", "tiro", "defensa"}:
        print("Atributo no válido. Usa: pase, tiro o defensa.")
        return

    valor = datos[atributo]  # valor del jugador elegido
    vmax, lista_max, vmin, lista_min = extremos_por_atributo(FUTBOLISTAS_DB, atributo)

    print("\n--- Resultado de la comparación ---")
    if valor == vmax:
        print(f"¡{nombre} está en el TOPE de {atributo} ({valor})!")
    elif valor == vmin:
        print(f"¡{nombre} es el MÁS BAJO en {atributo} ({valor})!")
    else:
        print(f"{nombre} tiene {atributo} = {valor} (nivel intermedio).")

    # Mostrar todos los que empatan en máximo y mínimo
    print(f"Máximo en {atributo}: {', '.join(lista_max)} ({vmax})")
    print(f"Mínimo en {atributo}: {', '.join(lista_min)} ({vmin})")

def menu_jugador(nombre: str, datos: dict) -> bool:
    """
    Menú interactivo para comparar atributos de un jugador.
    Retorna True si el usuario quiere salir del programa,
    o False si quiere volver al menú principal para elegir otro jugador.
    """
    while True:
        print("\n--- Menú de Comparación ---")
        print("¿Qué quieres revisar? (pase, tiro, defensa)")
        print("Escribe 'menu' para volver o 'salir' para terminar.")
        opcion = normalizar(input("Opción: "))

        if opcion == "salir":
            print("Saliendo del programa. ¡Hasta la próxima!")
            return True  # señal de terminar todo
        if opcion == "menu":
            return False  # señal de volver al menú principal
        if opcion in {"pase", "tiro", "defensa"}:
            comparar_caracteristica(nombre, datos, opcion)
        else:
            print("Opción no válida. Elige entre 'pase', 'tiro', 'defensa', 'menu' o 'salir'.")

def main():
    """Función principal que gestiona el flujo del programa."""
    while True:
        print("\n-------------------------------------")
        nombre_ingresado = input("Ingresa el nombre de un futbolista (o 'salir' para terminar): ")

        # Opción para salir directamente
        if normalizar(nombre_ingresado) == 'salir':
            print("Saliendo del programa. ¡Hasta la próxima!")
            break

        # Buscar datos del jugador
        canon = nombre_canonico(nombre_ingresado)
        datos_jugador = buscar_jugador(nombre_ingresado)

        if datos_jugador and canon:
            mostrar_datos(canon, datos_jugador)
            terminar = menu_jugador(canon, datos_jugador)
            if terminar:  # Si el usuario eligió salir en el submenú
                break
        else:
            print(f"Lo siento, '{nombre_ingresado}' no está en la base. "
                  f"Prueba con: {', '.join(FUTBOLISTAS_DB.keys())}")

if __name__ == "__main__":
    main()
