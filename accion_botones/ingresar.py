from configuraciones.estilos_widgets import msg_confirm


def ingresar(lista):
    cuadro_botones,configuracion_defecto,configuracion_personalizada,textos = lista
    cuadro_botones.pack_forget()
    res = msg_confirm(textos["MSJ_CONFIRMAR_CONFIG_DEFECTO"],textos)
    configuracion_defecto.pack() if res else configuracion_personalizada .pack()