from CapaDatos.Parcela_json import Parcela_json
from CapaDatos.Generales_json import Generales_json
from CapaDatos.Alertas_json import Alertas_json

alertas_archivo = Alertas_json()
parcela_archivo = Parcela_json()
generales_archivo = Generales_json()

def calcular_volumen_riego() -> list:

    lista_alertas:list = alertas_archivo.leer_json_alertas()
    lista_parcelas:list = parcela_archivo.leer_json_parcela()
    lista_generales:list = generales_archivo.leer_json_generales()
    
    # ID_CALCULO 
    # ID_Sensor  
    # A = Area de la Parcela 
    # 0act = Lectura # x 
    # 0tar = Vol de riego deseado 
    # Z = Zona radicular 
    # n = Eficiencia riego 
    
    # Vrec = Volumen de Riego deseado  

    A = 0
    Oact = 0 
    Otar = 0
    Z = 0
    n = 0
    lista_calculos:list = []
    # creo que no es necesario ver si Oact > Otar porque ya se 
    # filtra por el tipo de alerta, el valor detectado'
    # no es mayor, no hay alertas de exceso de humedad

    for alerta in lista_alertas:
        if (alerta["Tipo Alerta"] == "Alerta de Riego" or
            alerta["Tipo Alerta"] == "Alerta de Riego por Suelo"):
            A, Oact, Otar, Z, n = None, None, None, None, None

            for parcela in lista_parcelas:
                if alerta["ID Parcela"] == parcela["ID Parcela"]:
                    A = float(parcela["Area"])
                    Oact = float(alerta["Valor Detectado"])
                    break
            for generales in lista_generales:
                if alerta["ID Parcela"] == generales["ID Parcela"]:
                    Otar = float(generales["Volumen Riego Deseado"])
                    Z = float(generales["Zona Radicular"])
                    n = float(generales["Eficiencia Sistema"])
                    break
        Vrec = (A * (Otar - Oact) * Z) / n
        diccionario_calculos = {
            "ID Parcela": alerta["ID Parcela"],
            "A": A, 
            "Oact": Oact,
            "Otar": Otar,
            "Z": Z,
            "n": n,
            "Vrec": Vrec
        }
        lista_calculos.append(diccionario_calculos)
    
    return lista_calculos