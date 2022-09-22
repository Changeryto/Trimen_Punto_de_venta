
from tkinter import Button
cfnt = ('Consolas', 20)

#def insertar(chara):
    #ent_sv.set(ent_sv.get + chara)
    

class Letra:
    """Esta clase añade un botón con una letra a seleccionar"""
    def __init__(self, master, chara, row, col, sv):
        self.master = master
        self.chara = chara
        self.row = row
        self.col = col
        self.sv = sv
        
        self.button = Button(self.master, text=self.chara,
                             font=cfnt,
                             bg='#61db48',
                             #fg='#ffffff',
                            command=self.insertar
                            )
        
        self.button.grid(row=self.row, column=self.col, padx=2, ipady=0, pady=2)
        
    
    def insertar(self):
        self.sv.set(self.sv.get() + self.chara)

    
    
