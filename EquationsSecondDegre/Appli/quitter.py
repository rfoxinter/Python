import prgm
import urllib.request
import preferences
import __init__

def download():
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
        try:
            prgm.plt.close()
        except:
            pass
    prgm.root.destroy()
    if preferences.ver_maj==1:
        download()
        import version
        root=prgm.Tk()
        if 'DejaVu Sans' in list(prgm.font.families()):
            police=prgm.font.Font(root,family='DejaVu Sans',size=10)
            root.option_add('*Font',police)
        if version.version>prgm.version:
            url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/maj.py'
            urllib.request.urlretrieve(url,'maj.py')
            prgm.Label(root,text='Une mise \u00E0 jour est disponible.',width=50).grid(column=0,row=0)
            bouton_maj=prgm.Button(root,text='Mettre \u00E0 jour l\u2019application',command=__init__.mise_a_jour_quitter)
            bouton_maj.grid(column=0,row=1)
            bouton_fermer=prgm.Button(root,text='Fermer sans mettre \u00E0 jour l\u2019application',command=root.destroy)
            bouton_fermer.grid(column=0,row=2)
            root.title('Mise \u00E0 jour')
            root.resizable(width=False,height=False)
            if prgm.os.name=='nt':
                import ctypes
                ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('equations')
            img=prgm.PhotoImage(file='python.png')
            root.tk.call('wm','iconphoto',root._w,img)
            root.mainloop()
        else:
            root.destroy()

def abt_maj():
    try:
        download()
        prgm.maj_root=prgm.Tk()
        if 'DejaVu Sans' in list(prgm.font.families()):
            police=prgm.font.Font(prgm.maj_root,family='DejaVu Sans',size=10)
            prgm.maj_root.option_add('*Font',police)
        import version
        if version.version>prgm.version:
            url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/maj.py'
            urllib.request.urlretrieve(url,'maj.py')
            prgm.Label(prgm.maj_root,text='Une mise \u00E0 jour est disponible.',width=50).grid(column=0,row=0)
            bouton_maj=prgm.Button(prgm.maj_root,text='Mettre \u00E0 jour l\u2019application',command=__init__.mise_a_jour)
            bouton_maj.grid(column=0,row=2)
            bouton_fermer=prgm.Button(prgm.maj_root,text='Ne pas mettre à jour',command=prgm.maj_root.destroy)
            bouton_fermer.grid(column=0,row=3)
        else:
            prgm.Label(prgm.maj_root,text='L\u2019application est \u00E0 jour.',width=50).grid(column=0,row=0)
            bouton_fermer=prgm.Button(prgm.maj_root,text='Fermer',command=prgm.maj_root.destroy)
            bouton_fermer.grid(column=0,row=2)
        prgm.maj_root.title('Mise \u00E0 jour')
        prgm.maj_root.resizable(width=False,height=False)
        if prgm.os.name=='nt':
            prgm.maj_root.iconbitmap('python.ico')
        prgm.maj_root.mainloop()
    except:
        prgm.maj_root=prgm.Tk()
        if 'DejaVu Sans' in list(prgm.font.families()):
            police=prgm.font.Font(prgm.maj_root,family='DejaVu Sans',size=10)
            prgm.maj_root.option_add('*Font',police)
        prgm.Label(prgm.maj_root,text='Impossible de v\u00E9rifier les mises \u00E0 jour.',width=50).grid(column=0,row=0)
        bouton_fermer=prgm.Button(prgm.maj_root,text='Fermer',command=prgm.maj_root.destroy)
        bouton_fermer.grid(column=0,row=2)
        prgm.maj_root.title('Mise \u00E0 jour')
        prgm.maj_root.resizable(width=False,height=False)
        if prgm.os.name=='nt':
            prgm.maj_root.iconbitmap('python.ico')
        prgm.maj_root.mainloop()
