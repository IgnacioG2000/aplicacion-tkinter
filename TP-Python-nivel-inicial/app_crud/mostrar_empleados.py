from tkinter.messagebox import showwarning
from extras.funciones_aux import armar_tree_view


def mostrar_todos_los_empleados(conexion, ventana):
    cursor = conexion.cursor()
    sql = "SELECT * FROM empleados;"
    cursor.execute(sql)
    rows = cursor.fetchall()

    if len(rows) != 0:
        armar_tree_view(conexion, ventana, rows)
    else:
        showwarning("Mostrar empleados", "No hay ningún empleado dado de alta")
