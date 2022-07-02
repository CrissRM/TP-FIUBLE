def volver(argumentos):
  frame_hidden,btn_registro,btn_ingreso = argumentos
  frame_hidden.pack_forget()
  btn_ingreso["state"] = "normal"
  btn_registro["state"] = "normal"