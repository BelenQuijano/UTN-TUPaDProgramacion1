# UTN-TUPaDProgramacion1

#Ejercicio 1: "Caja del Kiosco"
# 1. Pedir nombre (solo letras)
while True:
    nombre = input("Ingrese nombre del cliente: ")
    if nombre.isalpha():
        break
    else:
        print("Error: el nombre debe contener solo letras.")

# 2. Pedir cantidad de productos (entero positivo)
while True:
    cantidad = input("Ingrese cantidad de productos: ")
    if cantidad.isdigit() and int(cantidad) > 0:
        cantidad = int(cantidad)
        break
    else:
        print("Error: debe ser un número entero positivo.")

total_sin_descuento = 0
total_con_descuento = 0

# 3. Procesar cada producto
for i in range(cantidad):
    print(f"\nProducto {i+1}")
 # Pedir precio
 while True:
        precio = input("Ingrese precio: ")
        if precio.isdigit():
            precio = int(precio)
            break
        else:
            print("Error: el precio debe ser un número entero.")

 total_sin_descuento += precio
 # Preguntar descuento
while True:
        descuento = input("¿Tiene descuento? (s/n): ").lower()
        if descuento == "s" or descuento == "n":
            break
        else:
            print("Error: ingrese 's' o 'n'.")
 # Aplicar descuento si corresponde
if descuento == "s":
        precio_final = precio * 0.9  # 10% descuento
    else:
        precio_final = precio
total_con_descuento += precio_final

# 4. Resultados finales
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad

print("\n--- RESUMEN ---")
print(f"Cliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento}")
print(f"Ahorro total: ${ahorro}")
print(f"Promedio por producto: ${promedio:.2f}")



#Ejercicio 2: "Acceso al Campus y Menu Seguro"
# 1. Definir credenciales fijas
usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso_concedido = False
# 2 y 3. Control de acceso (máximo 3 intentos)
while intentos < 3:
    intentos += 1
    print(f"\nIntento {intentos}/3")
    user_input = input("Usuario: ")
    pass_input = input("Clave: ")

 if user_input == usuario_correcto and pass_input == clave_correcta:
        acceso_concedido = True
        break
    else:
        print("Error: credenciales inválidas.")

if not acceso_concedido:
    print("\nCuenta bloqueada")
else:
    # 4. Menú repetitivo
    opcion = ""
    while opcion != "4":
        print("\n--- MENÚ DE ACCESO AL CAMPUS ---")
        print("1. Ver estado de inscripción")
        print("2. Cambiar clave")
        print("3. Mostrar mensaje motivacional")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

# 5. Validación del menú
if not opcion.isdigit():
            print("Error: Debe ingresar un número.")
            continue
        
if int(opcion) < 1 or int(opcion) > 4:
            print("Error: Debe estar entre 1 y 4.")
            continue
 # Lógica de las opciones
 if opcion == "1":
            print("Estado: Inscripto")
            
 elif opcion == "2":
            nueva_clave = input("Ingrese la nueva clave: ")
            # Validación de longitud mínima
            if len(nueva_clave) < 6:
                print("Rechazado: La clave debe tener mínimo 6 caracteres.")
            else:
                confirmacion = input("Confirme su nueva clave: ")
                if nueva_clave == confirmacion:
                    clave_correcta = nueva_clave
                    print("Clave cambiada con éxito.")
                else:
                    print("Error: Las claves no coinciden.")
                 elif opcion == "3":
            print("Mensaje: ¡El éxito es la suma de pequeños esfuerzos repetidos día tras día!")
             elif opcion == "4":
            print("Saliendo del sistema...")
            
# --- INICIALIZACIÓN DE VARIABLES (Sin listas) ---
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""


#Ejercicio 3: "Agenda de turnos con nombres sin listas"
#PASO 1: Nombre del Operador
operador_valido = False
nombre_operador = ""

while not operador_valido:
    nombre_operador = input("Ingrese el nombre del operador: ")
    if nombre_operador.isalpha():
        operador_valido = True
    else:
        print("Error: El nombre solo debe contener letras.")
