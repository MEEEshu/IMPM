import os
import datetime
import csv
import sys
import pandas as pd
import matplotlib.pyplot as plt
import serial
import time

#os.remove("date_meteo.csv")
#os.remove("date_meteo_temporare.csv")

with open("date_meteo.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Data","Temperatura","Umiditate","ValoareSenzorMq135","CalitateAer"])

with open("date_meteo_temporare.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Data","Temperatura","Umiditate","ValoareSenzorMq135","CalitateAer"])

def save_to_csv_temporary(data):
    with open('date_meteo_temporare.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writerow(data)

def save_to_csv(data):
    with open('date_meteo.csv', mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=data.keys())
        writer.writerow(data)

try:
    while True:
        with serial.Serial('COM6', 9600) as ser:
            line = ser.readline().decode('latin1').strip()
            data = line.split(',')
            if len(data) == 5:
                date_meteo = {
                    'Data': time.strftime("%Y-%m-%d %H:%M:%S"),
                    'Temperatura': float(data[0]),
                    'Umiditate': float(data[1]),
                    'ValoareSenzorMq135': float(data[2]),
                    'CalitateAer': data[4],
                    'IndiceConfort' : data[3]
                }
                save_to_csv(date_meteo)
                save_to_csv_temporary(date_meteo)
except KeyboardInterrupt:
    print("Oprirea memorarii")
