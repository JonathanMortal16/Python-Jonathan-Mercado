#Las tuplas no se pueden modificar
tupla_razas = ("Basenji","Pug","Pomerania","Chihuahua","Pug")               #Se usa () en vez de []
print(f"Las razas de perros que hay son: {tupla_razas}")
print("El Chihuahua esta en la posicion", tupla_razas.index("Chihuahua"))   #Aqui busca la posicion de del valor en la tupla
buscar_raza = input("Escriba el nombre de la raza que busca:\n")
coincidencias = tupla_razas.count(buscar_raza)                              #Busca el valor solicitado y te dice cuantas veces se repite
print(f"La raza que buscas: {buscar_raza}, sale {coincidencias} veces")