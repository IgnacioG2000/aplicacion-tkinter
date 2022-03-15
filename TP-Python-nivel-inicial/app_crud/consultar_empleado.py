import sqlite3
from funciones_aux import armar_tree_view, existe_empleado


def seleccionar(conexion, mi_id, ventana):
    resultado_query = existe_empleado(
        conexion, mi_id, "SELECT * FROM empleados WHERE id = ?;"
    )

    if resultado_query is not None:
        armar_tree_view(conexion, ventana)
        return True
    else:
        return False
