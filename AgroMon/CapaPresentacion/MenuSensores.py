from CapaNegocios.Sensor import Sensor
from CapaNegocios.Gestor_Sensores import Gestor_Sensores
from CapaNegocios.Gestor_Lecturas import Gestor_Lecturas
import os

gestor_sensores = Gestor_Sensores()
gestor_lecturas = Gestor_Lecturas()

def menu_sensores(banner:str):

    while True:

        print(banner)
        print("\n# Ubicación actual: ~/Menú Principal/Sensores\n")
        print(
            "[1] Agregar.\n" \
            "[2] Modificar.\n" \
            "[3] Borrar.\n" \
            "[4] Ver Lista de Sensores.\n" \
            "[5] Volver al Menú Principal.\n"
        )

        opcion:str = input("<<< Digite un número según las opciones disponibles: ")
        os.system("cls")

        match opcion:

            case "1": # Agregar
                agregar_sensor(banner)

            case "2": # Modificar
                modificar_sensor(banner)

            case "3": # Borrar
                borrar_sensor(banner)

            case "4": # Ver Lista de Sensores
                ver_lista_sensores(banner)

            case "5": # Volver al Menú Principal
                return

            case _: # Opción Imprevista
                print("\n>>> Notificaciones \n>>> No ha digitado ninguna de las opciones disponibles. \n>>> Por favor, intente de nuevo.")

# Agregar
def agregar_sensor(banner:str):

    while True:

        try:
            print(banner)
            print("\n# Ubicación actual: ~/Menú Principal/Sensores/Agregar\n")

            print(">>> Datos del Sensor:")
            id_sensor:str = input(" <<< ID del Sensor (SEN-000): ")
            tipo_sensor:str = escoger_sensor()
            ud_medida:str = obtener_udMedida(tipo_sensor)
            estado_sensor:str = escoger_estado(False)
            print(" >>> Ubicación en la Parcela:")
            id_parcela:str = input("  <<< ID de la Parcela (PAR-000): ")
            print(" >>> Punto de Ubicación en Parcela: ")
            ubicacion_X:str = input("  <<< Coordenada X: ")
            ubicacion_Y:str = input("  <<< Coordenada Y: ")
            print(" >>> Rangos Válidos: ")
            rango_minimo:str = input(f"  <<< Mínimo ({ud_medida}): ")
            rango_maximo:str = input(f"  <<< Máximo ({ud_medida}): ")

            sensor = Sensor(
                False,
                id_sensor, tipo_sensor, ud_medida,
                estado_sensor, id_parcela, 
                ubicacion_X, ubicacion_Y,
                rango_minimo, rango_maximo
            )
            gestor_sensores.guardar_datos(sensor)

            os.system("cls")
            break

        except Exception as e:
            os.system("cls")
            print("\n>>> Notificaciones ", e)

    print("\n>>> Notificaciones \n>>> El sensor se ha agregado correctamente al sistema.")

def obtener_udMedida(tipo_sensor:str) -> str:
    """
        Obtiene la unidad de medida según
        el tipo de sensor seleccionado.
    """

    if tipo_sensor == "Sensor de Humedad de la Hoja":
        return "%"
    elif tipo_sensor == "Sensor de Humedad del Suelo":
        return "m³/m³"
    elif tipo_sensor == "Sensor de Temperatura":
        return "°C"

def escoger_sensor() -> str:

    print(" >>> Tipo de Sensor:")
    print(
        "  [1] Sensor de Humedad de la Hoja.\n" \
        "  [2] Sensor de Humedad del Suelo.\n" \
        "  [3] Sensor de Temperatura."
    )

    opcion:str = input("  <<< Digite un número según las opciones disponibles: ")

    match opcion:

        case "1": # Sensor de Humedad de la Hoja.
            return "Sensor de Humedad de la Hoja"

        case "2": # Sensor de Humedad del Suelo.
            return "Sensor de Humedad del Suelo"

        case "3": # Sensor de Temperatura.
            return "Sensor de Temperatura"

        case _: # Opción Imprevista
            raise Exception("\n>>> No ha digitado ninguna de las opciones disponibles. \n>>> Por favor, intente de nuevo.")

