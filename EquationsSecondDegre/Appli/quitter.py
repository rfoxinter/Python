from tkinter import *
import urllib.request
import __main__

def about_quit():
    __main__.about_root.destroy()

def download():
    #Download version file
    url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/version.py'
    urllib.request.urlretrieve(url, 'version.py')

def close():
    def quit_quit():
        root.destroy()
    __main__.plt.close()
    __main__.root.destroy()
    download()
    import version
    root=Tk()
    root.option_add('*Font', 'Arial 10')
    #Check for a new version
    if version.version>__main__.version:
        url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/maj.pyw'
        urllib.request.urlretrieve(url, 'maj.pyw')
        Label(root,text='Une mise \u00E0 jour est disponible.',width=50).grid(column=0,row=0)
        Label(root,text='Lancer maj.pyw afin de mettre \u00E0 jour  l\u2019application.',width=50).grid(column=0,row=1)
    else:
        root.destroy()
    bouton_fermer=Button(root,text="Fermer",command=quit_quit)
    bouton_fermer.grid(column=0,row=2)
    root.title("Mise \u00E0 jour")
    root.resizable(width=False,height=False)
    root.iconbitmap(r'python.ico')
    root.mainloop()

def abt_maj():
    def quit_quit():
        quit()
    def later():
        maj_root.destroy()
    download()
    maj_root=Tk()
    maj_root.option_add('*Font', 'Arial 10')
    import version
    if version.version>__main__.version:
        url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/maj.pyw'
        urllib.request.urlretrieve(url, 'maj.pyw')
        Label(maj_root,text='Une mise \u00E0 jour est disponible.',width=50).grid(column=0,row=0)
        Label(maj_root,text='Lancer maj.pyw afin de mettre \u00E0 jour  l\u2019application.',width=50).grid(column=0,row=1)
        bouton_maj=Button(maj_root,text="Fermer pour mettre \u00E0 jour  l\u2019application",command=quit_quit)
        bouton_maj.grid(column=0,row=2)
        bouton_fermer=Button(maj_root,text="Ne pas mettre à jour",command=later)
        bouton_fermer.grid(column=0,row=3)
    else:
        Label(maj_root,text='L\u2019application est \u00E0 jour.',width=50).grid(column=0,row=0)
        bouton_fermer=Button(maj_root,text="Fermer",command=later)
        bouton_fermer.grid(column=0,row=2)
    maj_root.title("Mise \u00E0 jour")
    maj_root.resizable(width=False,height=False)
    maj_root.iconbitmap(r'python.ico')
    maj_root.mainloop()

#Close app
def main_quit():
    try:
        about_quit()
        close()
    except:
        close()
