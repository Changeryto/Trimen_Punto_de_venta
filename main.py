import tkinter as tk
from tkinter import CENTER, Y, ttk
from tkinter.tix import COLUMN
from turtle import width
from an_letra import Letra
from borrar import Borrar
from buscar import Buscar, Buscar2

from cfnt import cfnt
from guardar import Guardar

from buscar import Buscar
from validadores import precio, producto, entero


root = tk.Tk()
root.geometry('6000x700')
root.title('Trimen')
root.iconbitmap('ico.ico')



style = ttk.Style()


style.theme_create('MyStyle', parent='alt', settings={
    'TNotebook': {'configure': {'tabmargins': [2, 5, 2, 0]}},
    'TNotebook.Tab': {'configure': {'padding': [100, 10],
                                    'font': ('Consolas', 21),
                                    'background': '#A4B8C4'}}
})

style.theme_use('MyStyle')
style.configure("Vertical.TScrollbar", background="#E6AF2E", bordercolor="#3D348B", arrowcolor="#FFFAFB", size=20)

tabControl = ttk.Notebook(root)

ventana = tk.Frame(tabControl)
ventana2 = tk.Frame(tabControl)
ventana3 = tk.Frame(tabControl)

tabControl.add(ventana, text='Generar nota')
tabControl.add(ventana2, text='Cambiar precio')
tabControl.add(ventana3, text='Añadir producto')

tabControl.pack(expand=1, fill='both')


selector = tk.Frame(ventana)
lab_selec = tk.Label(selector, text='A buscar:', font=cfnt)
lab_selec.grid(row=0, column=0, sticky='W')

ent_sv = tk.StringVar(value='')
ent_busc = ttk.Entry(selector, textvariable=ent_sv, font=cfnt,
                     validate='key',
                     validatecommand=(root.register(producto), '%S'))

ent_busc.grid(row=1, column=0, columnspan=1, pady=0, sticky='NSWE')



but_borrar1 = Borrar(selector, 1,5,ent_sv)





abcd = tk.Frame(selector)

lA = Letra(abcd, 'A', 2,0,ent_sv)
#lA.button.configure(command=lA.insertar)
lB = Letra(abcd, 'B', 2,1,ent_sv)
lC = Letra(abcd, 'C', 2,3,ent_sv)
lD = Letra(abcd, 'D', 2,4,ent_sv)
lE = Letra(abcd, 'E', 2,5,ent_sv)
lF = Letra(abcd, 'F', 2,6,ent_sv)
lG = Letra(abcd, 'G', 2,7,ent_sv)
lH = Letra(abcd, 'H', 2,8,ent_sv)
lI = Letra(abcd, 'I', 2,9,ent_sv)
lJ = Letra(abcd, 'J', 2,10,ent_sv)
lK = Letra(abcd, 'K', 2,11,ent_sv)
lL = Letra(abcd, 'L', 2,12,ent_sv)
lM = Letra(abcd, 'M', 2,13,ent_sv)
lN = Letra(abcd, 'N', 2,14,ent_sv)
lO = Letra(abcd, 'O', 2,15,ent_sv)
lP = Letra(abcd, 'P', 2,16,ent_sv)
lQ = Letra(abcd, 'Q', 2,17,ent_sv)
lR = Letra(abcd, 'R', 2,18,ent_sv)
lS = Letra(abcd, 'S', 2,19,ent_sv)
lT = Letra(abcd, 'T', 2,20,ent_sv)
lU = Letra(abcd, 'U', 2,21,ent_sv)
lV = Letra(abcd, 'V', 2,22,ent_sv)
lW = Letra(abcd, 'W', 2,23,ent_sv)
lX = Letra(abcd, 'X', 2,24,ent_sv)
lY = Letra(abcd, 'Y', 2,25,ent_sv)
lZ = Letra(abcd, 'Z', 2,26,ent_sv)
l_ = Letra(abcd, ' ', 2,27,ent_sv)
l0 = Letra(abcd, '0', 3, 0,ent_sv)
l1 = Letra(abcd, '1', 3, 1,ent_sv)
l2 = Letra(abcd, '2', 3, 3,ent_sv)
l3 = Letra(abcd, '3', 3, 4,ent_sv)
l4 = Letra(abcd, '4', 3, 5,ent_sv)
l5 = Letra(abcd, '5', 3, 6,ent_sv)
l6 = Letra(abcd, '6', 3, 7,ent_sv)
l7 = Letra(abcd, '7', 3, 8,ent_sv)
l8 = Letra(abcd, '8', 3, 9,ent_sv)
l9 = Letra(abcd, '9', 3, 10,ent_sv)
lp = Letra(abcd, '.', 3, 11,ent_sv)
ld = Letra(abcd, '/', 3, 12,ent_sv)



