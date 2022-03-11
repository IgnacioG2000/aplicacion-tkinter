from tkinter import *
from tkinter.messagebox import *


main = Tk()

main.title("DG S.A.")
main.geometry("420x500+50+70")

############################ MENSAJE DE BIENVENIDA ######################################

bienvenida = Label(
    main,
    text="Bienvenido/a al servicio de administración de empleados de DG S.A.\n\nSeleccione la opción que quiera realizar\n",
)
bienvenida.grid(row=0, column=1)


############################ BOTONES ######################################


def dar_alta_empleado():
    pass


def dar_baja_empleado():
    pass


def modificar_empleado():
    pass


def consultar_empleado():
    pass


boton_alta_empleado = Button(
    main, text="Dar de alta empleado", command=dar_alta_empleado
)
boton_alta_empleado.grid(row=1, column=0)

boton_baja_empleado = Button(
    main, text="Dar de baja empleado", command=dar_baja_empleado
)
boton_baja_empleado.grid(row=1, column=1)

boton_consultar_empleado = Button(
    main, text="Consultar empleado", command=consultar_empleado
)
boton_consultar_empleado.grid(row=3, column=0)

boton_modificar_empleado = Button(
    main, text="Modificar empleado", command=modificar_empleado
)
boton_modificar_empleado.grid(row=3, column=1)


############################ MENU ######################################


def color():
    pass


def tipografia():
    pass


menubar = Menu(main)

menu_formato = Menu(menubar, tearoff=0)
menu_formato.add_command(label="Editar color", command=color)
menu_formato.add_command(label="Editar tipografia", command=tipografia)
menu_formato.add_separator()
menu_formato.add_command(label="Salir", command=main.quit)
menubar.add_cascade(label="Formato", menu=menu_formato)

main.config(menu=menubar)

main.mainloop()
