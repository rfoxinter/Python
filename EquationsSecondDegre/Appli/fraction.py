from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import __main__

def main_frac():
    __main__.plt.close()
    for label in __main__.Fen.grid_slaves():
        if int(label.grid_info()["column"])==6:
            label.destroy()
    Col7=Label(__main__.Fen,width=40)
    Col7.grid(column=6,row=5)
    L1=Label(__main__.Fen,text='Fonction actuellement indisponible.')
    L1.grid(column=6,row=0,sticky='w')
