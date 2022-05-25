#Reto los cinco doses
#obtener los números del 0 al 10 utilizando cinco 2's /
# y los signos suma (+), resta (-), multiplicación (x) y división (/) y paréntesis
numero_1 = (2 / 2 + 2 / 2) / 2
print(numero_1)
numero_2 = (2 * 2 + 2) - (2 * 2)
print(numero_2)
numero_3 = (2 * 2 * 2 -2) / 2
print(numero_3)
numero_4 = ( 2 + 2 + 2 + 2) / 2
print(numero_4)
numero_5 = (2 + 2 + 2) - (2 / 2)
print(numero_5)
numero_6 = (2 + 2 + 2 ) / (2 / 2)
print(numero_6)
numero_7 = ( 2 * 2 * 2) - (2 / 2)
print(numero_7)
numero_8 = (2 * 2 * 2 * 2) / 2
print(numero_8)
numero_9 = (2 * 2 * 2) + (2 / 2)
print(numero_9)
numero_10 = 2 + 2 + 2 + 2 + 2
print(numero_10)

# Estamos interesados en comprar un nuevo teléfono móvil y en el escaparate de una tienda aparece que el móvil cuesta 420€. El problema es que si nos esperamos a comprarlo al día siguiente sufrirá un incremento porcentual del 20%. ¿Cuánto costará entonces el teléfono si nos esperamos?
precio_telefono_movil = 420
aumento = 20
precio_telefono_movil *= (100 + aumento) / 100
print("Precio dia siguiente = ", precio_telefono_movil)

#¿Cuántas vueltas el spinner dará en 640 segundos? 
vueltas_por_minuto = 147
segundos_por_minuto = 60
tiempo_final = 640
vueltas_totales = (tiempo_final * vueltas_por_minuto) / segundos_por_minuto
print("En 640 segundos dara", vueltas_totales, "vueltas")

#¿Cuántas latas de refresco sobran?
cajas_de_referesco = 9
latas_por_caja = 24
personas = 56
latas_totales = (cajas_de_referesco * latas_por_caja)
latas_sobrantes = latas_totales % personas
print("latas sobrantes = ", latas_sobrantes)