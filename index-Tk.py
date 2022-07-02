import tkinter as tk
from configuraciones.estilos import estilos
from formularios.formulario_registro import formulario_registro
from formularios.formulario_configuracion_personalizada import formulario_configuracion_personalizada
from formularios.formulario_configuracion_defecto import formulario_configuracion_defecto
from configuraciones.estilos_widgets import *
from accion_botones.registrar import registrarse
from accion_botones.ingresar import ingresar as ingreso

def interfaz_grafica():
    root = tk.Tk()
    root.title("FIUBLE - SERPIENTE")
    root.geometry("+300+200")
    root.minsize(width=700,height=400)
    root.configure(background=estilos["BACKGROUND_PRIMARY"])

    titulo_aplicacion(root)

    botones = marco_visible(root)
    boton_registar(botones,registrarse,[formulario_registro,root,botones]) 
    boton_ingresar(botones,ingreso,[botones,formulario_configuracion_defecto(root,botones),formulario_configuracion_personalizada(root,botones)])

    root.mainloop()

interfaz_grafica()
