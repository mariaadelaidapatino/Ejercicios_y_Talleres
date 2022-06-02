#Ejercicio 1

frase = "el rápido zorro marrón salta sobre el perro perezoso"
def longitud(frase):
    #longitud de cada palabra de la frase
    longitud_palabra= list(len(palabras) for palabras in frase.split(" ") if palabras != "el")
    return longitud_palabra
print(longitud(frase))

#Ejercicio 2
 
numeros = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
def lista_numeros(numeros):
    #Lista de solo numeros positivos
    nueva_lista = list(positivos for positivos in numeros if positivos > 0)
    return nueva_lista
print(lista_numeros(numeros))

#Ejercicio 3

Frase ="Hello 12345 World 5602"
def digitos (Frase):
    #Conjunto con los digitos de una frase
    conjunto_digitos = set(digitos for digitos in Frase if digitos.isdigit())
    return conjunto_digitos
print(digitos(Frase))

#Ejercicio 4

valor_1=[x**2 for x in range(10)]
print(valor_1) 
valor_2 =[2**i for i in range(13)]
print(valor_2)

#Ejercicio 5
#List Comprehension para [0, 1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
cubo= list(x**3 for x in range(10))
print(cubo)

#Ejercicio 6

frutas = ['mango', 'kiwi', 'fresa', 'guayaba', 'piña', 'mandarina', 'uva', 'banano']
def num_caracteres(frutas):
    #lista con la cantidad de caracteres que tiene cada fruta 
    caracter_fruta= list(len(fruta) for fruta in frutas)
    return caracter_fruta
print(num_caracteres(frutas))

#Ejercicio 7
#lista con las frutas qeu contengan solo dos vocales
frutas = ['mango', 'kiwi', 'fresa', 'guayaba', 'piña', 'mandarina', 'uva', 'banano']
contador = 0
for palabra in frutas:
    print(palabra, end=",")
    for vocales in palabra:
        if vocales in "aeiou":
            
            vocales = len(vocales)
            numero_vocales= []
            numero_vocales.append(vocales)
            print(numero_vocales)

#Ejercicio 8
#lista de numeros primos del 2 al 100
primos = list( x for x in range(2,101) if not(x% 2 == 0 or x% 3 == 0 or x% 5 == 0 or x% 7 == 0))
primos.extend([2,3,5,7])
primos.sort()
print(primos)

#Ejercicio 9

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
def cuadrado(my_floats):
    # cuadrado de cada numero redondeado
    map_result = list(map(lambda x: round((x**2),3), my_floats))
    return map_result
print(cuadrado(my_floats))


my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
def menor_a_7_letras(my_names):
    #lista con los nombres que tengan 7 o menos letras
    filter_result = list(filter(lambda name: name if len(name) <= 7 else "", my_names)) 
    return filter_result
print(menor_a_7_letras)


my_numbers = [4, 6, 9, 23, 5]
def producto (my_numbers):
    #producto de los numeros de la lista
    from functools import reduce
    reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)
    return reduce_result
print(producto(my_numbers))

#Ejercicio 10

lista_de_numeros = [10, 20, 30, 400, 50, 100] # [10, 30, 50, 90, 100, 101] #[1, 2, 3, 4, 5, 6, 7, 8, 9] #[151, 60, -5, 135, 18, 40]
#Si todos los enteros son positivos, se debe revisar si algún entero es un número palíndromo
positivos = (all(list(map(lambda x: x> 0, lista_de_numeros))))
print(positivos)

palindromo = (any(list(map(lambda y: str(y) == str(y[::-1]), str(lista_de_numeros)))))
print(palindromo)
