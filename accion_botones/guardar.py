from configuraciones.estilos_widgets import msg_warning,msg_info,msg_confirm,msg_error
from acciones_funciones.validadores import contrasenia,usuario,nombre as nombres
from accion_botones.volver import volver
from configuraciones.textos import texto

def guardar(argumentos):
  textos = texto()
  form_registro,cuadro_botones,nombre_entry,clave_entry,clave_entry_repeat = argumentos
  nombre = nombre_entry.get()
  password = clave_entry.get()
  password_repeat = clave_entry_repeat.get()
  if nombre =="" and password =="":
    msg_warning(textos["MSJ_CONTRASEÑA_USUARIO_REQUERIDOS"])
  elif nombre =="":
    msg_warning(textos["MSJ_NOMBRE_REQUERIDO"])
  elif password =="":
    msg_warning(textos["MSJ_CONTRASEÑA_REQUERIDA"])
  elif password !=password_repeat:
    msg_error(textos["MSJ_CONTRASEÑAS_NO_COINCIDEN"])
  else:
    if nombres(nombre) and contrasenia(password):
      if usuario(nombre):
        msg_warning(textos["MSJ_USUARIO_YA_EXISTE"])
      else:
        with open("archivos/jugadores.csv","a") as jugadores:
            jugadores.write(f"{nombre},{password}\n")
        
        msg_info(textos["MSJ_USUARIO_REGISTRADO_EXITO"])
        res = msg_confirm(textos["MSJ_REGISTRAR_OTRO_USUARIO"])
        if res:
          nombre_entry.delete(0,"end")
          clave_entry.delete(0,"end")
          clave_entry_repeat.delete(0,"end")
        else:
          volver([form_registro,cuadro_botones])

