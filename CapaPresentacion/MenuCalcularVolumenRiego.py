from CapaNegocios.Calculos import calcular_volumen_riego
import os

def menu_calcular_volumen(banner:str): 
    
    while True:
        
        try:
        
            print(banner)
            print("\n# Ubicación actual: ~/Menú Principal/Calcular Volumen de Riego\n")

            lista_calculos:list = calcular_volumen_riego()

            for calculo in lista_calculos:
                print(
                    f"{calculo["A"]} * ({calculo["Otar"]} - {calculo["Oact"]}) * {calculo["Z"]}\n" \
                    "------------------------------------\n" \
                    f"              {calculo["n"]}\n"
                )

        except Exception as e:
            os.system("cls")
            print("\n>>> Notificaciones ", e)