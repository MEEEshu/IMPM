from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib import animation
import pandas as pd
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk

data = pd.read_csv('date_meteo.csv')

x=data['Data'].tolist()
y=data['Temperatura'].tolist()
z=data['Umiditate'].tolist()
w=data['ValoareSenzorMq135'].tolist()
a=data['CalitateAer'].tolist()
b=data['IndiceConfort'].tolist()

numar_randuri = len(data)

# Initializare fereastra
root = tk.Tk()
root.title('Date Meteorologice')
root.geometry('600x200')
# Setarea iconului ferestrei
root.iconbitmap("imagine.ico") 

def temperatura(): 
    plot1,ax1 = plt.subplots() 
    ax1.plot(x,y, linestyle='solid',color = "green",label= "Temperatura") 
    ax1.set_title("Temperatura medie") 
    ax1.set_xlabel("Perioada") 
    ax1.legend() 
    ax1.set_ylabel("Valori t*C") 
    ax1.set_ylim([0,50]) 
    plt.tight_layout() 
    plt.show() 

def Umiditate(): 
    plot2,ax2 = plt.subplots()   
    ax2.plot(x,z, linestyle='dotted',color = "red", label='Umiditate') 
    ax2.set_title("Umiditate medie") 
    ax2.set_xlabel("Perioada") 
    ax2.set_ylabel("Valori umiditate %") 
    ax2.set_ylim([10,70]) 
    ax2.legend() 
    plt.tight_layout() 
    plt.show()

def ValoareSenzor(): 
    plot2,ax3 = plt.subplots()   
    ax3.plot(x,w, linestyle='solid',color = "blue", label='Valoare Analogica') 
    ax3.set_title("Valoare Analogica medie") 
    ax3.set_xlabel("Perioada") 
    ax3.set_ylabel("Valori Analogice MQ135") 
    ax3.set_ylim([10,70]) 
    ax3.legend() 
    plt.tight_layout() 
    plt.show()

def IndiceConfort(): 
    plot2,ax4 = plt.subplots()   
    ax4.plot(x,b, linestyle='solid',color = "purple", label='Indice Confort') 
    ax4.set_title("Indice Confort") 
    ax4.set_xlabel("Perioada") 
    ax4.set_ylabel("Valori Indice Confort") 
    ax4.set_ylim([0,100]) 
    ax4.legend() 
    plt.tight_layout() 
    plt.show()

def Submit():
    if checktemp.get():
        temp = data.iloc[-1]['Temperatura']
        label_text1.set("Temperatura: " + str(temp) + "°C")
    else:
        label_text1.set("Bifeaza pentru temperatura")
    #conditiile pentru checkboxes - umiditate
    if checkhum.get():
        humidity = str(data.iloc[-1]['Umiditate']) + "%"
        label_text2.set("Umiditate: " + humidity)
    else:
        label_text2.set("Bifeaza pentru umiditate")
    #conditiile pentru checkboxes - calitatea aerului
    if checktempresim.get():
        feels_like = data.iloc[-1]['CalitateAer']
        label_text3.set("Calitate Aer " + feels_like )
    else:
        label_text3.set("Bifeaza pentru calitatea Aerului")
    #conditiile pentru checkboxes - indice confort
    if checkcomfort.get():
        comfort_index = data.iloc[-1]['IndiceConfort']
        label_text4.set("Indice Confort: " + str(comfort_index))
    else:
        label_text4.set("Bifeaza pentru Indice Confort")

# Buton pentru a afișa grafic cu temperatura
submit_button = tk.Button(root, text='Temperatura', command=temperatura)
submit_button.grid(row=2, column=0)

# Buton pentru a afișa grafic cu umiditatea
submit_button1 = tk.Button(root, text='Umiditate', command=Umiditate)
submit_button1.grid(row=2, column=1)

# Buton pentru a afișa grafic cu valoare analogica
submit_button2 = tk.Button(root, text='Valoare Analogica', command=ValoareSenzor)
submit_button2.grid(row=2, column=3)

# Buton pentru a afișa grafic cu indice confort
submit_button3 = tk.Button(root, text='Indice Confort', command=IndiceConfort)
submit_button3.grid(row=2, column=4)

# Buton pentru a afișa datele selectate
submit_button = tk.Button(root, text='Afiseaza Date', command=Submit)
submit_button.grid(row=6, column=1, columnspan=2)

# Eticheta pentru afisarea orasului
label_text0 = tk.StringVar()
label_text0.set("Orasul: Iasi")
label0 = tk.Label(root, textvariable=label_text0)
label0.grid(row=0, column=2, columnspan=2)

# Eticheta pentru afisarea populatiei orasului
label_textpop = tk.StringVar()
label_textpop.set("Student: Isachi Mihai")
label_pop = tk.Label(root, textvariable=label_textpop)
label_pop.grid(row=1, column=2, columnspan=2)

# Etichetă pentru afișarea Temperaturii
label_text1 = tk.StringVar()
label_text1.set("Bifeaza pentru temperatura")
label1 = tk.Label(root, textvariable=label_text1)
label1.grid(row=3, column=1, columnspan=2)

# Checkbutton pentru Temperatura
checktemp = tk.BooleanVar()
check1 = tk.Checkbutton(root, text = "Doresti temperatura?", variable = checktemp)
check1.grid(row = 3, column = 0)

# Etichetă pentru afișarea Umidității
label_text2 = tk.StringVar()
label_text2.set("Bifeaza pentru umiditate")
label2 = tk.Label(root, textvariable=label_text2)
label2.grid(row=4, column=1, columnspan=2)

# Checkbutton pentru Umiditate
checkhum = tk.BooleanVar()
check2 = tk.Checkbutton(root, text = "Doresti umiditatea?", variable = checkhum)
check2.grid(row = 4, column = 0)

# Etichetă pentru afișarea Calității Aerului
label_text3 = tk.StringVar()
label_text3.set("Bifeaza pentru calitatea Aerului")
label3 = tk.Label(root, textvariable=label_text3)
label3.grid(row=5, column=1, columnspan=2)

# Checkbutton pentru Calitatea Aerului
checktempresim = tk.BooleanVar()
check3 = tk.Checkbutton(root, text = "Doresti Calitatea Aerului?", variable = checktempresim)
check3.grid(row = 5, column = 0)

# Etichetă pentru afișarea Indice Confort
label_text4 = tk.StringVar()
label_text4.set("Bifeaza pentru Indice Confort")
label4 = tk.Label(root, textvariable=label_text4)
label4.grid(row=6, column=1, columnspan=2)

# Checkbutton pentru Indice Confort
checkcomfort = tk.BooleanVar()
check4 = tk.Checkbutton(root, text = "Doresti Indice Confort?", variable = checkcomfort)
check4.grid(row = 6, column = 0)

# Rulare aplicație
root.mainloop()
