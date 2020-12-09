from tkinter import *
import urllib.request

root=Tk()
root.option_add('*Font', 'Arial 10')

def quit():
	root.destroy()

#List of files to be downloaded
filename=[['__main__','entier','entier_deux_racines_plt','entier_pas_racine','entier_x0','entier_x1','entier_x2','fraction','fraction_deux_racines_plt','fraction_pas_racine','fraction_x0','fraction_x1','fraction_x1_delta_denom_entier','fraction_x1_delta_num_entier','fraction_x1_sinon','fraction_x2','version','quitter'],['a_propos'],['a_propos','python']]

#Download the files listed
for i in range(len(filename[0])):
    url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/'+filename[0][i]+'.py'
    urllib.request.urlretrieve(url, filename[0][i]+'.py')
for i in range(len(filename[1])):
    url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/'+filename[1][i]+'.gif'
    urllib.request.urlretrieve(url, filename[1][i]+'.gif')
for i in range(len(filename[1])):
    url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/'+filename[2][i]+'.ico'
    urllib.request.urlretrieve(url, filename[2][i]+'.ico')

root.title("Mise \u00E0 jour")
Label(root,text='L\u2019application \u00E0 bien \u00E9t\u00E9 mise \u00E0 jour.',width=50).grid(column=0,row=0)
bouton_ok=Button(root,text="Ok",command=quit)
bouton_ok.grid(column=0,row=2)
root.resizable(width=False,height=False)
root.iconbitmap(r'python.ico')
root.mainloop()
