import urllib.request
from tkinter import *

root=Tk()

def quit():
	root.destroy()

filename=['__main__','maj']
for i in range(len(filename)):
	url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/'+filename[i]+'.py'
	urllib.request.urlretrieve(url, filename[i]+'.py')

root.title("Mise \u00E0 jour")
Label(root,text='L\u2019application \u00E0 bien \u00E9t\u00E9 mise \u00E0 jour.',width=50).grid(column=0,row=0)
bouton_ok=Button(root,text="Ok",command=quit)
bouton_ok.grid(column=0,row=2)
root.resizable(width=False,height=False)
root.iconbitmap(r'python.ico')
root.mainloop()
