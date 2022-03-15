import sqlite3
from extras.funciones_aux import existe_empleado


def borrar(conexion, mi_id):
    resultado_query = existe_empleado(
        conexion, mi_id, "SELECT * FROM empleados WHERE id = ?;"
    )

    if len(resultado_query) != 0:
        cursor = conexion.cursor()
        data = (mi_id,)
        sql = "DELETE from empleados where id = ?;"
        cursor.execute(sql, data)
        conexion.commit()
        return True
    else:
        return False
