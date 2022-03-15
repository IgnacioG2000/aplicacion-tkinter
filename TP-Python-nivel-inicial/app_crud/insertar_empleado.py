import sqlite3


def insertar(conexion, nombre, apellido, direccion, dni, telefono):
    cursor = conexion.cursor()
    data = (dni,)
    sql_id = "SELECT COUNT(*) FROM empleados WHERE dni = ?;"
    cursor.execute(sql_id, data)
    resultado_query = cursor.fetchone()

    if resultado_query is not None:
        data_a_dar_alta = (nombre, apellido, direccion, dni, telefono)
        sql = "INSERT INTO empleados(nombre, apellido, direccion, dni, telefono) \
            VALUES(?, ?, ?, ?, ?)"
        cursor.execute(sql, data_a_dar_alta)
        conexion.commit()
        return True
    else:
        return False
