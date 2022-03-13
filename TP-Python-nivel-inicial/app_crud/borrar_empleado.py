import sqlite3


def borrar(conexion, mi_id):
    cursor = conexion.cursor()
    mi_id = int(mi_id)
    data = (mi_id,)
    sql_id = "SELECT COUNT(*) FROM empleados WHERE id = ?;"
    cursor.execute(sql_id, data)
    rows = cursor.fetchall()

    for row in rows:
        if row[0] == 1:
            sql = "DELETE from empleados where id = ?;"
            cursor.execute(sql, data)
            conexion.commit()
            return True
        else:
            return False
