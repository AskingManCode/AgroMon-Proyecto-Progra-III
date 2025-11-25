from CapaNegocios.Gestor_Parcelas import Gestor_Parcelas
from CapaNegocios.Gestor_Generales import Gestor_Generales
from CapaNegocios.Parcela import Parcela
from CapaNegocios.Generales import Generales
from CapaNegocios.Gestor_Sensores import Gestor_Sensores
from CapaNegocios.Gestor_Lecturas import Gestor_Lecturas
import os

gestor_parcelas = Gestor_Parcelas()
gestor_generales = Gestor_Generales()
gestor_sensores = Gestor_Sensores()
gestor_lecturas = Gestor_Lecturas()

# Menú Parcelas
def menu_parcelas(banner:str):

    while True:

        print(banner)
        print("\n# Ubicación actual: ~/Menú Principal/Parcelas\n")
        print(
            "[1] Agregar.\n" \
            "[2] Modificar.\n" \
            "[3] Borrar.\n" \
            "[4] Ver Lista de Parcelas.\n" \
            "[5] Valores Generales.\n" \
            "[6] Volver al Menú Principal.\n"
        )

        opcion:str = input("<<< Digite un número según las opciones disponibles: ")
        os.system("cls")

        match opcion:

            case "1": # Agregar
                agregar_parcela(banner)

            case "2": # Modificar
                modificar_parcela(banner)

            case "3": # Borrar
                borrar_parcela(banner)

            case "4": # Ver Lista de Parcelas
                ver_lista_parcelas(banner)

            case "5": # Ver/Modificar Valores Generales
                ver_modificar_generales(banner)

            case "6": # Volver al Menú Principal
                return

            case _: # Opción Imprevista
                print("\n>>> Notificaciones \n>>> No ha digitado ninguna de las opciones disponibles. \n>>> Por favor, intente de nuevo.")

# Agregar
def agregar_parcela(banner:str):

    while True:
            
        try:
            print(banner)
            print("\n# Ubicación actual: ~/Menú Principal/Parcelas/Agregar\n")

            print(">>> Datos Iniciales de la Parcela:")
            id_parcela:str = input(" <<< ID de la Parcela (PAR-000): ")
            nombre:str = input(" <<< Nombre: ")
            print(" >>> Ubicación Geográfica (Coordenadas):")
            ubicacion_latitud:str = input("  <<< Latitud: ")
            ubicacion_longitud:str = input("  <<< Longitud: ")
            tipo_cultivo:str = input(" <<< Tipo de Cultivo: ")
            area:str = input(" <<< Área (m²): ")

            # Datos Generales
            print("\n>>> Datos Generales de la Parcela:")
            zona_radicular:str = input(" <<< Profundidad Efectiva de la Raíz / Zona Radicular (m): ")
            eficiencia_sistema:str = input(" <<< Eficiencia del Sistema de Riego para Surco: ")
            print(" >>> Umbral de Humedad de la Hoja Permitido:")
            humedad_minima:str = input("  <<< Mínimo (%): ")
            humedad_maxima:str = input("  <<< Máximo (%): ")
            volumen_riego:str = input(" <<< Volumen de Riego Deseado (m³): ")
            
            # Crea un nuevo objeto Parcela
            parcela = Parcela(
                False,
                id_parcela, nombre, ubicacion_latitud, 
                ubicacion_longitud, tipo_cultivo, area,
            )

            # Crea un objeto Generales
            generales_parcela = Generales(
                False,
                id_parcela,  zona_radicular, eficiencia_sistema, 
                humedad_minima, humedad_maxima, volumen_riego
            )

            gestor_parcelas.guardar_datos(parcela)
            gestor_generales.guardar_datos(generales_parcela)
            
            os.system("cls")
            break

        except Exception as e:
            os.system("cls")
            print("\n>>> Notificaciones ", e)

    print("\n>>> Notificaciones \n>>> La parcela se ha agregado correctamente al sistema.")

