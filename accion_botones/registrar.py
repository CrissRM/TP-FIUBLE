def registrarse(lista):
    formulario_registro,root,cuadro_botones = lista
    form_registro = formulario_registro(root,cuadro_botones)
    form_registro.pack()
    cuadro_botones.pack_forget()
    