import math

def ejercicio_1(nombre:str):
    #Muestra en pantalla Saludo con nombre
    pantalla = f"¡hola {nombre}"
    return pantalla

def ejercicio_2(numero:int):
    #Devuelve factorial del numero ingresado 
    if numero > 0 : 
        if numero > 1:
            factorial = numero * ejercicio_2 (numero - 1)
        else :
            factorial = 1
    else: 
        factorial = "Ingrese un numero positivo"
    return factorial
    

def ejercicio_3(cantidad_sin_IVA, IVA):
    #Calcula el total de la factura tras aplicarle el IVA
    if IVA == "":
        total_factura = cantidad_sin_IVA * ((100 + 16) / 100)
    else:
        IVA =int(IVA)    
        total_factura = cantidad_sin_IVA * ((100 + IVA) / 100)
    return total_factura

def ejercicio_4_Area_circulo(radio):
    #Calcula el area de un circulo
    Area = math.pi * radio**2 
    return Area

def ejercicio_4_volumen_cilindro(altura):
    #Calcula el area de un cilindro
    area_de_la_base = ejercicio_4_Area_circulo(altura)
    volumen = area_de_la_base * altura
    return volumen

def ejercicio_5 (n):
    #Suma desde n hasta 1
    if n >= 0:
        suma = (int(n * (n + 1)) / 2)
    else: 
        suma = "ingrese un numero positivo" 
    return suma

def ejercicio_6(peso, estatura):
    #calcula el imc
    imc = peso / estatura**2
    imc= round(imc,2)
    return f"Tu índice de masa corporal es {imc}"

def ejercicio_7(n_payasos, n_muñecas):
    # Calcula el peso del paquete final
    peso_payasos = 112 
    peso_muñecas = 75
    peso_total_paquete = (n_payasos * peso_payasos) + (n_muñecas * peso_muñecas)
    return f"El peso total del paquete que será enviado es de {peso_total_paquete}"

def ejercicio_8(pan):
    #Da el precio final de compra de pan con descuento 
    descuento = 60
    precio_pan = 3.49
    precio_final= pan * (precio_pan *((100 - descuento) / 100))
    return f"El precio habitual de una barra de pan es de {precio_pan} \n Si el pan no es fresco tiene un descuento de {descuento} % \n El costo total es de {precio_final}"

def ejercicio_9 (cantidad_depositada):
    interes = 4
    ahorros_año_1 = round(cantidad_depositada + ((cantidad_depositada * interes) / 100), 2)
    ahorros_año_2 = round(ahorros_año_1 + ((ahorros_año_1 * interes) / 100), 2)
    ahorros_año_3 = round(ahorros_año_2 + ((ahorros_año_2 * interes) / 100),2)
    return f"La cantidad de ahorros para $ {cantidad_depositada} depositados \ntras el primer año es de ${ahorros_año_1} \ntras el segundo año es de ${ahorros_año_2} \ntras el tercer año es de ${ahorros_año_3}"

def ejercicio_10 (tiempo):
    dia = round(tiempo / 86400)
    hora = round((tiempo - (86400 * dia)) / 3600)
    minuto = round((tiempo - (86400 * dia) - (3600 * hora)) / 60)
    segundo = round(tiempo - (86400 * dia) - (3600 * hora) - (60 * minuto))
    return f"{tiempo} segundos serán {dia} días, {hora} horas, {minuto} minutos y {segundo} segundos"




