from .Lectura_de_json import leer_archivoX
from pathlib import Path
import json

class Lecturas_json():

    def __init__(self):
        self.__ruta:Path = Path("Archivos/Lecturas.json")
        self.__ruta.parent.mkdir(exist_ok=True)

    def leer_json_lecturas(self) -> list:

        lista_lecturas:list = leer_archivoX(self.__ruta)
        
        return lista_lecturas
    
    def escribir_json_lecturas(self, lista_lecturas:list):

        with open(self.__ruta, "w", encoding="utf-8") as archivo:
            json.dump(lista_lecturas, archivo, indent=4, ensure_ascii=False)

    def listar_ids(self) -> list:
        """
            Carga una lista con solamente los 
            ID de las lecturas ingresadas
        """
        lista_lecturas:list = self.leer_json_lecturas()
        lista_ids:list = []

        for lectura in lista_lecturas:
            lista_ids.append(lectura["ID Lectura"])
        
        return lista_ids