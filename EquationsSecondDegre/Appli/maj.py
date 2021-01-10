from tkinter import Tk,Label,Button
import urllib.request
import os

ttl=0

def title(act):
    root.title('Mise \u00E0 jour en cours ('+str(act)+'/'+str(ttl)+')')

#List of files to be downloaded
extension=['.py','.ico']
filename=[['a_propos','entier','entier_deux_racines_plt','entier_pas_racine','entier_x0','entier_x1','entier_x2','exporter','fraction','fraction_deux_racines_plt','fraction_pas_racine','fraction_x0','fraction_x1','fraction_x1_delta_denom_entier','fraction_x1_delta_num_entier','fraction_x1_sinon','fraction_x2','maj','menu','ouvrir','prgm','quitter','sauvegarder','version','extensions\u002F__init__','extensions\u002Fhtml','extensions\u002Frtf','extensions\u002Ftex','extensions\u002Ftxt'],['a_propos','avertissement','python']]

def maj_pref():
    root=Tk()
    root.option_add('*Font','Arial 10')
    Label(root,text='',width=50).grid(column=0,row=1)
    bouton_ok=Button(root,text='Fermer',command=root.destroy)
    bouton_ok.grid(column=0,row=2)
    root.resizable(width=False,height=False)
    root.iconbitmap(r'python.ico')
    root.mainloop()
    local_pref=open(r'preferences.py','r')
    local_lines=local_pref.readlines()
    url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/preferences.py'
    urllib.request.urlretrieve(url,'preferences_maj.py')
    maj_pref=open('preferences_maj.py','r')
    maj_lines=maj_pref.readlines()
    if len(local_lines)<len(maj_lines):
        for i in range(len(maj_lines)-len(local_lines)):
            local_lines.append(maj_lines[len(local_lines)+i])
            local_pref=open(r'preferences.py','w')
            local_pref.writelines(local_lines)
            local_pref.close()
    maj_pref.close()
    os.remove(r'preferences_maj.py')

def down():
    root=Tk()
    root.option_add('*Font','Arial 10')
    Label(root,text='',width=50).grid(column=0,row=1)
    bouton_ok=Button(root,text='Fermer',command=root.destroy)
    bouton_ok.grid(column=0,row=2)
    root.resizable(width=False,height=False)
    root.iconbitmap(r'python.ico')
    root.mainloop()
    act=0
    try:
        if os.path.exists('extensions')==False:
            os.mkdir('extensions')
        Label(root,text='T\u00E9l\u00E9chargement de la mise \u00E0 jour en cours.').grid(column=0,row=0)
        #Download the files listed
        for k in range(len(filename)):
            for i in range(len(filename[k])):
                url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/'+filename[k][i]+extension[k]
                urllib.request.urlretrieve(url,filename[k][i]+extension[k])
                act=act+1
                title(act)
        maj_pref()
        for label in root.grid_slaves():
            if int(label.grid_info()['row'])==0:
                label.destroy()
        Label(root,text='L\u2019application \u00E0 bien \u00E9t\u00E9 mise \u00E0 jour.').grid(column=0,row=0)
    except:
        Label(root,text='Une erreur est survenue lors de la mise \u00E0 jour.').grid(column=0,row=0)

for k in range(len(extension)):
    ttl=ttl+len(filename[k])
