from tkinter import *
import urllib.request
import __main__

def download():
    #List of files to be downloaded
    filename=['maj','version']

    #Download the files listed
    for i in range(len(filename)):
        url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/'+filename[i]+'.py'
        urllib.request.urlretrieve(url, filename[i]+'.py')
#Close app
def main_quit():
    def quit_quit():
        root.destroy()
    __main__.plt.close()
    __main__.root.destroy()
    download()
    import version
    root=Tk()
    #Check for a new version
    if main_version.version>__main__.version:
        Label(root,text='Une mise \u00E0 jour est disponible.',width=50).grid(column=0,row=0)
        Label(root,text='Lancer maj.py afin de mettre \u00E0 jour  l\u2019application.',width=50).grid(column=0,row=1)
    else:
        root.destroy()
    bouton_ok=Button(root,text="Ok",command=quit_quit)
    bouton_ok.grid(column=0,row=2)
    root.title("Mise \u00E0 jour")
    root.resizable(width=False,height=False)
    root.iconbitmap(r'python.ico')
    root.mainloop()
