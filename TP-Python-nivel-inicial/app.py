import tkinter as tk
import re
from tkinter import W
from tkinter.messagebox import askyesno, showinfo, showwarning, showerror
from tkinter.colorchooser import askcolor
from app_crud.sql_crud.creacion_bd import crear_base
from app_crud.sql_crud.creacion_tabla import crear_tabla
from app_crud.insertar_empleado import insertar
from app_crud.borrar_empleado import borrar
from app_crud.consultar_empleado import seleccionar
from app_crud.actualizar_empleado import actualizar
from app_crud.mostrar_empleados import mostrar_todos_los_empleados
from extras.funciones_aux import centrar_pantalla


main = tk.Tk()

# ----------------------------------------------------------------------------
#                                   VARIABLES
# ----------------------------------------------------------------------------

var_nombre = tk.StringVar()
var_apellido = tk.StringVar()
var_direccion = tk.StringVar()
var_dni = tk.IntVar()
var_telefono = tk.IntVar()
var_id = tk.StringVar()

# ----------------------------------------------------------------------------
#                              PATRON PARA REGEX
# ----------------------------------------------------------------------------

patron_numerico = "[0-9]"

# ----------------------------------------------------------------------------
#                              CREAR BASE DE DATOS
# ----------------------------------------------------------------------------

conexion = crear_base()

# ----------------------------------------------------------------------------
#                                 CREAR TABLA
# ----------------------------------------------------------------------------

crear_tabla(conexion)

# ----------------------------------------------------------------------------
#                               MENU DESPLEGABLE
# ----------------------------------------------------------------------------


def color(ventana):
    color_elegido = askcolor(color="#00ff00", title="Cambiar fondo")
    ventana.configure(bg=color_elegido[1])


def menu_desplegable(ventana):
    menubar = tk.Menu(ventana)

    menu_formato = tk.Menu(menubar, tearoff=0)
    menu_formato.add_command(
        label="Cambiar color de fondo", command=lambda: color(ventana)
    )
    menu_formato.add_separator()
    menu_formato.add_command(label="Salir", command=ventana.quit)
    menubar.add_cascade(label="Formato", menu=menu_formato)

    ventana.config(menu=menubar)


# ----------------------------------------------------------------------------
#                                  BOTONES
# ----------------------------------------------------------------------------

# Funcion global porque hay 4 botones que hacen lo mismo
def volver_al_menu(ventana):
    if askyesno("Menú principal", "¿Seguro quiere volver al menú principal?"):
        # Recibo el main global debido a que no lo quiero local de esa funcion,
        # quiero modificar el main posta.
        global main
        ventana.withdraw()
        ventana.resizable(False, False)
        main = tk.Toplevel()
        menu_principal()
        menu_desplegable(main)


"""""" """""" """""" """""" """""" """""" """""" """""" """
                    ALTA EMPLEADO
""" """""" """""" """""" """""" """""" """""" """""" """"""


def dar_alta_empleado():
    # El mensaje withdraw() cierra la ventana principal
    main.withdraw()
    ventana = tk.Toplevel()
    menu_desplegable(ventana)
    centrar_pantalla(ventana)

    ingresar_datos = tk.Label(
        ventana,
        text="Ingrese los datos del nuevo empleado",
    )
    ingresar_datos.grid(row=0, column=1, pady=50)

    nombre = tk.Label(ventana, text="Nombre")
    nombre.grid(row=1, column=1, padx=150, pady=5, sticky=W)
    entry_nombre = tk.Entry(ventana, textvariable=var_nombre)
    entry_nombre.grid(row=1, column=2)

    apellido = tk.Label(ventana, text="Apellido")
    apellido.grid(row=2, column=1, padx=150, pady=5, sticky=W)
    entry_apellido = tk.Entry(ventana, textvariable=var_apellido)
    entry_apellido.grid(row=2, column=2)

    direccion = tk.Label(ventana, text="Dirección")
    direccion.grid(row=3, column=1, padx=150, pady=5, sticky=W)
    entry_direccion = tk.Entry(ventana, textvariable=var_direccion)
    entry_direccion.grid(row=3, column=2)

    dni = tk.Label(ventana, text="DNI")
    dni.grid(row=4, column=1, padx=150, pady=5, sticky=W)
    entry_dni = tk.Entry(ventana, textvariable=var_dni)
    entry_dni.grid(row=4, column=2)

    telefono = tk.Label(ventana, text="Teléfono")
    telefono.grid(row=5, column=1, padx=150, pady=5, sticky=W)
    entry_telefono = tk.Entry(ventana, textvariable=var_telefono)
    entry_telefono.grid(row=5, column=2)

    def alta_empleado():
        global conexion
        if askyesno("Alta empleado", "¿Seguro quiere dar de alta este empleado?"):
            if insertar(
                conexion,
                var_nombre.get(),
                var_apellido.get(),
                var_direccion.get(),
                var_dni.get(),
                var_telefono.get(),
            ):
                showinfo("Alta empleado", "El empleado se dio de alta")
            else:
                showwarning("Alta empleado", "Ya está registrado ese DNI")

    boton_salir = tk.Button(
        ventana, text="Salir", command=lambda: volver_al_menu(ventana)
    )
    boton_salir.grid(row=6, column=1, pady=30)

    boton_insertar_empleado = tk.Button(
        ventana, text="Registrar empleado", command=alta_empleado
    )
    boton_insertar_empleado.grid(row=6, column=2, pady=30)


