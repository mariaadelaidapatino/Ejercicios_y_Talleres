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

# Ejercicio 3 

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

# Ejercicio 5 

entrada=input("ingresa pares de palabras (palabra:traduccion) separados por ,")
diccionario = {}
for i in entrada.split(","):
    palabra, traduccion = i.split(":")
    diccionario[palabra] = traduccion
frase = input("Ingrese una frase en español")
#falta traducir la frase ingresada 

diccionario2 = dict(palabras.split(":") for palabras in entrada.split(",")) #otra opcion encontrada para hacer el diccionario 

# Ejercicio 6

lista= input("ingresa el articulo y el precio con un = entre ellos, separe cada par con ,")
cesta_de_compra = {}
coste_total = 0
print(f"   Lista de Compra \n____________________________")
for i in lista.split(","):
    articulo, precio = i.split("=")
    cesta_de_compra[articulo] = precio
for j in cesta_de_compra.values():
    j = float(j)
    coste_total += j
    
for k, v in cesta_de_compra.items():
    key= k.capitalize()
    print(key, "      ","$", v,"\n","____________________________")

print("Total","      ","$",coste_total)

# Ejericio 7

asignatura =(input("ingrese las asignaturas"))
print("Yo estudio", end= " ")
while asignatura != "":
    print(asignatura, end = ", ")
    asignatura = input("ingrese la asignatura")

# Ejercicio 8

