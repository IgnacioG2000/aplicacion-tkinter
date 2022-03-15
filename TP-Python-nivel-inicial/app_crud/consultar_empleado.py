import sqlite3
from tkinter import ttk
from tkinter import *
from funciones_aux import armar_tree_view, existe_empleado


def seleccionar(conexion, mi_id, ventana):
    resultado_query = existe_empleado(conexion, mi_id)

    if rows is not None:
        armar_tree_view(conexion, ventana)
        return True
    else:
        return False
