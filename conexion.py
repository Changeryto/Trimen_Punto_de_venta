from logger_base import logger
from producto import Producto
from psycopg2 import pool
import sys

class Conexion:
    __DATABASE = 'Trimen'
    __USERNAME = 'postgres'
    __PASSWORD = 'admin'
    __DB_PORT = '5432'
    __HOST = '127.0.0.1'
    __MIN_CON = 1
    __MAX_CON = 5
    __pool = None
    
    
    @classmethod
    def obtenerPool(cls):
        if cls.__pool is None:
            try:
                cls.__pool = pool.SimpleConnectionPool(
                    cls.__MIN_CON,
                    cls.__MAX_CON,
                    host=cls.__HOST,
                    user=cls.__USERNAME,
                    password=cls.__PASSWORD,
                    port=cls.__DB_PORT,
                    database=cls.__DATABASE
                )
                logger.debug(f'Creación pool exitosa: {cls.__pool}')
                return cls.__pool
            except Exception as ex:
                logger.error(f'Error al crear el pool de conexiones: {ex}')
                sys.exit()
        else:
            return cls.__pool
                
    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        logger.debug(f'Conexión obtenida del pool: {conexion}')
        return conexion
    
    @classmethod
    def liberarConexion(cls, conexion):
        cls.obtenerPool().putconn(conexion)
        logger.debug(f'Regresamos la conexión al pool: {conexion}')
        logger.debug(f'Estado del pool: {cls.__pool}')
        
    @classmethod
    def cerrarConexiones(cls):
        cls.obtenerPool().closeall()
        logger.debug(f'Cerramos todas las conexiones del pool: {cls.__pool}')
                
                
if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    conexion2 = Conexion.obtenerConexion()
    
    Conexion.liberarConexion(conexion1)
    Conexion.liberarConexion(conexion2)
    
    Conexion.cerrarConexiones()
                