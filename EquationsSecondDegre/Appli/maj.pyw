from tkinter import *
import urllib.request

root=Tk()
root.option_add('*Font', 'Arial 10')

ttl=0

def quit():
	root.destroy()

def title(act):
    root.title('Mise \u00E0 jour ('+str(act)+'/'+str(ttl)+')')

#List of files to be downloaded
extension=['.py','.pyw','.ico']
filename=[['a_propos','entier','entier_deux_racines_plt','entier_pas_racine','entier_x0','entier_x1','entier_x2','fraction','fraction_deux_racines_plt','fraction_pas_racine','fraction_x0','fraction_x1','fraction_x1_delta_denom_entier','fraction_x1_delta_num_entier','fraction_x1_sinon','fraction_x2','version','quitter'],['a_propos'],['a_propos','python']]

def down():
    act=0
    for label in root.grid_slaves():
        if int(label.grid_info()["row"])==0:
            label.destroy()
    try:
        Label(root,text='T\u00E9l\u00E9chargement de la mise \u00E0 jour en cours.').grid(column=0,row=0)
        #Download the files listed
        for k in range(len(filename)):
            for i in range(len(filename[k])):
                url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/'+filename[k][i]+extension[k]
                urllib.request.urlretrieve(url, filename[k][i]+extension[k])
                act=act+1
                title(act)
        for label in root.grid_slaves():
            if int(label.grid_info()["row"])==0:
                label.destroy()
        Label(root,text='L\u2019application \u00E0 bien \u00E9t\u00E9 mise \u00E0 jour.').grid(column=0,row=0)
    except:
        Label(root,text='Une erreur est survenue lors de la mise \u00E0 jour.').grid(column=0,row=0)

for k in range(len(extension)):
    ttl=ttl+len(filename[k])

btn_maj=Button(root,text="T\u00E9l\u00E9charger la derni\u00E8re version",command=down)
btn_maj.grid(column=0,row=0)
Label(root,text='',width=50).grid(column=0,row=1)
root.title('Mise \u00E0 jour')
bouton_ok=Button(root,text="Ok",command=quit)
bouton_ok.grid(column=0,row=2)
root.resizable(width=False,height=False)
root.iconbitmap(r'python.ico')
root.mainloop()
