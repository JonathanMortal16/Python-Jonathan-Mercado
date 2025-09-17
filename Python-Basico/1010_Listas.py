#Listas sirven para guardar varios datos en una variable se usa []
personaje_1 = ["La mole","Tanque", 100, 60, 40]
print("Tu personaje es:", personaje_1)

#Metodos para listas
personajes_t = ["La mole","Hulk","Angela"]
personajes_d = ["Wolverine","Iron man","Spiderman"]
personajes_s = ["Ivisible woman","Rocket","Ultron"]
personajes_t[0] = "Venom"           #Sustituye el valor de la lista en la posicion que esta []
personajes_t.append("Dr. strange")  #Agrega un valor a la lista
personajes_t.insert(0, "La mole")   #Agreag un valor en esa posicion
personajes_d.extend(personajes_s)   #Extiende la lista con otra
print(f"\nY los tanques son {personajes_t}")
print(f"Y los demas personajes son {personajes_d}")

#Eliminar valores de una lista
movimientos = ["Golpe basico","Golpe cargado","Ulti","Escudo"]
print(f"Tus movimientos son: {movimientos}")
movimientos.pop(2)                                  #Se elimina el valor en la posicion entre (), si no tiene posicion se elimina el ultimo 
print(f"Usaste tu ulti, te quedan:{movimientos}")
movimientos.remove("Escudo")                        #Se elimiba el valor literal con ese mismo nombre
print(f"Se rompio tu escudo te quedan: {movimientos}")

#Buscar un valor en una lista
mapas = ["Central park","Midtown","Arakko","Krakoa","Midtown"]
print(f"\nLos posibles mapas son:{mapas}")
busca_m = mapas.index("Midtown")                                    #Busca ese valor y dice en que posicion esta el primer de este valor
print(f"Midtown esta en la posicion:{busca_m}")
busca_mu = input("Introduzca el nombre del mapa que busca:\n")
coincidencias = mapas.count(busca_mu)                               #Busca este valor y cuantas veces se repite
print(f"EL mapa elegido es: {busca_mu}, te puede tocar {coincidencias} veces")