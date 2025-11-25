from .Lectura_de_json import leer_archivoX
from pathlib import Path
import json

class Generales_json():

    def __init__(self):
        self.__ruta:Path = Path("Archivos/Datos_Generales_Parcela.json")
        self.__ruta.parent.mkdir(exist_ok=True) # Crea la carpeta si no existe

    def escribir_json_generales(self, lista_generales:list):

        with open(self.__ruta, "w", encoding="utf-8") as archivo:
            json.dump(lista_generales, archivo, indent=4) 
    
    def leer_json_generales(self) -> list:

        lista_generales:list = leer_archivoX(self.__ruta)

        return lista_generales 
    
    def modificar_datos_generales(self, generales_modificado:dict):
        
        lista_generales:list = leer_archivoX(self.__ruta)
        nueva_lista:list = []

        for dato in lista_generales:
            if generales_modificado["ID Parcela"] == dato["ID Parcela"]:
                nueva_lista.append(generales_modificado)
            else:
                nueva_lista.append(dato)

        with open(self.__ruta, "w", encoding="utf-8") as archivo:
            json.dump(nueva_lista, archivo, indent=4, ensure_ascii=False)
    
    def eliminar_generales_json(self, id_parcela:str):

        lista_generales:list = leer_archivoX(self.__ruta)
        nueva_lista:list = []

        for dato in lista_generales:
            if dato["ID Parcela"] != id_parcela:
                nueva_lista.append(dato)

        with open(self.__ruta, "w", encoding="utf-8") as archivo:
            json.dump(nueva_lista, archivo, indent=4, ensure_ascii=False)

    def listar_ids(self) -> list:
        """
            Carga una lista con solamente los ID
            de las Parcelas registradas en generales
        """
        lista_generales:list = self.leer_json_generales()

        lista_ids:list = []
        for parcela_general in lista_generales:
            lista_ids.append(parcela_general["ID Parcela"])

        return lista_ids
    
    def obtener_datos_por_id(self, id_parcela):
        """
            Carga unicamente una los datos
            generales que se han buscado por su 
            id de parcela
        """
        lista_generales:list = self.leer_json_generales()

        diccionario:dict = {}
        for parcela in lista_generales:
            if parcela["ID Parcela"] == id_parcela:
                diccionario = parcela
                break

        return diccionario