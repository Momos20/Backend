import functools
import db
import pymysql

#Cuando ya se tiene la conexion, le decimos a la conexion que cree un cursor 
#Es la representacion de la base de datos en si misma, con este cursor tenemos acceso a los datos

def get_cliente():
    con = db.get_connection()
    cursor = con.cursor(pymysql.cursors.DictCursor)
    try:
        sql="SELECT * FROM cliente" #Esto es lo que puede cambiar porque es lo que hace la consulta
        cursor.execute(sql)
        ret = cursor.fetchall()
        print(ret)
        return ret
    finally:
        con.close() #Se debe de cerrar la conexion
        #Ret = es donde se retorna la informacion en forma de tuplas , luego se cierra la conexion

def get_client(client_id):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM cliente WHERE id = {}".format(client_id)
        cursor.execute(sql)
        ret = cursor.fetchone()
        return ret
    finally:
        con.close()

def get_client_by_name(client_name):
    con = db.get_connection() 
    cursor = con.cursor(pymysql.cursors.DictCursor)
    ret={}
    try:
        sql="SELECT * FROM cliente WHERE name = '{}'".format(client_name)
        print(sql)
        cursor.execute(sql) #Se hace una ejecucion en el cursor
        ret = cursor.fetchone() #Se hace un fechone del cursor
        return ret
    finally:
        con.close()

def create_client(name, Contact,Direccion,Email):
    con = db.get_connection() #conexion
    cursor = con.cursor() #cursor
    try:
        sql="INSERT INTO cliente(name, Contact,Direccion,Email) VALUES('{}','{}','{}','{}')".format(name, Contact,Direccion,Email)
        #los campos se deben de hacer en orden (PILAS CON EL ORDEN)
        print(sql)
        cursor.execute(sql)
        con.commit() #Se hace un commit, que es una confirmacion, lo que significa que en realidad se inserto el dato
        #Este commit lo hace la conexion "CON"
        id_org = cursor.lastrowid #Se obtiene el id de lo ultimo que se inserto
        return {"message":"OK", "id": id_org}
    finally:
        con.close()

def update_client(name, Contact,Direccion,Email, client_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="UPDATE cliente set name='{0}', Contact='{1}', Direccion='{2}',Email='{3}'  WHERE id = {4}".format(name, Contact, Direccion, Email,client_id)
        print(sql)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()

def delete_client(client_id):
    con = db.get_connection()
    cursor = con.cursor()
    try:
        sql="DELETE FROM cliente WHERE id = {}".format(client_id)
        cursor.execute(sql)
        con.commit()
        return {"message":"OK"}
    finally:
        con.close()
