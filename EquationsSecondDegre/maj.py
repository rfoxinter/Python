import importlib
import urllib.request
import os
import edit_pref

def maj_pref():
    local_pref=open('preferences.py','r')
    local_lines=local_pref.readlines()
    url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/preferences.py'
    urllib.request.urlretrieve(url,'preferences_maj.py')
    maj_pref=open('preferences_maj.py','r')
    maj_lines=maj_pref.readlines()
    if len(local_lines)<len(maj_lines):
        for i in range(len(maj_lines)-len(local_lines)):
            local_lines.append(maj_lines[len(local_lines)])
            local_pref=open('preferences.py','w')
            local_pref.writelines(local_lines)
            local_pref.close()
    maj_pref.close()
    os.remove('preferences_maj.py')

def down():
    extension=['.py','.ico','.png','.xml','.rels']
    filename=[['a_propos','dejavusans','edit_pref','entier','entier_deux_racines_plt','entier_equation','entier_pas_racine','entier_x0','entier_x1','entier_x2','erreur','exporter','exporter_graph','fraction','fraction_deux_racines_plt','fraction_equation','fraction_pas_racine','fraction_x0','fraction_x1','fraction_x1_delta_denom_entier','fraction_x1_delta_num_entier','fraction_x1_sinon','fraction_x2','fraction_x2_delta_denom_entier','fraction_x2_delta_num_entier','fraction_x2_sinon','linux_distribution','maj','menu','ouvrir','packages','packages_linux','prgm','quitter','sauvegarder','version','extensions/__init__','extensions/docx','extensions/html','extensions/rtf','extensions/tex','extensions/txt','extensions/xhtml','images/__init__','images/jpg','images/png'],['a_propos','avertissement','python'],['a_propos_menu','coller_menu','copier_menu','couper_menu','exporter_menu','maj_menu','ouvrir_menu','package','preferences_menu','python','quitter_menu','sauvegarder_menu'],['extensions/docx/[Content_Types]','extensions/docx/numbering','extensions/docx/styles'],['extensions/docx/','extensions/docx/document.xml']]
    try:
        if not os.path.exists('extensions'):
            os.mkdir('extensions')
        if not os.path.exists('extensions/docx'):
            os.mkdir('extensions/docx')
        if not os.path.exists('images'):
            os.mkdir('images')
        #Download the files listed
        for k in range(len(extension)):
            for i in range(len(filename[k])):
                url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/'+filename[k][i]+extension[k]
                urllib.request.urlretrieve(url,filename[k][i]+extension[k])
        maj_pref()
        importlib.reload(edit_pref)
        edit_pref.main('etat_maj',"'L\\u2019application a bien \\u00E9t\\u00E9 mise \\u00E0 jour.'",2)
    except:
        importlib.reload(edit_pref)
        edit_pref.main('etat_maj',"'Une erreur est survenue lors de la mise \\u00E0 jour.'",2)
