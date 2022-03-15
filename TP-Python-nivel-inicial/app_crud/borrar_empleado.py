import sqlite3
from app_crud.funciones_aux import existe_empleado


def borrar(conexion, mi_id):
    resultado_query = existe_empleado(
        conexion, mi_id, "SELECT * FROM empleados WHERE id = ?;"
    )

    if resultado_query is not None:
        sql = "DELETE from empleados where id = ?;"
        cursor.execute(sql, data)
        conexion.commit()
        return True
    else:
        return False
