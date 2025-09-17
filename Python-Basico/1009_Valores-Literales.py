#Una variable literal quiere decir que no cambia el valor
años = 16
frase = "que no te bañas"

#Una variable no literal quiere decir que pude cambiar de valor
nombre = input("Escribe tu nombre\n")
nombre_pm = nombre.capitalize()

print(f"Tu nombre es {nombre_pm} y tines {años} años {frase}")