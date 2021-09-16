import urllib.request
from tkinter import *
from tkinter import messagebox
import datetime
import xml.dom.minidom
from tkinter import *
from tkinter.ttk import Combobox
import tkinter.ttk as ttk
import xml.dom.minidom
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter.ttk import Notebook, Frame
from code5 import arrName, arrValue,arrNominal,arrNameGraph



window=Tk()
window.title("Конвертер валют")
window.geometry("600x500")
tab_control = ttk.Notebook(window)  
tab1 = ttk.Frame(tab_control)  
tab2 = ttk.Frame(tab_control) 
tab_control.add(tab1, text='Конвертер валют')
tab_control.add(tab2, text='График')  
lbl1 = Label(tab1, text=' ')  
lbl1.grid(column=0, row=0) 
arrName.append("Российский рубль")
arrNominal.append("1")
arrValue.append("1")

combox1=ttk.Combobox (tab1, values = arrName)  
combox1.current(34)  
combox1.grid(column=1, row=0, pady=0, padx=0)
combox2=Combobox(tab2)
combox2=ttk.Combobox (tab1, values = arrName)  
combox2.current(0)  
combox2.grid(column=3, row=0, pady=0,padx=4)
message = StringVar()
message_entry = Entry(tab1,textvariable=message)
message_entry.place(relx=0.2,rely=0.2)
name_label = Label(tab1,text="Введите сумму:",font=("Arial Bold", 10))
name_label.place(relx=0.0,rely=0.2)
print(len(arrName))

def convertor():
    numb=int(float(message_entry.get()))
    value1=combox1.get()
    value2=combox2.get()
    for i in  range (len(arrName)):
        if value2==arrName[i]:
            p=int(float(arrNominal[i]))#номинал 2 строки
           
    for i in  range (len(arrName)):
        if value1==arrName[i]:
            k=int(float(arrNominal[i]))#номинал 1 строки
    
    for i in  range (len(arrName)):
        if value1==arrName[i]:
            a=arrValue[i]
            a=(float(a.replace(',','.')))#курс 1 строки
    for i in  range (len(arrName)):
        if value2==arrName[i]:
            e=arrValue[i]
            e=float(e.replace(',','.'))#курс 2 строки
    
            
    convert=0
    x=a/k
    z=e/p
    convert=(numb*x)/z
    print(convert)
    lbl = Label(tab1, text=convert)  
    lbl.place(relx=0.4,rely=0.2)
dates=["Январь 2019","Февраль 2019","Март 2019","Апрель 2019","Май 2019","Июнь 2019","Июль 2019","Август 2019",
       "Сентябрь 2019","Октябрь 2019","Ноябрь 2019","Декабрь 2019"]
combobox3=Combobox(tab2,values=dates,heigh=10)
combobox4=Combobox(tab2,values=arrName,heigh=10)
combobox3.place(relx=0.0,rely=0.01)
combobox4.place(relx=0.0,rely=0.05)
Dict={"Январь 2019": 31,"Февраль 2019": 28,
                  "Март 2019": 31,
                  "Апрель 2019": 30,
                  "Май 2019": 30,
                  "Июнь 2019": 30,
                  "Июль 2019": 31,
                  "Август 2019": 31,
                  "Сентябрь 2019": 30,
                  "Октябрь 2019": 31,
                  "Ноябрь 2019": 30,
                  "Декабрь 2019": 31}
def Gets():
    data=combobox3.get()
    for i,k in Dict.items():
        if data==i:
            return k
def GETX():
    days=[]
    for i in range(1, Gets()+1):
        days.append(i)
    return days

def GETY():
    baklan=[]
    dick2={"Январь 2019": '01',
                 "Февраль 2019": '02',
                 'Март 2019': '03',
                 'Апрель 2019': '04',
                 'Май 2019': '05',
                 'Июнь 2019': '06',
                 'Июль 2019': '07',
                 'Август 2019': '08',
                 'Сентябрь 2019': '09',
                 'Октябрь 2019': '10',
                 'Ноябрь 2019': '11',
                 'Декабрь 2019': '12'}
    mon=dick2.get(combobox3.get())
    valuename=combobox4.get()
   
    for i in range(1, Gets()+1):                     
        d1=str(i)                      
        i2=d1.rjust(2,"0")
        c=0
        urin=url="http://www.cbr.ru/scripts/XML_daily.asp?date_req={}/{}/2019".format(i2,mon)
        response = urllib.request.urlopen(urin)#обращение к ссылке(открытие сслыки) 
        dom = xml.dom.minidom.parse(response)
        dom.normalize()
        nodeArray = dom.getElementsByTagName("Valute")
        for node in nodeArray:
            childList = node.childNodes
            for child in childList:
                 if ((child.nodeName == 'Value') & (c == 1)):
                    baklan.append(child.childNodes[0].nodeValue)
                    c = 0
                 if (child.childNodes[0].nodeValue == combobox4.get()):
                    c = 1
    baklan=baklan[::-1]
    for i in range(len(arrName)):
        if valuename==arrName[i]:
            d=float(arrNominal[i])

    for i in range(len(baklan)):
        baklan[i]= baklan[i].replace(',','.')
        baklan[i]=float( baklan[i])/d
    
    return (baklan) 
    
 
def Choose():
    matplotlib.use('TkAgg')
    fig=plt.figure()
    plt.title("Зависимость курса от даты ")
    canvas=matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig,master=tab2)
    plot_widget = canvas.get_tk_widget()
    fig.clear()
    plt.plot(GETX(),GETY())
    plt.grid()
    plot_widget.grid(row=0,column=0,padx=200,pady=50)
button2=Button(tab2,text="График",command=Choose)
button2.place(relx=0.01,rely=0.11,width=70)


btn1 = Button(tab1, text="Конвертировать",command=convertor,bg = "green",relief='ridge',font=("Calibri", 10, "bold"),activebackground="red")#command=функция конвертирования!
btn1.grid(column=2, row=0, padx=9, pady=0)
tab_control.place(relheight=1, relwidth=1, relx=0, rely=0)
button2=Button(tab2,text="График",command=Choose)
button2.place(relx=0.01,rely=0.11,width=70)
window.mainloop()

