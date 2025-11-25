from .Parcela import Parcela
from .Sensor import Sensor
from datetime import datetime
import locale

class Lectura():

    def __init__(
            self, modificacion:bool, 
            id_lectura:str = None, id_sensor:str = None, 
            id_parcela:str = None, fecha_hora:datetime = None, 
            valor:str = None
    ):
        self.__parcela = Parcela(True)
        self.__sensor = Sensor(True)
        # Esto para dar formato de 12 horas a la hora
        try:
            locale.setlocale(locale.LC_TIME, 'es')
        except locale.Error:
            pass
        
        if modificacion:
            # Evita validaciones
            pass
        else:
            self.ID_Lectura = id_lectura
            self.ID_Sensor = id_sensor
            self.ID_Parcela = id_parcela
            self.Fecha_Hora = fecha_hora
            self.Valor_Detectado = valor
    
    # Getters
    @property
    def ID_Lectura(self) -> str:
        return self.__id_lectura
    @property
    def ID_Sensor(self) -> str:
        return self.__id_sensor
    @property
    def ID_Parcela(self) -> str:
        return self.__id_parcela
    @property
    def Fecha_Hora(self) -> str:
        return self.__fecha_hora
    @property
    def Valor_Detectado(self) -> float:
        return self.__valor_detectado
    
    # Setters
    @ID_Lectura.setter
    def ID_Lectura(self, id_lectura):

        # Formateo del texto para trabajar con el de forma estándar
        id_lectura = id_lectura.upper().strip()

        if not id_lectura:
            raise Exception("\n>>> El espacio 'ID de la Lectura (LEC-000)' no debe estar vacío.")
        
        if not "-" in id_lectura:
            raise Exception ("\n>>> El ID de la Lectura debe tener el formato 'LEC-000' (falta el guión).")
        codigo_separado:list = id_lectura.split("-")
        
        if len(codigo_separado) != 2:
            raise Exception("\n>>> El ID de la Lectura debe tener exactamente una parte alfabetica y una parte númerica, separadas por un guión. \n>>> Ejemplo: LEC-000")

        # separación del código
        prefijo, numero = codigo_separado
        
        # Validación del Prefijo
        if prefijo != "LEC":
            raise Exception("\n>>> El prefijo del ID de la Lectura debe ser 'LEC'.")
        
        # Validación del número
        if not numero.isdigit() or len(numero) != 3:
            raise Exception("\n>>> La parte númerica del ID de la Lectura debe contener 3 dígitos. \n>>> Ejemplo: LEC-000")
            
        # Asignación
        self.__id_lectura:str = id_lectura
    
    @ID_Sensor.setter
    def ID_Sensor(self, id_sensor:str):

        self.__sensor.ID_Sensor = id_sensor

        self.__id_sensor = self.__sensor.ID_Sensor

    @ID_Parcela.setter
    def ID_Parcela(self, id_parcela:str):

        self.__parcela.ID_Parcela = id_parcela

        self.__id_parcela = self.__parcela.ID_Parcela

    @Fecha_Hora.setter
    def Fecha_Hora(self, fecha_hora:datetime):
        
        if type(fecha_hora) != str:
            if not fecha_hora:
                raise Exception("\n>>> El espacio Fecha y Hora no debe estar vacío.")

            hora:int = fecha_hora.hour

            if hora >= 0 and hora < 12:
                am_pm:str = "AM"
            else:
                am_pm:str = "PM"

            # Esto le da formato a la hora
            fecha_hora_con_formato:str = fecha_hora.strftime(f"%d de %B de %Y a las %I:%M:%S {am_pm}")
        
            self.__fecha_hora = fecha_hora_con_formato
        
        else:
            self.__fecha_hora = fecha_hora

    @Valor_Detectado.setter
    def Valor_Detectado(self, valor_detectado:str):

        if not valor_detectado:
            raise Exception("\n>>> El espacio de 'Valor Detectado' no debe estar vacío.")
        
        try:
            valor:float = float(valor_detectado)
        except Exception:
            raise Exception("\n>>> Valor Detectado no válido. \n>>> Debe ingresar un número.")
        
        self.__valor_detectado:float = valor

    def __str__(self):
        
        return f"\n>>> ID Lectura: {self.__id_lectura}\n" \
                f">>> ID Sensor: {self.__id_sensor}\n" \
                f">>> ID Parcela: {self.__id_parcela}\n" \
                f">>> Fecha y Hora: {self.__fecha_hora}\n" \
                f">>> Valor Detectado: {self.__valor_detectado}"