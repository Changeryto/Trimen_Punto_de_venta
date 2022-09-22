from conexion import Conexion
from logger_base import logger

class CursorDelPool:
    def __init__(self) -> None:
        self.__conn = None
        self.__cursor = None
        
    def __enter__(self):
        logger.debug('Inicio del método __enter__')
        self.__conn = Conexion.obtenerConexion()
        self.__cursor = self.__conn.cursor()
        return self.__cursor
    
    def __exit__(self, exeption_type, exception_value, exception_traceback):
        logger.debug('Se ejecuta método __exit__()')
        
        if exception_value:
            self.__conn.rollback()
            logger.debug(f'Ocurrió una excepción: {exception_value}')
        else:
            
            self.__conn.commit()
            logger.debug('Commit de la transacción')
            
        self.__cursor.close()
        Conexion.liberarConexion(self.__conn)
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    #Obtenemos un cursor a partir de la conexión del pool
    #with se ejecuta primero el método __enter__ y termina con __exit__
    with CursorDelPool() as cursor:
        cursor.execute('SELECT * FROM productos')
        logger.debug('Listado de productos')
        logger.debug(cursor.fetchall()) 
            