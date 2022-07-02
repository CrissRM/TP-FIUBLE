from configuraciones.estilos_widgets import msg_confirm
from configuraciones.textos import texto

def ingresar(lista):
    textos = texto()
    cuadro_botones,configuracion_defecto,configuracion_personalizada = lista
    cuadro_botones.pack_forget()
    res = msg_confirm(textos["MSJ_CONFIRMAR_CONFIG_DEFECTO"])
    configuracion_defecto.pack() if res else configuracion_personalizada .pack()