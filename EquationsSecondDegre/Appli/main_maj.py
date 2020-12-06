import urllib.request
from tkinter import *

def quit():
	root.destroy()

filename=['__main__','maj']
for i in range(len(filename)):
	url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/'+filename[i]+'.py'
	urllib.request.urlretrieve(url, filename[i]+'.py')

root_maj=Tk()
root_maj.title("Mise \u00E0 jour")
Label(root_maj,text='L\u2019application \u00E0 bien \u00E9t\u00E9 mise \u00E0 jour.',width=50).grid(column=0,row=0)
bouton_oui=Button(root_maj,text="Oui",command=maj)
bouton_oui.grid(column=0,row=1)
bouton_ok=Button(root_maj,text="Ok",command=quit)
bouton_ok.grid(column=0,row=2)
root_maj.resizable(width=False,height=False)
root_maj.iconbitmap(r'python.ico')
root_maj.mainloop()
