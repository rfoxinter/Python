from tkinter import Tk,Label,Button
import prgm
import preferences
import os
import sys

def redemarrage():
    try:
        import matplotlib.pyplot as plt
    except:
        prgm.redemarrage=Tk()
        prgm.redemarrage.option_add('*Font','Arial 10')
        prgm.redemarrage.title('Avertissement')
        Label(prgm.redemarrage,text='Un red\u00E9marrage de l\u2019application est n\u00E9cessaire',width=50).grid(column=0,row=0)
        bouton_redemarrer=Button(prgm.redemarrage,text='Red\u00E9marrer l\u2019application',command=lambda:os.execl(sys.executable,sys.executable,*sys.argv))
        bouton_redemarrer.grid(column=0,row=1)
        bouton_fermer=Button(prgm.redemarrage,text='Red\u00E9marrer plus tard',command=prgm.redemarrage.destroy)
        bouton_fermer.grid(column=0,row=2)
        prgm.redemarrage.resizable(width=False,height=False)
        if os.name=='nt':
            prgm.redemarrage.iconbitmap(r'avertissement.ico')
        prgm.redemarrage.mainloop()

def main(var,val,line):
    file=open('preferences.py','r')
    list_of_lines=file.readlines()
    list_of_lines[line]=var+'='+val+'\n'
    file=open('preferences.py','w')
    file.writelines(list_of_lines)
    file.close()
    import importlib
    importlib.reload(preferences)
    if var=='afficher_graphs':
        redemarrage()