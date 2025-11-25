import math

class Sensor():
    # Notas:
    # 2. Validar código de parcelas para saber si existe la ingresada
    # 3. Validar Coordenadas según el área de la parcela

    def __init__(
            self, modificacion:bool, id_sensor:str = None, 
            tipo_sensor:str = None, ud_medida:str = None, 
            estado_sensor:str = None, id_parcela:str = None, 
            ubicacion_X:str = None, ubicacion_Y:str = None, 
            rango_minimo:str = None, rango_maximo:str = None
    ):
        """
            Inicializa un sensor enviando los datos a los setters 
            para su validación. Si algún dato no cumple las 
            condiciones, se lanza una excepción para reiniciar 
            el ingreso de datos.
        """
        if modificacion:
            # Evita validaciones
            pass
        else:
            # Datos Sensor
            self.ID_Sensor = id_sensor
            self.Tipo_Sensor = tipo_sensor
            self.Ud_Medida = ud_medida
            self.Estado_Sensor = estado_sensor
            # Datos en Parcela
            self.ID_Parcela = id_parcela
            self.Ubicacion_X = ubicacion_X
            self.Ubicacion_Y = ubicacion_Y
            self.Rango_Minimo = rango_minimo
            self.Rango_Maximo = rango_maximo


    # -- Getters -- #
    @property
    def ID_Sensor(self) -> str:
        return self.__id_sensor
    @property
    def Tipo_Sensor(self) -> str:
        return self.__tipo_sensor
    @property
    def Ud_Medida(self) -> str:
        return self.__ud_medida
    @property
    def Estado_Sensor(self) -> str:
        return self.__estado_sensor
    @property
    def ID_Parcela(self) -> str:
        return self.__id_parcela
    @property
    def Ubicacion_X(self) -> float:
        return self.__ubicacion_x
    @property
    def Ubicacion_Y(self) -> float:
        return self.__ubicacion_y
    @property
    def Rango_Minimo(self) -> float:
        return self.__rango_minimo
    @property
    def Rango_Maximo(self) -> float:
        return self.__rango_maximo
    
    # -- Setters -- #
    @ID_Sensor.setter
    def ID_Sensor(self, id_sensor:str):
        
        # Formateo del texto para trabajar con el de forma estándar
        id_sensor = id_sensor.upper().strip()

        self.__validar_codigo(id_sensor, "ID del Sensor", "SEN", "SEN-000")
            
        # Asignación
        self.__id_sensor:str = id_sensor

    @Tipo_Sensor.setter
    def Tipo_Sensor(self, tipo_sensor:str):
        
        tipo_sensor = tipo_sensor.strip()

        if not tipo_sensor:
            raise Exception("\n>>> El espacio 'Tipo de Sensor' debe contener datos.")
        
        if tipo_sensor not in["Sensor de Humedad de la Hoja", "Sensor de Humedad del Suelo", "Sensor de Temperatura"]:
            raise Exception("\n>>> El Tipo de Sensor ingresado al sistema no es válido.")

        # Asignación
        self.__tipo_sensor:str = tipo_sensor

    @Ud_Medida.setter
    def Ud_Medida(self, unidad_medida:str):
        
        unidad_medida = unidad_medida.strip()

        if not unidad_medida:
            raise Exception("\n>>> El espacio 'Unidad de Medida' debe contener datos.")
        
        if unidad_medida not in["%","m³/m³","°C"]:
            raise Exception("\n>>> La Unidad de Medida ingresada al sistema no es válida.")
        
        # Asignación
        self.__ud_medida:str = unidad_medida
    
    @Estado_Sensor.setter
    def Estado_Sensor(self, estado_sensor:str):
        
        # Formateo del texto para trabajar con el de forma estándar
        estado_sensor = estado_sensor.title().strip()

        if not estado_sensor:
            raise Exception("\n>>> El espacio 'Estado del Sensor' debe contener datos.")
        
        if estado_sensor not in["Activo", "Inactivo", "Requiere Revisión", "En Mantenimiento"]:
            raise Exception("\n>>> El Estado del Sensor ingresado al sistema no es válido.")
        
        # Asignación
        self.__estado_sensor:str = estado_sensor

    @ID_Parcela.setter
    def ID_Parcela(self, id_parcela:str):
        
        # Formateo del texto para trabajar con el de forma estándar
        id_parcela = id_parcela.upper().strip()

        self.__validar_codigo(id_parcela, "ID de la Parcela", "PAR", "PAR-000")
            
        # Asignación
        self.__id_parcela:str = id_parcela

    @Ubicacion_X.setter
    def Ubicacion_X(self, ubicacion_x:str):
        
        ubicacion_x = ubicacion_x.strip()

        if not ubicacion_x:
            raise Exception("\n>>> El espacio 'Punto de Ubicación en Parcela/Coordenada X' no debe estar vacío.")
        
        try:
            valor_x:float = float(ubicacion_x)
        except Exception:
            raise Exception("\n>>> La Coordenada X es inválida. \n>>> Debe ingresar un número válido.")
        
        # validar según el área de la parcela buscada
        #limite_maximo:float = math.sqrt(51816598)
        #if ubicacion_x > limite_maximo:
            #raise Exception("\n>>> ")

        # Asignación
        self.__ubicacion_x:float = valor_x

    @Ubicacion_Y.setter
    def Ubicacion_Y(self, ubicacion_y:str):
        
        ubicacion_y = ubicacion_y.strip()

        if not ubicacion_y:
            raise Exception("\n>>> El espacio 'Punto de Ubicación en Parcela/Coordenada Y' no debe estar vacío.")
        
        try:
            valor_y:float = float(ubicacion_y)
        except Exception:
            raise Exception("\n>>> La Coordenada Y es inválida. \n>>> Debe ingresar un número válido.")
        
        # validar según el área de la parcela
        #limite_maximo:float = math.sqrt(51816598)
        #if ubicacion_y > limite_maximo:
        #    raise Exception("\n>>> ")

        # Asignación
        self.__ubicacion_y:float = valor_y

    @Rango_Minimo.setter
    def Rango_Minimo(self, rango_minimo:str):
        
        rango_minimo = rango_minimo.strip()

        try:
            minimo:float = float(rango_minimo)
        except Exception:
            raise Exception("\n>>> El rango mínimo no es válido. \n>>> Debe ingresar un número válido.")

        self.__validar_rangos(minimo)

        if hasattr(self, "_Sensor__rango_maximo"):
            if minimo >= self.__rango_maximo:
                raise Exception("\n>>> El rango mínimo no debe ser mayor o igual que el rango máximo establecida.")

        # Asignación
        self.__rango_minimo:float = minimo

    @Rango_Maximo.setter
    def Rango_Maximo(self, rango_maximo):
        
        rango_maximo = rango_maximo.strip()

        try:
            maximo:float = float(rango_maximo)
        except Exception:
            raise Exception("\n>>> El rango máximo no es válido. \n>>> Debe ingresar un número válido.")
        
        self.__validar_rangos(maximo)
        
        if hasattr(self, "_Sensor__rango_minimo"):
            if maximo <= self.__rango_minimo:
                raise Exception("\n>>> El rango máximo no debe ser mayor o igual que el rango máximo establecida.")

        # Asignación
        self.__rango_maximo:float = maximo

    # -- Fromato de texto -- #
    def __str__(self) -> str:
        return f"\n>>> ID Sensor: {self.__id_sensor}\n" \
                f">>> Tipo de Sensor: {self.__tipo_sensor}\n" \
                f">>> Unidad de Medida: {self.__ud_medida}\n" \
                f">>> Estado: {self.__estado_sensor}\n" \
                f">>> Punto de Ubicación en Parcela:\n" \
                f" >>> ID Parcela: {self.__id_parcela}\n" \
                f" >>> Coordenada X: {self.__ubicacion_x}\n" \
                f" >>> Coordenada Y: {self.__ubicacion_y}\n" \
                f">>> Rangos Válidos:\n" \
                f" >>> Mínimo: {self.__rango_minimo}{self.__ud_medida}\n" \
                f" >>> Máximo: {self.__rango_maximo}{self.__ud_medida}"

    # -- Métodos y Funciones -- #
    def __validar_codigo(self, id, nombre:str, prefijo_cod:str, codigo:str):
        
        if not id:
            raise Exception(f"\n>>> El espacio '{nombre} ({codigo})' no debe estar vacío.")
        
        if not "-" in id:
            raise Exception (f"\n>>> El {nombre} debe tener el formato '{codigo}' (falta el guión).")
        codigo_separado:list = id.split("-")
        
        if len(codigo_separado) != 2:
            raise Exception(f"\n>>> El {nombre} debe tener exactamente una parte alfabetica y una parte númerica, separadas por un guión. \n>>> Ejemplo: {codigo}")

        # separación del código
        prefijo, numero = codigo_separado
        
        # Validación del Prefijo
        if prefijo != prefijo_cod:
            raise Exception(f"\n>>> El prefijo del {nombre} debe ser '{prefijo_cod}'.")
        
        # Validación del número
        if not numero.isdigit() or len(numero) != 3:
            raise Exception(f"\n>>> La parte númerica del {nombre} debe contener 3 dígitos. \n>>> Ejemplo: {codigo}")
    
    def __validar_rangos(self, valor:float):
        """ 
            Se encarga de validar que el valor ingresado
            cumpla con los rangos según el tipo de unidad
            de medida que se ha ingresado al sistema
        """
        
        if hasattr(self, "_Sensor__ud_medida"): # para saber si existe la unidad de medida preestablecida
            match self.__ud_medida: 

                # No se especificaron los rangos de medidas por lo que tomé medidas de instrumentos reales

                case "%": # Sensor Humedad de la Hoja
                    if valor < 0 or valor > 15: # Escala del Pythos 31
                        raise Exception("\n>>> El rango máximo debe estar entre 0% y 15%.")

                case "m³/m³": # Sensor de Humedad del Suelo
                    if valor < 0.0 or valor > 0.6: # Escala del Decagon EC-5 
                        raise Exception("\n>>> El rango máximo debe estar entre 0.00m³/m³ y 0.60m³/m³.")
                
                case "°C": # Sensor de Temperatura
                    if valor < -10 or valor > 60: # Rangos del PT100
                        raise Exception("\n>>> El rango máximo debe estar entre -10°C y 60°C") 
                
                case _: 
                    raise Exception("\n>>> La Unidad de Medida ingresada al sistema no es válida.")
        else:
            raise Exception("\n>>> El sistema no ha reconocido la unidad de medida para realizar los cálculos de rango.")
        
