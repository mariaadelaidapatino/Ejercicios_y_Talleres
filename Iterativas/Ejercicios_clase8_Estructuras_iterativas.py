#Ejercicio 3 
#Sumatoria de numeros ingresados 
sumatoria = 0
mensaje = "ingresar numero (0 para salir)"
num = int(input(mensaje))

while num != 0:
    sumatoria = sumatoria + num
    num = int(input(mensaje))

print("Sumatoria de los numeros ingresados es", sumatoria)

# Ejercicio 4
#Informa cual es el mayor numero ingresado 
mayor_numero = 0
mensaje = "ingresar numero (0 para salir)" 
num = int(input(mensaje))

while num > 0:
    mayor_numero = [num]
    num = int(input(mensaje))

mayor_numero = max(mayor_numero)

print("El mayor numero ingresado es", mayor_numero)

#Ejericio 5
#Ingresa unas frases en minusculas y las imprime en mayusculas
cadena = input("Ingresa la frase")
while cadena != "":
    mensaje = cadena.upper() 
    print(mensaje)
    cadena = input("Ingresa la frase")

#Ejercicio 6


            