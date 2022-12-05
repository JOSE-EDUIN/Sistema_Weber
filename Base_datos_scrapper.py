import mysql.connector
# from extraccion_dof import extraccion
class conexion_bd():
    '''
    Clase que establece la conexión a la Base de datos 
    '''
    def __init__(self):
        # extraction = extraccion()
        try:
            
            self.conexion=mysql.connector.connect(
                host='localhost',
                port='3306' ,
                user='root' ,
                db='scraper'
                )
                
            self.cursor = self.conexion.cursor()
        except mysql.connector.Error as e:
            print("No puedo conectar a la base de datos:",e)
        else:
            print("Conexion exitosa a BD")

    def close_connection(self):
        '''
        Función que  cierra la conexion a la bd
        '''
        # self.conexion.commit()
        self.conexion.close()
        
        print('Conexión a la base de datos cerrada exitosamente')
        # print("Proceso finalizado")
    
    
    def commit_connection(self):
        '''
        Función que envia los datos a la base de datos
        '''
        self.conexion.commit()


    