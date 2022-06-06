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
# Retorna el saldo de una cuenta bancaria segun la siguiente bitácora D 200, D 200, R 100, D 50. 
# Donde D es deposito y R es retiro

saldo = 0
entrada = input("entrada")
valor = 0

while entrada != "":
    if entrada[0] == "D":
        valor = entrada[2:]
        saldo += int(valor)
    elif entrada[0] == "R":
        valor = entrada[2:]
        saldo -= int(valor)
    else:
        pass

    entrada = input("entrada")

print(saldo)

            