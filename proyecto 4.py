#TO-DO LIST PARA GITHUB

import os

os.system('cls')

lista_de_tareas = []

while True:
    print ('!BIENVENIDO A TO-DO LIST!')
    print (' 1. Agregar tarea')
    print (' 2. Ver las tareas')
    print (' 3. Marcar tareas como hechas')
    print (' 4. Eliminar tareas')
    print (' 5. Guardarlas en un archivo')
    print (' 6. Salir')
    
    opcion = int(input('Introduce una opción: '))
    
    if opcion == 1:
        agregar = input('Agrega una tarea: ')
        lista_de_tareas.append(agregar)
        os.system('cls')
        
    elif opcion == 2:
        for i, tarea in enumerate(lista_de_tareas, start=1):
            print (f'{i}.{tarea}')

    elif opcion == 3:
        hecha = int(input('¿Qué tarea completaste?(número): '))
        indice = hecha - 1
        
        lista_de_tareas[indice] = "[✓] " + lista_de_tareas[indice]
    
    elif opcion == 4:
        for i, tarea in enumerate(lista_de_tareas, start=1):
            print(f'{i}.{tarea}')
        print()
        eliminar =  int(input('Qué tarea quieres eliminar?: '))
        
        lista_de_tareas.pop(eliminar-1)
    
    elif opcion == 5:
        with open('tareas.txt', 'w', encoding='utf-8') as archivo:
            for tarea in lista_de_tareas:
                archivo.write(tarea + '\n')
    
    elif opcion == 6:
        print('Hasta la próxima')
        break