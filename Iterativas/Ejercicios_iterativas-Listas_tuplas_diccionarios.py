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
    
    for i in range(1, numero+1, 2):
        for j in range(i, 0, -2):
            print(j, end=" ")
        print("")
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

entrada=input("ingresa pares de palabras (palabra:traduccion) separados por ,")
diccionario = dict(palabras.split(":") for palabras in entrada.split(","))
frase = input("Ingrese una frase en español")


print(entrada)
print(type(entrada))

# Ejercicio 6

# Ejericio 7

asignatura =(input("ingrese las asignaturas"))
print("Yo estudio", end= " ")
while asignatura != "":
    print(asignatura, end = ", ")
    asignatura = input("ingrese la asignatura")

# Ejercicio 8

