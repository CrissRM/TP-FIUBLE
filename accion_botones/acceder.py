from acciones_funciones.validadores import sesion
from configuraciones.estilos_widgets import msg_warning,msg_info,msg_error

def acceder(argumentos):
  nombre_entry,clave_entry,jugadores,cant,inicia_app,root = argumentos 
  nombre = nombre_entry.get()
  password = clave_entry.get()
  
  if sesion(nombre,password):
    if nombre in jugadores:
      msg_warning(f"El usuario {nombre} ya inicio sesión  ")
    else:
      jugadores.append(nombre)
      msg_info("Sesión Iniciada correctamente")
      nombre_entry.delete(0,"end")
      clave_entry.delete(0,"end")
        
  else:
    msg_error("Contraseña y/o usuario no son incorrectas")

  if len(jugadores) == cant:
    root.destroy()
    inicia_app(jugadores)