def escoger_estado(habilitado:bool) -> str:
    """
        True: Permite la selección de todos
        los tipos de estado que puede tener
        un sensor en el sistema.\n
        False: Solo se puede escoger entre
        dos estados: Activo o Inactivo
    """
    # Si requiere revisión o se pone en mantenimiento
    # entonces se modifica en la opción de modificar

    print(" >>> Estado del Sensor:")
    print("  [1] Activo.")
    print("  [2] Inactivo.")

    if habilitado:
        print("  [3] Requiere Revisión.")
        print("  [4] En Mantenimiento.")
    
    opcion:str = input("  <<< Digite un número según las opciones disponibles: ")

    match opcion:

        case "1": # Activo.
            return "Activo"

        case "2": # Inactivo.
            return "Inactivo"

        case "3": # Requiere Revisión.
            if not habilitado:
                raise Exception("\n>>> No ha digitado ninguna de las opciones disponibles. \n>>> Por favor, intente de nuevo.")
            
            return "Requiere Revisión"

        case "4": # En Mantenimiento.
            if not habilitado:
                raise Exception("\n>>> No ha digitado ninguna de las opciones disponibles. \n>>> Por favor, intente de nuevo.")
            
            return "En Mantenimiento"

        case _: # Opción Imprevista
            raise Exception("\n>>> No ha digitado ninguna de las opciones disponibles. \n>>> Por favor, intente de nuevo.")

