import pymysql

class BD:
    host = "127.0.0.1"
    port = 3307
    user = "root"
    passwd = "luisnunura123456"
    charset = "utf8mb4"
    tipo_obtencion = pymysql.cursors.DictCursor
    def __init__(self) -> None:
        self.base_datos = "cinestar"
    try:
        def get_connection(self):
            connection = pymysql.connect(host = self.host,
                                        port = self.port,
                                        user = self.user,
                                        passwd = self.passwd,
                                        db = self.base_datos,
                                        charset= self.charset,
                                        cursorclass= self.tipo_obtencion)
            return connection                
    except:
        print("Error en conexion")

    def sentencia(self,query):
        connection = BD.get_connection(self)
        data = []
        with connection.cursor() as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
            if data != None:
                return data
            else:
                return None
    def sentencia_unica(self,query):
        connection = BD.get_connection(self)
        data = []
        with connection.cursor() as cursor:
            cursor.execute(query)
            data = cursor.fetchone()
            if data != None:
                return data
            else:
                return None