# Modificar
def modificar_parcela(banner:str):
    
    while True:

        try:
            print(banner)
            print("\n# Ubicación actual: ~/Menú Principal/Parcelas/Modificar\n")

            print(">>> Buscar Parcela: ")
            id_parcela:str = input(" <<< ID de la Parcela (PAR-000): ")
            parcela:dict = gestor_parcelas.buscar_parcela(id_parcela)
            
            print(
                f"\n>>> Datos de la Parcela: {parcela["ID Parcela"]}\n" \
                f"[1] Nombre: {parcela["Nombre"]}\n" \
                f"[2] Ubicación Geográfica (Latitud): {parcela["Ubicacion Geografica"]["Latitud"]}\n" \
                f"[3] Ubicación Geográfica (Longitud): {parcela["Ubicacion Geografica"]["Longitud"]}\n" \
                f"[4] Tipo de Cultivo: {parcela["Tipo Cultivo"]}\n" \
                f"[5] Área: {parcela["Area"]}m²\n" \
                f"[6] Volver al Menú Parcelas.\n"
            )

            opcion:str = input("<<< Digite un número según las opciones disponibles: ")

            match opcion:

                case "1": # Nombre
                    nombre:str = input("\n<<< Nuevo Nombre: ")

                    parcela_modificada = Parcela(
                        False, parcela["ID Parcela"], nombre, 
                        str(parcela["Ubicacion Geografica"]["Latitud"]),
                        str(parcela["Ubicacion Geografica"]["Longitud"]), 
                        parcela["Tipo Cultivo"], str(parcela["Area"])
                    )

                case "2": # Latitud
                    print("\n>>> Ubicación Geográfica (Coordenadas)")
                    latitud:str = input(" <<< Nueva Latitud: ")

                    parcela_modificada = Parcela(
                        False, parcela["ID Parcela"], parcela["Nombre"], 
                        latitud, 
                        str(parcela["Ubicacion Geografica"]["Longitud"]), 
                        parcela["Tipo Cultivo"], str(parcela["Area"])
                    )

                case "3": # Longitud
                    print("\n>>> Ubicación Geográfica (Coordenadas)")
                    longitud:str = input(" <<< Nueva Longitud: ")

                    parcela_modificada = Parcela(
                        False, parcela["ID Parcela"], parcela["Nombre"], 
                        str(parcela["Ubicacion Geografica"]["Latitud"]),
                        longitud, 
                        parcela["Tipo Cultivo"], str(parcela["Area"])
                    )

                case "4": # Tipo de Cultivo 
                    tipo_cultivo:str = input("\n<<< Nuevo Tipo de Cultivo: ")

                    parcela_modificada = Parcela(
                        False, parcela["ID Parcela"], parcela["Nombre"],
                        str(parcela["Ubicacion Geografica"]["Latitud"]),
                        str(parcela["Ubicacion Geografica"]["Longitud"]),
                        tipo_cultivo, str(parcela["Area"])
                    )

                case "5": # Area 
                    area:str = input("\n<<< Nuevo Área (m²): ")

                    parcela_modificada = Parcela(
                        False, parcela["ID Parcela"], parcela["Nombre"],
                        str(parcela["Ubicacion Geografica"]["Latitud"]),
                        str(parcela["Ubicacion Geografica"]["Longitud"]),
                        parcela["Tipo Cultivo"], area
                    )
                
                case "6": # Salir
                    os.system("cls")
                    return

                case _: # Opción Imprevista
                    os.system("cls")
                    print("\n>>> Notificaciones \n>>> No ha digitado ninguna de las opciones disponibles. \n>>> Por favor, intente de nuevo.")

            if opcion in ["1", "2", "3", "4", "5"]:
                gestor_parcelas.modificar_parcela(parcela_modificada)
                os.system("cls")
                print("\n>>> Notificaciones \n>>> La Parcela se ha modificado correctamente en el sistema.")
                return

        except Exception as e:
            os.system("cls")
            print("\n>>> Notificaciones ", e)

