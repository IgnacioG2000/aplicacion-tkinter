from tkinter import *
from tkinter.messagebox import *
from tkinter.colorchooser import askcolor
from app_crud.creacion_bd import crear_base
from app_crud.creacion_tabla import crear_tabla
from app_crud.insertar_empleado import insertar
from app_crud.borrar_empleado import borrar
from app_crud.consultar_empleado import seleccionar
from app_crud.actualizar_empleado import actualizar

# import tkinter.font as tkFont

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

# fontfamilylist = list(tkFont.families())

# fontindex = 0

############################ MENSAJE DE BIENVENIDA ######################################

bienvenida = Label(
    main,
    text="Bienvenido/a al servicio de administración de empleados de DG S.A."
    "\n\nSeleccione la opción que quiera realizar\n",
)
bienvenida.grid(row=0, column=4)

############################ VARIABLES ######################################
var_nombre = StringVar()
var_apellido = StringVar()
var_direccion = StringVar()
var_dni = IntVar()
var_telefono = IntVar()
var_id = IntVar()

############################ CREAR BASE DE DATOS ######################################

conexion = crear_base()

############################ CREAR TABLA ######################################

crear_tabla(conexion)

############################ BOTONES ######################################


def volver_al_menu():
    pass


"""""" """""" """""" """""" """""" """""" """""" """""" """
                    ALTA EMPLEADO
""" """""" """""" """""" """""" """""" """""" """""" """"""


def dar_alta_empleado():
    global posicion
    # El mensaje withdraw() cierra la ventana principal
    main.withdraw()
    ventana = Toplevel()
    ventana.geometry(posicion)

    ingresar_datos = Label(ventana, text="Ingrese los datos del nuevo empleado")
    ingresar_datos.grid(row=0, column=1)

    nombre = Label(ventana, text="Nombre")
    nombre.grid(row=2, column=1, sticky=W)
    entry_nombre = Entry(ventana, textvariable=var_nombre)
    entry_nombre.grid(row=2, column=2)

    apellido = Label(ventana, text="Apellido")
    apellido.grid(row=3, column=1, sticky=W)
    entry_apellido = Entry(ventana, textvariable=var_apellido)
    entry_apellido.grid(row=3, column=2)

    direccion = Label(ventana, text="Direccion")
    direccion.grid(row=4, column=1, sticky=W)
    entry_direccion = Entry(ventana, textvariable=var_direccion)
    entry_direccion.grid(row=4, column=2)

    dni = Label(ventana, text="DNI")
    dni.grid(row=5, column=1, sticky=W)
    entry_dni = Entry(ventana, textvariable=var_dni)
    entry_dni.grid(row=5, column=2)

    telefono = Label(ventana, text="Telefono")
    telefono.grid(row=6, column=1, sticky=W)
    entry_telefono = Entry(ventana, textvariable=var_telefono)
    entry_telefono.grid(row=6, column=2)

    def alta_empleado():
        global conexion

        insertar(
            conexion,
            var_nombre.get(),
            var_apellido.get(),
            var_direccion.get(),
            var_dni.get(),
            var_telefono.get(),
        )

    boton_salir = Button(ventana, text="Salir", command=volver_al_menu)
    boton_salir.grid(row=8, column=1)

    boton_insertar_empleado = Button(
        ventana, text="Dar de alta empleado", command=alta_empleado
    )
    boton_insertar_empleado.grid(row=8, column=2)


boton_alta_empleado = Button(
    main, text="Dar de alta empleado", command=dar_alta_empleado
)
boton_alta_empleado.grid(row=1, column=1)


"""""" """""" """""" """""" """""" """""" """""" """""" """
                    BAJA EMPLEADO
""" """""" """""" """""" """""" """""" """""" """""" """"""


def dar_baja_empleado():
    global posicion
    main.withdraw()
    ventana2 = Toplevel()
    ventana2.geometry(posicion)

    ingresar_id_baja = Label(ventana2, text="Ingrese el ID del empleado a dar de baja")
    ingresar_id_baja.grid(row=0, column=1)
    entry_ingresar_id_baja = Entry(ventana2, textvariable=var_id)
    entry_ingresar_id_baja.grid(row=0, column=2)

    def baja_empleado():
        global conexion
        borrar(conexion, var_id.get())

    boton_salir2 = Button(ventana2, text="Salir", command=volver_al_menu)
    boton_salir2.grid(row=1, column=1)

    boton_borrar_empleado = Button(
        ventana2, text="Dar de baja empleado", command=baja_empleado
    )
    boton_borrar_empleado.grid(row=1, column=2)