"""""" """""" """""" """""" """""" """""" """""" """""" """
                    BAJA EMPLEADO
""" """""" """""" """""" """""" """""" """""" """""" """"""


def dar_baja_empleado():
    main.withdraw()
    ventana2 = tk.Toplevel()
    menu_desplegable(ventana2)
    centrar_pantalla(ventana2)

    ingresar_id_baja = tk.Label(
        ventana2, text="Ingrese el ID del empleado a dar de baja"
    )
    ingresar_id_baja.grid(row=0, column=1, padx=100, pady=150)
    entry_ingresar_id_baja = tk.Entry(ventana2, textvariable=var_id)
    entry_ingresar_id_baja.grid(row=0, column=2)

    def baja_empleado():
        global conexion
        if not re.match(patron_numerico, var_id.get()):
            showerror("Baja empleado", "Por favor ingrese un número")
        else:
            if askyesno("Baja empleado", "¿Seguro quiere dar de baja este empleado?"):
                if borrar(conexion, var_id.get()):
                    showinfo("Baja empleado", "El empleado se dio de baja")
                else:
                    showwarning(
                        "Baja empleado",
                        "No existe un empleado con ese ID",
                    )

    boton_salir2 = tk.Button(
        ventana2, text="Salir", command=lambda: volver_al_menu(ventana2)
    )
    boton_salir2.grid(row=1, column=1)

    boton_borrar_empleado = tk.Button(
        ventana2, text="Eliminar empleado", command=baja_empleado
    )
    boton_borrar_empleado.grid(row=1, column=2)


"""""" """""" """""" """""" """""" """""" """""" """""" """
                MODIFICAR EMPLEADO
""" """""" """""" """""" """""" """""" """""" """""" """"""


def modificar_empleado():
    main.withdraw()
    ventana3 = tk.Toplevel()
    menu_desplegable(ventana3)
    centrar_pantalla(ventana3)

    def busqueda_empleado():
        global conexion

        if not re.match(patron_numerico, var_id.get()):
            showerror("Modificación empleado", "Por favor ingrese un número")
        elif not seleccionar(conexion, var_id.get(), main):
            showwarning("Modificación empleado", "No hay un empleado con ese ID")
        else:
            nonlocal ventana3
            ventana3.withdraw()
            ventana4 = tk.Toplevel()
            centrar_pantalla(ventana4)

            ingresar_datos = tk.Label(
                ventana4, text="Ingrese los datos del empleado a modificar"
            )
            ingresar_datos.grid(row=0, column=1, pady=50)

            nombre = tk.Label(ventana4, text="Nombre")
            nombre.grid(row=2, column=1, padx=150, pady=5, sticky=W)
            entry_nombre = tk.Entry(ventana4, textvariable=var_nombre)
            entry_nombre.grid(row=2, column=2)

            apellido = tk.Label(ventana4, text="Apellido")
            apellido.grid(row=3, column=1, padx=150, pady=5, sticky=W)
            entry_apellido = tk.Entry(ventana4, textvariable=var_apellido)
            entry_apellido.grid(row=3, column=2)

            direccion = tk.Label(ventana4, text="Direccion")
            direccion.grid(row=4, column=1, padx=150, pady=5, sticky=W)
            entry_direccion = tk.Entry(ventana4, textvariable=var_direccion)
            entry_direccion.grid(row=4, column=2)

            dni = tk.Label(ventana4, text="DNI")
            dni.grid(row=5, column=1, padx=150, pady=5, sticky=W)
            entry_dni = tk.Entry(ventana4, textvariable=var_dni)
            entry_dni.grid(row=5, column=2)

            telefono = tk.Label(ventana4, text="Teléfono")
            telefono.grid(row=6, column=1, padx=150, pady=5, sticky=W)
            entry_telefono = tk.Entry(ventana4, textvariable=var_telefono)
            entry_telefono.grid(row=6, column=2)

            def editar_empleado():
                global conexion
                if askyesno(
                    "Modificación empleado",
                    "¿Seguro quiere modificar este empleado?",
                ):
                    if actualizar(
                        conexion,
                        var_id.get(),
                        var_nombre.get(),
                        var_apellido.get(),
                        var_direccion.get(),
                        var_dni.get(),
                        var_telefono.get(),
                    ):
                        showinfo(
                            "Modificación empleado",
                            "El empleado se modificó correctamente",
                        )

            boton_salir4 = tk.Button(
                ventana4, text="Salir", command=lambda: volver_al_menu(ventana4)
            )
            boton_salir4.grid(row=7, column=1, pady=30)

            boton_modificacion_empleado = tk.Button(
                ventana4, text="Editar empleado", command=editar_empleado
            )
            boton_modificacion_empleado.grid(row=7, column=2, pady=30)

    ingresar_id_modificacion = tk.Label(
        ventana3, text="Ingrese el ID del empleado a modificar"
    )
    ingresar_id_modificacion.grid(row=0, column=0, padx=100, pady=150)

    entry_ingresar_id_modificacion = tk.Entry(ventana3, textvariable=var_id)
    entry_ingresar_id_modificacion.grid(row=0, column=1)

    boton_salir3 = tk.Button(
        ventana3, text="Salir", command=lambda: volver_al_menu(ventana3)
    )
    boton_salir3.grid(row=3, column=0)

    boton_modificar_empleado = tk.Button(
        ventana3, text="Buscar empleado", command=busqueda_empleado
    )
    boton_modificar_empleado.grid(row=3, column=1)


