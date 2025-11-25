import xml.etree.ElementTree as ET
from pathlib import Path

class Archivo_xml():

    def obtener_datos_xml(self, ruta:str) -> list:

        ruta:Path = Path(ruta)

        if not ruta.exists() or ruta.stat().st_size == 0:
            raise Exception("\n>>> El Archivo elegido no cumple con los requerimientos \n>>> mínimos para ser ingresado al sistema.")
        
        arbol = ET.parse(ruta)
        raiz = arbol.getroot()

        lista_lecturas_xml:list = []
        for lectura in raiz.findall("Lectura"):
            diccionario:dict = {
                "ID Lectura": lectura.find("ID_Lectura").text,
                "ID Sensor": lectura.find("ID_Sensor").text,
                "ID Parcela": lectura.find("ID_Parcela").text,
                "Fecha y Hora": lectura.find("Fecha_y_Hora").text,
                "Valor Detectado": lectura.find("Valor_Detectado").text
            }
            lista_lecturas_xml.append(diccionario)
        
        return lista_lecturas_xml