#PASO 2: Menú Principal
sistema_activo = True
while sistema_activo:
    print(f"\n--- AGENDA DE TURNOS | Operador: {nombre_operador} ---")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
     opcion = input("Seleccione una opción: ")
    
if not opcion.isdigit():
        print("Error: Ingrese un número válido.")
        continue

#OPCIÓN 1: RESERVAR
    if opcion == "1":
        print("\n[RESERVAR] 1. Lunes | 2. Martes")
        dia = input("Seleccione día: ")
         if dia == "1" or dia == "2":
            nombre_paciente = ""
            val_paciente = False
            while not val_paciente:
                nombre_paciente = input("Nombre del paciente: ")
                if nombre_paciente.isalpha():
                    val_paciente = True
                else:
                    print("Error: Solo letras.")
         # Lógica para Lunes
            if dia == "1":
                if nombre_paciente == lunes1 or nombre_paciente == lunes2 or \
                   nombre_paciente == lunes3 or nombre_paciente == lunes4:
                    print("Error: El paciente ya tiene un turno este día.")
                elif lunes1 == "": lunes1 = nombre_paciente; print("Turno asignado en Lunes (Espacio 1)")
                elif lunes2 == "": lunes2 = nombre_paciente; print("Turno asignado en Lunes (Espacio 2)")
                elif lunes3 == "": lunes3 = nombre_paciente; print("Turno asignado en Lunes (Espacio 3)")
                elif lunes4 == "": lunes4 = nombre_paciente; print("Turno asignado en Lunes (Espacio 4)")
                else: print("Sin cupos para el Lunes.")
            
 # Lógica para Martes
  else:
                if nombre_paciente == martes1 or nombre_paciente == martes2 or nombre_paciente == martes3:
                    print("Error: El paciente ya tiene un turno este día.")
                elif martes1 == "": martes1 = nombre_paciente; print("Turno asignado en Martes (Espacio 1)")
                elif martes2 == "": martes2 = nombre_paciente; print("Turno asignado en Martes (Espacio 2)")
                elif martes3 == "": martes3 = nombre_paciente; print("Turno asignado en Martes (Espacio 3)")
                else: print("Sin cupos para el Martes.")
        else:
            print("Día no válido.")

 #OPCIÓN 2: CANCELAR
    elif opcion == "2":
        print("\n[CANCELAR] 1. Lunes | 2. Martes")
        dia = input("Seleccione día: ")
        
 nombre_cancelar = input("Nombre del paciente a cancelar: ")
        encontrado = False
        
  if dia == "1":
            if lunes1 == nombre_cancelar: lunes1 = ""; encontrado = True
            elif lunes2 == nombre_cancelar: lunes2 = ""; encontrado = True
            elif lunes3 == nombre_cancelar: lunes3 = ""; encontrado = True
            elif lunes4 == nombre_cancelar: lunes4 = ""; encontrado = True
        elif dia == "2":
            if martes1 == nombre_cancelar: martes1 = ""; encontrado = True
            elif martes2 == nombre_cancelar: martes2 = ""; encontrado = True
            elif martes3 == nombre_cancelar: martes3 = ""; encontrado = True
            
  if encontrado:
            print(f"Turno de {nombre_cancelar} cancelado exitosamente.")
        else:
            print("No se encontró al paciente en ese día.")
  #OPCIÓN 3: VER AGENDA
    elif opcion == "3":
        dia = input("Ver agenda de: 1. Lunes | 2. Martes: ")
        if dia == "1":
            print(f"1. {'(libre)' if lunes1 == '' else lunes1}")
            print(f"2. {'(libre)' if lunes2 == '' else lunes2}")
            print(f"3. {'(libre)' if lunes3 == '' else lunes3}")
            print(f"4. {'(libre)' if lunes4 == '' else lunes4}")
        elif dia == "2":
            print(f"1. {'(libre)' if martes1 == '' else martes1}")
            print(f"2. {'(libre)' if martes2 == '' else martes2}")
            print(f"3. {'(libre)' if martes3 == '' else martes3}")

  #OPCIÓN 4: RESUMEN
    elif opcion == "4":
        occ_lunes = 0
        if lunes1 != "": occ_lunes += 1
        if lunes2 != "": occ_lunes += 1
        if lunes3 != "": occ_lunes += 1
        if lunes4 != "": occ_lunes += 1
        occ_martes = 0
        if martes1 != "": occ_martes += 1
        if martes2 != "": occ_martes += 1
        if martes3 != "": occ_martes += 1
        print(f"\nResumen Lunes: {occ_lunes} ocupados, {4 - occ_lunes} disponibles.")
        print(f"Resumen Martes: {occ_martes} ocupados, {3 - occ_martes} disponibles.")
        
 if occ_lunes > occ_martes:
            print("El Lunes tiene más turnos.")
        elif occ_martes > occ_lunes:
            print("El Martes tiene más turnos.")
        else:
            print("Hay empate en la cantidad de turnos.")

  #OPCIÓN 5: CERRAR
    elif opcion == "5":
        print("Cerrando sistema...")
        sistema_activo = False
    
 else:
        print("Opción no válida.")
            
            
