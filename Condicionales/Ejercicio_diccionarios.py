amigo1 = {
    "nombre": "harold stiven",
    "capacidad_vaso":10.0,
    "capacidad_actual":5.5
}
amigo2 = {
   "nombre": "camilo hernadez",
    "capacidad_vaso":15.5,
    "capacidad_actual":10.5
} 
amigo3 = {
"nombre": "maria adelaida",
    "capacidad_vaso":5.5,
    "capacidad_actual":2.5
}

def desperdicio_de_gaseosa (amigo1,amigo2,amigo3,capacidad_boton):
    #Indica a cual de los amigos se le riega primero la gaseosa
    
    faltante_amigo_1 = (amigo1["capacidad_actual"] - amigo1["capacidad_vaso"])
    faltante_amigo_2 = (amigo2["capacidad_actual"] - amigo2["capacidad_vaso"])
    faltante_amigo_3 = (amigo3["capacidad_actual"] - amigo3["capacidad_vaso"])

    excedente_amigo_1 = faltante_amigo_1 + capacidad_boton
    excedente_amigo_2 = faltante_amigo_2 + capacidad_boton
    excedente_amigo_3 = faltante_amigo_3 + capacidad_boton

    excedentes = (excedente_amigo_1, excedente_amigo_2, excedente_amigo_3)
    excedentes = max(excedentes)

    if excedentes == excedente_amigo_1:
        amigo = (amigo1["nombre"])
    elif excedentes == excedente_amigo_2:
        amigo = (amigo2["nombre"])
    elif excedentes == excedente_amigo_3:
        amigo = (amigo3["nombre"])
    else:
        amigo = "None"
    
    return f"A {amigo} se le riega primero" 
    

print(desperdicio_de_gaseosa(amigo1, amigo2, amigo3, 5.0))