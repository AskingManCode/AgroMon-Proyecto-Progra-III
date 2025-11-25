class Generales():

    def __init__( 
            self, modificacion:bool, id_parcela:str = None,  
            zona_radicular:str = None, eficiencia_sistema:str = None, 
            humedad_minima:str = None, humedad_maxima:str = None, 
            volumen_riego:str = None
    ):
        """
            Inicializa un generales enviando los datos a los setters 
            para su validación. Si algún dato no cumple las 
            condiciones, se lanza una excepción para reiniciar 
            el ingreso de datos.
        """
        if modificacion:
            # Evita validaciones
            pass
        else:
            # Datos generales de parcela
            self.ID_Parcela = id_parcela
            # Datos Generales de la Parcela
            self.Zona_Radicular = zona_radicular
            self.Eficiencia_Sistema_Riego = eficiencia_sistema
            #
            # Umbral de Humedad de la Hoja Permitido
            self.Humedad_Minima = humedad_minima
            self.Humedad_Maxima = humedad_maxima
            #
            self.Volumen_Riego_Deseado = volumen_riego

    # -- Getters -- #
    @property
    def ID_Parcela(self) -> str:
        return self.__id_parcela
    
    # Datos Generales de la Parcela #
    @property
    def Zona_Radicular(self) -> float:
        return self.__zona_radicular
    @property
    def Eficiencia_Sistema_Riego(self) -> float:
        return self.__eficiencia_sistema_riego
    @property
    def Humedad_Minima(self) -> float:
        return self.__humedad_minima
    @property
    def Humedad_Maxima(self) -> float:
        return self.__humedad_maxima
    @property
    def Volumen_Riego_Deseado(self) -> float:
        return self.__volumen_riego_deseado
    

    # -- Setters -- #
    @ID_Parcela.setter
    def ID_Parcela(self, id_parcela:str):
        
        # Formateo del texto para trabajar con el de forma estándar
        id_parcela = id_parcela.upper().strip()

        if not id_parcela:
            raise Exception("\n>>> El espacio 'ID de la Parcela (PAR-000)' no debe estar vacío.")
        
        if not "-" in id_parcela:
            raise Exception ("\n>>> El ID de la Parcela debe tener el formato 'PAR-000' (falta el guión).")
        codigo_separado:list = id_parcela.split("-")
        
        if len(codigo_separado) != 2:
            raise Exception("\n>>> El ID de la Parcela debe tener exactamente una parte alfabetica y una parte númerica, separadas por un guión. \n>>> Ejemplo: PAR-000")

        # separación del código
        prefijo, numero = codigo_separado
        
        # Validación del Prefijo
        if prefijo != "PAR":
            raise Exception("\n>>> El prefijo del ID de la Parcela debe ser 'PAR'.")
        
        # Validación del número
        if not numero.isdigit() or len(numero) != 3:
            raise Exception("\n>>> La parte númerica del ID de la Parcela debe contener 3 dígitos. \n>>> Ejemplo: PAR-000")
            
        # Asignación
        self.__id_parcela:str = id_parcela

    #-- Datos Generales de la Parcela --#
    @Zona_Radicular.setter
    def Zona_Radicular(self, zona_radicular:str): # 0.00 - 1.00
        
        zona_radicular = zona_radicular.strip()

        if not zona_radicular:
            raise Exception("\n>>> El espacio 'Profundidad Efectiva de la Raíz (Zona Radicular) (m)' no debe estar vacío.")

        try:
            zona:float = float(zona_radicular)
        except Exception:
            raise Exception("\n>>> Profundidad Efectiva de la Raíz no válida. \n>>> Ingrese un número válido.")

        if zona < 0.00 or zona > 1.00:
            raise Exception("\n>>> La Profundidad Efectiva de la Raíz es muy baja o excede el rango válido. \n>>> Rango válido entre 0.00 y 1.00")
        
        # Asignación
        self.__zona_radicular:float = round(zona, 2) # Da formato, solo 2 números decimales

    @Eficiencia_Sistema_Riego.setter
    def Eficiencia_Sistema_Riego(self, eficiencia_sistema:str): # 0.0 - 0.9
        
        eficiencia_sistema.strip()

        if not eficiencia_sistema:
            raise Exception("\n>>> El espacio 'Eficiencia del Sistema de Riego para Surco' no debe estar vacío.")
        
        try:
            eficiencia_numero:float = float(eficiencia_sistema)
        except Exception:
            raise Exception("\n>>> La Eficiencia del Sistema de Riego para Surco no tiene valores válidos. \n>>> Ingrese un número válido.")
        
        if eficiencia_numero < 0.0 or eficiencia_numero > 0.9:
            raise Exception("\n>>> La Eficiencia del Sistema de Riego para Surco es muy baja o excede el rango válido. \n>>> Rango válido entre 0.0 y 0.9")
        
        # Asignación 
        self.__eficiencia_sistema_riego:float = round(eficiencia_numero, 2)

    @Humedad_Minima.setter 
    def Humedad_Minima(self, minima:str): 
        
        minima.strip()

        if not minima: 
            raise Exception("\n>>> El espacio 'Umbral de Humedad de la Hoja Permitido/Mínimo' no debe estar vacío.")
        
        try:
            humedad_min:float = float(minima)
        except Exception:
            raise Exception("\n>>> Valor mínimo de humedad no válido. \n>>> Debe ingresar un número válido.")
        
        # Cómo se debe ingresar en porcentaje es de 0% - 100%
        if humedad_min < 0 or humedad_min > 100:
            raise Exception("\n>>> La humedad mínima debe estar entre 0% y 100%.")
        
        # Implementé esto por si en algún momento se usara primero el setter Humedad_Maxima 
        # Sirve para saber si hay datos ingresados anteriormente en la propiedad, si no, simplemente continua
        if hasattr(self, "_Generales__humedad_maxima"):
            if humedad_min >= self.__humedad_maxima:
                raise Exception("\n>>> La humedad mínima no debe ser mayor o igual que la humedad máxima establecida.")

        # Asignación
        self.__humedad_minima = round(humedad_min, 2)

    @Humedad_Maxima.setter 
    def Humedad_Maxima(self, maxima:str): 

        maxima.strip()

        if not maxima: 
            raise Exception("\n>>> El espacio 'Umbral de Humedad de la Hoja Permitido/Máximo' no debe estar vacío.")

        try:
            humedad_max:float = float(maxima)
        except Exception:
            raise Exception("\n>>> Valor máximo de humedad no válido. \n>>> Debe ingresar un número válido.")
        
        # Cómo se debe ingresar en porcentaje es de 0% - 100%
        if humedad_max < 0 or humedad_max > 100:
            raise Exception("\n>>> La humedad máxima debe estar entre 0% y 100%.")

        # Implementé esto por si en algún momento se usara primero el setter Humedad_Mínima
        if hasattr(self, "_Generales__humedad_minima"):
            if humedad_max <= self.__humedad_minima:
                raise Exception("\n>>> La humedad máxima no debe ser menor o igual que la humedad mínima establecida.")

        # Asignación
        self.__humedad_maxima = round(humedad_max, 2) 

    @Volumen_Riego_Deseado.setter
    def Volumen_Riego_Deseado(self, volumen_riego:str):
        
        volumen_riego.strip()

        if not volumen_riego:
            raise Exception("\n>>> El espacio 'Volumen de Riego Deseado' no debe estar vacío.")
        
        try:
            volumen:float = float(volumen_riego)
        except Exception:
            raise Exception("\n>>> El Volumen de Riego Deseado no es válido. \n>>> Debe ingresar un  número válido.")

        if volumen <= 0:
            raise Exception("\n>>> El Volumen de Riego Deseado debe ser mayor a cero.")

        # Asignación
        self.__volumen_riego_deseado = round(volumen, 2)

    
    # -- Fromato de texto -- #
    def __str__(self) -> str:
        return f"\n>>> ID Parcela: {self.__id_parcela}\n" \
                f">>> Profundidad Efectiva de la Raíz / Zona Radicular: {self.__zona_radicular}m\n" \
                f">>> Eficiencia del Sistema de Riego para Surco: {self.__eficiencia_sistema_riego}\n" \
                f">>> Umbral de Humedad de la Hoja Permitido:\n" \
                f" >>> Mínimo: {self.__humedad_minima}%\n" \
                f" >>> Máximo: {self.Humedad_Maxima}%\n" \
                f">>> Volumen de Riego Deseado: {self.Volumen_Riego_Deseado}m³"


