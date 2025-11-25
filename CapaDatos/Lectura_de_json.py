from pathlib import Path
import json

def leer_archivoX(ruta:Path) -> list:
        """
            Lee un archivo, solo necesita la ruta.\n
            Retorna una lista con el contenido del archivo.
        """
        if ruta.exists() and ruta.stat().st_size > 0:
            with open(ruta, "r", encoding="utf-8") as archivo: # cierra el archivo de una vez
                try: # si el archivo existe cargo la lista
                    lista_diccionarios:list = json.load(archivo)
                except Exception:
                    # si por alguna razón hay error al leer se crea 
                    # una lista nueva para no perder los datos ingresados
                    lista_diccionarios:list = []
        else:
            lista_diccionarios:list = []

        return lista_diccionarios