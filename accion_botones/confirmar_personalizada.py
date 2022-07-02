from acciones_funciones.validadores import texto
from acciones_funciones.diccionario_de_palabras import diccionario_de_palabras
from configuraciones.datos_iniciales import condiciones_iniciales
from configuraciones.estilos_widgets import msg_warning
from configuraciones.formatear import formatear_configuracion_archivo
from formularios.formulario_ingreso import formulario_ingreso
from app.app_consola import inicia_app
from configuraciones.textos import texto as texto_msj

def confirmar(lista):
  textos = texto_msj()  
  players_entry,configuraciones,root,botones,letras_entry,partidas_entry = lista

  MAX_JUGADORES = condiciones_iniciales()["cantidad_jugadores"]
  MAX_LONG_LETRAS = condiciones_iniciales()["max_long_letras"]
  MAX_PARTIDAS = condiciones_iniciales()["max_partidas"]

  cantidad_jugadores = texto(players_entry.get())
  cantidad_letras = texto(letras_entry.get())
  cantidad_partidas = texto(partidas_entry.get())

  if cantidad_jugadores and cantidad_letras and cantidad_partidas:
    if cantidad_jugadores> MAX_JUGADORES:
      msg_warning(f"{textos['MSJ_MAXIMO_JUGADORES']} {MAX_JUGADORES}")
    elif cantidad_letras> MAX_LONG_LETRAS:
      msg_warning(f"{textos['MSJ_MAX_LETRAS_PALABRA']}{MAX_LONG_LETRAS}")
    elif cantidad_partidas>MAX_PARTIDAS:
      msg_warning(f"{textos['MSJ_MAX_PARTIDAS']}{MAX_PARTIDAS}")
    else:
      configuraciones.pack_forget()
      jugadores = []
      reiniciar =False if cantidad_jugadores == 1 else True
      
      formatear_configuracion_archivo(cantidad_letras,cantidad_partidas,reiniciar)
      diccionario_de_palabras()
      formulario_ingreso(root,botones,jugadores,cantidad_jugadores,inicia_app).pack()
    