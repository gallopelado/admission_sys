import psycopg2, yaml
from flask import current_app as app

class ConexionDb:

    def __getPropiedades(self):
        properties = app.config['APPLICATION_PROPERTIES']
        with open(properties) as file:
            properties = yaml.load(file, Loader=yaml.FullLoader)
            return properties

    def __init__(self):
        """Método constructor de la clase Conexion.

        Mediante el método connect se obtiene una instancia de la
        conexion a la base de datos.

        """
        properties = self.__getPropiedades()
        dbname = properties['dbname']
        user = properties['user']
        host = properties['host']
        port = properties['port']
        password = properties['password']
        self.con = psycopg2.connect(f"dbname={dbname} user={user} host={host} password={password} port={port}")