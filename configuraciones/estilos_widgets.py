from tkinter import Label,Button,Entry,Label,Frame,messagebox as mb
from configuraciones.estilos import estilos

def titulo_aplicacion(root):
    return Label(
        root,
        text="FIUBLE-SERPIENTE",
        padx=5,
        pady=5,
        font=("Raleway",25,"roman"),
        width=25,
        anchor="center",
        background=estilos["BACKGROUND_PRIMARY"],
        foreground=estilos["FOREGROUND_PRIMARY"],
        ).pack(side="top",padx=10,pady=10)

def boton_registar(root,funct):
    boton = Button(
        root,
        text="REGISTARSE",
        font=("Releway",10,"normal"),
        padx=5,
        pady=5,
        state="normal",
        background=estilos["BACKGROUND_BUTTON_REGISTRO"],
        foreground=estilos["FOREGROUND_BUTTON_REGISTRO"],
        activebackground=estilos["BACKGROUND_BUTTON_REGISTRO_ACTIVE"],
        command=funct
        )
    boton.pack(
            side="left",
            padx=10,
            pady=10
        )
    
    return boton

def boton_ingresar(root,funct):
    boton = Button(
        root,
        text="INGRESAR",
        font=("Releway",10,"normal"),
        padx=5,
        pady=5,
        state="normal",
        background=estilos["BACKGROUND_BUTTON_INGRESO"],
        foreground=estilos["FOREGROUND_BUTTON_INGRESO"],
        activebackground=estilos["BACKGROUND_BUTTON_INGRESO_ACTIVE"],
        command=funct
        )
    boton.pack(
            side="left",
            padx=10,
            pady=10
        )
    return boton

def boton_volver(root,funct,arg):
    boton = Button(
        root,
        text="VOLVER",
        padx=5,
        pady=5,
        font=("Releway",10,"normal"),
        foreground="#fff",
        background="red",
        command=lambda: funct(arg)
    )
    boton.pack(side="left",padx=10,pady=10)

    return boton

def boton_guardar_registro(root,funct,arg):
    boton = Button(
        root,
        text="GUARDAR",
        padx=5,
        pady=5,
        font=("Releway",10,"normal"),
        background="blue",
        foreground="#fff",
        command=lambda: funct(arg)
    )

    boton.pack(side="left",padx=10,pady=10)

    return boton

def boton_acceder(root,funct,arg):
    boton = Button(
        root,
        text="ACCEDER",
        padx=5,
        pady=5,
        font=("Releway",10,"normal"),
        background="blue",
        foreground="#fff",
        command=lambda: funct(arg)
    )

    boton.pack(side="left",padx=10,pady=10)

    return boton

def boton_confirmar(root,funct,arg):
    boton = Button(
        root,
        text="CONFIRMAR",
        padx=5,
        pady=5,
        font=("Releway",10,"normal"),
        background="green",
        foreground="#fff",
        command=lambda: funct(arg)
    )

    boton.pack(side="left",padx=10,pady=10)

    return boton

def entrada_texto(root):
    caja = Entry(
        root,
        font=("Releway",15,"normal"),
        width=15,
        background="#fff",
        foreground="#000",
        justify="left"
    )
    caja.pack(side="left",padx=10,pady=10)
    return caja

def entrada_clave(root):
    caja = Entry(
        root,
        font=("Releway",15,"normal"),
        width=15,
        background="#fff",
        foreground="#000",
        show="*",
        justify="left"
    )
    caja.pack(side="left",padx=10,pady=10)
    return caja

def etiqueta(root,texto):
    label = Label(
        root,
        text=texto,
        padx=5,
        pady=5,
        font=("Releway",12,"roman"),
        width=15,
        anchor="w",
        background=estilos["BACKGROUND_PRIMARY"],
        foreground=estilos["FOREGROUND_PRIMARY"]
    )
    label.pack(side="left",padx=10,pady=10)
    return label

def marco_visible(root):
    marco = Frame(
        root,
        padx=10,
        pady=10,
        background=estilos["BACKGROUND_PRIMARY"],
    )
    marco.pack()

    return marco

def marco_invisible(root):
    marco = Frame(
        root,
        padx=10,
        pady=10,
        background=estilos["BACKGROUND_PRIMARY"],
    )
    marco.pack_forget()

    return marco

def msg_warning(msg):
  mb.showwarning("Advertencia",msg)

def msg_error(msg):
  mb.showerror("Error",msg)

def msg_info(msg):
  mb.showinfo("Info",msg)

def msg_confirm(msg):
  return mb.askyesno("Preguntar",msg)
  