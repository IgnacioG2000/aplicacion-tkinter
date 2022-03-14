import sqlite3


def insertar(conexion, nombre, apellido, direccion, dni, telefono):
    cursor = conexion.cursor()
    dni = int(dni)
    data = (dni,)
    sql_id = "SELECT COUNT(*) FROM empleados WHERE dni = ?;"
    cursor.execute(sql_id, data)
    rows = cursor.fetchall()

    for row in rows:
        if row[0] == 0:
            data = (nombre, apellido, direccion, dni, telefono)
            sql = "INSERT INTO empleados(nombre, apellido, direccion, dni, telefono) \
            VALUES(?, ?, ?, ?, ?)"
            cursor.execute(sql, data)
            conexion.commit()
            return True
        else:
            return False
