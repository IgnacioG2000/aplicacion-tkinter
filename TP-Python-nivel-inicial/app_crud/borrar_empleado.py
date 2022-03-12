import sqlite3


def borrar(conexion, mi_id):
    cursor = conexion.cursor()
    mi_id = int(mi_id)
    data = (mi_id,)
    sql = "DELETE FROM empleados WHERE id = ?;"
    cursor.execute(sql, data)
    conexion.commit()
