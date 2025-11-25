from CapaDatos.Lectura_de_json import leer_archivoX
from pathlib import Path
import json 

class Sensor_json():

    def __init__(self):
        self.__ruta = Path("Archivos/Sensores.json")
        self.__ruta.parent.mkdir(exist_ok=True)
    
    def leer_json_sensores(self) -> list:
        
        lista_sensores:list = leer_archivoX(self.__ruta)

        return lista_sensores

    def escribir_json_Sensor(self, lista_sensores):

        with open(self.__ruta, "w", encoding="utf-8") as archivo:
            json.dump(lista_sensores, archivo, indent=4, ensure_ascii=False)

    def listar_ids(self) -> list:
        """
            Carga una lista con solamente los ID
            de los sensores registrados
        """
        lista_sensores:list = leer_archivoX(self.__ruta)
        lista_ids:list = []

        for sensor in lista_sensores:
            lista_ids.append(sensor["ID Sensor"])

        return lista_ids
