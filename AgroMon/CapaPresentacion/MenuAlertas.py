from CapaNegocios.Gestor_Lecturas import Gestor_Lecturas
from datetime import datetime
import locale
import os 

try:
    locale.setlocale(locale.LC_TIME, 'es')
except locale.Error:
    pass

gestor_lecturas = Gestor_Lecturas()

def menu_alertas(banner:str): 

    while True: 

        print(banner) 
        print("\n# Ubicación actual: ~/Menú Principal/Alertas\n") 
        print(
            "[1] Calcular.\n" \
            "[2] Ver Alertas Por Parcela.\n" \
            "[3] Volver al Menú Principal.\n"
        ) 

        opcion:str = input("<<< Digite un número según las opciones disponibles: ") 
        os.system("cls") 

        match opcion: 

            case "1": # Calcular 
                calcular_alertas(banner)

            case "2": # Ver Alertas 
                ver_por_parcela(banner)

            case "3": # Volver al Menú Principal 
                return 

            case _:# Opción Imprevista 
                print("\n>>> Notificaciones \n>>> No ha digitado ninguna de las opciones disponibles. \n>>> Por favor, intente de nuevo.") 

# Calcular 
def calcular_alertas(banner:str):

    while True: 

        try:

            print(banner) 
            print("\n# Ubicación actual: ~/Menú Principal/Alertas\Calcular\n")

            fecha_hora:str = input(f"<<< Fecha '{datetime.now().strftime("%d de %B de %Y")}' (Opcional): ")

            lista_alertas:list = gestor_lecturas.calcular_alertas(fecha_hora)

            if not lista_alertas:
                print("\n>>> No se encontraron alertas para la fecha indicada.")

            for alerta in lista_alertas:
                print(
                    f"\n>>> ID Parcela: {alerta["ID Parcela"]}\n" \
                    f">>> ID Sensor: {alerta["ID Sensor"]}\n" \
                    f">>> Fecha Alerta: {alerta["Fecha Alerta"]}\n" \
                    f">>> Tipo Alerta: {alerta["Tipo Alerta"]}\n" \
                    f">>> Valor Detectado: {alerta["Valor Detectado"]}"
                )
                if (alerta["Tipo Alerta"] == "Alerta de Riego" or
                    alerta["Tipo Alerta"] == "Alerta de Riego por Suelo"):
                    print(">>> Nota: Se recomienda calcular el volumen de regio necesario.\n")

            input("\n>>> Presione la tecla 'ENTER' para volver: ")
            os.system("cls")
            return

        except Exception as e:
            os.system("cls")
            print("\n>>> Notificaciones ", e)
            return

def ver_por_parcela(banner:str):

    while True: 

        try:

            print(banner) 
            print("\n# Ubicación actual: ~/Menú Principal/Alertas\Ver Alertas Por Parcela\n")

            id_parcela:str = input(" <<< ID de la Parcela (PAR-000): ")
            lista_alertas:list = gestor_lecturas.ver_alertas_parcela(id_parcela)

            for alerta in lista_alertas:
                print(
                    f"\n>>> ID Parcela: {alerta["ID Parcela"]}\n" \
                    f">>> ID Sensor: {alerta["ID Sensor"]}\n" \
                    f">>> Fecha Alerta: {alerta["Fecha Alerta"]}\n" \
                    f">>> Tipo Alerta: {alerta["Tipo Alerta"]}\n" \
                    f">>> Valor Detectado: {alerta["Valor Detectado"]}"
                )
            
            input("\n>>> Presione la tecla 'ENTER' para volver: ")
            os.system("cls")
            return

        except Exception as e:
            os.system("cls")
            print("\n>>> Notificaciones ", e)
            return
