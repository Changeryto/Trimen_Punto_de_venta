import sys
import tkinter as tk
from tkinter import Button
from cfnt import cfnt
from producto_dao import ProductoDao
from cfnt import cfnt
from functools import partial
from logger_base import logger
from datetime import date, datetime

import os
import sys
import psutil

from validadores import producto



class Buscar:
    
    def __init__(self, master=None, row=None, col=None, sv=None, gradilla_resultados=None, up=None, canv1=None, gradilla_agregados=None, up2=None, canv2=None, master_inf=None):
        self.master = master
        self.row = row
        self.col = col
        self.sv = sv
        self.gradilla_resultados = gradilla_resultados
        self.up = up
        self.canv1 = canv1
        
        self.gradilla_agregados = gradilla_agregados
        self.up2 = up2
        self.canv2 = canv2
        
        self.master_inf =master_inf
        
        self.l_cantidades = []
        self.pasado = []
        self.boton = Button(
            self.master,
            text='Buscar',
            font=cfnt,
            bg='#0052cc', 
            command=self.consulta,
            fg='#ffffff'
        )
        
        self.boton.grid(row=self.row, column=self.col)
        

        
        self.lab_total = tk.Label(self.master_inf, text='$0.00', bg='black', fg='white', font=('consolas', 50), width=10)
        self.lab_total.pack(side=tk.LEFT, padx=20)
        self.lab_total.pack_propagate(False)
        
        self.boton_print = tk.Button(self.master_inf, text='Imprimir', font=cfnt, command=self.imprimir, bg='#EDDEA4')
        self.boton_print.pack(side=tk.LEFT, padx=5)
        
        self.boton_nt = tk.Button(self.master_inf, text='Nueva nota', font=cfnt, command=self.nueva_nota, bg='#F7A072')
        self.boton_nt.pack(side=tk.LEFT)
        
        self.boton_apagar = tk.Button(self.master_inf, text='Apagar equipo', font=cfnt, command=self.apagar, bg='#EE2E31', fg='white')
        self.boton_apagar.pack(side=tk.RIGHT, padx=200)
        
        
    def consulta(self):
        for widgets in self.gradilla_resultados.winfo_children():
            widgets.destroy()
        
        try:    
            resultados = ProductoDao.seleccionar2(self.sv.get())
            resultados += ProductoDao.seleccionar(self.sv.get().upper())
        except Exception as ex:
            resultados = ProductoDao.seleccionar(self.sv.get().upper())
        """
        #for i in range()
        for resultado in resultados:

            tk.Label(self.gradilla_resultados, text=str(resultado)).pack()
        """    
        for i in range(len(resultados)):
            partes = resultados[i].split(',')
            logger.debug((partes))
            exec(f'self.f{i} = tk.Frame(self.gradilla_resultados, bg=\"#83f2e2\")')
            
            exec(f'self.cod{i} = tk.Label(self.f{i}, text= \"{partes[4]}\",  font=cfnt, bg=\"#83f2e2\", width=6, anchor=\"w\")')
            exec(f'self.cod{i}.grid(row={i}, column={0}, sticky=\"W\", padx=1)')
            exec(f'self.cod{i}.grid_propagate(False)')
            
            exec(f'self.desc{i} = tk.Label(self.f{i}, text= \"{partes[1]}\", font=cfnt, bg=\"#83f2e2\", width=51, anchor=\"w\")')
            exec(f'self.desc{i}.grid(row={i}, column={1}, sticky=\"W\", padx=10)')
            exec(f'self.desc{i}.grid_propagate(False)')

            #exec(f'self.tamaño{i} = tk.Label(self.f{i}, text= \"{partes[3]}\", font=cfnt, bg=\"#83f2e2\")')
            #exec(f'self.tamaño{i}.grid(row={i}, column={2}, sticky=\"NSWE\", padx=10)')
            
            exec(f'self.unid{i} = tk.Label(self.f{i}, text= \"{partes[2]}\", font=cfnt, bg=\"#83f2e2\")')
            exec(f'self.unid{i}.grid(row={i}, column={3}, sticky=\"NSWE\", padx=10)')
            
            exec(f'self.precio{i} = tk.Label(self.f{i}, text= \"{partes[3]}\", font=cfnt, bg=\"#83f2e2\", width=7)')
            exec(f'self.precio{i}.grid(row={i}, column={4}, sticky=\"NSWE\", padx=10)')
            exec(f'self.precio{i}.grid_propagate(False)')

            
            exec(f'self.addb{i} = tk.Button(self.f{i}, text=\"Añadir\", font=cfnt, bg=\"#f2af4b\", command= partial(self.pasar, partes))')
            exec(f'self.addb{i}.grid(row={i}, column={5}, sticky=\"NSWE\", padx=10, pady=1)')

            
            exec(f'self.f{i}.pack()')
            
        self.up.update()
        self.canv1.config(scrollregion=self.canv1.bbox('all'))
        self.canv1.pack()
    

    
    
    
    def pasar(self, partes):
        if not partes in self.pasado:    
            self.pasado.append(partes)
            self.l_cantidades.append(1.0)
        logger.debug(self.pasado)
        self.desplegar()
        self.pago()
        
    def desplegar(self):    
        
        for widgets in self.gradilla_agregados.winfo_children():
            widgets.destroy()

    
        
        for i in range(len(self.pasado)):
            exec(f'self.g{i} = tk.Frame(self.gradilla_agregados, bg=\"#83f2e2\")')
            
            exec(f'self.cod2{i} = tk.Label(self.g{i}, text= \"{self.pasado[i][4]}\",  font=cfnt, bg=\"#83f2e2\", width=6, anchor=\"w\")')
            exec(f'self.cod2{i}.grid(row={i}, column={0}, sticky=\"W\", padx=1)')
            exec(f'self.cod2{i}.grid_propagate(False)')
            
            exec(f'self.desc2{i} = tk.Label(self.g{i}, text= \"{self.pasado[i][1]}\", font=cfnt, bg=\"#83f2e2\", width=51, anchor=\"w\")')
            exec(f'self.desc2{i}.grid(row={i}, column={1}, sticky=\"NSWE\", padx=10)')
            exec(f'self.desc2{i}.grid_propagate(False)')
            
            #exec(f'self.tamaño2{i} = tk.Label(self.g{i}, text= \"{self.pasado[i][3]}\", font=cfnt, bg=\"#83f2e2\")')
            #exec(f'self.tamaño2{i}.grid(row={i}, column={2}, sticky=\"NSWE\", padx=10)')
            
            exec(f'self.unid2{i} = tk.Label(self.g{i}, text= \"{self.pasado[i][2]}\", font=cfnt, bg=\"#83f2e2\")')
            exec(f'self.unid2{i}.grid(row={i}, column={3}, sticky=\"NSWE\", padx=10)')
            
            exec(f'self.precio2{i} = tk.Label(self.g{i}, text= \"{self.pasado[i][3]}\", font=cfnt, bg=\"#83f2e2\", width=7)')
            exec(f'self.precio2{i}.grid(row={i}, column={4}, sticky=\"NSWE\", padx=10)')
            
            exec(f'self.cont{i} = tk.Frame(self.g{i}, bg=\"#83f2e2\")')
            
            #exec(f'self.cantidad{i} = tk.Label(self.cont{i}, text=1, bg=\"#fff9eb\", font=cfnt)')
            exec(f'self.cantidad{i} = tk.Label(self.cont{i}, text= {"{:.1f}".format(self.l_cantidades[i])}, bg=\"#fff9eb\", font=cfnt, width=5)')
            
            exec(f'self.reducir{i} = tk.Button(self.cont{i}, text=\"-\", bg=\"#d390de\", font=cfnt, repeatdelay=220, repeatinterval=150, command= partial(self.reducir, self.cantidad{i}, {i}))')
            
            exec(f'self.reducir_dec{i} = tk.Button(self.cont{i}, text=\"-\", bg=\"#90a5de\", font=cfnt, repeatdelay=220, repeatinterval=150, command= partial(self.reducir_dec, self.cantidad{i}, {i}))')
            
            exec(f'self.reducir{i}.pack(side=tk.LEFT)')
            exec(f'self.reducir_dec{i}.pack(side=tk.LEFT)')
            exec(f'self.cantidad{i}.pack(side=tk.LEFT, fill=tk.BOTH)')
            exec(f'self.cantidad{i}.pack_propagate(False)')
            
            exec(f'self.aumentar_dec{i} = tk.Button(self.cont{i}, text=\"+\", bg=\"#90a5de\", font=cfnt, repeatdelay=220, repeatinterval=150, command= partial(self.aumentar_dec, self.cantidad{i}, {i}))')
            exec(f'self.aumentar_dec{i}.pack(side=tk.LEFT)')
            
            exec(f'self.aumentar{i} = tk.Button(self.cont{i}, text=\"+\", bg=\"#d390de\", font=cfnt, repeatdelay=220, repeatinterval=150, command= partial(self.aumentar, self.cantidad{i}, {i}))')
            exec(f'self.aumentar{i}.pack(side=tk.LEFT)')
            
            exec(f'self.quitar{i} = tk.Button(self.cont{i}, text=\"Quitar\", bg=\"#ffa1ce\", font=cfnt, command= partial(self.quitar, {self.pasado[i]}, {i}))')
            exec(f'self.quitar{i}.pack(side=tk.LEFT, padx=5, pady=1)')
            
            exec(f'self.cont{i}.grid(row={i}, column={5}, sticky=\"NSWE\", padx=55)')
            
            exec(f'self.g{i}.pack()')
            
        self.up2.update()
        self.canv2.config(scrollregion=self.canv2.bbox('all'))
    
    def reducir(self, cant, indice):
        if float(cant.cget("text")) > 1:
            cant.config(text= str(float(cant.cget("text"))-1))
            self.l_cantidades[indice] -= 1
            self.pago()
            
    def reducir_dec(self, cant, indice):
        if float(cant.cget("text")) > 0.1:
            cant.config(text= "{:.1f}".format(float(cant.cget("text"))-0.1))
            self.l_cantidades[indice] -= 0.1
            self.pago()
            
    def aumentar(self, cant, indice):
        cant.config(text= str(float(cant.cget("text"))+1.0))
        self.l_cantidades[indice] += 1.0
        self.pago()
        
    def aumentar_dec(self, cant, indice):
        cant.config(text= "{:.1f}".format(float(cant.cget("text"))+0.1))
        self.l_cantidades[indice] += 0.1
        self.pago()
        
    def quitar(self, eliminado, indice):
        self.pasado.remove(eliminado)
        self.l_cantidades.pop(indice)
        self.desplegar()
        self.pago()
        
    
    
    @property
    def precios(self):
        precios_l = []
        for prod in self.pasado:
            precios_l.append(float(prod[3][1:]))
        return precios_l
    
    @property
    def cantidades(self):
        cantidades_l = []
        for i in range(len(self.pasado)):
            exec(f'cantidades_l.append(float(self.cantidad{i}.cget(\"text\")))')
        return cantidades_l
    
    
    def set_pasado(self, nlista):
        self.pasado = nlista
    
    def pago(self):
        total = 0.00
        for i in range(len(self.precios)):
            print(self.precios)
            print(self.cantidades)
            total += self.precios[i] * self.cantidades[i]
            total = float("{:.2f}".format(total))
        self.lab_total.config(text=f'${"{:.2f}".format(total)}')
        
        
    def nueva_nota(self):
        try:
            p = psutil.Process(os.getpid())
            for handler in p.get_open_files() + p.connections():
                os.close(handler.fd)
        except Exception as ex:
            logger.debug(ex)
            
        python = sys.executable
        os.execl(python, python, *sys.argv)
        
        
    def imprimir(self):
        archivo = open('serie.txt', 'r')
        serie = int(archivo.readline())
        archivo.close()
        now = datetime.now()
        nota = open('nota.txt', 'w')
        nota.write(f'           TLAPALERIA  TRIMEN           \n'#17
                   f'                                        \n'
                   f'   DIAMANTE 45 LA JOYA IXTACALA 54160   \n'
                   f'  TLALNEPANTLA DE BAZ ESTADO DE MEXICO  \n'
                   f'              55 5391 2934              \n'
                   f'        {date.today()}      {now.hour}:{now.minute}  HRS        \n'
                   f'                                        \n'
        )
        nota.close()
        
        nota = open('nota.txt', 'a')
        nota.write(f'NOTA NUMERO: {serie}\n'
                   f'----------------------------------------\n'
                   f'DESCRIPCION          CANT PR.UN. IMPORTE\n'
                   f'----------------------------------------\n'
        )
        
        
        for i in range(len(self.pasado)):
            self.pasado[i][1] += '          '
            nota.write(f'{self.pasado[i][4]} {self.pasado[i][1][:14]}')#18
            self.pasado[i][1] = self.pasado[i][1][:-10]
            cant_proc = (10*' ') + "{:.1f}".format(self.l_cantidades[i])
            nota.write(f'{cant_proc[-5:]} ')
            prec_proc = (10*' ') + (self.pasado[i][3][1:])
            #prec_proc = prec_proc[-8:]
            nota.write(f'{prec_proc[-6:]} ')
            prec_import = (10*' ') + "{:.2f}".format(float(self.pasado[i][3][1:]) * float(self.l_cantidades[i]))
            #self.lab_total.cget('text')
            #"{:.1f}".format(prec_import)
            nota.write(f'{prec_import[-7:]}\n')
            
        nota.write('='*40 + '\n')
        
        total_print = 40*' ' + self.lab_total.cget('text')
        nota.write('TOTAL:' + total_print[-34:] + '\n')
        nota.write(('\n' + '*'*40))
        nota.write('\n*  PRECIOS PROPIOS DE LA FECHA ACTUAL  *')
        nota.write('\n*      GRACIAS POR SU PREFERENCIA      *')
        nota.write(('\n' + '*'*40))
        
        nota.close()
        
        archivo = open('serie.txt', 'w')
        archivo.write(str(serie + 1))
        archivo.close()
        
        os.startfile('nota.txt', 'print')
        
    
    def apagar(self):
        os.system("shutdown /s /t 1")
        
        
        