abcd.grid(row=2, column=0)

upm = tk.Frame(selector) #upm: mensaje superior


lab_desc=tk.Label(upm, text=' Productos encontrados                                  Unidad  Precio', font=cfnt)
lab_desc.grid(row=1, column=0)

upm.grid(row=3, column=0, pady=7, sticky='W')



selector.grid(row=0, column=0, columnspan=1, sticky='W', padx=30, pady=10)



stock = tk.Frame(ventana, background='pink')
scrollbar1 = ttk.Scrollbar(stock)
c1 = tk.Canvas(stock, background='pink',yscrollcommand=scrollbar1.set, height=150)
scrollbar1.config(command=c1.yview)
scrollbar1.pack(side=tk.RIGHT, fill=tk.Y)

framecan1 = tk.Frame(c1)
c1.pack(side=('left'), fill='both', expand=True)

c1.create_window(0,0,window=framecan1, anchor='nw')

#borrar = tk.Label(framecan1, text='Placeholderaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab', wraplength=100, font=cfnt)
#borrar.pack()





stock.grid(row=1, column=0, columnspan=1, sticky='W', padx=30, pady=0, ipadx=410, ipady=0)





mostrador = tk.Frame(ventana)



most_upm2 = tk.Label(mostrador, text='Productos añadidos                                     Unidad  Precio', font=cfnt)
most_upm2.grid(row=1, column=0, sticky='W', ipadx=50)


añadido = tk.Frame(mostrador)
scrollbar2 = ttk.Scrollbar(añadido)
c2 = tk.Canvas(añadido, background='#aff065',yscrollcommand=scrollbar2.set, height=150)
scrollbar2.config(command=c2.yview)
scrollbar2.pack(side=tk.RIGHT, fill=tk.Y)

framecan2 = tk.Frame(c2)
c2.pack(side=('left'), fill='both', expand=True)

c2.create_window(0,0,window=framecan2, anchor='nw')

añadido.grid(row=2, column=0, sticky='W', ipadx=550, padx=30)

mostrador.grid(row=2, column=0, columnspan=1, sticky='W', pady=15)





inferior = tk.Frame(ventana)

but_buscar1 = Buscar(selector, row=1, col=6, sv=ent_sv, gradilla_resultados=framecan1, up=stock, canv1=c1, gradilla_agregados=framecan2, up2=mostrador, canv2=c2, master_inf=inferior)
#but_cal = Calcular(inferior, but_buscar1)


inferior.grid(row=3, column=0)


#ventana.wm_attributes('-transparentcolor','#000000')
#ventana.wm_attributes('-topmost', True)








#4









selector2 = tk.Frame(ventana2)
lab_selec2 = tk.Label(selector2, text='A buscar:', font=cfnt)
lab_selec2.grid(row=0, column=0, sticky='W')

ent_sv2 = tk.StringVar(value='')
ent_busc2 = ttk.Entry(selector2, textvariable=ent_sv2, font=cfnt,
                     validate='key',
                     validatecommand=(root.register(producto), '%S'))

ent_busc2.grid(row=1, column=0, columnspan=1, pady=0, sticky='NSWE')



but_borrar2 = Borrar(selector2, 1,5,ent_sv2)





abcd2 = tk.Frame(selector2)