#Ejercicio 4: "Escape Room LA BOVEDA"           
#CONFIGURACIÓN INICIAL
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidos = 0  # Contador para la regla anti-spam

#PASO 1: Validación del Nombre
nombre_agente = ""
nombre_valido = False

while not nombre_valido:
    nombre_agente = input("Ingrese el nombre del agente: ")
    if nombre_agente.isalpha():
        nombre_valido = True
    else:
        print("Error: El nombre solo debe contener letras.")

print(f"\n--- BIENVENIDO AGENTE {nombre_agente.upper()} ---")
print("Objetivo: Abrir 3 cerraduras antes de agotar tus recursos.")

#CICLO PRINCIPAL DEL JUEGO
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    
 # Verificación de bloqueo por alarma
if alarma and tiempo <= 3:
        print("\n¡SISTEMA BLOQUEADO! La alarma detectó actividad crítica con poco tiempo.")
        break

 print(f"\nESTADO: Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3")
    if alarma: print("⚠️ ¡ALARMA ACTIVADA! ⚠️")
    print(f"Código parcial: [{codigo_parcial}]")
    
 print("-" * 20)
    print("1. Forzar cerradura (-20 E, -2 T)")
    print("2. Hackear panel (-10 E, -3 T)")
    print("3. Descansar (+15 E, -1 T)")
    
 opcion = ""
    val_opcion = False
    while not val_opcion:
        opcion = input("Seleccione una acción: ")
        if opcion.isdigit() and opcion in ["1", "2", "3"]:
            val_opcion = True
        else:
            print("Error: Seleccione 1, 2 o 3.")

  #LÓGICA DE OPCIONES

if opcion == "1":
        # Ejecutar costos
        energia -= 20
        tiempo -= 2
        forzar_seguidos += 1
        
  # Regla Anti-Spam
  if forzar_seguidos == 3:
            alarma = True
            print("¡CRÍTICO! La cerradura se trabó por forzarla repetidamente. ¡Alarma activada!")
        else:
            # Riesgo de alarma por baja energía
            if energia < 40:
                print("¡ADVERTENCIA! Tienes poca energía, podrías activar la alarma.")
                num_valido = False
                while not num_valido:
                    riesgo = input("Elige un número de seguridad (1-3): ")
                    if riesgo.isdigit() and riesgo in ["1", "2", "3"]:
                        if riesgo == "3":
                            alarma = True
                            print("¡Mala suerte! Activaste la alarma por falta de precisión.")
                        num_valido = True
                    else:
                        print("Error: Debe ser 1, 2 o 3.")
        # Si no hay alarma (o ya estaba pero no se trabó ahora), abre cerradura
            if not alarma or (alarma and forzar_seguidos < 3):
                cerraduras_abiertas += 1
                print("¡ÉXITO! Has abierto una cerradura.")