boton_baja_empleado = Button(
    main, text="Dar de baja empleado", command=dar_baja_empleado
)
boton_baja_empleado.grid(row=1, column=4)

"""""" """""" """""" """""" """""" """""" """""" """""" """
                MODIFICAR EMPLEADO
""" """""" """""" """""" """""" """""" """""" """""" """"""


def modificar_empleado():
    global posicion
    main.withdraw()
    ventana3 = Toplevel()
    ventana3.geometry(posicion)

    def busqueda_empleado():
        global conexion
        seleccionar(conexion, var_id.get())

        global posicion
        nonlocal ventana3
        ventana3.withdraw()
        ventana4 = Toplevel()
        ventana4.geometry(posicion)

        ingresar_datos = Label(
            ventana4, text="Ingrese los datos del empleado a modificar"
        )
        ingresar_datos.grid(row=0, column=1)

        nombre = Label(ventana4, text="Nombre")
        nombre.grid(row=2, column=1, sticky=W)
        entry_nombre = Entry(ventana4, textvariable=var_nombre)
        entry_nombre.grid(row=2, column=2)

        apellido = Label(ventana4, text="Apellido")
        apellido.grid(row=3, column=1, sticky=W)
        entry_apellido = Entry(ventana4, textvariable=var_apellido)
        entry_apellido.grid(row=3, column=2)

        direccion = Label(ventana4, text="Direccion")
        direccion.grid(row=4, column=1, sticky=W)
        entry_direccion = Entry(ventana4, textvariable=var_direccion)
        entry_direccion.grid(row=4, column=2)

        dni = Label(ventana4, text="DNI")
        dni.grid(row=5, column=1, sticky=W)
        entry_dni = Entry(ventana4, textvariable=var_dni)
        entry_dni.grid(row=5, column=2)

        telefono = Label(ventana4, text="Telefono")
        telefono.grid(row=6, column=1, sticky=W)
        entry_telefono = Entry(ventana4, textvariable=var_telefono)
        entry_telefono.grid(row=6, column=2)

        def editar_empleado():
            global conexion
            actualizar(
                conexion,
                var_id.get(),
                var_nombre.get(),
                var_apellido.get(),
                var_direccion.get(),
                var_dni.get(),
                var_telefono.get(),
            )

        boton_salir4 = Button(ventana4, text="Salir", command=volver_al_menu)
        boton_salir4.grid(row=1, column=1)

        boton_modificacion_empleado = Button(
            ventana4, text="Modificar empleado", command=editar_empleado
        )
        boton_modificacion_empleado.grid(row=1, column=2)

    ingresar_id_modificacion = Label(
        ventana3, text="Ingrese el ID del empleado a modificar"
    )
    ingresar_id_modificacion.grid(row=0, column=0)

    entry_ingresar_id_modificacion = Entry(ventana3, textvariable=var_id)
    entry_ingresar_id_modificacion.grid(row=0, column=1)

    boton_salir3 = Button(ventana3, text="Salir", command=volver_al_menu)
    boton_salir3.grid(row=1, column=1)

    boton_modificar_empleado = Button(
        ventana3, text="Buscar empleado", command=busqueda_empleado
    )
    boton_modificar_empleado.grid(row=3, column=0)


boton_modificar_empleado = Button(
    main, text="Modificar empleado", command=modificar_empleado
)
boton_modificar_empleado.grid(row=6, column=4)

"""""" """""" """""" """""" """""" """""" """""" """""" """
                CONSULTAR EMPLEADO
""" """""" """""" """""" """""" """""" """""" """""" """"""


def consultar_empleado():
    global posicion
    main.withdraw()
    ventana5 = Toplevel()
    ventana5.geometry(posicion)

    ingresar_id_consulta = Label(
        ventana5, text="Ingrese el ID del empleado a consultar"
    )
    ingresar_id_consulta.grid(row=0, column=0)

    entry_ingresar_id_consulta = Entry(ventana5, textvariable=var_id)
    entry_ingresar_id_consulta.grid(row=0, column=1)

    def consultar_empleado():
        global conexion
        seleccionar(conexion, var_id.get())

    boton_salir5 = Button(ventana5, text="Salir", command=volver_al_menu)
    boton_salir5.grid(row=1, column=1)

    boton_consulta_empleado = Button(
        ventana5, text="Buscar empleado", command=consultar_empleado
    )
    boton_consulta_empleado.grid(row=3, column=0)


boton_consultar_empleado = Button(
    main, text="Consultar empleado", command=consultar_empleado
)
boton_consultar_empleado.grid(row=6, column=1)

"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """
                MOSTRAR TODOS LOS EMPLEADOS
""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""

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