# Modificar
def modificar_sensor(banner:str):
    
    while True:

        try:
            print(banner)
            print("\n# Ubicación actual: ~/Menú Principal/Sensores/Modificar\n")

            print(">>> Buscar Sensor: ")
            id_sensor:str = input(" <<< ID del Sensor (SEN-000): ")
            sensor:dict = gestor_sensores.buscar_sensor(id_sensor)

            print(
                f"\n>>> Datos del Sensor: {sensor["ID Sensor"]}\n"                
                f"[1] Tipo de Sensor: {sensor["Tipo Sensor"]}\n" \
                f"[2] Estado del Sensor: {sensor["Estado Sensor"]}\n" \
                f"[3] ID de la Parcela: {sensor["ID Parcela"]}\n" \
                f"[4] Punto de Ubicación en Parcela (Coordenada X): {sensor["Ubicacion en Parcela"]["Coordenada X"]}\n" \
                f"[5] Punto de Ubicación en Parcela (Coordenada Y): {sensor["Ubicacion en Parcela"]["Coordenada Y"]}\n" \
                f"[6] Rangos Válidos (Mínimo): {sensor["Rangos Validos"]["Minimo"]}{sensor["Unidad de Medida"]}\n" \
                f"[7] Rangos Válidos (Máximo): {sensor["Rangos Validos"]["Maximo"]}{sensor["Unidad de Medida"]}\n" \
                f"[8] Volver al Menú Sensores\n"
            )

            opcion:str = input("<<< Digite un número según las opciones disponibles: ")

            match opcion:

                case "1": # Tipo de Sensor
                    print("\n>>> Nuevo Tipo de Sensor: ")
                    tipo_sensor:str = escoger_sensor()
                    ud_medida:str = obtener_udMedida(tipo_sensor)

                    if sensor["Tipo Sensor"] != tipo_sensor:
                        print("\n>>> Debe cambiar el valor de los Rangos Válidos:")
                        rango_minimo:str = input(f" <<< Nuevo Rango Mínimo ({ud_medida}): ")
                        rango_maximo:str = input(f" <<< Nuevo Rango Máximo ({ud_medida}): ")

                        sensor_modificado = Sensor(
                            False,
                            sensor["ID Sensor"], tipo_sensor, ud_medida,
                            sensor["Estado Sensor"], sensor["ID Parcela"],
                            str(sensor["Ubicacion en Parcela"]["Coordenada X"]),
                            str(sensor["Ubicacion en Parcela"]["Coordenada Y"]),
                            rango_minimo, rango_maximo
                        )
                    else:
                        sensor_modificado = Sensor(
                            False,
                            sensor["ID Sensor"], sensor["Tipo Sensor"], sensor["Unidad de Medida"],
                            sensor["Estado Sensor"], sensor["ID Parcela"],
                            str(sensor["Ubicacion en Parcela"]["Coordenada X"]),
                            str(sensor["Ubicacion en Parcela"]["Coordenada Y"]),
                            str(sensor["Rangos Validos"]["Minimo"]),
                            str(sensor["Rangos Validos"]["Maximo"])
                        )


                case "2": # Estado del Sensor
                    print("\n>>> Nuevo Estado del Sensor: ")
                    estado_sensor:str = escoger_estado(True)

                    sensor_modificado = Sensor(
                            False,
                            sensor["ID Sensor"], sensor["Tipo Sensor"], sensor["Unidad de Medida"],
                            estado_sensor, sensor["ID Parcela"],
                            str(sensor["Ubicacion en Parcela"]["Coordenada X"]),
                            str(sensor["Ubicacion en Parcela"]["Coordenada Y"]),
                            str(sensor["Rangos Validos"]["Minimo"]),
                            str(sensor["Rangos Validos"]["Maximo"])
                        )

                case "3": # ID de la Parcela
                    print("\n>>> Ubicación en la Parcela:")
                    id_parcela:str = input(" <<< Nuevo ID de Parcela (PAR-000): ")

                    sensor_modificado = Sensor(
                            False,
                            sensor["ID Sensor"], sensor["Tipo Sensor"], sensor["Unidad de Medida"],
                            sensor["Estado Sensor"], id_parcela,
                            str(sensor["Ubicacion en Parcela"]["Coordenada X"]),
                            str(sensor["Ubicacion en Parcela"]["Coordenada Y"]),
                            str(sensor["Rangos Validos"]["Minimo"]),
                            str(sensor["Rangos Validos"]["Maximo"])
                        )

                case "4": # Punto de Ubicación en Parcela (Coordenada X)
                    print("\n>>> Punto de Ubicación en Parcela: ")
                    ubicacion_X:str = input(" <<< Coordenada X: ")

                    sensor_modificado = Sensor(
                            False,
                            sensor["ID Sensor"], sensor["Tipo Sensor"], sensor["Unidad de Medida"],
                            sensor["Estado Sensor"], sensor["ID Parcela"],
                            ubicacion_X,
                            str(sensor["Ubicacion en Parcela"]["Coordenada Y"]),
                            str(sensor["Rangos Validos"]["Minimo"]),
                            str(sensor["Rangos Validos"]["Maximo"])
                        )

                case "5": # Punto de Ubicación en Parcela (Coordenada Y)
                    print("\n>>> Punto de Ubicación en Parcela: ")
                    ubicacion_Y:str = input(" <<< Coordenada Y: ")

                    sensor_modificado = Sensor(
                            False,
                            sensor["ID Sensor"], sensor["Tipo Sensor"], sensor["Unidad de Medida"],
                            sensor["Estado Sensor"], sensor["ID Parcela"],
                            str(sensor["Ubicacion en Parcela"]["Coordenada X"]),
                            ubicacion_Y,
                            str(sensor["Rangos Validos"]["Minimo"]),
                            str(sensor["Rangos Validos"]["Maximo"])
                        )

                case "6": # Rangos Válidos (Mínimo)
                    print("\n>>> Rangos Válidos: ")
                    rango_minimo:str = input(f" <<< Mínimo ({sensor["Unidad de Medida"]}): ")

                    sensor_modificado = Sensor(
                            False,
                            sensor["ID Sensor"], sensor["Tipo Sensor"], sensor["Unidad de Medida"],
                            sensor["Estado Sensor"], sensor["ID Parcela"],
                            str(sensor["Ubicacion en Parcela"]["Coordenada X"]),
                            str(sensor["Ubicacion en Parcela"]["Coordenada Y"]),
                            rango_minimo,
                            str(sensor["Rangos Validos"]["Maximo"])
                        )

                case "7": # Rangos Válidos (Máximo)
                    print("\n>>> Rangos Válidos: ")
                    rango_maximo:str = input(f" <<< Máximo ({sensor["Unidad de Medida"]}): ")

                    sensor_modificado = Sensor(
                            False,
                            sensor["ID Sensor"], sensor["Tipo Sensor"], sensor["Unidad de Medida"],
                            sensor["Estado Sensor"], sensor["ID Parcela"],
                            str(sensor["Ubicacion en Parcela"]["Coordenada X"]),
                            str(sensor["Ubicacion en Parcela"]["Coordenada Y"]),
                            str(sensor["Rangos Validos"]["Minimo"]),
                            rango_maximo
                        )

                case "8": # Salir
                    os.system("cls")
                    return

                case _: # Opción Imprevista
                    os.system("cls")
                    print("\n>>> Notificaciones \n>>> No ha digitado ninguna de las opciones disponibles. \n>>> Por favor, intente de nuevo.")

            if opcion in ["1", "2", "3", "4", "5", "6", "7"]:
                gestor_sensores.modificar_sensor(sensor_modificado)
                os.system("cls")
                print("\n>>> Notificaciones \n>>> El Sensor se ha modificado correctamente en el sistema.")
                return

        except Exception as e:
            os.system("cls")
            print("\n>>> Notificaciones ", e)

