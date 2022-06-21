import vista
import modelo
pedido = []
costo =[]
def menu_principal_opciones ():
    # 
    salir = False
    while not salir:
        opcion = vista.menu_principal_app()
        if opcion == 1:
            crear_pedido()
        elif opcion == 0:
            vista.mensaje_salida()
            salir = True
            
        
           
def crear_pedido ():
    pedido.append(vista.numero_de_mesa())
    otra_orden = True
    menu_dia = vista.menu_segun_dia()
    if menu_dia == 1: 
        while otra_orden == True:
            opcion_sopa = vista.sopa_lunes()
            if opcion_sopa == 1:
                pedido.append(modelo.df.loc[0,"sopa_1"])
            elif opcion_sopa == 2:
                pedido.append(modelo.df.loc[0,"sopa_2"])
            elif opcion_sopa == 0:
                #salir
                pass
            else:#error
                pass
            opcion_principio = vista.principio_lunes()
            if opcion_principio == 1:
                pedido.append(modelo.df.loc[0,"principio_1"])
            elif opcion_principio == 2:
                pedido.append(modelo.df.loc[0,"principio_2"])
            elif opcion_principio == 0:
                #Salir 
                pass
            else:#error
                pass
            opcion_proteina = vista.proteina_lunes()
            if opcion_proteina == 1:
                pedido.append(modelo.df.loc[0,"carne_1"])
            elif opcion_proteina == 2:
                pedido.append(modelo.df.loc[0,"carne_2"])
            elif opcion_proteina == 3:
                pedido.append(modelo.df.loc[0,"carne_3"])
            elif opcion_proteina == 0:
                #salir
                pass
            else: #error
                pass
            opcion_ensalada = vista.ensalada()
            if opcion_ensalada == 1:
                pedido.append(modelo.df.loc[0,"ensalada"])
            elif opcion_ensalada == 2:
                #no hace nada
                pass
            elif opcion_ensalada == 0:
            #salir
                pass
            else: #error
                pass
            opcion_jugo = vista.jugo_lunes()
            if opcion_jugo == 1:
                pedido.append(modelo.df.loc[0,"jugo_1"])
            elif opcion_jugo ==2:
                pedido.append(modelo.df.loc[0,"jugo_2"])
            elif opcion_jugo == 0:
                #salir
                pass
            else: # Error
                pass
            costo.append(15000)
            terminar = vista.terminar_mesa()    
            if terminar == 2:
                otra_orden = True
            else:
                otra_orden = False
    print(pedido)
    print(costo)
    
     
    
      

print(menu_principal_opciones())
