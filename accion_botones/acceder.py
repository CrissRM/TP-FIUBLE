from acciones_funciones.validadores import sesion
from configuraciones.estilos_widgets import msg_warning,msg_info,msg_error
from configuraciones.textos import texto

def acceder(argumentos):
    textos = texto()
    nombre_entry,clave_entry,jugadores,cant,inicia_app,root = argumentos 
    nombre = nombre_entry.get()
    password = clave_entry.get()
  
    if sesion(nombre,password):
        if nombre in jugadores:
            msg_warning(f'{nombre}{textos["MSJ_ADVERTENCIA_SESION_YA_INICIADA"]}')
        else:
            jugadores.append(nombre)
            msg_info(textos["MSJ_INFORMACION_SESION"])
            nombre_entry.delete(0,"end")
            clave_entry.delete(0,"end")
            
    else:
        msg_error(textos["MSJ_ERROR_USUARIO_CONTRASEÑA"])

    if len(jugadores) == cant:
        root.destroy()
        inicia_app(jugadores)

