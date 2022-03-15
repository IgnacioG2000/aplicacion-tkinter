import sqlite3
from app_crud.funciones_aux import armar_tree_view, existe_empleado


def seleccionar(conexion, mi_id, ventana):
    resultado_query = existe_empleado(
        conexion, mi_id, "SELECT * FROM empleados WHERE id = ?;"
    )

    if len(resultado_query) != 0:
        armar_tree_view(conexion, ventana, resultado_query)
        return True
    else:
        return False
