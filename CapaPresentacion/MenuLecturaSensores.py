from CapaNegocios.Gestor_Lecturas import Gestor_Lecturas
from CapaNegocios.Lectura import Lectura
from datetime import datetime
import locale
from tkinter import filedialog # esto me permite traer la ventana de dialo para facilitar ecoger cualquier ruta
import os

gestor_lecturas = Gestor_Lecturas()
try:
    locale.setlocale(locale.LC_TIME, 'es')
except locale.Error:
    pass

def menu_lectura_sensores(banner:str):

    while True:

        print(banner)
        print("\n# Ubicación actual: ~/Menú Principal/Lectura de Sensores\n")
        print(
            "[1] Agregar.\n" \
            "[2] Cargar Archivo.\n" \
            "[3] Ver Lecturas.\n" \
            "[4] Borrar Información.\n" \
            "[5] Volver al Menú Principal.\n"
        )
        
        opcion:str = input("<<< Digite un número según las opciones disponibles: ")
        os.system("cls")

        match opcion:

            case "1": # Agregar
                agregar_lectura(banner)

            case "2": # Cargar Archivo
                cargar_archivo(banner)

            case "3": # Ver Lecturas
                listar_lecturas(banner)

            case "4": # Borrar Información.
                borrar_info(banner)

            case "5": # Volver al Menú Principal
                return 

            case _: # Opción Imprevista
                print("\n>>> Notificaciones \n>>> No ha digitado ninguna de las opciones disponibles. \n>>> Por favor, intente de nuevo.")

# Agregar
def agregar_lectura(banner:str):
    
    while True:

        try:
            print(banner)
            print("\n# Ubicación actual: ~/Menú Principal/Lectura de Sensores/Agregar\n")

            print(">>> Datos de Lectura Manual:")
            id_lectura:str = input(" <<< ID de la Lectura (LEC-000): ")
            id_sensor:str = input(" <<< ID del Sensor (SEN-000): ")
            id_parcela:str = input(" <<< ID de la Parcela (PAR-000): ")
            fecha_hora:datetime = datetime.now()
            valor_lectura:str = input(" >>> Valor detectado: ")

            lectura = Lectura(
                False,
                id_lectura, id_sensor,
                id_parcela, fecha_hora,
                valor_lectura
            )

            gestor_lecturas.guardar_lectura(lectura)

            os.system("cls")
            break

        except Exception as e:
            os.system("cls")
            print("\n>>> Notificaciones ", e)
            
    print("\n>>> Notificaciones \n>>> La lectura se ha agregado correctamente al sistema.")
    
# Cargar Archivo
def cargar_archivo(banner: str):

    while True:

        try:
            print(banner)
            print("\n# Ubicación actual: ~/Menú Principal/Lectura de Sensores/Cargar Archivo\n")
            print(">>> Abriendo ventana de archivos...")

            ruta_xml = filedialog.askopenfilename(
                title="Seleccionar Archivo de Lecturas (XML)",
                defaultextension=".xml",
                filetypes=[("Archivos XML", "*.xml")]
            )

            gestor_lecturas.guardar_datos_xml(ruta_xml)

            os.system("cls")
            break

        except Exception as e:
            os.system("cls")
            print("\n>>> Notificaciones ", e)
            return
        
    print("\n>>> Notificaciones \n>>> Las lecturas se han agregado correctamente al sistema.")

# Ver Lecturas
def listar_lecturas(banner:str):
    
    while True:

        try:

            print(banner)
            print("\n# Ubicación actual: ~/Menú Principal/Lectura de Sensores/Ver Lecturas\n")

            print(
                "[1] Todo.\n" \
                "[2] Por Sensor.\n" \
                "[3] Por Parcela.\n" \
                "[4] Volver al Menú Lectura de Sensores.\n"
            )

            opcion:str = input("<<< Digite un número según las opciones disponibles: ")
            os.system("cls")

            match opcion:

                case "1": # Todo 
                    listar_sensores(banner)

                case "2": # Por Parcela
                    ver_por_sensor(banner)

                case "3": # Por Parcela.
                    ver_por_dia(banner)

                case "4": # Volver al Menú Lectura de Sensores.
                    return

                case _: 
                    print("\n>>> Notificaciones \n>>> No ha digitado ninguna de las opciones disponibles. \n>>> Por favor, intente de nuevo.")

        except Exception as e:
            os.system("cls")
            print("\n>>> Notificaciones ", e)
            return
        
