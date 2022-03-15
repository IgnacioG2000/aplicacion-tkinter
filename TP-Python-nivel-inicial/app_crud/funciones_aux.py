import sqlite3
from tkinter import ttk


def armar_tree_view(conexion, ventana):
    tree = ttk.Treeview(ventana)
    tree["columns"] = ("col1", "col2", "col3", "col4", "col5")
    tree.column("#0", width=30, minwidth=30, anchor=CENTER)
    tree.column("col1", width=100, minwidth=100, anchor=CENTER)
    tree.column("col2", width=100, minwidth=100, anchor=CENTER)
    tree.column("col3", width=150, minwidth=150, anchor=CENTER)
    tree.column("col4", width=100, minwidth=100, anchor=CENTER)
    tree.column("col5", width=100, minwidth=100, anchor=CENTER)

    tree.heading("#0", text="ID", anchor=CENTER)
    tree.heading("col1", text="Nombre", anchor=CENTER)
    tree.heading("col2", text="Apellido", anchor=CENTER)
    tree.heading("col3", text="Direccion", anchor=CENTER)
    tree.heading("col4", text="dni", anchor=CENTER)
    tree.heading("col5", text="Telefono", anchor=CENTER)

    tree.grid(column=1, row=4, columnspan=5)

    tree.insert(
        "", END, text=rows[0], values=(rows[1], rows[2], rows[3], rows[4], rows[5])
    )


def existe_empleado(conexion, mi_id):
    cursor = conexion.cursor()
    mi_id = int(mi_id)
    data = (mi_id,)
    sql_id = "SELECT * FROM empleados WHERE id = ?;"
    cursor.execute(sql_id, data)
    return cursor.fetchone()


############################ CENTRAR PANTALLA ######################################
def centrar_pantalla(ventana):

    ancho_ventana = 700
    alto_ventana = 300

    x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
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
    ventana.geometry(posicion)
