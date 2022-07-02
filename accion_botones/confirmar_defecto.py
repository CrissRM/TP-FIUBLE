from configuraciones.datos_iniciales import condiciones_iniciales
from acciones_funciones.validadores import texto
from acciones_funciones.diccionario_de_palabras import diccionario_de_palabras
from formularios.formulario_ingreso import formulario_ingreso
from app.app_consola import inicia_app
from configuraciones.estilos_widgets import msg_warning

def confirmar(lista):
    players_entry,entrada_jugadores,root,registro,ingresar = lista
    MAX_JUGADORES = condiciones_iniciales()["cantidad_jugadores"]
    cantidad = texto(players_entry.get())

    if cantidad and cantidad <= MAX_JUGADORES:
        entrada_jugadores.pack_forget()
        jugadores = []
        
        diccionario_de_palabras()
        formulario_ingreso(root,registro,ingresar,jugadores,cantidad,inicia_app).pack()
    else:
        msg_warning(f"El juego está implementado para un máximo de {MAX_JUGADORES}jugadoes")