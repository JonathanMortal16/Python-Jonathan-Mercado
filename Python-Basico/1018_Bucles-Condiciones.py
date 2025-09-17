"""
Comparador de Pokémon
- Base de datos con stats: ataque, defensa, velocidad, tipo
- Búsqueda tolerante a acentos y mayúsculas
- Menú para comparar un stat contra el resto del plantel
"""

import unicodedata

def normalizar(txt: str) -> str:
    """Quita acentos, baja a minúsculas y recorta espacios."""
    nfkd = unicodedata.normalize("NFKD", txt)
    sin_acentos = "".join(c for c in nfkd if not unicodedata.combining(c))
    return sin_acentos.casefold().strip()

# --- Base de datos de Pokémon -------------------------------------------------
pokedex = {
    "Pikachu":   {"ataque": 55, "defensa": 40, "velocidad": 90, "tipo": "eléctrico"},
    "Charizard": {"ataque": 84, "defensa": 78, "velocidad": 100, "tipo": "fuego/volador"},
    "Blastoise": {"ataque": 83, "defensa": 100, "velocidad": 78, "tipo": "agua"},
    "Venusaur":  {"ataque": 82, "defensa": 83, "velocidad": 80, "tipo": "planta/veneno"},
    "Gengar":    {"ataque": 65, "defensa": 60, "velocidad": 110, "tipo": "fantasma/veneno"},
}

# Índice auxiliar para búsqueda robusta
indice_nombres = {normalizar(nombre): nombre for nombre in pokedex}

# --- Loop principal -----------------------------------------------------------
while True:
    print("\n================= POKÉDEX =================")
    nombre_in = input("Escribe un Pokémon (o 'salir' para terminar): ")

    if normalizar(nombre_in) == "salir":
        print("¡Hasta la próxima, entrenador!")
        break

    clave = normalizar(nombre_in)
    if clave not in indice_nombres:
        print(f"No encontré '{nombre_in}'. Prueba con: {', '.join(pokedex.keys())}")
        continue

    nombre_pk = indice_nombres[clave]
    ficha = pokedex[nombre_pk]
    print(f"\n¡Pokémon encontrado!\n"
          f"Nombre    : {nombre_pk}\n"
          f"Ataque    : {ficha['ataque']}\n"
          f"Defensa   : {ficha['defensa']}\n"
          f"Velocidad : {ficha['velocidad']}\n"
          f"Tipo      : {ficha['tipo']}")

    # Submenú de comparación
    while True:
        print("\n--- Menú de Comparación ---")
        print("¿Qué stat quieres revisar? (ataque, defensa, velocidad)")
        print("Escribe 'menu' para elegir otro Pokémon o 'salir' para terminar.")
        opcion = normalizar(input("Opción: "))

        if opcion == "salir":
            print("¡Hasta la próxima, entrenador!")
            raise SystemExit(0)
        if opcion == "menu":
            break
        if opcion not in {"ataque", "defensa", "velocidad"}:
            print("Opción no válida. Elige: ataque, defensa, velocidad, menu o salir.")
            continue

        valor_objetivo = pokedex[nombre_pk][opcion]
        # Encontrar máximo y mínimo del stat elegido
        nombre_max = max(pokedex, key=lambda n: pokedex[n][opcion])
        nombre_min = min(pokedex, key=lambda n: pokedex[n][opcion])
        valor_max = pokedex[nombre_max][opcion]
        valor_min = pokedex[nombre_min][opcion]

        print("\n--- Resultado de la comparación ---")
        if valor_objetivo == valor_max:
            print(f"¡{nombre_pk} está en el TOPE de {opcion} ({valor_objetivo})!")
        elif valor_objetivo == valor_min:
            print(f"¡{nombre_pk} es el MÁS BAJO en {opcion} ({valor_objetivo})!")
        else:
            print(f"{nombre_pk} tiene {opcion} = {valor_objetivo} (nivel intermedio).")

        print(f"Máximo en {opcion}: {nombre_max} ({valor_max}) | Mínimo: {nombre_min} ({valor_min})")