# Borrar
def borrar_parcela(banner:str):
    
    while True:
        
        try:
            print(banner)
            print("\n# Ubicación actual: ~/Menú Principal/Parcelas/Borrar\n")

            print(">>> Buscar Parcela: ")
            id_parcela:str = input(" <<< ID de la Parcela (PAR-000): ")
            parcela:dict = gestor_parcelas.buscar_parcela(id_parcela)

            print(
                f"\n>>> Datos de la Parcela: {parcela["ID Parcela"]}\n" \
                f">>> Nombre: {parcela["Nombre"]}\n" \
                f">>> Ubicación Geográfica (Coordenadas):\n" \
                f" >>> Latitud: {parcela["Ubicacion Geografica"]["Latitud"]}\n" \
                f" >>> Longitud: {parcela["Ubicacion Geografica"]["Longitud"]}\n" \
                f">>> Tipo de Cultivo: {parcela["Tipo Cultivo"]}\n" \
                f">>> Área: {parcela["Area"]}m²\n"
            )
        
            print(
                ">>> ¿Seguro que desea eliminar esta parcela? \n>>> Esto eliminará todos sus datos asociados.\n" \
                "[1] Sí, Eliminar todos los datos.\n" \
                "[2] No, Volver al Menú Parcelas.\n"
            )

            opcion:str = input("<<< Digite un número según las opciones disponibles: ")
            os.system("cls")

            match opcion:

                case "1": # Sí, Eliminar todos los datos.
                    gestor_parcelas.borrar_parcela(parcela["ID Parcela"])
                    gestor_generales.borrar_datos_generales(parcela["ID Parcela"])
                    gestor_sensores.borrar_sensores_parcela(parcela["ID Parcela"])
                    gestor_lecturas.borrar_todas_lecturas(parcela["ID Parcela"])
                    print("\n>>> Notificaciones \n>>> La Parcela y sus datos relacionados se han borrado correctamente del sistema.")
                    return

                case "2": # Salir
                    return

                case _: # Opción Imprevista 
                    print("\n>>> Notificaciones \n>>> No ha digitado ninguna de las opciones disponibles. \n>>> Por favor, intente de nuevo.")
        
        except Exception as e:
            os.system("cls")
            print("\n>>> Notificaciones ", e)

# Ver Lista de Parcelas
def ver_lista_parcelas(banner:str):

    print(banner)
    print("\n# Ubicación actual: ~/Menú Principal/Parcelas/Ver Lista de Parcelas\n")

    print(">>> Parcelas Registradas:")

    lista_parcelas:list = gestor_parcelas.listar_parcelas()

    for parcela in lista_parcelas:
        print(parcela)
        
    input("\n>>> Presione la tecla 'ENTER' para volver: ")
    os.system("cls")

# Valores Generales (Ver/Modificar)
def ver_modificar_generales(banner:str):
    
    while True:

        print(banner)
        print("\n# Ubicación actual: ~/Menú Principal/Parcelas/Valores Generales\n")
        print(
            "[1] Ver.\n" \
            "[2] Modificar.\n" \
            "[3] Volver al Menú Parcelas.\n"
        )
        opcion:str = input("<<< Digite un número según las opciones disponibles: ")
        os.system("cls")

        match opcion:

            case "1": # Ver 
                ver_valores_generales(banner)

            case "2": # Modificar Valores Generales.
                modificar_valores_generales(banner)

            case "3": # Volver al menú.
                return

            case _: # Opción Imprevista
                print("\n>>> Notificaciones \n>>> No ha digitado ninguna de las opciones disponibles. \n>>> Por favor, intente de nuevo.")

# Ver Valores Generales
def ver_valores_generales(banner:str):

    print(banner)
    print("\n# Ubicación actual: ~/Menú Principal/Parcelas/Valores Generales/Ver\n")

    print(">>> Valores Generales de Parcelas Registradas:")
                
    lista_generales:list = gestor_generales.listar_datos_generales()

    for valores in lista_generales:
        print(valores)

    input("\n>>> Presione la tecla 'ENTER' para volver: ")
    os.system("cls")

