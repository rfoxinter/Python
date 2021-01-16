from tkinter import Label
import urllib.request
import os

def maj_pref():
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
    extension=['.py','.ico','.png','.xml','.rels']
    filename=[['a_propos','entier','entier_deux_racines_plt','entier_pas_racine','entier_x0','entier_x1','entier_x2','exporter','fraction','fraction_deux_racines_plt','fraction_pas_racine','fraction_x0','fraction_x1','fraction_x1_delta_denom_entier','fraction_x1_delta_num_entier','fraction_x1_sinon','fraction_x2','linux_distribution','maj','menu','ouvrir','packages','packages_linux','prgm','quitter','sauvegarder','version','extensions/__init__','extensions/docx','extensions/html','extensions/rtf','extensions/tex','extensions/txt','extensions/xhtml'],['a_propos','avertissement','package','python'],['python','package'],['extensions/docx/[Content_Types]','extensions/docx/numbering','extensions/docx/styles'],['extensions/docx/','extensions/docx/document.xml']]
    try:
        if os.path.exists('extensions')==False:
            os.mkdir('extensions')
        #Download the files listed
        for k in range(len(extension)):
            for i in range(len(filename[k])):
                url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/'+filename[k][i]+extension[k]
                urllib.request.urlretrieve(url,filename[k][i]+extension[k])
        maj_pref()
    except:
        import prgm
        Label(prgm.maj_root,text='Une mise \u00E0 jour est disponible.',width=50).grid(column=0,row=0)
