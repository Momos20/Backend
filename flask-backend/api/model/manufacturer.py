import functools
import db
import pymysql

def get_fabricante():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql = "SELECT * FROM fabricante"
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close()

def get_manufacturer(manufacturer_id):
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret = {}
    try:
        sql = "SELECT * FROM fabricante WHERE id = {}".format(manufacturer_id)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def get_manufacturer_by_name(manufacturer_name):
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret = {}
    try:
        sql = "SELECT * FROM fabricante WHERE Nombre_Empresa = '{}'".format(manufacturer_name)
        print(sql)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def create_manufacturer(Nombre_Empresa, Contacto, Direccion, Email, Calificacion):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql = "INSERT INTO fabricante (Nombre_Empresa, Contacto, Direccion, Email, Calificacion) VALUES ('{}', '{}', '{}', '{}', {})".format(Nombre_Empresa, Contacto, Direccion, Email, Calificacion)
        print(sql)
        cursor.execute(sql)
        con.commit()
        id_org = cursor.lastrowid
        return {"message": "OK", "id": id_org}
    finally:
        con.close()

def update_manufacturer(Nombre_Empresa, contacto, direccion, email, calificacion, manufacturer_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql = "UPDATE fabricante SET Nombre_Empresa = '{0}', Contacto = '{1}', Direccion = '{2}', Email = '{3}', Calificacion = {4} WHERE id = {5}".format(Nombre_Empresa, contacto, direccion, email, calificacion, manufacturer_id)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message": "OK"}
    finally:
        con.close()

def delete_manufacturer(manufacturer_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql = "DELETE FROM fabricante WHERE id = {}".format(manufacturer_id)
        cursor.execute(sql)
        con.commit()
        return {"message": "OK"}
    finally:
        con.close()