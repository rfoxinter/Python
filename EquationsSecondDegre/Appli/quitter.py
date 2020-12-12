from tkinter import *
import urllib.request
import __main__

def about_quit():
    __main__.about_root.destroy()

def download():
    #List of files to be downloaded
    extension=['.py','.pyw']
    filename=[['version'],['maj']]

    #Download the files listed
    for k in range(len(extension)):
        for i in range(len(filename[k])):
            url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/'+filename[k][i]+extension[k]
            urllib.request.urlretrieve(url, filename[k][i]+extension[k])

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
