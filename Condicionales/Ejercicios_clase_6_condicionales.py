# Ejercicio 1
def notaD(nota:float):
    # imprime un mensaje de felicitaciones si la nota es mayor o igual a 4.0
    if nota >= 0.0 and nota <= 5.0:
        if nota >= 4.0:
            nota_definitivA = "¡Felicitaciones!"
    else:
        nota_definitivA("La nota ingresada no es valida")
    return nota_definitivA

print(notaD(4.1))

# Ejercicio 2
def nota_D(nota:float):
    # Imprime la nota ingresada, si es mayor a 3.0 imprime mensaje "Ganó el curso" si no "Perdió el curso"
    if nota >= 0.0 and nota <= 5.0:
        if nota >= 3.0:
            nota_final = "Ganó el curso"
        else:
            nota_final = "Perdió el curso"
    else:
        nota_final = "La nota ingresada no es valida" 
    return nota_final 

nota = int(input("nota"))
print(nota_D(nota))

#Ejercicio 3
def persona(nombre : str, edad : int):
    #Indica si con la edad ingresada se es Mayor o Menor de edad
    if not isinstance (edad, int):
         return "Edad no valida"
    if edad >= 18:
        Mayoria_de_edad = "Mayor de edad"
    else:
        Mayoria_de_edad = "Menor de edad"
    mensaje = f"La persona {nombre} con {edad} años es {Mayoria_de_edad}"
    return mensaje

nombre = input("nombre")
edad = float(input("edad"))
print(persona(nombre, edad))

#Ejercicio 4
def tipo_numero(numero:float):
    #Indica si el numero ingresado es par o impar
    if numero % 2 == 0:
        tipo_de_numero = "es un numero par"
    else:
        tipo_de_numero = "es un numero impar"
    Tipo_de_numero = f"El {numero} es {tipo_de_numero} "
    return Tipo_de_numero

numero = float(input("numero"))
print(tipo_numero(numero))

#Ejercicio 5
def numero_r(dato: float):
    #Indica si el numero ingresado esta dentro del ranco (3.5 , 7.8)
    if not isinstance (dato, float) and not isinstance(dato, int):
         return "Numero no valido"
    if dato > 3.5 and dato <= 7.8:
        dato ="Esta dentro del rango"
    else:
        dato= "No esta dentro del rango"
    return dato
dato = float(input("numero"))
print(numero_r(dato))

# Ejercicio 6
def numero_r(dato: float):
    #Indica si el numero ingresado esta dentro de los rangos (3.5 , 7.8],[9.3, 4.5] y [23.4, 45.3]
    if not isinstance (dato, float) and not isinstance(dato, int):
         return "Numero no valido"
    if [(dato > 3.5 and dato <= 7.8) or (dato >= 9.3 and dato <= 4.5) or (dato >= 23.4 and dato >= 45.3)]:
        dato ="Esta dentro del rango (3.5 , 7.8],[9.3, 4.5] y [23.4, 45.3]"
    else:
        dato= "No esta dentro de ningun rango"
    return dato
dato = float(input("numero"))
print(numero_r(dato))


#Ejercicio 7
def mensaje(caracter : str):
    #Imprime un mensaje segun el caracter ingresado  
    if caracter == "a":
        caracter = "Android"
    elif caracter == "A":
        caracter = "Android"
    elif caracter == "i": 
        caracter ="IOS"
    elif caracter == "I":
        caracter = "IOS"
    else:
        caracter = "Opcion inválida"
    msj = caracter
    return msj 
caracter = (input("caracter"))
print(mensaje(caracter))  

#Ejercicio 8
def Nota_Definitiva(nota : float):
    #Imprime un mensaje segun la nota definitiva
    if nota >= 0 and nota <=5.0:
        if nota <3:
            nota = "Insuficiente"
        elif nota >=3 and nota <=3.5:
            nota = "Aceptable"
        elif nota >3.5 and nota <=4.0:
            nota = "Sobresaliente"
        elif nota >4.0 and nota <=5.0:
            nota = "Excelente"
    else: nota = "Nota no valida"
    return nota

print(Nota_Definitiva(5))

#Ejercicio 9
def Mayor_numero(num_1: float, num_2: float, num_3: float, num_4: float):
    #Indica el mayor numero entre cuatro posibles numeros
    Numeros = (num_1, num_2, num_3, num_4)
    Num_max = max(Numeros)
    return Num_max
num_1 =float(input("numero 1"))
num_2 =float(input("numero 2"))
num_3 =float(input("numero 3"))
num_4 =float(input("numero 4"))

print(Mayor_numero(num_1, num_2, num_3, num_4)) 

#Ejercicio 10
def cargo_fijo(estrato: float):
    #Indica el cargo fijo a cobrar segun el estrato
    if estrato == 1:
        return 2500
    if estrato == 2:
        return 2800
    if estrato == 3:
        return 3000
    if estrato == 4:
        return 3300
    if estrato == 5:
        return 3700
    if estrato == 6:
        return 4400

def consumo_m3( estrato:float): 
    #Indica el valor a cobrar del metro cubico segun el estrato 
    if estrato == 1:
        return 2200
    if estrato == 2:
        return 2350
    if estrato == 3:
        return 2600
    if estrato == 4:
        return 3400
    if estrato == 5:
        return 3900
    if estrato == 6:
        return 4800

def basura_alcantarillado(estrato:float):
    #Indica el valor de basuras y alcantarillado a cobrar segun el estrato
    if estrato == 1:
        return 5500
    if estrato == 2:
        return 620
    if estrato == 3:
        return 7400
    if estrato == 4:
        return 8600
    if estrato == 5:
        return 9700
    if estrato == 6:
        return 11000

def cobro(estrato:int, consumo_de_agua_en_el_periodo: float):
    #Indica el cobro de factura 
    if estrato >= 1 and estrato <= 6:
        cobro_factura = cargo_fijo(estrato) + (consumo_de_agua_en_el_periodo * consumo_m3 (estrato)) + basura_alcantarillado(estrato)
        return cobro_factura
    else:
        return "Ingrese un estrato valido"
    
estrato = int(input("Estrato"))
consumo_agua = float(input("Consumo de agua"))
print(cobro(estrato, consumo_agua))


#Ejercicio 11
def aspirante(nombre:str, genero:str, estatura:float, edad:int, estado_civil:str):
    ##Indica si el aspirante a ingresar es apto o no
    if estado_civil == "soltero":
        if genero == "mujer":
            if estatura > 1.60 and (edad >=20 and edad <=25):
                situacion ="es apto"
            else:
                situacion = "No es apto"
        else:
            if estatura > 1.65 and (edad >=18 and edad <=24):
                situacion = "es apto"
            else: 
                situacion = "No es apto"
    else:
        situacion ="No es apto"
    situacion = f"El aspitante {nombre} {situacion} para ingresar al ejercito"
    return situacion 
nombre = input("nombre")
genero = input("¿Es usted mujer u hombre?")
estatura = float(input("Estatuta"))
edad = int(input("Edad"))
estado_civil = input ("Estado civil ")
print(aspirante(nombre, genero, estatura, edad, estado_civil))


    