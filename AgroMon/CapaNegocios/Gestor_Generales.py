from CapaDatos.Generales_json import Generales_json
from .Generales import Generales

class Gestor_Generales():

    def __init__(self):
        self.__generales_archivo = Generales_json()

    def guardar_datos(self, generales:object):
        """
            Recibe el objeto Generales y prepara
            los datos para escribir en el archivo
        """
        # Validación de duplicados
        self.__buscar_id_generales(generales.ID_Parcela, False)

        # Datos Generales de la Parcela
        generales_dict:dict ={
            "ID Parcela": generales.ID_Parcela,
            "Zona Radicular": generales.Zona_Radicular,
            "Eficiencia Sistema": generales.Eficiencia_Sistema_Riego,
            "Umbral Humedad Hoja": {
                "Humedad Minima": generales.Humedad_Minima,
                "Humedad Maxima": generales.Humedad_Maxima
            },
            "Volumen Riego Deseado": generales.Volumen_Riego_Deseado
        }
        lista_generales:list = self.__generales_archivo.leer_json_generales()
        lista_generales.append(generales_dict)
        self.__generales_archivo.escribir_json_generales(lista_generales)

    def listar_datos_generales(self) -> list:
        """ 
            Carga una lista con todas
            los datos generales de parcelas 
            registradas
        """
        lista_datos_generales:list = []
        lista_diccionarios_generales:list = self.__generales_archivo.leer_json_generales()

        for datos in lista_diccionarios_generales:
            generales = Generales(
                False,
                datos["ID Parcela"],
                str(datos["Zona Radicular"]),
                str(datos["Eficiencia Sistema"]),
                str(datos["Umbral Humedad Hoja"]["Humedad Minima"]),
                str(datos["Umbral Humedad Hoja"]["Humedad Maxima"]),
                str(datos["Volumen Riego Deseado"])
            )
            lista_datos_generales.append(generales)

        return lista_datos_generales

    def borrar_datos_generales(self, id_parcela):
        """
            Borra los datos generales de una única 
            parcela y sus datos relacionados
        """
        self.__generales_archivo.eliminar_generales_json(id_parcela)

    def buscar_datos_generales(self, id_parcela:str):

        datos_gen = Generales(True)
        datos_gen.ID_Parcela = id_parcela
        self.__buscar_id_generales(datos_gen.ID_Parcela, True)

        datos_buscados:dict = self.__generales_archivo.obtener_datos_por_id(datos_gen.ID_Parcela)

        return datos_buscados
    
    def modificar_generales(self, datos_generales:object):
        
        generales_dict:dict ={
            "ID Parcela": datos_generales.ID_Parcela,
            "Zona Radicular": datos_generales.Zona_Radicular,
            "Eficiencia Sistema": datos_generales.Eficiencia_Sistema_Riego,
            "Umbral Humedad Hoja": {
                "Humedad Minima": datos_generales.Humedad_Minima,
                "Humedad Maxima": datos_generales.Humedad_Maxima
            },
            "Volumen Riego Deseado": datos_generales.Volumen_Riego_Deseado
        }

        self.__generales_archivo.modificar_datos_generales(generales_dict)

    def __buscar_id_generales(self, id_parcela:str, modo_modificacion:bool):
        """
            Valida que no exista un ID de Parcela
            igual en el archivo Json de Generales
        """
        lista_ids:list = self.__generales_archivo.listar_ids()

        if modo_modificacion:
            if id_parcela.upper() not in lista_ids: 
                # El modo modificación hace validación de que si no existe tira excepción
                raise Exception("\n>>> El ID de la Parcela no coincide con los registros actuales.")
        else:
            if id_parcela.upper() in lista_ids:
                # Porque ya existe y estamos ingresando datos de cero
                raise Exception("\n>>> El ID de la Parcela ingresado no es válido.") 