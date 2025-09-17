consolas = {
    "PlayStation 5": {
        "fabricante": "Sony",
        "generacion": "Novena",
        "lanzamiento": 2020,
    },
    "Xbox Series X": {
        "fabricante": "Microsoft",
        "generacion": "Novena",
        "lanzamiento": 2020,
    },
    "Nintendo Switch": {
        "fabricante": "Nintendo",
        "generacion": "Octava/Nueva Híbrida",
        "lanzamiento": 2017,
    }
}

# Buscar consola
print("Las consolas actuales en el diccionario son: PlayStation 5, Xbox Series X, Nintendo Switch")
consola_buscar = input("Indique la consola a buscar:\n")
print(f"\nInformación de la consola: {consola_buscar}")
print(f"Fabricante: {consolas[consola_buscar]['fabricante']}")
print(f"Lanzamiento: {consolas[consola_buscar]['lanzamiento']}")

# Agregar una nueva consola
consolas["Steam Deck"] = {
    "fabricante": "Valve",
    "generacion": "Portátil/Híbrida",
    "lanzamiento": 2022,
}
print("\n--- Diccionario actualizado con 'Steam Deck' ---")
print(consolas)
print("Las consolas actuales en el diccionario son: PlayStation 5, Xbox Series X, Nintendo Switch, Steam Deck")


# Eliminar una consola
consola_eliminar = input("\nIndique la consola a eliminar: ")
del consolas[consola_eliminar]
print(f"\n--- Diccionario después de eliminar '{consola_eliminar}' ---")
print(consolas)
