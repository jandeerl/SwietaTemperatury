from ctypes import alignment
from datetime import date
import tkinter
from tkinter import INSERT, ttk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from pyparsing import col
from sqlalchemy import column, literal
import Services

class Wykres:
    @staticmethod
    def WstawWykres(frame, pierwszaData, drugaData, swietaVar):
        slownik = Services.Service.get_data(pierwszaData,drugaData,swietaVar)
        keys = [key for key in slownik.keys()]
        values = [value for value in slownik.values()]
        figure1 = plt.Figure(figsize=(5,4), dpi=100)
        dane = {"Temperatura" : values, "Data" : keys}
        df1 = DataFrame(dane, columns=["Data","Temperatura"])
        ax1 = figure1.add_subplot(111)
        bar1 = FigureCanvasTkAgg(figure1, frame)
        bar1.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        df1 = df1[['Data','Temperatura']].groupby('Data').sum()
        df1.plot(kind='bar', legend=True, ax=ax1, rot=0  )
        ax1.set_title('Pogoda na %s' % (swietaVar))
