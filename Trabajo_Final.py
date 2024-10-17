import datetime

parqueadero = ["v" + str(i+1) for i in range(50)] + ["m" + str(i+1) for i in range(25)]
estado_parqueadero = ["D" for _ in range(75)] 

vehiculos = {}
alquiler_mensual = {}  

def mostrar_parqueadero():
    print("Estado actual del parqueadero:")
    for i in range(0, 50, 10):
        print("-".join(parqueadero[i:i+10]), "-", "-".join(estado_parqueadero[i:i+10]))
    print("-".join(parqueadero[50:]), "-", "-".join(estado_parqueadero[50:]))

def alquilar_espacio(tipo):
    if tipo.lower() == "carro":
        espacios = parqueadero[:50]
        rango_espacios = range(50)  
    else:
        espacios = parqueadero[50:]
        rango_espacios = range(50, 75) 
    
    disponibles = [i for i in rango_espacios if estado_parqueadero[i] == 'D']
    
    if not disponibles:
        print(f"No hay espacios disponibles para {tipo}.")
        return
    
    print(f"Espacios disponibles para {tipo}: {[espacio+1 for espacio in disponibles]}")
    espacio = int(input(f"Selecciona un espacio disponible: ")) - 1
    
    if espacio not in rango_espacios or estado_parqueadero[espacio] != "D":
        print("El espacio seleccionado no es válido o está ocupado.")
        return

    print("1. Alquiler mensual ($200.000)")
    print("2. Ocupación por horas ($5.000/hora)")
    opcion_alquiler = int(input("Selecciona el tipo de alquiler: "))
    
    placa = input("Ingresa la placa del vehículo: ")
    
    hora_entrada = input("Ingresa la hora de entrada (formato HH:MM): ")
    hora_entrada = datetime.datetime.strptime(hora_entrada, "%H:%M")

    if opcion_alquiler == 1:
        estado_parqueadero[espacio] = "A"
        alquiler_mensual[placa] = espacio
        vehiculos[placa] = {'tipo': tipo, 'modo': 'mensual', 'hora_entrada': hora_entrada, 'espacio': espacio}
        print(f"Espacio {espacio+1} alquilado por un mes.")
    elif opcion_alquiler == 2:
        estado_parqueadero[espacio] = "O"
        vehiculos[placa] = {'tipo': tipo, 'modo': 'horas', 'hora_entrada': hora_entrada, 'espacio': espacio}
        print(f"Espacio {espacio+1} ocupado por horas.")

def registrar_entrada():
    placa = input("Ingresa la placa del vehículo: ")
    tipo = input("Es un carro o una moto? ")
    alquilar_espacio(tipo)

def registrar_salida():
    placa = input("Ingresa la placa del vehículo: ")
    if placa in vehiculos:
        hora_salida = input("Ingresa la hora de salida (formato HH:MM): ")
        hora_salida = datetime.datetime.strptime(hora_salida, "%H:%M")
        vehiculos[placa]['hora_salida'] = hora_salida
        print(f"Registro de salida completado para la placa {placa}.")
    else:
        print("No se encontró un vehículo con esa placa.")

def facturar():
    placa = input("Ingresa la placa del vehículo: ")
    if placa in vehiculos:
        vehiculo = vehiculos[placa]
        if vehiculo['modo'] == 'mensual':
            print("Factura del mes: $200.000")
        elif vehiculo['modo'] == 'horas':
            hora_entrada = vehiculo['hora_entrada']
            hora_salida = vehiculo.get('hora_salida')
            horas_ocupadas = (hora_salida - hora_entrada).total_seconds() / 3600
            tarifa = horas_ocupadas * 5000
            print(f"Factura por horas: ${tarifa:.2f}")
        else:
            print("Modo de alquiler no reconocido.")
        estado_parqueadero[vehiculo['espacio']] = "D"
        del vehiculos[placa]
    else:
        print("No se encontró un vehículo con esa placa.")

def actualizar_parqueadero():
    mostrar_parqueadero()

def menu_principal():
    while True:
        print("\nMenú de opciones:")
        print("1. Mostrar matriz del parqueadero")
        print("2. Alquiler (entrada del vehículo por placa y tipo)")
        print("3. Registrar entrada")
        print("4. Actualizar")
        print("5. Registrar salida")
        print("6. Facturar")
        print("7. Salir")

        opcion = int(input("Elige una opción: "))
        if opcion == 1:
            mostrar_parqueadero()
        elif opcion == 2:
            tipo = input("Es un carro o una moto? ")
            alquilar_espacio(tipo)
        elif opcion == 3:
            registrar_entrada()
        elif opcion == 4:
            actualizar_parqueadero()
        elif opcion == 5:
            registrar_salida()
        elif opcion == 6:
            facturar()
        elif opcion == 7:
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

print("Bienvenido al sistema de Administración de Parqueadero")
menu_principal()
