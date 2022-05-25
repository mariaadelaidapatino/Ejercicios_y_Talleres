import math

def ejercicio_1(nombre:str):
    #Muestra en pantalla Saludo con nombre
    pantalla = f"¡hola {nombre}"
    return pantalla

def ejercicio_2(numero:int):
    #Devuelve factorial del numero ingresado 
    if numero > 0:
        return numero

def ejercicio_3(cantidad_sin_IVA, IVA):
    #Calcula el total de la factura tras aplicarle el IVA
    total_factura = cantidad_sin_IVA * ((100 + IVA) / 100)
    return total_factura

def ejercicio_4_Area_circulo(radio):
    #Calcula el area de un circulo
    Area = math.pi * radio**2 
    return Area

def ejercicio_4_volumen_cilindro(radio, altura):
    #Calcula el area de un cilindro
    area_de_la_base = ejercicio_4_Area_circulo 
    volumen = area_de_la_base * altura
    return volumen

def ejercicio_5 (n):
    if n >= 0:
        suma = (n * (n + 1)) / 2
    else: "ingrese un numero positivo" #Falta

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
    return peso_total_paquete

def ejercicio_8(pan):
    #Da el precio final de compra de pan con descuento 
    descuento = 60
    precio_pan = 3.49
    precio_final= pan * (precio_pan *((100 - descuento) / 100))
    return precio_final

def ejercicio_9 (deposito):

def ejercicio_10(segundos):
    minutos = segundos / 60
    horas = minutos / 60
    dias = horas / 24
    return f"{segundos} segundos serán {dias} días, {horas} horas, {minutos} minutos y segundos"




