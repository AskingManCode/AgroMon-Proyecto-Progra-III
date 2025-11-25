from .Lectura_de_json import leer_archivoX
from pathlib import Path
import json

class Parcela_json():

    def __init__(self):
        self.__ruta:Path = Path("Archivos/Parcelas.json")
        # Creo que es mejor tener una carpeta de solo Archvos Json
        self.__ruta.parent.mkdir(exist_ok=True) # Crea la carpeta si no existe

        # Lo que aprendí: 
        # ruta.parent es "Archivos"
        # mkdir crea esta carpeta si no existe, crea la carpeta de ruta.parent
        # exist_ok=True evita que el programa lance una excepción si la carpeta ya existe

    def escribir_json_parcelas(self, datos_parcela:dict):
        
        lista_parcelas:list = leer_archivoX(self.__ruta)

        lista_parcelas.append(datos_parcela)

        with open(self.__ruta, "w", encoding="utf-8") as archivo:
            json.dump(lista_parcelas, archivo, indent=4, ensure_ascii=False) # identación para que se vea bien

    def leer_json_parcela(self) -> list:

        lista_parcelas:list = leer_archivoX(self.__ruta)
        
        return lista_parcelas
    
    def modificar_datos_parcela(self, parcela_modificada:dict):
        
        lista_parcelas:list = leer_archivoX(self.__ruta)
        nueva_lista:list = []

        for parcela in lista_parcelas:
            if parcela_modificada["ID Parcela"] == parcela["ID Parcela"]:
                nueva_lista.append(parcela_modificada)
            else:
                nueva_lista.append(parcela)
            
        with open(self.__ruta, "w", encoding="utf-8") as archivo:
            json.dump(nueva_lista, archivo, indent=4, ensure_ascii=False)

    def elimiar_parcela_json(self, id_parcela:str):
        
        lista_parcelas:list = leer_archivoX(self.__ruta)
        nueva_lista:list = []

        for parcela in lista_parcelas:
            if parcela["ID Parcela"] != id_parcela:
                nueva_lista.append(parcela)
        
        with open(self.__ruta, "w", encoding="utf-8") as archivo:
            json.dump(nueva_lista, archivo, indent=4, ensure_ascii=False)
    
    def listar_ids(self) -> list:
        """
            Carga una lista con solamente los ID
            de las Parcelas registradas
        """
        lista_parcelas:list = self.leer_json_parcela()

        lista_ids:list = []
        for parcela in lista_parcelas:
            lista_ids.append(parcela["ID Parcela"])

        return lista_ids
    
    def obtener_parcela_por_id(self, id_parcela:str) -> dict:
        """
            Carga unicamente una parcela
            que se ha buscado por su id
        """
        lista_parcelas:list = self.leer_json_parcela()
        diccionario:dict = {}
        
        for parcela in lista_parcelas:
            if parcela["ID Parcela"] == id_parcela:
                diccionario = parcela
                break

        return diccionario


    