if __name__ == "__main__":
    # Sensor de Humedad de la Hoja
    sensor_hoja = Sensor(
        False,
        id_sensor="SEN-000",
        tipo_sensor="Sensor de Humedad de la Hoja",
        ud_medida="%",
        estado_sensor="Activo",
        id_parcela="PAR-001",
        ubicacion_X="12.5",       # coordenadas dentro del área válida
        ubicacion_Y="8.3",
        rango_minimo="3.5",       # dentro del 0–15%
        rango_maximo="12.0"
    )

    # Sensor de Humedad del Suelo
    sensor_suelo = Sensor(
        False,
        id_sensor="SEN-002",
        tipo_sensor="Sensor de Humedad del Suelo",
        ud_medida="m³/m³",
        estado_sensor="En Mantenimiento",
        id_parcela="PAR-002",
        ubicacion_X="5.8",
        ubicacion_Y="4.1",
        rango_minimo="0.10",      # dentro del 0.00–0.60
        rango_maximo="0.45"
    )

    # Sensor de Temperatura
    sensor_temp = Sensor(
        False,
        id_sensor="SEN-003",
        tipo_sensor="Sensor de Temperatura",
        ud_medida="°C",
        estado_sensor="Requiere Revisión",
        id_parcela="PAR-003",
        ubicacion_X="9.6",
        ubicacion_Y="10.2",
        rango_minimo="5",         # dentro del -10–60°C
        rango_maximo="45"
    )

    # Mostrar datos
    print(sensor_hoja)
    print(sensor_suelo)
    print(sensor_temp)