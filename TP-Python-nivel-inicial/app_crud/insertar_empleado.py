import sqlite3


def insertar(conexion, nombre, apellido, direccion, dni, telefono):
    cursor = conexion.cursor()
    data = (nombre, apellido, direccion, dni, telefono)
    sql = "INSERT INTO empleados(nombre, apellido, direccion, dni, telefono) \
        VALUES(?, ?, ?, ?, ?)"
    cursor.execute(sql, data)
    conexion.commit()