# Ver Todo
def listar_sensores(banner:str):

    print(banner)
    print("\n# Ubicación actual: ~/Menú Principal/Lectura de Sensores/Ver Lecturas/Todo\n")

    print(">>> Lecturas Registradas:")

    lista_lecturas:list = gestor_lecturas.listar_lecturas()

    for lectura in lista_lecturas:
        print(lectura)

    input("\n>>> Presione la tecla 'ENTER' para volver: ")
    os.system("cls")

# Ver por Parcela y sensor
def ver_por_sensor(banner:str):
    
    while True:
        
        try:

            print(banner)
            print("\n# Ubicación actual: ~/Menú Principal/Lectura de Sensores/Ver Lecturas/Por Sensor\n")

            id_parcela:str = input("<<< ID de la Parcela (PAR-000): ")
            id_sensor:str = input("<<< ID del Sensor (SEN-000): ")
            fecha_hora:str = input(f"<<< Fecha '{datetime.now().strftime("%d de %B de %Y")}' (Opcional): ")

            lectura:list = gestor_lecturas.listar_por_sensor_fecha(id_parcela, id_sensor, fecha_hora)
            print(lectura)

            input("\n>>> Presione la tecla 'ENTER' para volver: ")
            os.system("cls")
            return

        except Exception as e:
            os.system("cls")
            print("\n>>> Notificaciones ", e)

# Por Parcela
def ver_por_dia(banner:str):
    
    while True:
        
        try:

            print(banner)
            print("\n# Ubicación actual: ~/Menú Principal/Lectura de Sensores/Ver Lecturas/Por Parcela\n")

            id_parcela:str = input(" <<< ID de la Parcela (PAR-000): ")
            fecha_hora:str = input(f"<<< Fecha '{datetime.now().strftime("%d de %B de %Y")}': ")

            lista_lecturas_buscadas:list = gestor_lecturas.listar_por_parcela_dia(id_parcela, fecha_hora)

            for lectura in lista_lecturas_buscadas:
                print(lectura)

            input("\n>>> Presione la tecla 'ENTER' para volver: ")
            os.system("cls")
            return

        except Exception as e:
            os.system("cls")
            print("\n>>> Notificaciones ", e)

# Borrar Información
def borrar_info(banner:str):
    
    while True:

        try:

            print(banner)
            print("\n# Ubicación actual: ~/Menú Principal/Lectura de Sensores/Borrar Información\n")

            id_parcela:str = input("<<< ID de la Parcela (PAR-000): ")
            id_sensor:str = input("<<< ID del Sensor (SEN-000): ")
            fecha_hora:str = input(f"<<< Fecha '{datetime.now().strftime("%d de %B de %Y")}': ")

            lista_lecturas:list = gestor_lecturas.buscar_informacion_sensor_parcela(id_parcela, id_sensor, fecha_hora)

            for lectura in lista_lecturas:
                print(lectura)

            print(
                ">>> ¿Seguro que desea eliminar las lecturas de este sensor? \n" \
                "[1] Sí, Eliminar todos los datos.\n" \
                "[2] No, Volver al Menú Lectura de Sensores.\n"
            )
            
            opcion:str = input("<<< Digite un número según las opciones disponibles: ")
            os.system("cls")

            match opcion:

                case "1": # Sí, Eliminar todos los datos.
                    gestor_lecturas.borrar_informacion_sensor(id_parcela, id_sensor, fecha_hora)
                    print("\n>>> Notificaciones \n>>> Las lecturas se han borrado correctamente del sistema.")
                    return

                case "2": # Salir
                    return

                case _: # Opción Imprevista 
                    print("\n>>> Notificaciones \n>>> No ha digitado ninguna de las opciones disponibles. \n>>> Por favor, intente de nuevo.")

        except Exception as e:
            os.system("cls")
            print("\n>>> Notificaciones ", e)



