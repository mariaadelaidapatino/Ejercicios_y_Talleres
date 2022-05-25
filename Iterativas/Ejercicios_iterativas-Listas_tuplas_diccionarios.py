# Ejercicio 1

numero = (int(input("Ingrese un numero")))

def linea_numeros(numero):
    while numero >= 0: 
        print(numero, end= ",")
        numero = numero - 1

# Ejercicio 2

numero = (int(input("Ingrese un numero: ")))

def triangulo (numero):
    for i in range(numero):
        asteriscos = 1 + i 
        print("*" * asteriscos)
    return ""
   
print(triangulo(numero))

# Ejercicio 3 #Falta

numero = (int(input("Ingrese un numero: ")))

def triangulo (numero):
    for i in range(numero):
        lineas = 1 + (2 * i)
                    
        print(lineas)
    return ""
   
print(triangulo(numero))

# Ejercicio 4

mensaje = "Escriba algo si quiere salir digite: salir "
eco = input(mensaje)
guardar = " "
while eco != "salir":
    guardar= guardar + " " + eco
    eco = input(mensaje)

print(guardar)

# Ejercicio 5 #falta

entrada=(input("ingresa pares de palabras (palabra:traduccion) separados por ,"))
entrada.split(",")
diccionario ={}

print(entrada)
print(type(entrada))

# Ejercicio 6
# Ejericio 7
# Ejercicio 8

