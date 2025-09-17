#Diferentes variables:
nombre_persona = "Juan"
NOMBRES_PERSONA = "Emiliano"
Nombre_Persona = "Carlo"
print(nombre_persona,Nombre_Persona,NOMBRES_PERSONA)

#Variables validos:
numero_1 = 1
fecha_actual1 = 16
resultado = 5
'''
Variables invalidas:
1numero = 1                     (no debe iniciar con un numero)
$resultado = 3                  (no debe llevar simbolos)
nombre-usuario = "Perenganito"  (no se debe usar "-")
'''
print(numero_1,fecha_actual1,resultado)

#Variables validas a nivel regla pero nombres correctos por poco descriptivos:
_n0c3e = "Tilin"
a1_b1_c3 = "Toño fox" 
print(_n0c3e,a1_b1_c3)

"""
Usar varibles descriptivas y con cuerden con el dato, las siguientes son una mala praxis:
Fecha = "Hola"
Nombre = 16
a = "Vicente fox"
"""
#Buena praxis:
Nombre = "Victor Mendevil"
Edad = 20
Cancion = "Punta cana"
print(Nombre,Edad,Cancion)

#Las constantes se escriben en mayuscula
PI = 3.14159
numero_2 = 34
print(PI,numero_2)