class Buscar2:
    def __init__(self, master=None, row=None, col=None, sv=None, gradilla_resultados=None, up=None, canv1=None, master_inf=None, lab_prod=None, row2=None, col2=None, nprec=None, busc_1 = None):

        self.master = master
        self.row = row
        self.col = col
        self.sv = sv
        self.gradilla_resultados = gradilla_resultados
        self.up = up
        self.canv1 = canv1
        self.lab_prod = lab_prod
        self.nprec = nprec
        self.busc_1 = busc_1
        
        self.master_inf =master_inf
        self.row2 = row2
        self.col2 = col2
        
        self.pasado = []
        self.boton = Button(
            self.master,
            text='Buscar',
            font=cfnt,
            bg='#0052cc', 
            command=self.consulta,
            fg='#ffffff'
        )
        
        self.boton_apagar = tk.Button(self.master_inf, text='Apagar equipo', font=cfnt, command=self.apagar, bg='#EE2E31', fg='white')
        self.boton_apagar.grid(row=self.row2+1, column=self.col2+2, sticky='SE', padx=10)
        
        self.boton.grid(row=self.row, column=self.col)
        
        self.boton_guardar = tk.Button(master_inf, text='Guardar precio', command=self.guardar, font=cfnt, bg='#F7A072')
        
        self.boton_guardar.grid(row=self.row2, column=self.col2+1, sticky='W', padx=0)
        
        
    def consulta(self):
        for widgets in self.gradilla_resultados.winfo_children():
            widgets.destroy()
        
        try:    
            resultados = ProductoDao.seleccionar2(self.sv.get())
            resultados += ProductoDao.seleccionar(self.sv.get().upper())
        except Exception as ex:
            resultados = ProductoDao.seleccionar(self.sv.get().upper())    
        
        """
        #for i in range()
        for resultado in resultados:

            tk.Label(self.gradilla_resultados, text=str(resultado)).pack()
        """    
        for i in range(len(resultados)):
            partes = resultados[i].split(',')
            logger.debug((partes))
            exec(f'self.f{i} = tk.Frame(self.gradilla_resultados, bg=\"#83f2e2\")')
            
            exec(f'self.cod{i} = tk.Label(self.f{i}, text= \"{partes[4]}\",  font=cfnt, bg=\"#83f2e2\", width=6, anchor=\"w\")')
            exec(f'self.cod{i}.grid(row={i}, column={0}, sticky=\"W\", padx=1)')
            exec(f'self.cod{i}.grid_propagate(False)')
            
            exec(f'self.desc{i} = tk.Label(self.f{i}, text= \"{partes[1]}\", font=cfnt, bg=\"#83f2e2\", width=51, anchor=\"w\")')
            exec(f'self.desc{i}.grid(row={i}, column={1}, sticky=\"NSWE\", padx=10)')

            
            exec(f'self.unid{i} = tk.Label(self.f{i}, text= \"{partes[2]}\", font=cfnt, bg=\"#83f2e2\")')
            exec(f'self.unid{i}.grid(row={i}, column={2}, sticky=\"NSWE\", padx=10)')

            
            #exec(f'self.tamaño{i} = tk.Label(self.f{i}, text= \"{partes[3]}\", font=cfnt, bg=\"#83f2e2\")')
            #exec(f'self.tamaño{i}.grid(row={i}, column={2}, sticky=\"NSWE\", padx=10)')

            
            exec(f'self.precio{i} = tk.Label(self.f{i}, text= \"{partes[3]}\", font=cfnt, bg=\"#83f2e2\", width=7)')
            exec(f'self.precio{i}.grid(row={i}, column={3}, sticky=\"NSWE\", padx=10)')
            exec(f'self.precio{i}.grid_propagate(False)')

            
            exec(f'self.addb{i} = tk.Button(self.f{i}, text=\"Cambiar precio\", font=cfnt, bg=\"#f2af4b\", command= partial(self.pasar, partes))')
            exec(f'self.addb{i}.grid(row={i}, column={4}, sticky=\"NSWE\", padx=10, pady=1)')

            
            exec(f'self.f{i}.pack()')
            
        self.up.update()
        self.canv1.config(scrollregion=self.canv1.bbox('all'))
        self.canv1.pack()
        
        
    def pasar(self, partes):
        self.pasado.clear()
        self.pasado.append(partes)
        self.lab_prod.config(text=('\n' + partes[1]), fg='black')
        #print(partes)
        
        
    def guardar(self):
        #ProductoDao.actualizar_precio(precio, producto)
        try:
            print(float(self.nprec.get()))
            print(self.pasado[0][0])
            ProductoDao.actualizar_precio(precio=self.nprec.get(), id_=self.pasado[0][0])
            self.consulta()
            self.lab_prod.config(text='\nGuardado correctamente', fg='green')
            
            
            
            try:
                self.busc_1.pasado[self.busc_1.pasado.index(self.pasado[0])][3] = f'${"{:.2f}".format(float(self.nprec.get()))}' #############
            except Exception as ex:
                pass

            self.nprec.set('')
            
            self.busc_1.desplegar()
            self.busc_1.consulta()
            self.busc_1.pago()
            
        except Exception as ex:
            self.lab_prod.config(text=f'Error al guardar el precio, \nintente de nuevo', fg='red')
            #print(str(ex)+' aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
            self.nprec.set('')
            
            
    def apagar(self):
        os.system("shutdown /s /t 1")