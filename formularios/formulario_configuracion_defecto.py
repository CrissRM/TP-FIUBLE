from accion_botones.confirmar_defecto import confirmar
from accion_botones.volver import volver 
from configuraciones.estilos_widgets import *
from configuraciones.textos import texto


def formulario_configuracion_defecto(root,botones):
    textos = texto()
    entrada_jugadores = marco_invisible(root)
    #------------------------------------------------------------------------------
    jugadores = marco_visible(entrada_jugadores)
    etiqueta(jugadores,textos["LABEL_JUGADORES"])
    players_entry = entrada_texto(jugadores)
    #-----------------------------------------------------------------------------
    marco_botones = marco_visible(entrada_jugadores)
    boton_confirmar(marco_botones,confirmar,[players_entry,entrada_jugadores,root,botones])

    boton_volver(marco_botones,volver,[entrada_jugadores,botones])
  
    return entrada_jugadores
