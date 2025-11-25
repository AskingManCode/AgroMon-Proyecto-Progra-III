from Utilerias.config import *
from tkinter import Frame, Label, Button

class Ventana_Parcelas():

    def __init__(self, ventana):
        self.Config_Botones_Superiores(ventana.panel_superior)

    def Config_Botones_Superiores(self, panel_superior):
        
        opciones = ["Parcelas", "Valores Generales"]

        col = 1
        for texto in opciones:
            item = Button(
                panel_superior,
                text=texto,
                foreground=COLOR_TITULO_PRINCIPAL,
                background=COLOR_PANEL_SUPERIOR,
                font= FUENTE_MENU_SUPERIOR,
                border=0,
                padx=8,
                pady=5,
                cursor="hand2"
            )

            # Hover
            item.bind("<Enter>", lambda e, w=item: w.config(bg=COLOR_BOTON_SELECCIONADO))
            item.bind("<Leave>", lambda e, w=item: w.config(bg=COLOR_PANEL_SUPERIOR))

            # Click (a definir más adelante)
            item.bind("<Button-1>", lambda e, nombre=texto: print("Click en", nombre))

            item.grid(column=col, row=0)
            col += 1

        # Ajustar columnas
        panel_superior.grid_columnconfigure(col, weight=1)