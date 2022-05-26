import Taller


#1
nombre = input("Ingresa tu nombre")
print(Taller.ejercicio_1(nombre))

#2


#3 
cantidad_sin_IVA = float(input("ingresa el precio sin iva"))
IVA = input("Ingrese el valor del IVA")
print(Taller.ejercicio_3(cantidad_sin_IVA, IVA))

#4 
radio = float(input("ingrese el radio del circulo"))
print(Taller.ejercicio_4_Area_circulo(radio))
altura = float(input("ingrese la altura del cilindro"))
print(Taller.ejercicio_4_volumen_cilindro(altura))

#5

#6
peso = float(input("Ingrese su peso en Kilos"))
estatura = float(input("Ingrese su altura en Metros"))
print(Taller.ejercicio_6(peso,estatura))

#7
n_payasos = int(input("Numero de payasos vendidos"))
n_muñecas = int(input("Numero de muñecas vendidas"))
print(Taller.ejercicio_7(n_payasos, n_muñecas))

#8
pan=int(input("Ingrese el # de panes vendidos que no son del día"))
print(Taller.ejercicio_8(pan))

#9
#10