from Utilerias.config import *
from Utilerias import miscelaneos as util
from tkinter import Tk, Frame, Label, Button, Menu, Menubutton
from CapaPresentacion.Ventana_Parcelas import Ventana_Parcelas

class Contenedor_Principal(Tk): # Hereda de Tk

    def __init__(self):
        super().__init__() # Inicializa al padre
        self.Config_Ventana()
        self.Paneles()
        self.Abrir_Ventana_Parcelas()


    def Config_Ventana(self):
        """
            Configuraciones iniciales de la 
            ventana: titulo, imagenes, tamaños
        """
        self.title("Sistema Gestor de Parcelas y Sensores: AgroMon")
        self.iconbitmap("./Imagenes/icono.ico")
        self.geometry(util.Centrar_Ventana(self, 1024, 600))
        
        # Imagenes
        self.img_hamburguesa = util.Leer_Imagen("./Imagenes/menu.png", (24, 24))
        self.img_parcela = util.Leer_Imagen("./Imagenes/parcela.png", (24, 24))
        self.img_sensor = util.Leer_Imagen("./Imagenes/sensor.png", (24, 24))
        self.img_alertas = util.Leer_Imagen("./Imagenes/alertas.png", (24, 24))
        self.img_calculos = util.Leer_Imagen("./Imagenes/calculos.png", (24, 24))
        self.img_acercade = util.Leer_Imagen("./Imagenes/acerca-de.png", (24, 24))


    def Paneles(self):
        """
            Definición de paneles: panel superior (menú superior),
            panel central y panel izquierdo (menú lateral)
        """
        # Barra para información y Menú Superior
        self.panel_superior = Frame(
            self, 
            background=COLOR_PANEL_SUPERIOR, 
            height=35 # height da tamaño según los caracteres que caben
        )
        self.panel_superior.pack( # Acomoda de acuerdo a secciones (left, right, top, bottom)
            side="top", 
            fill="x" # rellena a los lados
        )

        # Barra lateral para el Menú principal
        self.panel_lateral = Frame(
            self, 
            background=COLOR_PANEL_LATERAL, 
            width=ANCHO_LATERAL_CERRADO
        )
        self.panel_lateral.pack(
            side="left", 
            fill="both", # rellena el espacio correspondiente
            expand=False 
        ) 
        """
        # Cuerpo central que contiene todas las ventanas de información 
        self.panel_central = Frame(
            self, 
            background=COLOR_PANEL_CENTRAL
        )
        self.panel_central.pack(
            side="right", 
            fill="both", 
            expand=True
        )"""

        # Configuración de Paneles
        self.Config_Panel_Superior()
        self.Config_Panel_Lateral()


    def Config_Panel_Superior(self):
        """
            Definición de las características del panel superior
        """
        self.titulo_principal = Label(
            self.panel_superior,
            text="AgroMon"
        )
        self.titulo_principal.config(
            fg=COLOR_TITULO_PRINCIPAL,
            font=FUENTE_TITULO,
            bg=COLOR_PANEL_SUPERIOR,
            pady=5, 
            padx=20
        )
        self.titulo_principal.grid(column=0, row=0)


    def Config_Panel_Lateral(self):
        """
            Definición de las características del panel lateral
        """
        self.panel_lateral.pack_propagate(False) # Para que el ancho del panel sea fijo
        self.panel_abierto = False # Bandera

        self.btn_menu = Button(
            self.panel_lateral,
            image=self.img_hamburguesa,
            command=self.Accion_Abrir_Cerrar,
            activebackground=COLOR_BOTON_SELECCIONADO,
            background=COLOR_PANEL_LATERAL,
            border=0,
            height=35,
            cursor="sb_h_double_arrow"
        )
        self.btn_menu.pack(
            side="top", 
            anchor="w", 
            padx=16, 
            pady=10
        )
        self.Bind_Hover_Events(self.btn_menu)

        # Panel para agregar las opciones del sistema
        self.panel_opciones = Frame(
            self.panel_lateral,
            bg=COLOR_PANEL_LATERAL
        )
        
        # Configuración de Panel Interno para Opciones
        self.Config_Panel_Opciones()


    def Config_Panel_Opciones(self):
        """
            Definición de las características del panel de opciones:\n
            Opciones del sistema, apertura de ventanas
        """
        self.btn_parcelas = Button(self.panel_opciones) # Parcelas, Datos Generales
        self.btn_sensores = Button(self.panel_opciones) # Sensores, Lecturas (Agregar, Cargar, Ver(Tabla(Borrar), Gráfico)), 
        self.btn_alertas = Button(self.panel_opciones) # Calcular Alertas, Visualizar Alertas Existentes
        self.btn_calculos = Button(self.panel_opciones) # Calcular Volumen de Riego 
        self.btn_acercade = Button(self.panel_opciones) # Acerca de
        
        btn_info = [
            (self.btn_parcelas, "Parcelas", self.img_parcela, self.Abrir_Ventana_Parcelas),
            (self.btn_sensores, "Sensores", self.img_sensor, self.Abrir_Ventana_Sensores),
            (self.btn_alertas, "Alertas", self.img_alertas, self.Abrir_Ventana_Alertas),
            (self.btn_calculos, "Cálculos", self.img_calculos, self.Abrir_Ventana_Calculos),
            (self.btn_acercade, "Acerca de", self.img_acercade, self.Abrir_Ventana_Calculos)
        ]
        
        for button, text, img, action in btn_info:
            self.Config_Botones_Panel_Opciones(button, text, img, action)


    def Accion_Abrir_Cerrar(self):
        """
            Expande y Contrae el Panel Lateral
        """
        if not self.panel_abierto:
            # Expande el panel
            self.panel_opciones.pack(fill="both")
            self.panel_lateral.config(width=ANCHO_LATERAL_ABIERTO)
            self.panel_abierto = True
        else:
            # Contrae el panel
            self.panel_opciones.pack_forget()
            self.panel_lateral.config(width=ANCHO_LATERAL_CERRADO)
            self.panel_abierto = False
            
        
    def Abrir_Ventana_Parcelas(self):
        Ventana_Parcelas(self)


    def Abrir_Ventana_Sensores(self):
        pass


    def Abrir_Ventana_Alertas(self):
        pass


    def Abrir_Ventana_Calculos(self):
        pass


    def Config_Botones_Panel_Opciones(self, button:Button, text, img, action):
        """
            Definición de las características de cada botón del menú lateral
        """
        button.config(
            text=f" {text}",
            image=img,
            compound="left",
            anchor="w",
            padx=13,
            font=FUENTE_BOTON_LATERAL,
            border=0,
            background=COLOR_PANEL_LATERAL,
            activebackground=COLOR_BOTON_SELECCIONADO,
            command=action,
            foreground=COLOR_TITULO_PRINCIPAL,
            height=50,
            cursor="hand2"
        )
        button.pack(
            side="top",
            fill="x"
        )
        self.Bind_Hover_Events(button)

    def Bind_Hover_Events(self, button):
        """
            Se definen los eventos del botón a la hora de pasar el mouse
        """ 
        # Evento al pasar el Mouse por encima del botón
        button.bind(
            "<Enter>",
            lambda event: self.Mouse_On(button)
        )

        # Evento al dejar de pasar el mouse por el botón
        button.bind(
            "<Leave>",
            lambda event: self.Mouse_Out(button)
        )

    def Mouse_On(self, button):
        """ 
            Evento al pasar el Mouse por encima del botón
        """
        button.config(
            background=COLOR_BOTON_SELECCIONADO
        )

    def Mouse_Out(self, button):
        """
            Evento al dejar de pasar el mouse por el botón
        """ 
        button.config(
            background=COLOR_PANEL_LATERAL 
        )

