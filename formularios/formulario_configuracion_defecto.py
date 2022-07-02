from accion_botones.confirmar_defecto import confirmar
from accion_botones.volver import volver
from configuraciones.estilos_widgets import etiqueta,entrada_texto,boton_confirmar,boton_volver,marco_visible,marco_invisible


def formulario_configuracion_defecto(root,registro,ingresar):
    
    entrada_jugadores = marco_invisible(root)
    #------------------------------------------------------------------------------
    jugadores = marco_visible(entrada_jugadores)
    etiqueta(jugadores,"Jugadores: ")
    players_entry = entrada_texto(jugadores)
    #-----------------------------------------------------------------------------
    marco_botones = marco_visible(entrada_jugadores)
    boton_confirmar(marco_botones,confirmar,[players_entry,entrada_jugadores,root,registro,ingresar])

    boton_volver(marco_botones,volver,[entrada_jugadores,registro,ingresar])
  
    return entrada_jugadores
