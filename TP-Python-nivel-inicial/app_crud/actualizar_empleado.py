import sqlite3


def actualizar(conexion, mi_id, nombre, apellido, direccion, dni, telefono):
    cursor = conexion.cursor()
    mi_id = int(mi_id)
    data = (nombre, apellido, direccion, dni, telefono, mi_id)
    sql = "UPDATE empleados SET nombre=?, apellido=?, direccion=?, dni=?, telefono=? WHERE id=?;"
    cursor.execute(sql, data)
    conexion.commit()
    return True
