from .Lectura_de_json import leer_archivoX
from pathlib import Path
import json

class Alertas_json():

    def __init__(self):
        self.__ruta:Path = Path("Archivos/Alertas.json")
        self.__ruta.parent.mkdir(exist_ok=True)

    def escribir_json_alertas(self, lista_alertas:list):

        with open(self.__ruta, "w", encoding="utf-8") as archivo:
            json.dump(lista_alertas, archivo, indent=4) 

    def leer_json_alertas(self) -> list:

        lista_generales:list = leer_archivoX(self.__ruta)

        return lista_generales 