lA = Letra(abcd2, 'A', 2,0,ent_sv2)
#lA.button.configure(command=lA.insertar)
lB = Letra(abcd2, 'B', 2,1,ent_sv2)
lC = Letra(abcd2, 'C', 2,3,ent_sv2)
lD = Letra(abcd2, 'D', 2,4,ent_sv2)
lE = Letra(abcd2, 'E', 2,5,ent_sv2)
lF = Letra(abcd2, 'F', 2,6,ent_sv2)
lG = Letra(abcd2, 'G', 2,7,ent_sv2)
lH = Letra(abcd2, 'H', 2,8,ent_sv2)
lI = Letra(abcd2, 'I', 2,9,ent_sv2)
lJ = Letra(abcd2, 'J', 2,10,ent_sv2)
lK = Letra(abcd2, 'K', 2,11,ent_sv2)
lL = Letra(abcd2, 'L', 2,12,ent_sv2)
lM = Letra(abcd2, 'M', 2,13,ent_sv2)
lN = Letra(abcd2, 'N', 2,14,ent_sv2)
lO = Letra(abcd2, 'O', 2,15,ent_sv2)
lP = Letra(abcd2, 'P', 2,16,ent_sv2)
lQ = Letra(abcd2, 'Q', 2,17,ent_sv2)
lR = Letra(abcd2, 'R', 2,18,ent_sv2)
lS = Letra(abcd2, 'S', 2,19,ent_sv2)
lT = Letra(abcd2, 'T', 2,20,ent_sv2)
lU = Letra(abcd2, 'U', 2,21,ent_sv2)
lV = Letra(abcd2, 'V', 2,22,ent_sv2)
lW = Letra(abcd2, 'W', 2,23,ent_sv2)
lX = Letra(abcd2, 'X', 2,24,ent_sv2)
lY = Letra(abcd2, 'Y', 2,25,ent_sv2)
lZ = Letra(abcd2, 'Z', 2,26,ent_sv2)
l_ = Letra(abcd2, ' ', 2,27,ent_sv2)
l0 = Letra(abcd2, '0', 3, 0,ent_sv2)
l1 = Letra(abcd2, '1', 3, 1,ent_sv2)
l2 = Letra(abcd2, '2', 3, 3,ent_sv2)
l3 = Letra(abcd2, '3', 3, 4,ent_sv2)
l4 = Letra(abcd2, '4', 3, 5,ent_sv2)
l5 = Letra(abcd2, '5', 3, 6,ent_sv2)
l6 = Letra(abcd2, '6', 3, 7,ent_sv2)
l7 = Letra(abcd2, '7', 3, 8,ent_sv2)
l8 = Letra(abcd2, '8', 3, 9,ent_sv2)
l9 = Letra(abcd2, '9', 3, 10,ent_sv2)
lp = Letra(abcd2, '.', 3, 11,ent_sv2)
ld = Letra(abcd2, '/', 3, 12,ent_sv2)


abcd2.grid(row=2, column=0)


upm2 = tk.Frame(selector2) #upm: mensaje superior


#lab_prodenc = tk.Label(upm, text='\nProductos encontrados:', font=cfnt)
#lab_prodenc.grid(row=0, column=0, sticky='W')

lab_desc2=tk.Label(upm2, text='Productos encontrados                                   Unidad  Precio', font=cfnt)
lab_desc2.grid(row=1, column=0)



upm2.grid(row=3, column=0, pady=7, sticky='W')



selector2.grid(row=0, column=0, columnspan=1, sticky='W', padx=30, pady=10)




stock2 = tk.Frame(ventana2, background='pink')
scrollbar3 = ttk.Scrollbar(stock2)
c3 = tk.Canvas(stock2, background='pink',yscrollcommand=scrollbar3.set, height=150)
scrollbar3.config(command=c3.yview)
scrollbar3.pack(side=tk.RIGHT, fill=tk.Y)

framecan3 = tk.Frame(c3)
c3.pack(side=('left'), fill='both', expand=True)

c3.create_window(0,0,window=framecan3, anchor='nw')







stock2.grid(row=1, column=0, columnspan=1, sticky='W', padx=30, pady=0, ipadx=470, ipady=0)



nuevo_precio = tk.Frame(ventana2)

label_nuevo_precio = tk.Label(nuevo_precio, text='\nPrecio nuevo del producto:', font=cfnt)
label_nuevo_precio.grid(row=0, column=0, sticky='E')

label_producto_precio = tk.Label(nuevo_precio, text='', font=cfnt, width=40, anchor='w')
label_producto_precio.grid(row=0, column=1, columnspan=3, sticky='W')
label_producto_precio.grid_propagate(False)

sv_nuevo_precio = tk.StringVar(value='')
ent_nuevo_precio = tk.Entry(nuevo_precio, textvariable=sv_nuevo_precio, font=cfnt, validate='key',
                     validatecommand=(root.register(precio), '%P'))
ent_nuevo_precio.grid(row=2, column=0, sticky='E')

boton_borrar_precio = Borrar(nuevo_precio, 2,1,sv_nuevo_precio)

pan_numer = tk.Frame(nuevo_precio)


l1 = Letra(pan_numer, '1',0,0,sv_nuevo_precio)
l1 = Letra(pan_numer, '2',0,1,sv_nuevo_precio)
l1 = Letra(pan_numer, '3',0,2,sv_nuevo_precio)
l1 = Letra(pan_numer, '4',0,3,sv_nuevo_precio)
l1 = Letra(pan_numer, '5',0,4,sv_nuevo_precio)
l1 = Letra(pan_numer, '6',1,0,sv_nuevo_precio)
l1 = Letra(pan_numer, '7',1,1,sv_nuevo_precio)
l1 = Letra(pan_numer, '8',1,2,sv_nuevo_precio)
l1 = Letra(pan_numer, '9',1,3,sv_nuevo_precio)
l1 = Letra(pan_numer, '0',1,4,sv_nuevo_precio)
l1 = Letra(pan_numer, '.',1,5,sv_nuevo_precio)


