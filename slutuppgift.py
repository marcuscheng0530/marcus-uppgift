import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt

def data():
    dataset = pd.read_csv("covid_19_india.csv")
    dataset
    df = pd.read_csv('covid_19_india.csv')
    stad = input("skriv en stad du vill kolla information på, DU kan välja mellan Kerala, Delhi, Haryana, Telengana, Rajasthan och Telengana\n")
    kerala_data = df[df['State/UnionTerritory'] == stad]
    print(kerala_data)
    
data()

def graf():
    x_axel = input("vad vill du ska vara på x alxen på grafen. Du kan välja mellan [Date, Time, State/UnionTerritory, ConfirmedIndianNational, ConfirmedForeignNational, Cured, Deaths, Confirmed]\n\n")
    y_axel = input("vad vill du ska vara på y axlen på grafen. Du kan välja mellan [Date, Time, State/UnionTerritory, ConfirmedIndianNational, ConfirmedForeignNational, Cured, Deaths, Confirmed]\n\n")

    df = pd.read_csv('covid_19_india.csv')

    x_axel = df['Date']
    y_axel = df['Confirmed']

    plt.plot(y_axel, x_axel)
    plt.xlabel(x_axel)
    plt.ylabel(y_axel)
    plt.title('COVID-19 Cases in India')
    plt.xticks(rotation=45)  
    plt.grid(True) 
    plt.show()

#graf()
