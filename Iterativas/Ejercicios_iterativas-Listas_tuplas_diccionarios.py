# Ejercicio 1

numero = (int(input("Ingrese un numero")))

def linea_numeros(numero):
    #cuenta atras desde el numero ingresado hasta cero 
    while numero >= 0: 
        print(numero, end= ",")
        numero = numero - 1

# Ejercicio 2

numero = (int(input("Ingrese un numero: ")))

def triangulo (numero):
    #Triangulo rectangulo de altura del numero ingresado 
    for i in range(numero):
        asteriscos = 1 + i 
        print("*" * asteriscos)
    return ""
   
print(triangulo(numero))

# Ejercicio 3 

numero = (int(input("Ingrese un numero: ")))

def triangulo (numero):
    #Triangulo rectangulo de numeros de altura del numero ingresado 
    for i in range(1, numero+1, 2):
        for j in range(i, 0, -2):
            print(j, end=" ")
        print("")
    return ""
   
print(triangulo(numero))

# Ejercicio 4

eco = input("Escriba algo si quiere salir digite: salir ")
def palabra (eco):
    # Eco de todo lo que el usuario ingrese 
    guardar = " "
    while eco != "salir":
        guardar= guardar + " " + eco
        eco = input("Escriba algo si quiere salir digite: salir ")
    return guardar

print(palabra(eco))

# Ejercicio 5 

entrada=input("ingresa pares de palabras (palabra:traduccion) separados por ,")
def diccionario_traduccion (entrada):
    diccionario = {}
    for i in entrada.split(","):
        palabra, traduccion = i.split(":")
        diccionario[palabra] = traduccion
    frase = input("Ingrese una frase en español")

#falta traducir la frase ingresada 

diccionario2 = dict(palabras.split(":") for palabras in entrada.split(",")) #otra opcion encontrada para hacer el diccionario 

# Ejercicio 6

lista= input("ingresa el articulo y el precio con un = entre ellos, separe cada par con ,")
def compra (lista):
    #Lista de compra con articulo y precio ingresado, y coste total de la compra 
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
def estudio (asignatura):
    #Muestra en pantalla el mensaje "Yo estudio (las asignaturas ingresadas)"
    print("Yo estudio", end= " ")
    while asignatura != "":
        print(asignatura, end = ", ")
        asignatura = input("ingrese la asignatura")

# Ejercicio 8

#Ejercicio 9
palabras = input("Ingrese una palabra")
def palindroma(palabras):
    #Retorna si la palabra ingresada en palindroma
    if palabras == palabras[::-1]:
        mostrar = "La palabra es palíndroma"
    else:
        mostrar = "La palabra no es palíndroma"
    return mostrar
    
print(palindroma(palabras))

#Ejercicio 10
lista_precios= [50, 75, 46, 22, 80, 65, 8]

def menor_y_mayor(lista_precios):
    # Retorna el menor y mayor de los precios
    menor_de_los_precios = min(lista_precios)
    mayor_de_los_precios = max(lista_precios)
    return f"El menor de los precios es {menor_de_los_precios} \nEl mayor de los precios es {mayor_de_los_precios}"

print(menor_y_mayor(lista_precios))

#Ejercicio 11


