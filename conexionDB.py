import mysql.connector as mysql
from mysql.connector import Error 

class Manejo_datos():
    try:
        def __init__(self):
            self.conexion = mysql.Connect( host='localhost',
                                            database ='asadero', 
                                            user = 'root',
                                            password ='12345')

            if self.conexion.is_connected():
                print('Conexion exitosa')

        def insertar_producto(self, nombre, precio, cantidad):
            cursor = self.conexion.cursor()
            sql='''insert into inventario (nombre_producto, precio_producto, cantidad) 
            values ('{}', '{}','{}')'''.format(nombre, precio, cantidad)
            cursor.execute(sql)
            self.conexion.commit() 
            print('Registro insertado con éxito')   
            cursor.close()

        def listar_productos(self):
            cursor = self.conexion.cursor()
            sql = "select * from inventario" 
            cursor.execute(sql)
            registro = cursor.fetchall()
            # print(registro)
            for row in registro:
                print(row)
            return registro
            
        def buscar_producto(self, id_producto):
            cursor = self.conexion.cursor()
            sql = "select * from inventario where id_producto = '{}'".format(id_producto)
            cursor.execute(sql)
            productox = cursor.fetchall()
            cursor.close()
            print(productox)    
            return productox
        
        def eliminar_producto(self,id):
            cursor = self.conexion.cursor()
            sql = "delete from inventario where id_producto = '{}'".format(id)
            cursor.execute(sql)
            nom = cursor.rowcount
            self.conexion.commit()    
            cursor.close()
            print('Registro eliminado')
            return nom 

        def actualizar_producto(self, nombre, precio, cantidad, id):
            cursor = self.conexion.cursor()
            sql = '''update inventario set nombre_producto = %s, precio_producto = %s, cantidad = %s 
                where id_producto = %s'''
            values = (nombre, precio, cantidad, id)
            cursor.execute(sql, values)
            act = cursor.rowcount
            self.conexion.commit()    
            cursor.close()
            print('Producto actualizado' if act else 'No se actualizó ningun registro')
            return act

    except Error as er:
        print('Error durante la conexion:', er)