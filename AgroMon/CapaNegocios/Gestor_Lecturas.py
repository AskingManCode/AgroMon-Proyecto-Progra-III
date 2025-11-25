from CapaDatos.Lecturas_json import Lecturas_json
from CapaDatos.Archivo_xml import Archivo_xml
from .Gestor_Sensores import Gestor_Sensores
from .Gestor_Parcelas import Gestor_Parcelas
from .Gestor_Generales import Gestor_Generales
from .Gestor_Sensores import Gestor_Sensores
from CapaDatos.Alertas_json import Alertas_json
from .Sensor import Sensor
from .Lectura import Lectura

class Gestor_Lecturas():

    def __init__(self):
        self.__lectura_archivo = Lecturas_json()
        self.__gestor_sensores = Gestor_Sensores()
        self.__gestor_parcelas = Gestor_Parcelas()
        self.__gestor_generales = Gestor_Generales()
        self.__gestor_sensores = Gestor_Sensores()
        self.__alertas_archivo = Alertas_json()

    def guardar_lectura(self, lectura:object):
        
        self.buscar_id_lectura(lectura.ID_Lectura, False)
        self.__gestor_sensores.buscar_id_sensor(lectura.ID_Sensor, True)
        self.__gestor_sensores.validad_parcela_de_sensor(lectura.ID_Sensor, lectura.ID_Parcela)
        
        lectura_dict:dict = {
            "ID Lectura": lectura.ID_Lectura,
            "ID Sensor": lectura.ID_Sensor,
            "ID Parcela": lectura.ID_Parcela,
            "Fecha y Hora": lectura.Fecha_Hora,
            "Valor Detectado": lectura.Valor_Detectado
        }
        
        lista_lecturas:list = self.__lectura_archivo.leer_json_lecturas()
        lista_lecturas.append(lectura_dict)
        self.__lectura_archivo.escribir_json_lecturas(lista_lecturas)

    def guardar_datos_xml(self, ruta_xml:str):
        
        if not ruta_xml:
            raise Exception("\n>>> No ha seleccionado ningún archivo xml.")

        xml_archivo = Archivo_xml()
        lista_lecturas_xml:list = xml_archivo.obtener_datos_xml(ruta_xml)
        
        lista_lecturas:list = self.__lectura_archivo.leer_json_lecturas()
        for diccionario in lista_lecturas_xml:
            lectura = Lectura(True)
            lectura.ID_Lectura = diccionario["ID Lectura"]
            lectura.ID_Sensor = diccionario["ID Sensor"]
            lectura.ID_Parcela = diccionario["ID Parcela"]
            lectura.Fecha_Hora = diccionario["Fecha y Hora"]
            lectura.Valor_Detectado = str(diccionario["Valor Detectado"])

            self.buscar_id_lectura(lectura.ID_Lectura, False)
            self.__gestor_sensores.buscar_id_sensor(lectura.ID_Sensor, True)
            self.__gestor_sensores.validad_parcela_de_sensor(lectura.ID_Sensor, lectura.ID_Parcela)
            lista_lecturas.append(diccionario)
            
        self.__lectura_archivo.escribir_json_lecturas(lista_lecturas)

    def borrar_todas_lecturas(self, id_parcela:str):

        lista_lecturas:list = self.__lectura_archivo.leer_json_lecturas()
        nueva_lista:list = []

        for lectura in lista_lecturas:
            if lectura["ID Parcela"] != id_parcela:
                nueva_lista.append(lectura)

        self.__lectura_archivo.escribir_json_lecturas(nueva_lista)

    def borrar_lecturas_sensor(self, id_sensor:str):

        lista_lecturas:list = self.__lectura_archivo.leer_json_lecturas()
        nueva_lista:list = []

        for lectura in lista_lecturas:
            if lectura["ID Sensor"] != id_sensor:
                nueva_lista.append(lectura)

        self.__lectura_archivo.escribir_json_lecturas(nueva_lista)

    def borrar_informacion_sensor(self, id_parcela:str, id_sensor:str, fecha:str):

        # Validaciones
        sensor_validador = Sensor(True)
        sensor_validador.ID_Parcela = id_parcela 
        self.__gestor_parcelas.buscar_id_parcela(sensor_validador.ID_Parcela, True)
        fecha = fecha.strip().lower()
        sensor_validador.ID_Sensor = id_sensor 
        self.__gestor_sensores.buscar_id_sensor(sensor_validador.ID_Sensor, True)
        self.__gestor_sensores.validad_parcela_de_sensor(sensor_validador.ID_Sensor, sensor_validador.ID_Parcela)
        if not fecha:
            raise Exception("\n>>> El espacio 'Fecha' no debe estar vacío.")
        
        lista_lecturas:list = self.__lectura_archivo.leer_json_lecturas()
        nueva_lista:list = []

        for diccionario in lista_lecturas:

            if (diccionario["ID Sensor"] == sensor_validador.ID_Sensor or
                diccionario["ID Parcela"] == sensor_validador.ID_Parcela):
                if fecha in diccionario["Fecha y Hora"]: 
                    continue
            
            nueva_lista.append(diccionario)
            
        self.__lectura_archivo.escribir_json_lecturas(nueva_lista)
    
    def buscar_informacion_sensor_parcela(self, id_parcela:str, id_sensor:str, fecha:str) -> list:
        
        # Validaciones
        sensor_validador = Sensor(True)
        sensor_validador.ID_Parcela = id_parcela 
        self.__gestor_parcelas.buscar_id_parcela(sensor_validador.ID_Parcela, True)
        fecha = fecha.strip().lower()
        sensor_validador.ID_Sensor = id_sensor 
        self.__gestor_sensores.buscar_id_sensor(sensor_validador.ID_Sensor, True)
        self.__gestor_sensores.validad_parcela_de_sensor(sensor_validador.ID_Sensor, sensor_validador.ID_Parcela)
        if not fecha:
            raise Exception("\n>>> El espacio 'Fecha' no debe estar vacío.")
        
        lista_lecturas:list = self.__lectura_archivo.leer_json_lecturas()
        nueva_lista:list = []

        for lectura_dict in lista_lecturas:
            
            if (lectura_dict["ID Sensor"] != sensor_validador.ID_Sensor or
                lectura_dict["ID Parcela"] != sensor_validador.ID_Parcela):
                continue

            if fecha not in lectura_dict["Fecha y Hora"]: 
                continue
            
            lectura = Lectura(
                False,
                lectura_dict["ID Lectura"],
                lectura_dict["ID Sensor"],
                lectura_dict["ID Parcela"],
                lectura_dict["Fecha y Hora"],
                str(lectura_dict["Valor Detectado"])
            )
            nueva_lista.append(lectura)
            
        if nueva_lista:
            return nueva_lista
        else:
            raise Exception("\n>>> No se han encontrado concidencias.")

    def listar_lecturas(self) -> list:

        lista_diccionarios_lecturas:list = self.__lectura_archivo.leer_json_lecturas()
        lista_lecturas:list = []

        for diccionario in lista_diccionarios_lecturas:
            lectura = Lectura(
                False,
                diccionario["ID Lectura"],
                diccionario["ID Sensor"],
                diccionario["ID Parcela"],
                diccionario["Fecha y Hora"],
                str(diccionario["Valor Detectado"])
            )
            lista_lecturas.append(lectura)

        return lista_lecturas

    def listar_por_sensor_fecha(self, id_parcela: str, id_sensor:str, fecha:str) -> object:
        
        # Validaciones
        fecha = fecha.strip().lower()
        sensor_validador = Sensor(True)
        sensor_validador.ID_Parcela = id_parcela 
        self.__gestor_parcelas.buscar_id_parcela(sensor_validador.ID_Parcela, True)
        sensor_validador.ID_Sensor = id_sensor 
        self.__gestor_sensores.buscar_id_sensor(sensor_validador.ID_Sensor, True)
        self.__gestor_sensores.validad_parcela_de_sensor(sensor_validador.ID_Sensor, sensor_validador.ID_Parcela)
    
        lista_lecturas:list = self.__lectura_archivo.leer_json_lecturas()

        for lectura_dict in lista_lecturas:
            
            if (lectura_dict["ID Sensor"] != sensor_validador.ID_Sensor or
                lectura_dict["ID Parcela"] != sensor_validador.ID_Parcela):
                continue

            if fecha:
                # La fecha debe agregarse como en el ejemplo del input
                if fecha not in lectura_dict["Fecha y Hora"]: 
                    continue
            
            lectura = Lectura(
                False,
                lectura_dict["ID Lectura"],
                lectura_dict["ID Sensor"],
                lectura_dict["ID Parcela"],
                lectura_dict["Fecha y Hora"],
                lectura_dict["Valor Detectado"]
            )
            return lectura
        
        raise Exception("\n>>> No se han encontrado concidencias.")
    
    def listar_por_parcela_dia(self, id_parcela:str, fecha:str) -> list:
        
        # Validaciones
        sensor_validador = Sensor(True)
        sensor_validador.ID_Parcela = id_parcela 
        self.__gestor_parcelas.buscar_id_parcela(sensor_validador.ID_Parcela, True)
        fecha = fecha.strip().lower()
        if not fecha:
            raise Exception("\n>>> El espacio 'Fecha' no debe estar vacío.")

        lista_lecturas:list = self.__lectura_archivo.leer_json_lecturas()
        nueva_lista:list = []
        
        for diccionario in lista_lecturas:
            if diccionario["ID Parcela"] == sensor_validador.ID_Parcela and fecha in diccionario["Fecha y Hora"]:
                lectura = Lectura(
                    False,
                    diccionario["ID Lectura"],
                    diccionario["ID Sensor"],
                    diccionario["ID Parcela"],
                    diccionario["Fecha y Hora"],
                    diccionario["Valor Detectado"]
                )
                nueva_lista.append(lectura)

        return nueva_lista

    def buscar_id_lectura(self, id_lectura:str, modo_modificacion:bool):
        
        lista_ids:list = self.__lectura_archivo.listar_ids()

        if modo_modificacion:
            if id_lectura.upper() not in lista_ids:
                raise Exception("\n>>> El ID de la Lectura no coincide con los registros actuales.")
        else:
            if id_lectura.upper() in lista_ids:
                raise Exception("\n>>> El ID de la Lectura ingresado no es válido.")
            
    def calcular_alertas(self, fecha:str):
        
        if not fecha:
            raise Exception("\n>>> El espacio 'Fecha' no debe estar vacío.")
        
        lista_lecturas:list = self.__lectura_archivo.leer_json_lecturas()
        lista_sensores:list = self.__gestor_sensores.listar_sensores()
        lista_generales:list = self.__gestor_generales.listar_datos_generales()
        
        lista_alertas:list = []

        for lectura in lista_lecturas:
            if fecha in lectura["Fecha y Hora"]:
                for sensor in lista_sensores:
                    if sensor.Estado_Sensor == "Activo" and sensor.ID_Sensor == lectura["ID Sensor"]:
                        if sensor.Ud_Medida == "%":
                            if float(lectura["Valor Detectado"]) < float(sensor.Rango_Minimo):
                                alerta:dict = {
                                    "ID Parcela": sensor.ID_Parcela,
                                    "ID Sensor": sensor.ID_Sensor,
                                    "Fecha Alerta": lectura["Fecha y Hora"],
                                    "Tipo Alerta": "Alerta de Riego",
                                    "Valor Detectado": lectura["Valor Detectado"]
                                }
                                lista_alertas.append(alerta)
                            elif float(lectura["Valor Detectado"]) > float(sensor.Rango_Maximo):
                                alerta:dict = {
                                    "ID Parcela": sensor.ID_Parcela,
                                    "ID Sensor": sensor.ID_Sensor,
                                    "Fecha Alerta": lectura["Fecha y Hora"],
                                    "Tipo Alerta": "Alerta de Humedad Excesiva",
                                    "Valor Detectado": lectura["Valor Detectado"]
                                }
                                lista_alertas.append(alerta)
                        elif sensor.Ud_Medida == "m³/m³":
                            for generales in lista_generales:
                                if sensor.ID_Parcela == generales.ID_Parcela :
                                    if float(lectura["Valor Detectado"]) < float(generales.Volumen_Riego_Deseado):
                                        alerta:dict = {
                                            "ID Parcela": sensor.ID_Parcela,
                                            "ID Sensor": sensor.ID_Sensor,
                                            "Fecha Alerta": lectura["Fecha y Hora"],
                                            "Tipo Alerta": "Alerta de Riego por Suelo",
                                            "Valor Detectado": lectura["Valor Detectado"]
                                        }
                                        lista_alertas.append(alerta)
        
        self.__alertas_archivo.escribir_json_alertas(lista_alertas)

        return lista_alertas
                            
    def ver_alertas_parcela(self, id_parcela):

        sensor_validador = Sensor(True)
        sensor_validador.ID_Parcela = id_parcela 
        self.__gestor_parcelas.buscar_id_parcela(sensor_validador.ID_Parcela, True)

        lista_alertas_parcela:list = self.__alertas_archivo.leer_json_alertas()
        lista_nueva:list = []
                
        for alerta in lista_alertas_parcela:
            if sensor_validador.ID_Parcela == alerta["ID Parcela"]:
                lista_nueva.append(alerta)

        return lista_nueva

