from CapaDatos.Sensor_json import Sensor_json
from .Gestor_Parcelas import Gestor_Parcelas
from .Sensor import Sensor
from .Parcela import Parcela

class Gestor_Sensores():
    
    def __init__(self):
        self.__sensor_archivo = Sensor_json()
        self.__gestor_parcelas = Gestor_Parcelas()

    def guardar_datos(self, sensor:object):
        """
            Recibe el objeto Parcela y prepara
            los datos para escribir en el archivo
        """
        # Validación de duplicados
        self.buscar_id_sensor(sensor.ID_Sensor, False)
        self.__gestor_parcelas.buscar_id_parcela(sensor.ID_Parcela, True)

        sensor_dict:dict = {
            "ID Sensor": sensor.ID_Sensor,
            "Tipo Sensor": sensor.Tipo_Sensor,
            "Unidad de Medida": sensor.Ud_Medida,
            "Estado Sensor": sensor.Estado_Sensor,
            "ID Parcela": sensor.ID_Parcela,
            "Ubicacion en Parcela": {
                "Coordenada X": sensor.Ubicacion_X,
                "Coordenada Y": sensor.Ubicacion_Y
            },
            "Rangos Validos": {
                "Minimo": sensor.Rango_Minimo,
                "Maximo": sensor.Rango_Maximo
            }
        }

        lista_sensores:list = self.__sensor_archivo.leer_json_sensores()
        lista_sensores.append(sensor_dict)
        self.__sensor_archivo.escribir_json_Sensor(lista_sensores)

    def modificar_sensor(self, sensor_modificado:object):
        
        self.__gestor_parcelas.buscar_id_parcela(sensor_modificado.ID_Parcela, True)
        lista_sensores:list = self.__sensor_archivo.leer_json_sensores()
        nueva_lista:list = []

        sensor_dict:dict = {
            "ID Sensor": sensor_modificado.ID_Sensor,
            "Tipo Sensor": sensor_modificado.Tipo_Sensor,
            "Unidad de Medida": sensor_modificado.Ud_Medida,
            "Estado Sensor": sensor_modificado.Estado_Sensor,
            "ID Parcela": sensor_modificado.ID_Parcela,
            "Ubicacion en Parcela": {
                "Coordenada X": sensor_modificado.Ubicacion_X,
                "Coordenada Y": sensor_modificado.Ubicacion_Y
            },
            "Rangos Validos": {
                "Minimo": sensor_modificado.Rango_Minimo,
                "Maximo": sensor_modificado.Rango_Maximo
            }
        }

        for sensor in lista_sensores:
            if sensor_dict["ID Sensor"] == sensor["ID Sensor"]:
                nueva_lista.append(sensor_dict)
            else:
                nueva_lista.append(sensor)

        self.__sensor_archivo.escribir_json_Sensor(nueva_lista)

    def borrar_sensores_parcela(self, id_parcela):
        """
            Borra todos los sensores que se 
            encuentren ubicados en una parcela,
        """
        lista_sensores:list = self.__sensor_archivo.leer_json_sensores()
        nueva_lista:list = []

        for sensor in lista_sensores:
            if sensor["ID Parcela"] != id_parcela:
                nueva_lista.append(sensor)

        self.__sensor_archivo.escribir_json_Sensor(nueva_lista)

    def borrar_un_sensor(self, id_sensor):
        """
            Elimina solamente un sensor
            según el id del parámetro
        """
        lista_sensores:list = self.__sensor_archivo.leer_json_sensores()
        nueva_lista:list = []

        for sensor in lista_sensores:
            if sensor["ID Sensor"] != id_sensor:
                nueva_lista.append(sensor)

        self.__sensor_archivo.escribir_json_Sensor(nueva_lista)

    def listar_sensores(self) -> list:
        """ 
            Carga una lista con todas
            los sensores registrados
        """
        lista_diccionarios_sensores:list = self.__sensor_archivo.leer_json_sensores()
        lista_parcelas:list = []

        for diccionario in lista_diccionarios_sensores:
            # Todo se carga en una lista de Sensores
            # para mayor facilidad en el print
            sensor = Sensor(
                False,
                diccionario["ID Sensor"],
                diccionario["Tipo Sensor"],
                diccionario["Unidad de Medida"],
                diccionario["Estado Sensor"],
                diccionario["ID Parcela"],
                str(diccionario["Ubicacion en Parcela"]["Coordenada X"]),
                str(diccionario["Ubicacion en Parcela"]["Coordenada Y"]),
                str(diccionario["Rangos Validos"]["Minimo"]),
                str(diccionario["Rangos Validos"]["Maximo"])
            )
            lista_parcelas.append(sensor)

        return lista_parcelas
    
    def lista_por_parcela(self, id_parcela) -> list:
        """
            Busca los sensores de una parcela
            especifica y devuelve una lista de
            sensores
        """
        parcela = Parcela(True)
        parcela.ID_Parcela = id_parcela # Validaciones
        self.__gestor_parcelas.buscar_id_parcela(parcela.ID_Parcela, True)
        
        lista_diccionarios_sensores:list = self.__sensor_archivo.leer_json_sensores()
        lista_por_parcelas:list = []

        for diccionario in lista_diccionarios_sensores:
            if diccionario["ID Parcela"] == parcela.ID_Parcela:
                sensor = Sensor(
                    False,
                    diccionario["ID Sensor"],
                    diccionario["Tipo Sensor"],
                    diccionario["Unidad de Medida"],
                    diccionario["Estado Sensor"],
                    diccionario["ID Parcela"],
                    str(diccionario["Ubicacion en Parcela"]["Coordenada X"]),
                    str(diccionario["Ubicacion en Parcela"]["Coordenada Y"]),
                    str(diccionario["Rangos Validos"]["Minimo"]),
                    str(diccionario["Rangos Validos"]["Maximo"])
                )
                lista_por_parcelas.append(sensor)

        return lista_por_parcelas
    
    def buscar_sensor(self, id_sensor:str) -> dict:
        """
            Busca solamente un sensor 
            según el id del sensor
            ingresado como parametro.
        """
        sensor = Sensor(True)
        sensor.ID_Sensor = id_sensor
        self.buscar_id_sensor(sensor.ID_Sensor, True)

        lista_sensores:list = self.__sensor_archivo.leer_json_sensores()
        sensor_buscado:dict = {}
        
        for diccionario in lista_sensores:
            if diccionario["ID Sensor"] == sensor.ID_Sensor:
                sensor_buscado = diccionario
                break
        return sensor_buscado

    def buscar_id_sensor(self, id_sensor:str, modo_modificacion:bool):
        """
            Busca si existe un id igual registrado
        """
        lista_ids:list = self.__sensor_archivo.listar_ids()

        #lista_sensores:list = self.__sensor_archivo.leer_json_sensores()
        #lista_ids:list = []

        #for sensor in lista_sensores:
        #    lista_ids.append(sensor["ID Sensor"])

        if modo_modificacion:
            if id_sensor.upper() not in lista_ids: 
                # El modo modificación hace validación de que si no existe tira excepción
                raise Exception("\n>>> El ID del Sensor no coincide con los registros actuales.")
        else:
            if id_sensor.upper() in lista_ids:
                # Porque ya existe y estamos ingresando datos de cero
                raise Exception("\n>>> El ID del Sensor ingresado no es válido.")
            
    def validad_parcela_de_sensor(self, id_sensor:str, id_parcela:str):

        lista_sensores:list = self.__sensor_archivo.leer_json_sensores()

        for sensor in lista_sensores:
            if sensor["ID Sensor"] == id_sensor and sensor["ID Parcela"] != id_parcela:
                raise Exception("\n>>> EL ID de la Parcela ingresado no está relacionado al ID del Sensor ingresado.")