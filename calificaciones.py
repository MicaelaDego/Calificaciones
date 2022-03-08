#desarrollar una funcion que imprima   un menu:  agregar materia, conocer estado de una materia, salir
###### FUNCIONES

def imprimir_menu ():
    print ('###### MENU #####')
    print ('1. Agregar materia')
    print ('2. Conocer estado de una materia')
    print ('3. Salir')

def solicitar_datos ():
    materia = input ('ingrese una materia: ')
    calificaciones = input('ingrese las calificaciones separadas por coma: ')

    calificaciones = calificaciones.split(',')
    return materia, calificaciones 

def agregar_materia(materia, calificaciones):
    archivo = open(r'.\miscalificaciones.txt', 'w') # ./ va a la carpeta donde se esta ejecutando este programa y crea el archivo
    cadena = materia + ',' + ','.join(calificaciones) + '\n'
    archivo.write(cadena)

    archivo.close()

def conocer_estado (nombre):
    archivo = open(r'.\miscalificaciones.txt', 'r') # r es modo lectura (read)
    for linea in archivo.readlines():
        listado = linea.split(',')
        nombre_materia = listado[0]
        calificaiones = listado[1: ]

        if nombre_materia.lower() == nombre.lower():
            suma_total = 0
            for calificacion in calificaciones:
                calificacion = int(calificacion)
                suma_total += calificacion
            promedio = suma_total / len(calificaciones)
            if promedio >= 6:
                print ('aprobado')
            else:
                print ('desaprobado')
                archivo.close()
            return
    archivo.close()

imprimir_menu()

opcion = input ('ingrese una opcion: ')

while opcion != 3:

    if opcion == '1' :
        materia, calificaciones = solicitar_datos()
        agregar_materia(materia, calificaciones)
    elif opcion == '2':
        nombre_materia = input ('Ingrese el nombre de la materia: ')
        conocer_estado (nombre_materia)
    imprimir_menu()
    opcion = input ('ingrese una opcion: ')