pan_numer.grid(row=3, column=0, sticky='NE')

nuevo_precio.grid(row=2, column=0)
#nuevo_precio.grid_propagate(False)



inferior2 = tk.Frame(ventana2)
but_buscar2 = Buscar2(selector2, row=1, col=6, sv=ent_sv2, gradilla_resultados=framecan3, up=stock2, canv1=c3, master_inf=nuevo_precio, lab_prod=label_producto_precio, nprec=sv_nuevo_precio, row2=2, col2=1, busc_1=but_buscar1)
#Buscar(selector, row=1, col=6, sv=ent_sv, gradilla_resultados=framecan1, up=stock, canv1=c1, gradilla_agregados=framecan2, up2=mostrador, canv2=c2, master_inf=inferior)
inferior2.grid(row=3, column=0)




entradas_c = tk.Frame(ventana3)



label_codigo = tk.Label(entradas_c, font=cfnt, text='Código del nuevo produto: ')
label_codigo.grid(row=0, column=0, padx=5, sticky='E')

sv_codigo = tk.StringVar(value='')
entry_codigo = tk.Entry(entradas_c, textvariable=sv_codigo, font=cfnt,
                     validate='key',
                     validatecommand=(root.register(entero), '%P'))

entry_codigo.grid(row=0, column=1, sticky='WESN', pady=5)

numpad_codigo = tk.Frame(entradas_c)
n0 = Letra(numpad_codigo, '0', 0,0,sv_codigo)
n1 = Letra(numpad_codigo, '1', 0,1,sv_codigo)
n2 = Letra(numpad_codigo, '2', 0,2,sv_codigo)
n3 = Letra(numpad_codigo, '3', 0,3,sv_codigo)
n4 = Letra(numpad_codigo, '4', 0,4,sv_codigo)
n5 = Letra(numpad_codigo, '5', 0,5,sv_codigo)
n6 = Letra(numpad_codigo, '6', 0,6,sv_codigo)
n7 = Letra(numpad_codigo, '7', 0,7,sv_codigo)
n8 = Letra(numpad_codigo, '8', 0,8,sv_codigo)
n9 = Letra(numpad_codigo, '9', 0,9,sv_codigo)
numpad_codigo.grid(row=1, column=1)

borrar_codigo = Borrar(entradas_c, 0, 2, sv_codigo)

label_descripcion = tk.Label(entradas_c, font=cfnt, text='Descripción del nuevo producto: ')
label_descripcion.grid(row=2, column=0, pady=10, padx=5, sticky='E')

sv_descripcion = tk.StringVar(value='')

entry_descrpcion = tk.Entry(entradas_c, font=cfnt,
                            textvariable=sv_descripcion,
                            validate='key',
                            validatecommand=(root.register(producto), '%S'))

entry_descrpcion.grid(row=2, column=1, sticky='WESN', pady=5)


