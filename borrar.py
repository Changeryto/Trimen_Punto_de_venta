from doctest import master
from tkinter import Button
from cfnt import cfnt


def borrar(sv):
    sv.set('')
    
class Borrar:
    
    def __init__(self, master, row, col, sv):
        self.master = master
        self.row = row
        self.col = col
        self.sv = sv
        
        self.boton = Button(
            self.master,
            text='Borrar',
            font=cfnt,
            bg='#BC4749', 
            command=self.borrar,
            fg='#ffffff'
        )
        self.boton.grid(row=self.row, column=self.col, sticky='W')
        
    def borrar(self):
        self.sv.set('')