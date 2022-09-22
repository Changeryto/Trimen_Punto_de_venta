import tkinter as tk
from cfnt import cfnt



class Calcular:
    def __init__(self, master, buscar):
        self.master = master
        self.buscar = buscar
        
        #self.boton_cal = tk.Button(self.master, text='Calcular', font=cfnt)
        #self.boton_cal.pack(side=tk.LEFT)
        
        self.lab_total = tk.Label(self.master, text='$2       ', bg='black', fg='white', font=('consolas', 40), width=20)
        self.lab_total.pack(side=tk.LEFT)
        self.lab_total.pack_propagate(False)
        
        self.boton_print = tk.Button(self.master, text='Imprimir', font=cfnt)
        self.boton_print.pack(side=tk.LEFT)
        
        
        
        
        
    
        
    