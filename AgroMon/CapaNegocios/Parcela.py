class Parcela(): 

    # Constructor 
    def __init__( 
            self, modificacion:bool, id_parcela:str = None, 
            nombre:str = None, ubicacion_latitud:str = None, 
            ubicacion_longitud:str = None, tipo_cultivo:str = None, 
            area:str = None
    ):
        """
            Inicializa una parcela enviando los datos a los setters 
            para su validación. Si algún dato no cumple las 
            condiciones, se lanza una excepción para reiniciar 
            el ingreso de datos.
        """
        if modificacion:
            # Evita validaciones
            pass  
        else:
            # Datos iniciales de parcels
            self.ID_Parcela = id_parcela
            self.Nombre = nombre
            # Ubicación Geográfica
            self.Ubicacion_Latitud = ubicacion_latitud
            self.Ubicacion_Longitud = ubicacion_longitud
            #
            self.Tipo_Cultivo = tipo_cultivo
            self.Area = area


    # -- Getters -- #
    @property
    def ID_Parcela(self) -> str:
        return self.__id_parcela
    @property
    def Nombre(self) -> str:
        return self.__nombre
    @property
    def Ubicacion_Latitud(self) -> float:
        return self.__ubicacion_latitud
    @property
    def Ubicacion_Longitud(self) -> float:
        return self.__ubicacion_longitud
    @property
    def Tipo_Cultivo(self) -> str:
        return self.__tipo_cultivo
    @property
    def Area(self) -> float:
        return self.__area_m2


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

    @Nombre.setter
    def Nombre(self, nombre:str):
        
        # Formateo del texto para trabajar con el de forma estándar
        nombre = nombre.title().strip()

        if not nombre:
            raise Exception("\n>>> El espacio 'Nombre de la Parcela' no debe estar vacío.")

        # Asignación
        self.__nombre:str = nombre

    @Ubicacion_Latitud.setter
    def Ubicacion_Latitud(self, latitud:str):
        
        latitud = latitud.strip()

        if not latitud:
            raise Exception("\n>>> El espacio 'Ubicación Geográfica/Latitud' no debe estar vacío.")
        
        try:
            numero_latitud:float = float(latitud)
        except Exception:
            raise Exception("\n>>> Latitud inválida. \n>>> Debe ser un número válido, puede incluir decimales o signo de negativo.")
        
        # Limitación planetaria
        if numero_latitud < -90 or numero_latitud > 90:
            raise Exception("\n>>> Latitud fuera de rango. Debe estar entre -90 y 90.")

        # Asignación
        self.__ubicacion_latitud:float = numero_latitud

    @Ubicacion_Longitud.setter
    def Ubicacion_Longitud(self, longitud:str):
        
        longitud.strip()

        if not longitud:
            raise Exception("\n>>> Es espacio 'Ubicación Geográfica/Longitud' no debe estar vacío.")
        
        try:
            numero_longitud:float = float(longitud)
        except Exception:
            raise Exception("\n>>> Longitud inválida. \n>>> Debe ingresar un número válido, puede incluir decimales o signo de negativo.")
        
        # Limitación planetaria
        if numero_longitud < -180 or numero_longitud > 180:
            raise Exception("Longitud fuera de rango. Debe estar entre -180 y 180.")

        # Asignación
        self.__ubicacion_longitud:float = numero_longitud

    @Tipo_Cultivo.setter
    def Tipo_Cultivo(self, tipo_cultivo:str):
        
        # Formateo del texto para trabajar con el de forma estándar
        tipo_cultivo = tipo_cultivo.title().strip()
        
        if not tipo_cultivo:
            raise Exception("\n>>> Es espacio 'Tipo de Cultivo' no debe estar vacío.")

        for letra in tipo_cultivo:
            if letra.isdigit():
                raise Exception("\n>>> El espacio 'Tipo de Cultivo' no debe contener números.")
        
        # Asignación
        self.__tipo_cultivo:str = tipo_cultivo

    @Area.setter 
    def Area(self, area:str): 
        
        area.strip()

        if not area:
            raise Exception("\n>>> El espacio 'Área de la Parcela (m²)' no debe estar vacío.")

        try:
            area_mts2:float = float(area)
        except Exception:
            raise Exception("\n>>> Área de la Parcela no válida. \n>>> Debe ingresar un número válido.")
        
        if area_mts2 <= 0:
            raise Exception("\n>>> El Área de la Parcela debe ser mayor a cero.")
        
        # Asignación
        self.__area_m2:float = area_mts2


    # -- Fromato de texto -- #
    def __str__(self) -> str:
        return f"\n>>> ID Parcela: {self.__id_parcela}\n" \
                f">>> Nombre: {self.__nombre}\n" \
                f">>> Ubicación Geográfica (Coordenadas):\n" \
                f" >>> Latitud: {self.__ubicacion_latitud}\n" \
                f" >>> Longitud: {self.__ubicacion_longitud}\n" \
                f">>> Tipo de Cultivo: {self.__tipo_cultivo}\n" \
                f">>> Área: {self.__area_m2}m²"


# Pruebas
if __name__ == "__main__":
       
    # Parcela 1: Ejemplo básico de un cultivo de cereales
    parcela1 = Parcela(
        "PAR-001", 
        "Hacienda El Sol", 
        "13.56",     # Latitud
        "-32.50",    # Longitud
        "Maíz", 
        "3500.25"    # Área en m²
    )

    # Parcela 2: Ejemplo de un cultivo de frutas con coordenadas extremas
    parcela2 = Parcela(
        "PAR-002", 
        "Valle de Manzanas", 
        "-34.60",    # Latitud (Hemisferio Sur)
        "58.38",     # Longitud
        "Manzana", 
        "1500.00"
    )

    # Parcela 3: Ejemplo de un cultivo de tubérculos con un área menor
    parcela3 = Parcela(
        "PAR-003", 
        "Finca Raíces", 
        "5.00", 
        "74.00",
        "Papa", 
        "850.75"
    )

    print("\n--- Pruebas de Parcela ---")
    print(parcela1)
    print(parcela2)
    print(parcela3)
    
    # Pruebas de getters (opcional)
    print(f"\nID de Parcela 1: {parcela1.ID_Parcela}")
    print(f"Área de Parcela 3: {parcela3.Area} m²")