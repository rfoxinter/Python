from tkinter import Tk,Label,Button
import urllib.request
import __main__
import preferences

def about_quit():
    __main__.about_root.destroy()

def download():
    #Download version file
    url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/version.py'
    urllib.request.urlretrieve(url,'version.py')

def close():
    try:
        __main__.about_root.destroy()
    except:
        pass
    try:
        __main__.maj_root.destroy()
    except:
        pass
    __main__.plt.close()
    __main__.root.destroy()
    if preferences.ver_maj==1:
        def quit_quit():
            root.destroy()
        download()
        import version
        root=Tk()
        root.option_add('*Font','Arial 10')
        #Check for a new version
        if version.version>__main__.version:
            url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/maj.pyw'
            urllib.request.urlretrieve(url,'maj.pyw')
            Label(root,text='Une mise \u00E0 jour est disponible.',width=50).grid(column=0,row=0)
            Label(root,text='Lancer maj.pyw afin de mettre \u00E0 jour  l\u2019application.',width=50).grid(column=0,row=1)
        else:
            root.destroy()
        bouton_fermer=Button(root,text='Fermer',command=quit_quit)
        bouton_fermer.grid(column=0,row=2)
        root.title('Mise \u00E0 jour')
        root.resizable(width=False,height=False)
        root.iconbitmap(r'python.ico')
        root.mainloop()

def abt_maj():
    def quit_quit():
        quit()
    def later():
        __main__.maj_root.destroy()
    download()
    __main__.maj_root=Tk()
    __main__.maj_root.option_add('*Font','Arial 10')
    import version
    if version.version>__main__.version:
        url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/maj.pyw'
        urllib.request.urlretrieve(url,'maj.pyw')
        Label(__main__.maj_root,text='Une mise \u00E0 jour est disponible.',width=50).grid(column=0,row=0)
        Label(__main__.maj_root,text='Lancer maj.pyw afin de mettre \u00E0 jour  l\u2019application.',width=50).grid(column=0,row=1)
        bouton_maj=Button(__main__.maj_root,text='Fermer pour mettre \u00E0 jour  l\u2019application',command=quit_quit)
        bouton_maj.grid(column=0,row=2)
        bouton_fermer=Button(__main__.maj_root,text='Ne pas mettre à jour',command=later)
        bouton_fermer.grid(column=0,row=3)
    else:
        Label(__main__.maj_root,text='L\u2019application est \u00E0 jour.',width=50).grid(column=0,row=0)
        bouton_fermer=Button(__main__.maj_root,text='Fermer',command=later)
        bouton_fermer.grid(column=0,row=2)
    __main__.maj_root.title('Mise \u00E0 jour')
    __main__.maj_root.resizable(width=False,height=False)
    __main__.maj_root.iconbitmap(r'python.ico')
    __main__.maj_root.mainloop()

def ctrl_q(event):
    close()
