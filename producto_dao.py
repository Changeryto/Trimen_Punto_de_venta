
from producto import Producto
from cursor_del_pool import CursorDelPool
from logger_base import logger

class ProductoDao:
    __SELECCIONAR = 'SELECT prod_id, prod_descripcion, prod_unidad, prod_precio, prod_codigo FROM productos WHERE prod_descripcion LIKE %s ORDER BY prod_descripcion LIMIT 40'
    __SELECCIONAR2 = 'SELECT prod_id, prod_descripcion, prod_unidad, prod_precio, prod_codigo FROM productos WHERE prod_codigo = %s ORDER BY prod_descripcion LIMIT 40'
    __INSERTAR = 'INSERT INTO productos(prod_descripcion, prod_unidad, prod_precio, prod_codigo, prod_id) VALUES (%s, %s, %s, %s, (SELECT max(prod_id)+1 FROM productos))'
    __ACTUALIZAR = 'UPDATE productos SET prod_descripcion=%s, prod_unidad=%s, prod_precio=%s, prod_codigo=%s WHERE prod_id=%s'
    __ACTUALIZAR_PRECIO = 'UPDATE productos SET prod_precio=%s WHERE prod_id=%s'
    
    
    @classmethod
    def seleccionar(cls, query):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECCIONAR))
            cursor.execute(cls.__SELECCIONAR, (f'{query}%',)) 
            #cursor.execute(cls.__SELECCIONAR, (f'TUBO FLEXIBLE DESNUDO',)) 
            registros = cursor.fetchall()
            productos = []
            for registro in registros:
                producto = Producto(registro[0], registro[1], registro[2], registro[3], registro[4])
                productos.append(producto.__str__())
            return productos
        
    @classmethod
    def seleccionar2(cls, query):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECCIONAR2))
            cursor.execute(cls.__SELECCIONAR2, (query,)) 
            #cursor.execute(cls.__SELECCIONAR, (f'TUBO FLEXIBLE DESNUDO',)) 
            registros = cursor.fetchall()
            productos = []
            for registro in registros:
                producto = Producto(registro[0], registro[1], registro[2], registro[3], registro[4])
                productos.append(producto.__str__())
            return productos
        
    @classmethod
    def insertar(cls, producto):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Producto a insertar: {producto}')
            valores = (producto.descripcion, producto.unidad, producto.precio, producto.codigo)
            cursor.execute(cls.__INSERTAR, valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, producto):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Producto a actualizar: {producto}')
            valores = (producto.descripcion, producto.unidad, producto.precio, producto.codigo, producto.id)
            cursor.execute(cls.__ACTUALIZAR, valores)
            return cursor.rowcount
  
    @classmethod
    def actualizar_precio(cls, precio, id_):
        with CursorDelPool() as cursor:
            valores = (float(precio), int(id_))
            cursor.execute(cls.__ACTUALIZAR_PRECIO, valores)
            return cursor.rowcount
  
        

if __name__ == "__main__":
    prod = Producto(prod_codigo=12345,
                    prod_descripcion='Azada',
                    prod_precio=99.99,
                    prod_unidad='PZ')
    print(prod)
    print(prod.descripcion)
    
    ProductoDao.insertar(prod)
            