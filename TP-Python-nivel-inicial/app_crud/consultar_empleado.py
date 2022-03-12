import sqlite3


def seleccionar(conexion, mi_id):
    cursor = conexion.cursor()
    mi_id = int(mi_id)
    data = (mi_id,)
    sql = "SELECT * FROM empleados WHERE id =?;"
    cursor.execute(sql, data)
    rows = cursor.fetchall()

    for row in rows:
        print(row)
