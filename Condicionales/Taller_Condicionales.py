#Ejericio documento 
num = int(input("Digite un numero entero"))
if num > 0 : 
    if num >= 10 and num <= 99:
        print("El número es positivo y tiene dos dígitos")
    else : 
        print("El número es positivo y no tiene dos dígitos")
else : 
    if num >= -999 and num <= -100:
        print("El número es negativo y tiene tres dígitos")
    else:
        print("El número es negativo y no tiene tres dígitos")

## Ejercicio 1
def entero(numero):
    #Leer un numero de dos digitos e indica si ambos con digitos son pares
    if not isinstance(numero, int):
        return "Caracter no valido"
    if numero <10 or numero > 99:
        return "No es un numero de dos digitos"
    elif numero >= 10 and numero <=99:
        numero = str (numero)
        primer_digito = numero[0]
        segundo_digito = numero[1]
        primer_digito = int(primer_digito)
        segundo_digito = int(segundo_digito)
                   
        if primer_digito % 2 == 0:
            primer_digito = True
        else:
            primer_digito = False
        
        if segundo_digito % 2 == 0:
            segundo_digito = True
        else:
            segundo_digito = False

        if primer_digito and segundo_digito == True:
            numero = "Los dos digitos son pares"
        else:
            numero = "Uno o ambos digitos son impares"
    
    return numero 

print(entero(20))

# Ejercicio 2

def salario (horas_trabajadas, tarifa_de_pago_por_hora):
    #Calcula el salario de un trabajador segun las horas trabajadas
        if horas_trabajadas > 40:
            horas_extras= horas_trabajadas - 40 
            incremento = 50
            tarifa_por_hora_extra = ((tarifa_de_pago_por_hora * incremento) / 100 ) + tarifa_de_pago_por_hora
            pago = (40 * tarifa_de_pago_por_hora) + (horas_extras * tarifa_por_hora_extra)
        else:
            pago = (horas_trabajadas * tarifa_de_pago_por_hora)
        return pago
horas_trabajadas = float(input("horas trabajadas"))
tarifa_de_pago_por_hora = float(input("Tarifa de pago por hora"))
print(salario (horas_trabajadas, tarifa_de_pago_por_hora))

# Ejercicio 3

def pago_total(cantidad_camisas, precio):
    # Indica el total a pagar de una compra de camisas
    precio_compra = cantidad_camisas * precio
    if cantidad_camisas >= 3:
        descuento = 20
        pago_compra = precio_compra - ((descuento * precio_compra) / 100)
    elif cantidad_camisas < 3:
        descuento = 10
        pago_compra = precio_compra - ((descuento * precio_compra) / 100)
    return pago_compra
cantidad_camisas = int(input("Cantidad de camisas compradas"))
precio = float(input("Precio por camisa"))
print(pago_total(cantidad_camisas, precio))

# Ejercicio 4

def programa(nombre, numero):
    #Imprime el nombre ingresado las veces que indica el numero ingresado en diferentes lineas
    if not isinstance (numero, int):
        return "Ingrese un numero sin decimales"
    impresion = ((nombre + "\n") * numero)
    return impresion
    
nombre = input("nombre")
numero =int(input("numero"))

print(programa(nombre, numero))


# Ejercicio 5

def programa2(nombre):
    #da el numero de letras del nombre ingresado en mayusculas
    longitud = len(nombre)
    nombre = nombre.upper()
    return f"{nombre} tiene {longitud} letras"

nombre = input("nombre")
print(programa2(nombre))

# Ejercicio 6

def programa3(numero_de_telefono):
    # Muestra en pantalla el numero de telefono sin prefijo ni extension 
    numero_de_telefono = str(numero_de_telefono)
    return numero_de_telefono[4:13]

numero_de_telefono = input("numero de telefono")
print(programa3(numero_de_telefono))

# Ejercicio 7

def nota_final(nota_1, nota_2, nota_3):
    if (nota_1 and nota_2 and nota_3) < 0 or (nota_1 and nota_2 and nota_3) > 5:
        #Calcula el promedio de notas e indica si aprobó o no el curso
        return "Ingrese un nota valida"
    promedio = (nota_1 + nota_2 + nota_3) / 3
    if promedio >= 3:
        promedio = "Aprobó"
    else:
        promedio = "No aprobó"
    return promedio

nota_1 = int(input("nota 1"))
nota_2 = int(input("nota 2"))
nota_3 = int(input("nota 3"))

print(nota_final(nota_1, nota_2, nota_3))

# Ejercicio 8

def indicador_de_descuento(valor):
    #Indica el valor del descuento de un articulo segun su valor 
    if valor >= 0 and valor <= 100000:
        descuento = 0
        valor_de_descuento= valor - ((descuento * valor) / 100)
    elif valor > 100000 and valor <= 225000:
            descuento = 1.5
            valor_de_descuento= valor - ((descuento * valor) / 100)
    elif valor > 225000 and valor <= 375000:
            descuento = 3.8
            valor_de_descuento= valor - ((descuento * valor) / 100)
    elif valor > 375000:
            descuento = 1.5
            valor_de_descuento= valor - ((descuento * valor) / 100)
    return valor_de_descuento
valor = float(input("valor"))
print(indicador_de_descuento(valor))

# Ejercicio 9

def ecuacion_cuadratica(a, b, c):
    #indica si una ecuacion cuadratica tiene o no solucion 
    if a == 0:
        ecuacion = "No tiene solución"
    elif (b **2 - 4 * (a * c) ) >= 0:
        ecuacion = "Tiene solución"
    else: 
        ecuacion = "No tiene solución"
    return ecuacion 

a = int(input("valor a"))
b = int(input("valor b"))
c = int(input("valor c"))

print(ecuacion_cuadratica(a, b, c))