elif opcion == "2":
        # Hackear panel
        forzar_seguidos = 0 # Rompe la racha de forzar
        energia -= 10
        tiempo -= 3
        
 print("Iniciando hackeo...")
        for i in range(1, 5):
            print(f"Procesando bit {i}...")
            codigo_parcial += "A"
        
 if len(codigo_parcial) >= 8:
            if cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("¡Código completo! Una cerradura se desbloqueó digitalmente.")
                # Opcional: Reiniciar código tras abrir
                codigo_parcial = "" 

 elif opcion == "3":
        # Descansar
        forzar_seguidos = 0 # Rompe la racha de forzar
        recuperacion = 15
        if alarma:
            recuperacion -= 10 # Penalización por alarma
            print("El ruido de la alarma no te deja descansar bien...")
        
 energia += recuperacion
        if energia > 100: energia = 100
        tiempo -= 1
        print(f"Has descansado. Energía actual: {energia}")

#CONDICIONES DE FIN
print("\n" + "="*30)
if cerraduras_abiertas == 3:
    print(f"¡VICTORIA! El agente {nombre_agente} ha abierto la bóveda.")
elif alarma and tiempo <= 3:
    print("DERROTA: El sistema se bloqueó permanentemente por la alarma.")
elif energia <= 0:
    print("DERROTA: Te has quedado sin energía y te desmayaste.")
elif tiempo <= 0:
    print("DERROTA: Se terminó el tiempo y llegó la policía.")
print("="*30)
            
            
            
            
            
#Ejercicio 5: Escape room "La Arena del Gladiador"           
#PASO 1: Configuración del Personaje ---
nombre_valido = False
nombre = ""

while not nombre_valido:
    nombre = input("Introduce el nombre del Gladiador: ")
    # Validación: Solo letras y que no esté vacío
    if nombre.isalpha():
        nombre_valido = True
    else:
        print("Error: Solo se permiten letras")

#PASO 2: Inicialización de Estadísticas
vida_jugador = 100          # int
vida_enemigo = 100          # int
pociones = 3                # int
ataque_pesado_base = 15     # int
ataque_enemigo = 12         # int
turno_gladiador = True      # boolean
juego_activo = True         # boolean

print(f"\n--- ¡BIENVENIDO A LA ARENA, {nombre.upper()}! ---")

#PASO 3: El Ciclo de Combate
while vida_jugador > 0 and vida_enemigo > 0:
    
  if turno_gladiador:
        print("-" * 30)
        print(f"ESTADO: {nombre}: {vida_jugador} HP | Enemigo: {vida_enemigo} HP")
        print(f"Pociones restantes: {pociones}")
        print("-" * 30)
        print("MENÚ DE ACCIONES:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")
        
 # Validación del Menú
 seleccion_valida = False
        opcion = ""
        
  while not seleccion_valida:
            opcion = input("Elige tu acción (1-3): ")
            
  if opcion.isdigit():
                if opcion == "1" or opcion == "2" or opcion == "3":
                    seleccion_valida = True
                else:
                    print("Error: Elige un número entre 1 y 3.")
            else:
                print("Error: Entrada no válida. Debe ser un número.")
        
  #Lógica de las Acciones
        if opcion == "1":
            # Acción A: Ataque Pesado
            danio_final = float(ataque_pesado_base)
            if vida_enemigo < 20:
                danio_final = ataque_pesado_base * 1.5
                print("¡GOLPE CRÍTICO!")
            
  vida_enemigo -= int(danio_final)
            print(f"¡Atacaste al enemigo por {danio_final} puntos de daño!")

 elif opcion == "2":
            # Acción B: Ráfaga Veloz (Uso de for)
            print("Iniciando Ráfaga Veloz...")
            for i in range(3):
                vida_enemigo -= 5
                print(" > Golpe conectado por 5 de daño")
        
  elif opcion == "3":
            # Acción C: Curar
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print(f"¡Te has curado! Ahora tienes {vida_jugador} HP.")
            else:
                print("¡No quedan pociones! Pierdes la oportunidad de curarte.")

 # Cambio de turno
  turno_gladiador = False
    
  else:
        # Turno del Enemigo
        if vida_enemigo > 0: # El enemigo solo ataca si sigue vivo
            print("\n--- Turno del Enemigo ---")
            vida_jugador -= ataque_enemigo
            print(f"¡El enemigo te atacó por {ataque_enemigo} puntos de daño!")
        
 turno_gladiador = True

# PASO 4: Fin del Juego
print("\n" + "="*30)
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")
print("="*30)
