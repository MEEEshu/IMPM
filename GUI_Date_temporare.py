from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib import animation
import pandas as pd
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk

data = pd.read_csv('date_meteo_temporare.csv')

x=data['Data'].tolist()
y=data['Temperatura'].tolist()
z=data['Umiditate'].tolist()
w=data['ValoareSenzorMq135'].tolist()
a=data['CalitateAer'].tolist()

numar_randuri = len(data)

# Initializare fereastra
root = tk.Tk()
root.title('Date Meteorologice Temporare')
root.geometry('600x200')
# Setarea iconului ferestrei
root.iconbitmap("imagine.ico") 

def temperatura(): 
    #realizam o functie pentru animarea in timp real a valorilor intr-un grafic 
    plot1,ax1 = plt.subplots() 
    ax1.plot(x,y, linestyle='solid',color = "green",label= "Temperatura") 
    ax1.set_title("Temperatura medie") 
    ax1.set_xlabel("Perioada") 
    ax1.legend() 
    ax1.set_ylabel("Valori t*C") 
    ax1.set_ylim([0,50]) 
    plt.tight_layout() 
    plt.show() 
#ax1.set_xlim([0,3]) 

def Umiditate(): 
    plot2,ax2 = plt.subplots()   
    ax2.plot(x,z, linestyle='dotted',color = "red", label='Umiditate') 
    ax2.set_title("Umiditate medie") 
    ax2.set_xlabel("Perioada") 
    ax2.set_ylabel("Valori umiditate %") 
    ax2.set_ylim([10,70]) 
    #ax2.set_xlim([0,3]) 
    ax2.legend() 
    plt.tight_layout() 
    plt.show()

def ValoareSenzor(): 
    plot2,ax3 = plt.subplots()   
    ax3.plot(x,z, linestyle='solid',color = "blue", label='Umiditate') 
    ax3.set_title("Valoare Analogica medie") 
    ax3.set_xlabel("Perioada") 
    ax3.set_ylabel("Valori Analogice MQ135") 
    ax3.set_ylim([10,70]) 
    #ax3.set_xlim([0,3]) 
    ax3.legend() 
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
    #conditiile pentru checkboxes - temperatura resimtita
    if checktempresim.get():
        feels_like = data.iloc[-1]['CalitateAer']
        label_text3.set("Calitate Aer " + feels_like )
    else:
        label_text3.set("Bifeaza pentru calitatea Aerului")


# Buton pentru a afișa grafic cu temperatura
submit_button = tk.Button(root, text='Temperatura', command=temperatura)
submit_button.grid(row=2, column=0)

# Buton pentru a afișa grafic cu temperatura
submit_button1 = tk.Button(root, text='Umiditate', command=Umiditate)
submit_button1.grid(row=2, column=1)

# Buton pentru a afișa grafic cu temperatura
submit_button2 = tk.Button(root, text='Valoare Analogica', command=ValoareSenzor)
submit_button2.grid(row=2, column=3)

# Buton pentru a afișa grafic cu temperatura
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

# Etichetă pentru afișarea Temperaturii resimțite
label_text3 = tk.StringVar()
label_text3.set("Bifeaza pentru calitatea Aerului")
label3 = tk.Label(root, textvariable=label_text3)
label3.grid(row=5, column=1, columnspan=2)

# Checkbutton pentru temperatura resimtita
checktempresim = tk.BooleanVar()
check3 = tk.Checkbutton(root, text = "Doresti Calitatea Aerului?", variable = checktempresim)
check3.grid(row = 5, column = 0)

# Rulare aplicație
root.mainloop()
