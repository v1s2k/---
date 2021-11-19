from Converter.convert import *
from tkinter import *
import tkinter.ttk as ttk


conv = Convert()


def clicked1():
    ins = conv.convert_it(int(txt1.get()), conv.length, combo1.get(), combo2.get())
    lbl1 = ttk.Label(tab1, text=ins, width=15)
    lbl1.grid(column=1, row=1, padx=10, pady=0)


def clicked2():
    ins = conv.convert_it(int(txt2.get()), conv.square, combo3.get(), combo4.get())
    lbl2 = ttk.Label(tab2, text=ins, width=15)
    lbl2.grid(column=1, row=1, padx=10, pady=0)


def clicked3():
    ins = conv.convert_it(int(txt3.get()), conv.volume, combo5.get(), combo6.get())
    lbl3 = ttk.Label(tab3, text=ins, width=15)
    lbl3.grid(column=1, row=1, padx=10, pady=0)


def clicked4():
    ins = conv.convert_it(int(txt4.get()), conv.mass, combo7.get(), combo8.get())
    lbl4 = ttk.Label(tab4, text=ins, width=15)
    lbl4.grid(column=1, row=1, padx=10, pady=0)


window = Tk()
window.title("Конвертер")
window.geometry('450x250')

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab_control.add(tab1, text="длина")
tab_control.add(tab2, text="площадь")
tab_control.add(tab3, text="объем")
tab_control.add(tab4, text="масса")

combo1 = ttk.Combobox(tab1, values=list(conv.length.keys()), width=15)
combo1.grid(column=0, row=0, padx=10, pady=10)
combo2 = ttk.Combobox(tab1, values=list(conv.length.keys()), width=15)
combo2.grid(column=1, row=0, padx=10, pady=10)
txt1 = ttk.Entry(tab1)
txt1.grid(column=0, row=1, padx=10, pady=0)
txt1.insert(0, 1)
btn = ttk.Button(tab1, text="Конвертировать", command=clicked1)
btn.grid(column=2, row=0, padx=10, pady=0)

combo3 = ttk.Combobox(tab2, values=list(conv.square.keys()), width=15)
combo3.grid(column=0, row=0, padx=10, pady=10)
combo4 = ttk.Combobox(tab2, values=list(conv.square.keys()), width=15)
combo4.grid(column=1, row=0, padx=10, pady=10)
txt2 = ttk.Entry(tab2)
txt2.grid(column=0, row=1, padx=10, pady=0)
txt2.insert(0, 1)
btn = ttk.Button(tab2, text="Конвертировать", command=clicked2)
btn.grid(column=2, row=0, padx=10, pady=0)

combo5 = ttk.Combobox(tab3, values=list(conv.volume.keys()), width=15)
combo5.grid(column=0, row=0, padx=10, pady=10)
combo6 = ttk.Combobox(tab3, values=list(conv.volume.keys()), width=15)
combo6.grid(column=1, row=0, padx=10, pady=10)
txt3 = ttk.Entry(tab3)
txt3.grid(column=0, row=1, padx=10, pady=0)
txt3.insert(0, 1)
btn = ttk.Button(tab3, text="Конвертировать", command=clicked3)
btn.grid(column=2, row=0, padx=10, pady=0)

combo7 = ttk.Combobox(tab4, values=list(conv.mass.keys()), width=15)
combo7.grid(column=0, row=0, padx=10, pady=10)
combo8 = ttk.Combobox(tab4, values=list(conv.mass.keys()), width=15)
combo8.grid(column=1, row=0, padx=10, pady=10)
txt4 = ttk.Entry(tab4)
txt4.grid(column=0, row=1, padx=10, pady=0)
txt4.insert(0, 1)
btn = ttk.Button(tab4, text="Конвертировать", command=clicked4)
btn.grid(column=2, row=0, padx=10, pady=0)

tab_control.pack(expand=True, fill=BOTH)
window.mainloop()