# Borrar
def borrar_sensor(banner:str):
    
    while True:
        try:
            print(banner)
            print("\n# Ubicación actual: ~/Menú Principal/Sensores/Borrar\n")

            print(">>> Buscar Sensor: ")
            id_sensor:str = input(" <<< ID del Sensor (SEN-000): ")
            sensor:dict = gestor_sensores.buscar_sensor(id_sensor)

            print(
                f"\n>>> Datos del Sensor: {sensor["ID Sensor"]}\n" \
                f">>> Tipo de Sensor: {sensor["Tipo Sensor"]}\n" \
                f">>> Unidad de Medida: {sensor["Unidad de Medida"]}\n" \
                f">>> Estado: {sensor["Estado Sensor"]}\n" \
                f">>> Punto de Ubicación en Parcela:\n" \
                f" >>> ID Parcela: {sensor["ID Parcela"]}\n" \
                f" >>> Coordenada X: {sensor["Ubicacion en Parcela"]["Coordenada X"]}\n" \
                f" >>> Coordenada Y: {sensor["Ubicacion en Parcela"]["Coordenada Y"]}\n" \
                f">>> Rangos Válidos: " \
                f" >>> Mímino: {sensor["Rangos Validos"]["Minimo"]}{sensor["Unidad de Medida"]}\n" \
                f" >>> Máximo: {sensor["Rangos Validos"]["Maximo"]}{sensor["Unidad de Medida"]}\n" 
            )

            print(
                ">>> ¿Seguro que desea eliminar esta sensor? \n>>> Esto eliminará todos sus datos asociados.\n" \
                "[1] Sí, Eliminar todos los datos.\n" \
                "[2] No, Volver al Menú Sensores.\n"
            )

            opcion:str = input("<<< Digite un número según las opciones disponibles: ")
            os.system("cls")

            match opcion:

                case "1": # Sí, Eliminar todos los datos
                    gestor_sensores.borrar_un_sensor(sensor["ID Sensor"])
                    gestor_lecturas.borrar_lecturas_sensor(sensor["ID Sensor"])
                    print("\n>>> Notificaciones \n>>> El sensor y sus datos relacionados se han borrado correctamente del sistema.")
                    return

                case "2": # No, Volver al Menú Sensores
                    return

                case _:
                    print("\n>>> Notificaciones \n>>> No ha digitado ninguna de las opciones disponibles. \n>>> Por favor, intente de nuevo.")
        
        except Exception as e:
            os.system("cls")
            print("\n>>> Notificaciones ", e)

# Ver Lista de Sensores
def ver_lista_sensores(banner:str):
    
    while True:

        try:
            
            print(banner)
            print("\n# Ubicación actual: ~/Menú Principal/Sensores/Ver Lista de Sensores\n")

            print(
                "[1] Por Parcela.\n" \
                "[2] Todos.\n" \
                "[3] Volver al Menú Sensores.\n"
            )

            opcion:str = input("<<< Digite un número según las opciones disponibles: ")
            os.system("cls")

            match opcion:

                case "1": # Por Parcela.
                    mostrar_sensores_por_parcela(banner)
                
                case "2": # Todos.
                    mostrar_sensores(banner)

                case "3":
                    return
                
                case _:
                    print("\n>>> Notificaciones \n>>> No ha digitado ninguna de las opciones disponibles. \n>>> Por favor, intente de nuevo.")

        except Exception as e:
            os.system("cls")
            print("\n>>> Notificaciones ", e)

# Ver por Parcela.
def mostrar_sensores_por_parcela(banner:str):
    
    print(banner)
    print("\n# Ubicación actual: ~/Menú Principal/Sensores/Ver Lista de Sensores/Por Parcela\n")

    print(">>> Buscar por Parcela: ")
    id_parcela:str = input(" <<< ID de la Parcela (PAR-000): ")
    lista_sensores:list = gestor_sensores.lista_por_parcela(id_parcela)

    for sensor in lista_sensores:
        print(sensor)

    input("\n>>> Presione la tecla 'ENTER' para volver: ")
    os.system("cls")

# Ver Todos
def mostrar_sensores(banner:str):

    print(banner)
    print("\n# Ubicación actual: ~/Menú Principal/Sensores/Ver Lista de Sensores/Todos\n")

    print(">>> Sensores Registrados:")

    lista_sensores:list = gestor_sensores.listar_sensores()

    for sensor in lista_sensores:
        print(sensor)

    input("\n>>> Presione la tecla 'ENTER' para volver: ")
    os.system("cls")