# Pruebas
if __name__ == "__main__":
       
    # Generales 1: Condiciones ideales para un cultivo típico
    generales1 = Generales(
        "PAR-001",
        "0.75",   # Zona Radicular (m)
        "0.85",   # Eficiencia del Sistema de Riego (0.0 - 1.0)
        "50.0",   # Humedad Mínima (%)
        "75.0",   # Humedad Máxima (%)
        "3.50"    # Volumen de Riego Deseado (m³)
    )

    # Generales 2: Condiciones para un cultivo que tolera menos humedad
    generales2 = Generales(
        "PAR-002",
        "0.50",   # Zona Radicular (m)
        "0.70",   # Eficiencia del Sistema de Riego
        "35.0",   # Humedad Mínima (más bajo)
        "60.0",   # Humedad Máxima (más bajo)
        "1.80"    # Volumen de Riego Deseado (m³)
    )

    # Generales 3: Cultivo con raíces profundas y alta eficiencia de riego
    generales3 = Generales(
        "PAR-003",
        "1.00",   # Zona Radicular (m) (más profundo)
        "0.90",   # Eficiencia del Sistema de Riego (más alto)
        "65.0",   # Humedad Mínima (%)
        "90.0",   # Humedad Máxima (%)
        "5.00"    # Volumen de Riego Deseado (m³)
    )

    print("\n--- Pruebas de Datos Generales ---")
    print(generales1)
    print(generales2)
    print(generales3)
    
    # Pruebas de getters (opcional)
    print(f"\nZona Radicular de PAR-001: {generales1.Zona_Radicular} m")
    print(f"Humedad Máxima de PAR-003: {generales3.Humedad_Maxima}%")