"""""" """""" """""" """""" """""" """""" """""" """""" """
                CONSULTAR EMPLEADO
""" """""" """""" """""" """""" """""" """""" """""" """"""


def consultar_empleado():
    main.withdraw()
    ventana5 = tk.Toplevel()
    menu_desplegable(ventana5)
    centrar_pantalla(ventana5)

    ingresar_id_consulta = tk.Label(
        ventana5, text="Ingrese el ID del empleado a consultar"
    )
    ingresar_id_consulta.grid(row=0, column=0)

    entry_ingresar_id_consulta = tk.Entry(ventana5, textvariable=var_id)
    entry_ingresar_id_consulta.grid(row=0, column=1)

    def consultar_empleado():
        global conexion
        nonlocal ventana5

        if not re.match(patron_numerico, var_id.get()):
            showerror("Consulta empleado", "Por favor ingrese un número")
        elif not seleccionar(conexion, var_id.get(), ventana5):
            showwarning(
                "Consulta empleado",
                "No existe un empleado con ese ID",
            )

    boton_salir5 = tk.Button(
        ventana5, text="Salir", command=lambda: volver_al_menu(ventana5)
    )
    boton_salir5.grid(row=1, column=0)

    boton_consulta_empleado = tk.Button(
        ventana5, text="Mostrar empleado", command=consultar_empleado
    )
    boton_consulta_empleado.grid(row=1, column=1)


"""""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """
                MOSTRAR TODOS LOS EMPLEADOS
""" """""" """""" """""" """""" """""" """""" """""" """""" """""" """"""


def mostrar_empleados():
    mostrar_todos_los_empleados(conexion, main)


# ----------------------------------------------------------------------------
#                               MENU PRINCIPAL
# ----------------------------------------------------------------------------
def menu_principal():
    main.title("DG S.A.")
    bienvenida = tk.Label(
        main,
        text="Bienvenido/a al servicio de administración de empleados de DG SA"
        "\n\nSeleccione la opción que quiera realizar\n",
    )
    main.resizable(False, False)
    centrar_pantalla(main)
    bienvenida.grid(row=0, column=2)

    boton_alta_empleado = tk.Button(
        main, text="Dar de alta empleado", command=dar_alta_empleado
    )
    boton_alta_empleado.grid(row=1, column=1)

    boton_baja_empleado = tk.Button(
        main, text="Dar de baja empleado", command=dar_baja_empleado
    )
    boton_baja_empleado.grid(row=1, column=4)

    boton_modificar_empleado = tk.Button(
        main, text="Modificar empleado", command=modificar_empleado
    )
    boton_modificar_empleado.grid(row=3, column=4)

    boton_mostrar_empleados = tk.Button(
        main, text="Mostrar todos los empleados", command=mostrar_empleados
    )
    boton_mostrar_empleados.grid(row=2, column=2, columnspan=2)

    boton_consultar_empleado = tk.Button(
        main, text="Consultar empleado", command=consultar_empleado
    )
    boton_consultar_empleado.grid(row=3, column=1)


menu_principal()
menu_desplegable(main)

main.mainloop()
