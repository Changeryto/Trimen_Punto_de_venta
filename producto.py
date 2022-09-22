
from logger_base import logger

class Producto:
    def __init__(self, prod_id=None, prod_descripcion=None, prod_unidad=None, prod_precio=None, prod_codigo=None):
        self.prod_id = prod_id
        self.prod_descripcion = prod_descripcion
        self.prod_unidad = prod_unidad
        self.prod_precio = prod_precio
        self.prod_codigo = prod_codigo
        
    def __str__(self):
        return (
            f'{self.prod_id},'
            f'{self.prod_descripcion},'
            f'{self.prod_unidad},'
            f'{self.prod_precio},'
            f'{self.prod_codigo}'
        )
    
    @property
    def id(self):
        return self.prod_id
    
    @property
    def descripcion(self):
        return self.prod_descripcion
    
    @property
    def unidad(self):
        return self.prod_unidad
    
    @property
    def precio(self):
        return self.prod_precio
    
    @property
    def codigo(self):
        return self.prod_codigo
    
    
