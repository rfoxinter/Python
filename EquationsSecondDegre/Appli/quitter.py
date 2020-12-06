import urllib.request
from tkinter import *
import __main__

def main_quit():
    def quit_quit():
        root.destroy()
    __main__.plt.close()
    __main__.root.destroy()
    url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/main_version.py'
    urllib.request.urlretrieve(url, 'main_version.py')
    import main_version
    root=Tk()
    if main_version.version>__main__.version:
        Label(root,text='Une mise \u00E0 jour est disponible.',width=50).grid(column=0,row=0)
        Label(root,text='Lancer main_maj.py afin de mettre \u00E0 jour  l\u2019application.',width=50).grid(column=0,row=1)
    else:
        Label(root,text='L\u2019application est \u00E0 jour.',width=50).grid(column=0,row=0)
    bouton_ok=Button(root,text="Ok",command=quit_quit)
    bouton_ok.grid(column=0,row=2)
    root.title("Mise \u00E0 jour")
    root.resizable(width=False,height=False)
    root.iconbitmap(r'python.ico')
    root.mainloop()

def maj_quit():
    __main__.root_maj.destroy()
