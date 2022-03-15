import sqlite3
from tkinter import ttk
from tkinter import *
from app_crud.funciones_aux import centrar_pantalla, armar_tree_view


def mostrar_todos_los_empleados(conexion, ventana):
    cursor = conexion.cursor()
    sql = "SELECT * FROM empleados;"
    cursor.execute(sql)
    rows = cursor.fetchall()

    centrar_pantalla(ventana)
    armar_tree_view(conexion, ventana, rows)
