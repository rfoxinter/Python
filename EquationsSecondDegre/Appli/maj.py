from tkinter import *
import urllib.request

root=Tk()

def quit():
	root.destroy()

#List of files to be downloaded
filename=['__main__','entier','entier_deux_racines_plt','entier_pas_racine','entier_x0','entier_x1','entier_x2','fraction','fraction_deux_racines_plt','fraction_pas_racine','fraction_x0','fraction_x1','fraction_x1_delta_denom_entier','fraction_x1_delta_num_entier','fraction_x1_sinon','fraction_x2','version','quitter']

#Download the files listed
for i in range(len(filename)):
    url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/'+filename[i]+'.py'
    urllib.request.urlretrieve(url, filename[i]+'.py')
url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/python.ico'
urllib.request.urlretrieve(url, 'python.ico')

root.title("Mise \u00E0 jour")
Label(root,text='L\u2019application \u00E0 bien \u00E9t\u00E9 mise \u00E0 jour.',width=50).grid(column=0,row=0)
bouton_ok=Button(root,text="Ok",command=quit)
bouton_ok.grid(column=0,row=2)
root.resizable(width=False,height=False)
root.iconbitmap(r'python.ico')
root.mainloop()
