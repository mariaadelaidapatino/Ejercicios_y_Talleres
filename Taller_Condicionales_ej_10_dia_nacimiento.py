def A(año):
    #Da valor a A segun el siglo 
    if año >= 1700 and año <= 1799:
        return 5
    if año >= 1800 and año <= 1899:
        return 3
    if año >= 1900 and año <= 1999:
        return 1
    if año >= 2000 and año <= 2099:
        return 0
    if año >= 2100 and año <= 2199:
        return -2
    if año >= 2200 and año <= 2299:
        return -4

def ultimos_dos_digitos(año):
    #Saca los dos ultimos digitos del año
    año = str(año)
    ultimos_2_digitos = año[2:5]
    ultimos_2_digitos = int(ultimos_2_digitos)
    return ultimos_2_digitos

def B(año):
    #Da valor a B 
    b = int(ultimos_dos_digitos(año) / 4) + ultimos_dos_digitos(año)
    return b

def C(mes,año):
    #Da valor a C
    if ultimos_dos_digitos(año) == 00:
        c = ultimos_dos_digitos(año) % 400
        if c == 0 and mes == 1 or mes == 2:
            c = -1
        else:
            c = 0
    else:
        c = ultimos_dos_digitos(año) % 4
        if c == 0 and mes == 1 or mes == 2:
            c = -1
        else:
            c = 0
    return c

def D (mes):
    #Da valor a D
    if mes == 1 or mes == 10:
        return 6
    if mes == 2 or mes == 3 or mes ==11:
        return 2
    if mes == 4 or mes == 7:
        return 5
    if mes == 5:
        return 0
    if mes == 6:
        return 3
    if mes == 8:
        return 1
    if mes == 9 or mes == 12:
        return 4
    return mes

def E(dia):
    #Da valor a E
    e = dia
    return e

def dia_nacimiento(dia, mes, año):
    #Calcula el dia de la semana en la fecha indicada
    if año >= 1700 and año <= 2299:
        if mes >= 1 and mes <=12:
            if dia >= 1 and dia <= 31:
                algoritmo = A(año) + B(año) + C(mes,año) + D(mes) + E(dia)
                R = algoritmo % 7
                if R == 1:
                    R = "Lunes"
                elif R == 2:
                    R = "Martes"
                elif R == 3:
                    R = "Miercoles"
                elif R == 4:
                    R = "Jueves"
                elif R == 5:
                    R = "Viernes"
                elif R == 6:
                    R = "Sabado"
                elif R == 0:
                    R = "Domingo"
                R = f"En la fecha {dia}/{mes}/{año} el dia será {R}"
            else:
                R = f"Para la fecha {dia}/{mes}/{año} ingrese un dia entre 1 y 31"
        else: 
            R =f"Para la fecha {dia}/{mes}/{año} ingrese un mes entre 1 y 12"
    else:
        R = f"Para la fecha {dia}/{mes}/{año} ingrese un año entre 1700 y 2299"
    return R

año = int(input("año de nacimiento"))
mes = int (input("mes de nacimiento"))
dia = int(input("dia de nacimiento"))

print(dia_nacimiento(dia, mes, año))