import sqlite3
from tkinter import ttk
from tkinter import *


def armar_tree_view(conexion, ventana, rows):
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
    tree.heading("col3", text="Dirección", anchor=CENTER)
    tree.heading("col4", text="DNI", anchor=CENTER)
    tree.heading("col5", text="Teléfono", anchor=CENTER)

    tree.grid(column=0, row=4, columnspan=5, rowspan=2)

    for row in rows:
        tree.insert(
            "", END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5])
        )


def existe_empleado(conexion, dato, query):
    cursor = conexion.cursor()
    dato = int(dato)
    data = (dato,)
    sql = query
    cursor.execute(sql, data)
    return cursor.fetchall()


def centrar_pantalla(ventana):

    ancho_ventana = 700
    alto_ventana = 400

    x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2

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
    ventana.resizable(False, False)
