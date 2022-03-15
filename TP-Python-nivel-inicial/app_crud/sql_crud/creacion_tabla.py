import sqlite3


def crear_tabla(conexion):

    cursor = conexion.cursor()
    sql = "CREATE TABLE IF NOT EXISTS empleados(id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, \
         apellido TEXT, direccion TEXT, dni INTEGER, telefono INTEGER)"
    cursor.execute(sql)
    conexion.commit()
