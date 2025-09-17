#Concatenacion
#Variables str
cancion_p1 = "Vivo muy a prisa, "
cancion_p2 = "la vidad de artista"
filosofo = " -Peso pluma"

#Se usa "+" para sumar (juntar) las cadenas de caracteres
cancion_c = cancion_p1 + cancion_p2 + filosofo
print(cancion_c)

#Comillas si quieres usar "" o '' se puede poner de diferentes formas:
print('\nUna vez Junior h dijo, "Derechito o chueco, el dinero es dinero y ya"')
print("Y yo pense, 'Actulicen la biblia'")

#f-string sirve para poner variables dentro de las ""
nombre_c = input("\nEscribe el nombre de tu artista favorito\n")
print(f"Entonces tu artista favorito es {nombre_c}?, es mejor Junior H")

#Metodos de string se usa "nombre de la variable"."nombre del metodo"()
frase = input("\nDime una frase\n")
frase_pm = frase.capitalize()   #Convierte la primera letra en mayuscula
frase_tm = frase.upper()        #Conviete todas las letras en mayuscula
frase_m = frase.lower()         #Convierte todas las letras en minuscula
print(f"Esta es tu frase con la primer letra en mayuscula {frase_pm}")
print(f"Esta es tu frase con todas las letras en mayuscula {frase_tm}")
print(f"Esta es tu frase con todas las letras en minuscula {frase_m}")
