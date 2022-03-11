from tkinter import *
from tkinter.messagebox import *
from tkinter.colorchooser import askcolor
import tkinter.font as tkFont


main = Tk()

main.title("DG S.A.")

############################ CENTRAR PANTALLA ######################################
ancho_ventana = 700
alto_ventana = 300

x_ventana = main.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = main.winfo_screenheight() // 2 - alto_ventana // 2

posicion = (
    str(ancho_ventana)
    + "x"
    + str(alto_ventana)
    + "+"
    + str(x_ventana)
    + "+"
    + str(y_ventana)
)
main.geometry(posicion)

fontfamilylist = list(tkFont.families())

# fontindex = 0

############################ MENSAJE DE BIENVENIDA ######################################

bienvenida = Label(
    main,
    text="Bienvenido/a al servicio de administración de empleados de DG S.A."
    "\n\nSeleccione la opción que quiera realizar\n",
)
bienvenida.grid(row=0, column=4)


############################ BOTONES ######################################


def dar_alta_empleado():
    # El mensaje withdraw() cierra la ventana principal
    global posicion
    main.withdraw()
    ventana = Toplevel()
    ventana.geometry(posicion)

    ingresar_datos = Label(ventana, text="Ingrese los datos del nuevo empleado")
    ingresar_datos.grid(row=0, column=1)

    nombre = Label(ventana, text="Nombre")
    nombre.grid(row=2, column=1, sticky=W)
    entry_nombre = Entry(ventana)
    entry_nombre.grid(row=2, column=2)

    apellido = Label(ventana, text="Apellido")
    apellido.grid(row=3, column=1, sticky=W)
    entry_apellido = Entry(ventana)
    entry_apellido.grid(row=3, column=2)

    direccion = Label(ventana, text="Direccion")
    direccion.grid(row=4, column=1, sticky=W)
    entry_direccion = Entry(ventana)
    entry_direccion.grid(row=4, column=2)

    dni = Label(ventana, text="DNI")
    dni.grid(row=5, column=1, sticky=W)
    entry_dni = Entry(ventana)
    entry_dni.grid(row=5, column=2)

    telefono = Label(ventana, text="Telefono")
    telefono.grid(row=6, column=1, sticky=W)
    entry_telefono = Entry(ventana)
    entry_telefono.grid(row=6, column=2)

    def volver_al_menu():
        pass

    def alta_empleado():
        pass

    boton_salir = Button(ventana, text="Salir", command=volver_al_menu)
    boton_salir.grid(row=8, column=1)

    boton_insertar_empleado = Button(
        ventana, text="Dar de alta empleado", command=alta_empleado
    )
    boton_insertar_empleado.grid(row=8, column=2)


def dar_baja_empleado():
    pass


def modificar_empleado():
    pass


def consultar_empleado():
    pass


boton_alta_empleado = Button(
    main, text="Dar de alta empleado", command=dar_alta_empleado
)
boton_alta_empleado.grid(row=1, column=1)

boton_baja_empleado = Button(
    main, text="Dar de baja empleado", command=dar_baja_empleado
)
boton_baja_empleado.grid(row=1, column=4)

boton_consultar_empleado = Button(
    main, text="Consultar empleado", command=consultar_empleado
)
boton_consultar_empleado.grid(row=6, column=1)

boton_modificar_empleado = Button(
    main, text="Modificar empleado", command=modificar_empleado
)
boton_modificar_empleado.grid(row=6, column=4)


############################ MENU ######################################


def color():
    color_elegido = askcolor(color="#00ff00", title="Cambiar fondo")
    main.configure(bg=color_elegido[1])
    bienvenida.configure(bg=color_elegido[1])


menubar = Menu(main)

menu_formato = Menu(menubar, tearoff=0)
menu_formato.add_command(label="Cambiar color de fondo", command=color)
menu_formato.add_separator()
menu_formato.add_command(label="Salir", command=main.quit)
menubar.add_cascade(label="Formato", menu=menu_formato)

main.config(menu=menubar)

main.mainloop()
