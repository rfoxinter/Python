import urllib.request
from tkinter import *
import __main__

root=Tk()

def main_quit():
    __main__.plt.close()
    __main__.root.destroy()
    url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/main_version.py'
    urllib.request.urlretrieve(url, 'main_version.py')
    import main_version
    if main_version.version>__main__.version:
        root_maj=Tk()
        root_maj.title("Mise \u00E0 jour")
        Label(root_maj,text='Une mise \u00E0 jour est disponible.',width=40).grid(column=0,row=0)
        Label(root_maj,text='Lancer main_maj.py afin de mettre \u00E0 jour  l\u2019application.',width=40).grid(column=0,row=1)
        bouton_ok=Button(root_maj,text="Ok",command=quitter.maj_quit)
        bouton_ok.grid(column=0,row=2)
        root_maj.resizable(width=False,height=False)
        root_maj.iconbitmap(r'python.ico')
        root_maj.mainloop()

def maj_quit():
    __main__.root_maj.destroy()

def quit_maj_quit():
    root.destroy()
