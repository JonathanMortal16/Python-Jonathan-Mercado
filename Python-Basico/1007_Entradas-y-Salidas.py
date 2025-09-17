print("¡¡\nHola\nMundo\n!!") #se usa "\n" para un salto de linea

#introducir datos con input():
nombre = input("\nEscribe tu nombre\n") 
print("\nHola",nombre,"\nhueles algo mal\nbañate porfa")

numero_1 = int(input("\nDime que edad tienes\n")) #se unsa int para convertir la entrada a entero
numero_2 = int(input("\n¿Cuantos meses han pasado desde tu cumpleaños?\n"))

meses_t = (numero_1 * 12) + numero_2
print("\nHan pasado:",meses_t,"meses desde que naciste :D")