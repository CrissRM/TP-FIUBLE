import tkinter as tk
from configuraciones.estilos import estilos
from formularios.formulario_registro import formulario_registro
from formularios.formulario_configuracion_personalizada import formulario_configuracion_personalizada
from formularios.formulario_configuracion_defecto import formulario_configuracion_defecto
from configuraciones.estilos_widgets import *


def btn_registrarse():
    form_registro = formulario_registro(root,registro,ingresar)
    form_registro.pack()
    registro["state"] = "disabled"
    ingresar["state"] = "disabled"
  
def btn_ingresar():
  registro["state"] = "disabled"
  ingresar["state"] = "disabled"
  res = msg_confirm("¿Quiere usar las configuraciones por defecto ?")
  configuracion_defecto.pack() if res else configuracion_personalizada .pack()




root = tk.Tk()
root.title("FIUBLE - SERPIENTE")
root.geometry("+300+200")
root.minsize(width=700,height=400)
root.configure(background=estilos["BACKGROUND_PRIMARY"])

titulo_aplicacion(root)

botones = marco_visible(root)
registro = boton_registar(botones,btn_registrarse)
ingresar = boton_ingresar(botones,btn_ingresar)

configuracion_defecto =formulario_configuracion_defecto(root,registro,ingresar)

configuracion_personalizada = formulario_configuracion_personalizada(root,registro,ingresar)
#-------------------------------------------------------------------------------






root.mainloop()
