import sqlite3


def borrar(conexion, mi_id):
    cursor = conexion.cursor()
    mi_id = int(mi_id)
    data = (mi_id,)
    sql_id = "SELECT * FROM empleados WHERE id = ?;"
    cursor.execute(sql_id, data)
    resultado_query = cursor.fetchone()

    if resultado_query is not None:
        sql = "DELETE from empleados where id = ?;"
        cursor.execute(sql, data)
        conexion.commit()
        return True
    else:
        return False