# Modificar Valores Generales
def modificar_valores_generales(banner:str):

    while True:

        try:

            print(banner)
            print("\n# Ubicación actual: ~/Menú Principal/Parcelas/Valores Generales/Modificar\n")

            print(">>> Buscar Valores Generales de Parcela: ")
            id_parcela:str = input(" <<< ID de la Parcela (PAR-000): ")
            generales:dict = gestor_generales.buscar_datos_generales(id_parcela)

            print(
                f"\n>>> Datos de la Parcela: {generales["ID Parcela"]}\n" \
                f"[1] Profundidad Efectiva de la Raíz / Zona Radicular: {generales["Zona Radicular"]}m\n" \
                f"[2] Eficiencia del Sistema de Riego para Surco: {generales["Eficiencia Sistema"]}\n" \
                f"[3] Umbral de Humedad de la Hoja Permitido (Mínimo): {generales["Umbral Humedad Hoja"]["Humedad Minima"]}%\n" \
                f"[4] Umbral de Humedad de la Hoja Permitido (Máximo): {generales["Umbral Humedad Hoja"]["Humedad Maxima"]}%\n" \
                f"[5] Volumen de Riego Deseado: {generales["Volumen Riego Deseado"]}m³\n" \
                f"[6] Volver al Menú Parcelas.\n"
            )
            
            opcion:str = input("<<< Digite un número según las opciones disponibles: ")

            match opcion:

                case "1": # Profundidad Efectiva de la Raíz / Zona Radicular:
                    zona_radicular:str = input("\n<<< Nueva Profundidad Efectiva de la Raíz / Zona Radicular (m): ")

                    datos_generales = Generales(
                        False, generales["ID Parcela"], zona_radicular,
                        str(generales["Eficiencia Sistema"]),
                        str(generales["Umbral Humedad Hoja"]["Humedad Minima"]),
                        str(generales["Umbral Humedad Hoja"]["Humedad Maxima"]),
                        str(generales["Volumen Riego Deseado"])
                    )

                case "2": # Eficiencia del Sistema de Riego para Surco
                    eficiencia_sistema:str = input("\n<<< Nueva Eficiencia del Sistema de Riego para Surco: ")

                    datos_generales = Generales(
                        False, generales["ID Parcela"], str(generales["Zona Radicular"]),
                        eficiencia_sistema,
                        str(generales["Umbral Humedad Hoja"]["Humedad Minima"]),
                        str(generales["Umbral Humedad Hoja"]["Humedad Maxima"]),
                        str(generales["Volumen Riego Deseado"])
                    )

                case "3": # Umbral de Humedad de la Hoja Permitido (Mínimo)
                    print("\n>>> Umbral de Humedad de la Hoja Permitido:")
                    humedad_minima:str = input(" <<< Mínimo (%): ")

                    datos_generales = Generales(
                        False, generales["ID Parcela"], str(generales["Zona Radicular"]),
                        str(generales["Eficiencia Sistema"]),
                        humedad_minima,
                        str(generales["Umbral Humedad Hoja"]["Humedad Maxima"]),
                        str(generales["Volumen Riego Deseado"])
                    )

                case "4": # Umbral de Humedad de la Hoja Permitido (Máximo) 
                    print("\n>>> Umbral de Humedad de la Hoja Permitido:")
                    humedad_maxima:str = input(" <<< Máximo (%): ")

                    datos_generales = Generales(
                        False, generales["ID Parcela"], str(generales["Zona Radicular"]),
                        str(generales["Eficiencia Sistema"]),
                        str(generales["Umbral Humedad Hoja"]["Humedad Minima"]),
                        humedad_maxima,
                        str(generales["Volumen Riego Deseado"])
                    )

                case "5": # Volumen de Riego Deseado
                    volumen_riego:str = input("\n<<< Volumen de Riego Deseado (m³): ")

                    datos_generales = Generales(
                        False, generales["ID Parcela"], str(generales["Zona Radicular"]),
                        str(generales["Eficiencia Sistema"]),
                        str(generales["Umbral Humedad Hoja"]["Humedad Minima"]),
                        str(generales["Umbral Humedad Hoja"]["Humedad Maxima"]),
                        volumen_riego
                    )
                
                case "6": # Salir
                    os.system("cls")
                    return

                case _: # Opción Imprevista
                    os.system("cls")
                    print("\n>>> Notificaciones \n>>> No ha digitado ninguna de las opciones disponibles. \n>>> Por favor, intente de nuevo.")

            if opcion in ["1", "2", "3", "4", "5"]:
                gestor_generales.modificar_generales(datos_generales)
                os.system("cls")
                print("\n>>> Notificaciones \n>>> Los Valores Generales de la Parcela se han modificado correctamente en el sistema.")
                return

        except Exception as e:
            os.system("cls")
            print("\n>>> Notificaciones ", e)

    