teclado_descipcion = tk.Frame(entradas_c)
lA = Letra(teclado_descipcion, 'A', 2,0,sv_descripcion)
lB = Letra(teclado_descipcion, 'B', 2,1,sv_descripcion)
lC = Letra(teclado_descipcion, 'C', 2,2,sv_descripcion)
lD = Letra(teclado_descipcion, 'D', 2,3,sv_descripcion)
lE = Letra(teclado_descipcion, 'E', 2,4,sv_descripcion)
lF = Letra(teclado_descipcion, 'F', 2,5,sv_descripcion)
lG = Letra(teclado_descipcion, 'G', 2,6,sv_descripcion)
lH = Letra(teclado_descipcion, 'H', 2,7,sv_descripcion)
lI = Letra(teclado_descipcion, 'I', 2,8,sv_descripcion)
lJ = Letra(teclado_descipcion, 'J', 2,9,sv_descripcion)
lK = Letra(teclado_descipcion, 'K', 2,10,sv_descripcion)
lL = Letra(teclado_descipcion, 'L', 2,11,sv_descripcion)
lM = Letra(teclado_descipcion, 'M', 2,12,sv_descripcion)
lN = Letra(teclado_descipcion, 'N', 2,13,sv_descripcion)
lO = Letra(teclado_descipcion, 'O', 2,14,sv_descripcion)
lP = Letra(teclado_descipcion, 'P', 2,15,sv_descripcion)
lQ = Letra(teclado_descipcion, 'Q', 2,16,sv_descripcion)
lR = Letra(teclado_descipcion, 'R', 2,17,sv_descripcion)
lS = Letra(teclado_descipcion, 'S', 2,18,sv_descripcion)
lT = Letra(teclado_descipcion, 'T', 2,19,sv_descripcion)
lU = Letra(teclado_descipcion, 'U', 3,0,sv_descripcion)
lV = Letra(teclado_descipcion, 'V', 3,1,sv_descripcion)
lW = Letra(teclado_descipcion, 'W', 3,2,sv_descripcion)
lX = Letra(teclado_descipcion, 'X', 3,3,sv_descripcion)
lY = Letra(teclado_descipcion, 'Y', 3,4,sv_descripcion)
lZ = Letra(teclado_descipcion, 'Z', 3,5,sv_descripcion)
l_ = Letra(teclado_descipcion, ' ', 3,19,sv_descripcion)
l0 = Letra(teclado_descipcion, '0', 3, 7,sv_descripcion)
l1 = Letra(teclado_descipcion, '1', 3, 8,sv_descripcion)
l2 = Letra(teclado_descipcion, '2', 3, 9,sv_descripcion)
l3 = Letra(teclado_descipcion, '3', 3, 10,sv_descripcion)
l4 = Letra(teclado_descipcion, '4', 3, 11,sv_descripcion)
l5 = Letra(teclado_descipcion, '5', 3, 12,sv_descripcion)
l6 = Letra(teclado_descipcion, '6', 3, 13,sv_descripcion)
l7 = Letra(teclado_descipcion, '7', 3, 14,sv_descripcion)
l8 = Letra(teclado_descipcion, '8', 3, 15,sv_descripcion)
l9 = Letra(teclado_descipcion, '9', 3, 16,sv_descripcion)
lp = Letra(teclado_descipcion, '.', 3, 17,sv_descripcion)
ld = Letra(teclado_descipcion, '/', 3, 18,sv_descripcion)
teclado_descipcion.grid(row=3, column=1)

borrar_descipcion = Borrar(entradas_c, 2, 2, sv_descripcion)


label_nuevo_precio2 = tk.Label(entradas_c, 
                               text='Precio del nuevo producto: ',
                               font=cfnt)
label_nuevo_precio2.grid(row=4, column=0, sticky='E')


sv_precio = tk.StringVar(value='')

entry_nuevo_precio2 = tk.Entry(entradas_c,
                               font=cfnt,
                               textvariable=sv_precio,
                               validate='key',
                               validatecommand=(root.register(precio), '%P'))

entry_nuevo_precio2.grid(row=4, column=1, sticky='WESN', pady=5)

borrar_nuevo_precio2 = Borrar(entradas_c, 4, 2, sv_precio)

numpad_precio = tk.Frame(entradas_c)
n0 = Letra(numpad_precio, '0', 0,0,sv_precio)
n1 = Letra(numpad_precio, '1', 0,1,sv_precio)
n2 = Letra(numpad_precio, '2', 0,2,sv_precio)
n3 = Letra(numpad_precio, '3', 0,3,sv_precio)
n4 = Letra(numpad_precio, '4', 0,4,sv_precio)
n5 = Letra(numpad_precio, '5', 0,5,sv_precio)
n6 = Letra(numpad_precio, '6', 0,6,sv_precio)
n7 = Letra(numpad_precio, '7', 0,7,sv_precio)
n8 = Letra(numpad_precio, '8', 0,8,sv_precio)
n9 = Letra(numpad_precio, '9', 0,9,sv_precio)
np = Letra(numpad_precio, '.', 0,10,sv_precio)
numpad_precio.grid(row=5, column=1)


label_unidad = tk.Label(entradas_c,text='Tipo de unidad: ', font=cfnt)
label_unidad.grid(row=6, column=0, sticky='E')


unidades = ('PZ', 'MT', 'KG', 'LT')

sv_unidad = tk.StringVar()
sv_unidad.set(unidades[0])

def desplegar_seleccion(opcion):
    opcion = sv_unidad.get()


menu_unidad = tk.OptionMenu(entradas_c, sv_unidad, 'PZ', 'MT', 'KG', 'LT', command=desplegar_seleccion)
menu_unidad.config(bg='lightgoldenrod', font=cfnt)
menu_unidad['menu'].config(font=cfnt)
menu_unidad.grid(row=6, column=1, sticky='W')

boton_guardar = Guardar(entradas_c,
                        7,
                        0,
                        sv_codigo,
                        sv_descripcion,
                        sv_unidad,
                        sv_precio)


entradas_c.grid(row=0,column=0)



root.state('zoomed')
root.attributes('-fullscreen', True)
root.mainloop()