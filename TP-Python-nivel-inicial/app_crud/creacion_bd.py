import sqlite3


def crear_base():

    conexion = sqlite3.connect("DG_SA.db")
    return conexion
