from CapaDatos.Parcela_json import Parcela_json
from .Parcela import Parcela

class Gestor_Parcelas():
    
    def __init__(self):
        self.__parcela_archivo = Parcela_json()

    def guardar_datos(self, parcela:object):
        """
            Recibe el objeto Parcela y prepara
            los datos para escribir en el archivo
        """
        # Validación de duplicados
        self.buscar_id_parcela(parcela.ID_Parcela, False)

        # Datos Iniciales de la Parcela
        parcela_dict:dict = {
            "ID Parcela": parcela.ID_Parcela,
            "Nombre": parcela.Nombre,
            "Ubicacion Geografica": {
                "Latitud": parcela.Ubicacion_Latitud,
                "Longitud": parcela.Ubicacion_Longitud
            },
            "Tipo Cultivo": parcela.Tipo_Cultivo,
            "Area": parcela.Area
        }

        self.__parcela_archivo.escribir_json_parcelas(parcela_dict)
    
    def listar_parcelas(self) -> list:
        """ 
            Carga una lista con todas
            las parcelas registradas
        """
        lista_parcelas = []
        lista_diccionarios_parcela:list = self.__parcela_archivo.leer_json_parcela()
        
        for diccionario in lista_diccionarios_parcela:
            parcela = Parcela(
                False,
                diccionario['ID Parcela'],
                diccionario['Nombre'],
                str(diccionario['Ubicacion Geografica']['Latitud']),
                str(diccionario['Ubicacion Geografica']['Longitud']),
                diccionario['Tipo Cultivo'],
                str(diccionario["Area"])
            )
            lista_parcelas.append(parcela)
            
        return lista_parcelas
    
    def buscar_parcela(self, id_parcela:str) -> dict:
        """
            Busca solamente la parcela buscada
            según el id parcela ingresado
        """
        parcela = Parcela(True)
        parcela.ID_Parcela = id_parcela
        self.buscar_id_parcela(parcela.ID_Parcela, True)

        parcela_buscada:dict = self.__parcela_archivo.obtener_parcela_por_id(parcela.ID_Parcela)

        return parcela_buscada

    def modificar_parcela(self, parcela:object):
        """
            Modifica los datos de una parcela
            especificada por medio del id parcela
        """
        
        parcela_dict:dict = {
            "ID Parcela": parcela.ID_Parcela,
            "Nombre": parcela.Nombre,
            "Ubicacion Geografica": {
                "Latitud": parcela.Ubicacion_Latitud,
                "Longitud": parcela.Ubicacion_Longitud
            },
            "Tipo Cultivo": parcela.Tipo_Cultivo,
            "Area": parcela.Area
        }
        
        self.__parcela_archivo.modificar_datos_parcela(parcela_dict)
        
    def borrar_parcela(self, id_parcela:str):
        """
            Borra los datos de una única parcela
            y sus datos relacionados
        """
        self.__parcela_archivo.elimiar_parcela_json(id_parcela)

    def buscar_id_parcela(self, id_parcela:str, modo_modificacion:bool):
        """
            Busca si existe un id igual registrado
        """
        lista_ids:list = self.__parcela_archivo.listar_ids()

        if modo_modificacion:
            if id_parcela.upper() not in lista_ids: 
                # El modo modificación hace validación de que si no existe tira excepción
                raise Exception("\n>>> El ID de la Parcela no coincide con los registros actuales.")
        else:
            if id_parcela.upper() in lista_ids:
                # Porque ya existe y estamos ingresando datos de cero
                raise Exception("\n>>> El ID de la Parcela ingresado no es válido.") 