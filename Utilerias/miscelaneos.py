from PIL import Image, ImageTk # Para manejar imagenes PNG (tkinter no soporta PNG)

def Centrar_Ventana(ventana, ventana_ancho, ventana_alto): # ventana_ancho = 1024, ventana_alto = 600
    """
        Centra la ventana según el tamaño de la pantalla
    """
    pantalla_ancho = ventana.winfo_screenwidth() # 1920 
    pantalla_alto = ventana.winfo_screenheight() # 1080 
    x = int((pantalla_ancho/2) - (ventana_ancho/2)) # 960 - 512 = 448
    y = int((pantalla_alto/2) - (ventana_alto/2)) # 540 - 300 = 240
    return f"{ventana_ancho}x{ventana_alto}+{x}+{y}"

def Leer_Imagen(ruta, size): 
    """
        Lee una imagen y define su tamaño 
    """
    imagen_original = Image.open(ruta) # Lee desde disco 
    imagen_original.resize(size, Image.LANCZOS) # tamaño y control de perdida de imagen 
    imagen_tk = ImageTk.PhotoImage(imagen_original) # devuelve objeto tipo PhotoImage 
    return imagen_tk 