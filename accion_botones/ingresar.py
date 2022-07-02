from configuraciones.estilos_widgets import msg_confirm

def ingresar(lista):
    cuadro_botones,configuracion_defecto,configuracion_personalizada = lista
    cuadro_botones.pack_forget()
    res = msg_confirm("¿Quiere usar las configuraciones por defecto ?")
    configuracion_defecto.pack() if res else configuracion_personalizada .pack()