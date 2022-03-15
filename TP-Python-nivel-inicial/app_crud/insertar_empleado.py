import sqlite3


def insertar(conexion, nombre, apellido, direccion, dni, telefono):
    resultado_query = existe_empleado(
        conexion, dni, "SELECT * FROM empleados WHERE dni = ?;"
    )

    if resultado_query is not None:
        data_a_dar_alta = (nombre, apellido, direccion, dni, telefono)
        sql = "INSERT INTO empleados(nombre, apellido, direccion, dni, telefono) \
            VALUES(?, ?, ?, ?, ?)"
        cursor.execute(sql, data_a_dar_alta)
        conexion.commit()
        return True
    else:
        return False
