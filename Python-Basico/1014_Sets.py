#los sets no se modifican
set_personajes = {"Luffy","Zoro","Sanji","Choper","Naruto","Luffy","Goku"}  #los imprime aleatoriamente, si el valor esta duplicado solo lo muestra una vez
print(f"Algunos de los personajes de one piece son:{set_personajes}")

set_personajes.add("Nami")  #agrega un valor
print(f"Se me olvidaban unos, serian: {set_personajes}")

set_personajes.remove("Naruto") #remueve un personaje, si no existe da error
print(f"Es cierto Naruto no es de one piece, entoces quedaria como: {set_personajes}")

set_personajes.discard("Goku")
set_personajes.discard("Ichigo")    #No existe pero no da error
print(f"Es cierto Goku tampoco es de one piece, entoces quedaria como: {set_personajes}")

cantidad_personajes = len(set_personajes)   #Lee la cantidad de elementos en el set
print(f"Hasta ahorita llevamos {cantidad_personajes}")

personaje = "Luffy"
cantidad_caracteres = len(personaje)    #lee la cantidad de caracteres 
print(f"Luffy tiene {cantidad_caracteres} caracteres, Los cuales son:\n{personaje[0]}\n{personaje[1]}\n{personaje[2]}\n{personaje[3]}\n{personaje[4]}")

personaje_min = min(set_personajes) #Toma el elemento mayor o primero alfabeticamente
personaje_max = max(set_personajes) #Toma el elemento menor o ultimo alfabeticamente
print(f"El primero alfabeticamente es: {personaje_min}")
print(f"El ultimo alfabeticamente es: {personaje_max}")

mejor_personaje = frozenset(["Zoro","Choper"])  #no se pueden modificar estos
print(f"Pero de ellos mis favoritos son: {mejor_personaje}")