from configuraciones.estilos_widgets import msg_warning,msg_info,msg_confirm,msg_error
from acciones_funciones.validadores import contrasenia,usuario,nombre as nombres
from accion_botones.volver import volver

def guardar(argumentos):
  
  form_registro,btn_registro,btn_ingreso,nombre_entry,clave_entry,clave_entry_repeat = argumentos
  nombre = nombre_entry.get()
  password = clave_entry.get()
  password_repeat = clave_entry_repeat.get()
  if nombre =="" and password =="":
    msg_warning("Los camos nombre y contraseña son requeridos")
  elif nombre =="":
    msg_warning("El campo nombre es requerido")
  elif password =="":
    msg_warning("El campo contraseña es requerido")
  elif password !=password_repeat:
    msg_error("Las contraseñas no coinciden")
  else:
    if nombres(nombre) and contrasenia(password):
      if usuario(nombre):
        msg_warning("El usuario ya existe")
      else:
        with open("archivos/jugadores.csv","a") as jugadores:
            jugadores.write(f"{nombre},{password}\n")
        
        msg_info("Usuario registrado con éxito")
        res = msg_confirm("¿Quiere registrar otro usuario?")
        if res:
          nombre_entry.delete(0,"end")
          clave_entry.delete(0,"end")
          clave_entry_repeat.delete(0,"end")
        else:
          volver([form_registro,btn_registro,btn_ingreso])

