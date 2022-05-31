#Ejercicio 1
frase = "el rápido zorro marrón salta sobre el perro perezoso"
longitud_palabra= list(len(palabras) for palabras in frase.split(" ") if palabras != "el")
print(longitud_palabra)

#Ejercicio 2
numeros = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
nueva_lista = list(positivos for positivos in numeros if positivos > 0)
print(nueva_lista)

#Ejercicio 3
Frase ="Hello 12345 World 5602"
conjunto_digitos = set(digitos for digitos in Frase if digitos.isdigit())
print(conjunto_digitos)

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
caracter_fruta= list(len(fruta) for fruta in frutas)
print(caracter_fruta)

#Ejercicio 7
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
primos = list( x for x in range(2,101) if not(x% 2 == 0 or x% 3 == 0 or x% 5 == 0 or x% 7 == 0))
primos.extend([2,3,5,7])
primos.sort()
print(primos)

#Ejercicio 9
from functools import reduce 
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
map_result = list(map(lambda x: round((x**2),3), my_floats))
print(map_result)

my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
filter_result = list(filter(lambda name: name if len(name) <= 7 else "", my_names)) 
print(filter_result)

my_numbers = [4, 6, 9, 23, 5]
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)
print(reduce_result)

#Ejercicio 10

lista_de_numeros = [10, 20, 30, 400, 50, 100] # [10, 30, 50, 90, 100, 101] #[1, 2, 3, 4, 5, 6, 7, 8, 9] #[151, 60, -5, 135, 18, 40]
#Si todos los enteros son positivos, se debe revisar si algún entero es un número palíndromo
positivos = (all(list(map(lambda x: x> 0, lista_de_numeros))))
print(positivos)

palindromo = (any(list(map(lambda y: str(y) == str(y[::-1]), str(lista_de_numeros)))))
print(palindromo)
