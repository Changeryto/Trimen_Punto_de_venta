import tkinter as tk
from cfnt import cfnt
from producto import Producto
from producto_dao import ProductoDao
import os

class Guardar():
    def __init__(self, master, row, col, codigo, descripcion, unidad, precio):
        self.master = master
        self.row = row
        self.col = col,
        self.codigo = codigo
        self.descripcion = descripcion
        self.unidad = unidad
        self.precio = precio
        
        self.boton_guardar = tk.Button(self.master,
                            text='Guardar producto',
                            font=cfnt,
                            command=self.guardar,
                            bg='#F7A072')
        
        self.boton_guardar.grid(row=self.row,
                                column=self.col)
        
        self.estado = tk.Label(self.master, text='', font=cfnt)
        self.estado.grid(column=self.col, row=self.row+1, columnspan=1)
        
        self.boton_apagar = tk.Button(self.master, text='Apagar equipo', font=cfnt,
                                      command=self.apagar,
                                      bg='#EE2E31',
                                      fg='white')
    
        self.boton_apagar.grid(column=1, row=8, sticky='NE')
        
    def guardar(self):
        try:
            prod = Producto(prod_codigo=int(self.codigo.get()),
                            prod_descripcion=str(self.descripcion.get().upper()),
                            prod_precio=("{:.2f}".format(float(self.precio.get()))),
                            prod_unidad=str(self.unidad.get()))
            ProductoDao.insertar(prod)
            self.estado.config(text=f'\nGuardado correctamente: \n{prod.codigo} \n{prod.descripcion} \n{prod.prod_unidad} \n${prod.precio}',
                               fg='green')
            self.codigo.set('')
            self.descripcion.set('')
            self.precio.set('')
            self.unidad.set('PZ')
        except Exception as ex:
            print(ex)
            self.estado.config(text='\nHubo un error al guardar el \nproducto, corrija y reintente',
                               fg='red')
        
    def apagar(self):
        os.system("shutdown /s /t 1")
        