# [Reputacion del jugador]
reputacion_p = 100      #reputacion positiva
reputacion_n = 20       #reputacion negativa
ayuda = 3               #gente que haz ayudado
experiencia_mt = 1634   #experiencia que puedes recibir por mision
compañeros_t = 155      #compañeros totales
coste_p = 1555          #coste del producto
asesinatos_gi = 2       #asesinatos a gente inocente 
años = 4                #años trascurridos

# [Operaciones]
# *suma*
reputacion_t = reputacion_p+reputacion_n  #reputacion total
print("Tu reputacion total es de:", reputacion_t )

# *resta*
reputacion_nb = reputacion_p-reputacion_n #reputacion de npc's buenos
reputacion_nm = reputacion_n-reputacion_p #reputacion de npc's malos
print("Tu reputacion a npc's buenos es de:", reputacion_nb)
print("Tu reputacion a npc's buenos es de:", reputacion_nm)

# *multiplicacion*
reputacion_pt = reputacion_p*ayuda  #reputacion temporal positiva
print("Haz ayudado a 3 personas el dia de hoy tu reputacion es de:", reputacion_pt, "por los siguientes 6 dias")

# *division 
experncia_md = experiencia_mt/reputacion_n  #experiencia descontada 
print("Se te desconto en esta mision:", experncia_md, "de experiencia por tu mal comportamiento")

# *modulo*
coste_j = coste_p%reputacion_p #porcentaje de descuento al jugador
print("Los comerciantes te hace un descuento de $", coste_j)

# *division entera
compañeros_j = compañeros_t//reputacion_n    #total de compañeros que el jugador puede tener
print("Tus posibles compañeros son en total:", compañeros_j)

# *potencias* (elevar)
reputacion_nt = reputacion_n**asesinatos_gi #reputacion temporal negativa
print("haz matado a dos inocentes, tu reputacion negativa a subido a:", reputacion_nt, "por los siguientes 4 dias")

# *operacion compleja*
puntaje_f= (reputacion_p-(reputacion_n+asesinatos_gi)) * ((compañeros_j/ayuda)**años) #puntuaje final
print("Tu puntuaje final es de:", puntaje_f)
