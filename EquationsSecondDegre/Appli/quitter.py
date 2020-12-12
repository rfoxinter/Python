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
    bouton_ok=Button(root,text="Ok",command=quit_quit)
    bouton_ok.grid(column=0,row=2)
    root.title("Mise \u00E0 jour")
    root.resizable(width=False,height=False)
    root.iconbitmap(r'python.ico')
    root.mainloop()

#Close app
def main_quit():
    try:
        about_quit()
        close()
    except:
        close()
