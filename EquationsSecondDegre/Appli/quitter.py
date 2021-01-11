from tkinter import Tk,Label,Button,PhotoImage
import os
import urllib.request
import prgm
import preferences
import __init__

def about_quit():
    prgm.about_root.destroy()

def redemarrage_quit():
    prgm.redemarrage.destroy()

def download():
    #Download version file
    url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/version.py'
    urllib.request.urlretrieve(url,'version.py')

def close(event=None):
    try:
        prgm.about_root.destroy()
    except:
        pass
    try:
        prgm.maj_root.destroy()
    except:
        pass
    try:
        prgm.redemarrage.destroy()
    except:
        pass
    if preferences.afficher_graphs==1:
        prgm.plt.close()
    prgm.root.destroy()
    if preferences.ver_maj==1:
        download()
        import version
        root=Tk()
        root.option_add('*Font','Arial 10')
        #Check for a new version
        if version.version>prgm.version:
            url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/maj.py'
            urllib.request.urlretrieve(url,'maj.py')
            import importlib
            importlib.reload(maj)
            Label(root,text='Une mise \u00E0 jour est disponible.',width=50).grid(column=0,row=0)
        else:
            root.destroy()
        bouton_maj=Label(root,text='Mettre \u00E0 jour  l\u2019application.',width=50,command=__init__.mise_a_jour_quitter)
        bouton_maj.grid(column=0,row=1)
        bouton_fermer=Button(root,text='Fermer sans mettre \u00E0 jour  l\u2019application',command=root.destroy)
        bouton_fermer.grid(column=0,row=2)
        root.title('Mise \u00E0 jour')
        root.resizable(width=False,height=False)
        if os.name=='nt':
            prgm.maj_root.iconbitmap(r'python.ico')
        else:
            img=PhotoImage(file='python.png')
            root.tk.call('wm','iconphoto',root._w,img)
        root.mainloop()

def abt_maj():
    download()
    prgm.maj_root=Tk()
    prgm.maj_root.option_add('*Font','Arial 10')
    import version
    if version.version>prgm.version:
        url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/maj.py'
        urllib.request.urlretrieve(url,'maj.py')
        import importlib
        importlib.reload(maj)
        Label(prgm.maj_root,text='Une mise \u00E0 jour est disponible.',width=50).grid(column=0,row=0)
        bouton_maj=Button(prgm.maj_root,text='Mettre \u00E0 jour l\u2019application',command=__init__.mise_a_jour)
        bouton_maj.grid(column=0,row=2)
        bouton_fermer=Button(prgm.maj_root,text='Ne pas mettre à jour',command=prgm.maj_root.destroy)
        bouton_fermer.grid(column=0,row=3)
    else:
        Label(prgm.maj_root,text='L\u2019application est \u00E0 jour.',width=50).grid(column=0,row=0)
        bouton_fermer=Button(prgm.maj_root,text='Fermer',command=prgm.maj_root.destroy)
        bouton_fermer.grid(column=0,row=2)
    prgm.maj_root.title('Mise \u00E0 jour')
    prgm.maj_root.resizable(width=False,height=False)
    if os.name=='nt':
        prgm.maj_root.iconbitmap(r'python.ico')
    prgm.maj_root.mainloop()
