import sqlite3
from tkinter import ttk
from tkinter import *


def seleccionar(conexion, mi_id, ventana):
    cursor = conexion.cursor()
    mi_id = int(mi_id)
    data = (mi_id,)
    sql = "SELECT * FROM empleados WHERE id =?;"
    cursor.execute(sql, data)
    rows = cursor.fetchone()

    if rows is not None:
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
        return True
    else:
        return False
