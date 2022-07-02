from accion_botones.volver import volver
from accion_botones.confirmar_personalizada import confirmar
from configuraciones.estilos_widgets import *
from configuraciones.textos import texto

    
def formulario_configuracion_personalizada(root,botones):
    textos = texto()
    configuraciones = marco_invisible(root) 

    #---CANT JUGADORES
    cantidad_jugadores = marco_visible(configuraciones)
    etiqueta(cantidad_jugadores,textos["LABEL_JUGADORES"])
    players_entry = entrada_texto(cantidad_jugadores)

    #--LONG PALABRA
    longitud_palabra = marco_visible(configuraciones)

    etiqueta(longitud_palabra,textos["LABEL_LETRAS"])
    letras_entry = entrada_texto(longitud_palabra)

    #--- CANT PARTIDAS
    cantidad_partidas = marco_visible(configuraciones)
    etiqueta(cantidad_partidas,textos["LABEL_PARTIDAS"])
    partidas_entry = entrada_texto(cantidad_partidas)
    #-----------------------------------------------------------------------------
    frame_botones = marco_visible(configuraciones)

    boton_confirmar(frame_botones,confirmar,[players_entry,configuraciones,root,botones,letras_entry,partidas_entry])

    boton_volver(frame_botones,volver,[configuraciones,botones])

    return configuraciones