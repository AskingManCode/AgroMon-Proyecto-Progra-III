# Importaciones
from CapaPresentacion.MenuParcelas import menu_parcelas
from CapaPresentacion.MenuSensores import menu_sensores
from CapaPresentacion.MenuLecturaSensores import menu_lectura_sensores
from CapaPresentacion.MenuAlertas import menu_alertas
from CapaPresentacion.MenuCalcularVolumenRiego import menu_calcular_volumen
import os # Permite trabajar con el SO pero yo lo utilizo simplemente para limpiar la consola

# Menú Principal
def menu_principal(banner:str) -> str:
    """ 
        Menú Principal: Muestra opciones principales 
        que servirán para mostrar los distintos tipos
        de menú del programa
    """
    print(banner)
    print("\n# Ubicación actual: ~/Menú Principal\n") # Este print ubicará al usuario en el programa
    print(
        "[1] Parcelas.\n" \
        "[2] Sensores.\n" \
        "[3] Lectura de Sensores.\n" \
        "[4] Alertas.\n" \
        "[5] Calcular Volumen de Riego.\n" \
        "[6] Salir.\n"
    )

    return input("<<< Digite un número según las opciones disponibles: ") ### <<<: Representa Input ### >>> Representa Output

# Salir
def salir_def(banner:str) -> bool:

    while True:
            
        print(banner)
        print("\n# Ubicación actual: ~/\n")
        print(
            "¿Seguro de que desea salir?\n\n" \
            "[1] Salir.\n" \
            "[2] Volver al Menú Principal.\n"
        )

        opcion_salir = input("<<< Digite un número según las opciones disponibles: ")
        os.system("cls")

        match opcion_salir:
                            
            case "1": # Salir
                return True
                
            case "2": # Volver al Menú Principal
                return False

            case _: # Opción Imprevista
                print("\n>>> Notificaciones \n>>> No ha digitado ninguna de las opciones disponibles. \n>>> Por favor, intente de nuevo.")

# Main
if __name__ == "__main__":
    
    os.system('cls') # Limpia la consola
    opcion:str = ""
    banner:str = "\n" \
            "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|\n" \
            "| <+>  SISTEMA GESTOR DE PARCELAS Y SENSORES: AGROMON  <+> |\n" \
            "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|"

    while opcion != "6":

        opcion = menu_principal(banner)
        os.system("cls")
        
        match opcion:
            case "1": # Parcelas
                menu_parcelas(banner)

            case "2": # Sensores
                menu_sensores(banner)

            case "3": # Lectura de Sensores
                menu_lectura_sensores(banner)

            case "4": # Alertas
                menu_alertas(banner)

            case "5": # Calcular Volumen de Riego
                menu_calcular_volumen(banner)
            
            case "6": # Salir
                salir:bool = salir_def(banner)

                if salir:
                    print(banner)
                    print("\n>>> Saliendo del Sistema...\n")
                else:
                    opcion = "Hello World!"
                    
            case _: # Opción Imprevista
                print("\n>>> Notificaciones \n>>> No ha digitado ninguna de las opciones disponibles. \n>>> Por favor, intente de nuevo.")