from ctypes import alignment
from datetime import date
import tkinter
from tkinter import INSERT, ttk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from pyparsing import col
from sqlalchemy import column, literal
import wykres

frm = tkinter.Tk()

frm.title("Program")
frm.geometry("800x600")

title = tkinter.Label(frm, text="Pogoda na święta", font=("Times New Roman",20))
title.grid()

lata = [2022-i for i in range(6)]
swieta = ["Nowy Rok", "Wielkanoc", "Święto Pracy", "Boże Ciało"]

pierwszaData = tkinter.IntVar(frm)
pierwszaData.set(lata[len(lata)-1])
drugaData = tkinter.IntVar(frm)
drugaData.set(lata[0])
swietaVar = tkinter.StringVar(frm)
swietaVar.set(swieta[0])

holidayPickerFrame = tkinter.Frame(frm,highlightbackground="black")
holidayPickerFrame.grid()
swietaLabel = tkinter.Label(holidayPickerFrame, text="Wybierz dla jakiego święta chcesz zobaczyć wyniki:")
swietaLabel.grid()
holidayPicker = tkinter.OptionMenu(holidayPickerFrame, swietaVar, *swieta)
holidayPicker.grid()

datePickerFrame = tkinter.Frame(frm,highlightbackground="black")
datePickerFrame.grid()

txt = tkinter.Label(datePickerFrame, text="Wybierz przedział w jakim chcesz zobaczyć wyniki:")
txt.grid(row=0)

txt1 = tkinter.Label(datePickerFrame,text="Od")
txt1.grid(row=1, column=0, sticky="w", columnspan=1)

datePicker1 = tkinter.OptionMenu(datePickerFrame, pierwszaData, *lata)
datePicker1.grid(row=1)

txt2 = tkinter.Label(datePickerFrame,text="do")
txt2.grid(row=2, column=0,sticky="w")

datePicker2 = tkinter.OptionMenu(datePickerFrame, drugaData, *lata)
datePicker2.grid(row=2)

fwykres = tkinter.Frame(frm,highlightbackground="black")
fwykres.grid()



btn = tkinter.Button(datePickerFrame,text="Print", command= lambda: wykres.Wykres.WstawWykres(fwykres,pierwszaData.get(),drugaData.get(),swietaVar.get()))
btn.grid(row=3, column=0)



tkinter.mainloop()