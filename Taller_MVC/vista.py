import modelo
import controlador
def pedirNumeroEntero():
    # Pide al usuario el número de la opción a seleccionar en el menú
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce la opcion que quieres seleccionar "))
            correcto=True
        except ValueError:
            print('Error, introduce un numero entero')
     
    return num

def mensaje_salida():
    #Imprime el mensaje de salida
    print("Ha salido exitosamente")
    

def menu_principal_app ():
    #Imprime menu principal  
    print("-- Aplicación CRUD EL CORRIENTAZO ---")
    print("1. Crear pedido")
    print("2. Adicionar al pedido")
    print("3. Actualizar pedido")
    print("4. Cuenta del pedido")
    print("0. Salir")
    
    valor = None
    while valor == None:
        valor = pedirNumeroEntero()
        if valor not in range(5):
            print("Numero de opción inválido. Intente de nuevo.")
            valor = None
    return valor

def numero_de_mesa ():
    #Pregunta el numero de mesa y lo guarda en una lista
    mesa = int(input("Numero de la mesa "))
    mesa = str(mesa)
    n_mesa = "Mesa numero: " + mesa
    return n_mesa

def menu_segun_dia ():
    #Imprime el menu para elegir el menu del día
    print("--- Elija el día ---")
    print("1. Menu Lunes")
    print("2. Menu Martes")
    print("3. Menu Miercoles")
    print("4. Menu Jueves")
    print("5. Menu Viernes")
    print("0. Atras")

    dia = None
    while dia == None:
        dia = pedirNumeroEntero()
        if dia not in range(6):
            print("Numero de opción inválido. Intente de nuevo.")
            dia = None

    return dia

def sopa_lunes():
    # Imprime las opciones de sopa del dia lunes
    print("--- Elija que Sopa desea ---")
    print("1.", modelo.df.loc[0, "sopa_1"])
    print("2.", modelo.df.loc[0, "sopa_2"])
    print("0. Atras")
    sopa = None
    while sopa == None:
        sopa = pedirNumeroEntero()
        if sopa not in range(3):
            print("Numero de opción inválido. Intente de nuevo.")
            sopa = None

    return sopa

def principio_lunes():
    #Imprime las opciones de principio del dia lunes
    print("--- Elija que Principio desea ---")
    print("1.", modelo.df.loc[0, "principio_1"])
    print("2.", modelo.df.loc[0, "principio_2"])
    print("0. Atras")
    principio = None
    while principio == None:
        principio = pedirNumeroEntero()
        if principio not in range(3):
            print("Numero de opción inválido. Intente de nuevo.")
            principio = None

    return principio

def proteina_lunes():
    #imprime las opciones de proteina del dia lunes
    print("--- Elija que Proteina desea ---")
    print("1.", modelo.df.loc[0, "carne_1"])
    print("2.", modelo.df.loc[0, "carne_2"])
    print("3.", modelo.df.loc[0, "carne_3"])
    print("0. Atras")
    proteina = None
    while proteina == None:
        proteina = pedirNumeroEntero()
        if proteina not in range(4):
            print("Numero de opción inválido. Intente de nuevo.")
            proteina = None

    return proteina

def ensalada ():
    #imprime el menu que pregunta si desea ensalada en el pedido
    print("--- ¿Desea ensalada? ---")
    print("1. Si")
    print("2. No")
    print("0. Atras")
    ensalada = None
    while ensalada == None:
        ensalada = pedirNumeroEntero()
        if ensalada not in range(3):
            print("Numero de opción inválido. Intente de nuevo.")
            ensalada = None

    return ensalada

def jugo_lunes ():
    #imprime las opciones de jugo del dia lunes 
    print("--- Elija que Jugo desea ---")
    print("1.", modelo.df.loc[0, "jugo_1"])
    print("2.", modelo.df.loc[0, "jugo_2"])
    print("0. Atras")
    jugo = None
    while jugo == None:
        jugo = pedirNumeroEntero()
        if jugo not in range(3):
            print("Numero de opción inválido. Intente de nuevo.")
            jugo = None

    return jugo

def terminar_mesa ():
    # imprime las opciones para terminar el pedido de la mesa
    print("--- ¿Terminar el pedido de la mesa? ---")
    print("1. Si")
    print("2. No")
    print("0. Atras")
    terminar = None
    while terminar == None:
        terminar = pedirNumeroEntero()
        if terminar not in range(3):
            print("Numero de opción inválido. Intente de nuevo.")
            terminar = None

    return terminar




