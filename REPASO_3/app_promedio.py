cantidad_alumnos=0
alumnos_aprobados=0
alumnos_reprobados=0
import os
import time

while True:

    opcion_menu= str(input('''
    ----------MENU----------
    1.- Calcular promedio
    2.- Ver Resultados Estadisticas
    3.- Salir
    ------------------------
    
    Seleccione una opcion: '''))

    if opcion_menu=="1":
        os.system("cls")
        cantidad_alumnos= cantidad_alumnos + 1
        nota_1= float(input('''
        ------------Calcular Promedio------------
        -Nota 1:
        -Nota 2:
        -Nota 3:
        -Promedio:
        -Estado:
        -----------------------------------------
        Ingrese su primera nota porfavor: '''))

        os.system("cls")

        nota_2=float(input(f'''
        ------------Calcular Promedio------------
        -Nota 1: {nota_1}
        -Nota 2:
        -Nota 3:
        -Promedio:
        -Estado:
        --------------------------
        Ingrese su segunda nota porfavor: '''))

        os.system("cls")

        nota_3=float(input(f'''
        ------------Calcular Promedio------------
        -Nota 1: {nota_1}
        -Nota 2: {nota_2}
        -Nota 3:
        -Promedio:
        -Estado:
        -----------------------------------------
        Ingrese su tercera nota porfavor: '''))

        promedio = (nota_1+ nota_2+ nota_3)/3

        if promedio >= 4.0:
            estado= "Aprobado"
            alumnos_aprobados= alumnos_aprobados + 1
            os.system("cls")
            print(f'''
            ------------Calcular Promedio------------
            -Nota 1: {nota_1}
            -Nota 2: {nota_2}
            -Nota 3: {nota_3}
            -Promedio: {promedio}
            -Estado:{estado}
            -----------------------------------------
            ''') 
        
        else:
            estado= "Reprobado"
            os.system("cls")
            alumnos_reprobados= alumnos_reprobados + 1
            print(f'''
            ------------Calcular Promedio------------
            -Nota 1: {nota_1}
            -Nota 2: {nota_2}
            -Nota 3: {nota_3}
            -Promedio: {promedio}
            -Estado: {estado}
            -----------------------------------------
            ''')
        volver= str(input("Desea volver al menu principal? S/N: ")).upper()

        os.system("cls")

        if volver=="N":
            seguro = str(input("¿Esta seguro de salir?: ")).upper()
            if seguro=="S":
                print('''
                Usted marco que si
                En unos segundos saldra de la aplicacion
                ''')
                time.sleep(5)
                break
        
    if opcion_menu=="2":
        os.system("cls")
        print(f'''
        ----------Ver Resultados Estadisticas----------

        -Alumnos Atendidos: {cantidad_alumnos}
        -Alumnos Aprobados: {alumnos_aprobados}
        -Alumnos Reprobados: {alumnos_reprobados}

        -----------------------------------------------
        ''')
        volver= str(input("¿Desea volver al menu principal? S/N: ")).upper()
        os.system("cls")
        if volver=="N":
            if seguro=="S":
                print('''
                Usted marco que si
                En unos segundos saldra de la aplicacion
                ''')
                time.sleep(5)
                break


    if opcion_menu=="3":
        seguro= str(input("¿Esta seguro de salir?: ")).upper()
        if seguro=="S":
            print('''
            Usted marco que si
            En unos segundos saldra de la aplicacion
            ''')
            time.sleep(5)
            break





