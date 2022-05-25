#EJERCICIO 1 
## Lee el peso de una persona en lb y lo devuelve en kg
### Simple
peso_en_libras = float(input("peso en libras"))
libra = 0.423592
peso_kilogramos = peso_en_libras * libra
print(peso_kilogramos)

### funcion
def peso (peso_en_libras):
    libra = 0.423592
    peso_kilogramos = peso_en_libras * libra 
    return peso_kilogramos

peso_en_libras = float(input("peso en libras"))
print(peso(peso_en_libras))


#EJERCICIO 2
## Calcular la longitude de la hipotenusa
### simple
a = float(input("longitud lado a"))
b = float(input("longitud lado b"))
c = ((a**2)+ (b**2))**0.5
print(c)

### Funcion
def longitud_hipotenusa (a : float, b :float ):
    if a < 0 or b < 0:
        c= "Ponga un numero positivo"
    else: 
        c = ((a**2)+ (b**2))**0.5
    return f"La longitud de la hipotenusa es de {c}"

a = float(input("longitud lado a"))
b = float(input("longitud lado b"))
print(longitud_hipotenusa(a,b))

#EJERCICIO 3
## Conversion de millas a kilometros y de kilometros a millas 
### Simple 
millas_convertir = float(input("ingrese las millas"))
una_milla_son = 1.60934 #kilomentros
km_a_millas = millas_convertir * una_milla_son
print(km_a_millas)

kilometros_convertir = float(input("ingrese los kilometros"))
un_kilometro_son = 0.621371 #millas
millas_a_kilometro = kilometros_convertir * un_kilometro_son
print(millas_a_kilometro)

### Funcion 
def conversor (millas):
    if millas < 0:
        km_a_millas = "Ingrese un numero mayor a cero"
    else: 
        una_milla_son = 1.60934 #kilomentros
        km_a_millas = millas * una_milla_son
    return f"{millas} millas son {km_a_millas} kilometros"
    
millas = float(input("ingrese las millas a convertir"))
print(conversor(millas))

def Conversor (kilometros):
    if kilometros < 0:
        millas_a_kilometro = "Ingrese un numero mayor a cero"
    else:
        un_kilometro_son =  0.621371 #millas
        millas_a_kilometro = kilometros * un_kilometro_son
    return f"{kilometros} son {millas_a_kilometro} kilometros"

kilometros = float(input("ingrese los kilometros a convertir"))
print(Conversor(kilometros))

#EJERCICIO 4
## Suma de dos numeros, resta de dos numeros, multiplicacion de dos numeros, division de dos numeros
### simple
num_1 = float(input("ingresa el numero 1"))
num_2 = float(input("ingresa el numero 2"))
suma = num_1 + num_2
resta = num_1 - num_2
multiplicacion = num_1 * num_2
division = num_1 / num_2
print(suma)
print(resta)
print(multiplicacion)
print(division)

## funcion
def suma_2_numeros (num_1 : float, num_2 : float):
    suma = num_1 + num_2
    return f"El resultado de la suma de {num_1} más {num_2} es {suma}"

num_1 = float(input("ingresa el numero 1"))
num_2 = float(input("ingresa el numero 2"))
print(suma_2_numeros(num_1, num_2))

def resta_2_numeros (num_1 : float, num_2 : float):
    resta = num_1 - num_2
    return f"El resultado de la resta de {num_1} menos {num_2} es {resta}"

num_1 = float(input("ingresa el numero 1"))
num_2 = float(input("ingresa el numero 2"))
print(resta_2_numeros(num_1, num_2))

def multiplicacion_2_numeros (num_1 : float, num_2 : float):
    multiplicacion = num_1 * num_2
    return f"El resultado de la multiplicacion de {num_1} por {num_2} es {multiplicacion}"

num_1 = float(input("ingresa el numero 1"))
num_2 = float(input("ingresa el numero 2"))
print(multiplicacion_2_numeros(num_1, num_2))

def division_2_numeros (num_1 : float, num_2 : float):
    if num_2 == 0 :
        division = "No es posible dividir por cero"
    else:
        division = num_1 / num_2
    return f"El resultado de la division de {num_1} dividido {num_2} es {division}"

num_1 = float(input("ingresa el numero 1"))
num_2 = float(input("ingresa el numero 2"))
print(division_2_numeros(num_1, num_2))