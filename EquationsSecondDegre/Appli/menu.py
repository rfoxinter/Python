from tkinter import Menu,IntVar
import __main__
import quitter
import a_propos
import sauvegarder
import ouvrir
import preferences

ver_maj=IntVar()
ver_maj.set(preferences.ver_maj)

def edit_ver_maj():
    file=open('preferences.py','r')
    list_of_lines =file.readlines()
    list_of_lines[0]='ver_maj='+str(ver_maj.get())
    file=open('preferences.py','w')
    file.writelines(list_of_lines)
    file.close()

menuBar=Menu(__main__.root)

menu_fichier=Menu(menuBar,tearoff=0)
menu_edition=Menu(menuBar,tearoff=0)
menu_preference=Menu(menu_edition,tearoff=0)
menu_aide=Menu(menuBar,tearoff=0)

menu_fichier.add_command(label='Enregistrer l\u2019\u00E9quation Ctrl+S',command=sauvegarder.main)
menu_fichier.add_command(label='Ouvrir une \u00E9quation Ctrl+O',command=ouvrir.main)
menu_fichier.add_separator()
menu_fichier.add_command(label='Quitter Ctrl+q',command=quitter.close)
menuBar.add_cascade(label='Fichier',menu=menu_fichier)

menu_preference.add_checkbutton(label='V\u00E9rifier automatiquement les mises à jour',variable=ver_maj,command=edit_ver_maj)

menu_edition.add_cascade(label='Pr\u00E9f\u00E9rences',menu=menu_preference)
menuBar.add_cascade(label='\u00C9dition',menu=menu_edition)

menu_aide=Menu(menuBar,tearoff=0)
menu_aide.add_command(label='\u00C0 propos',command=a_propos.main)
menu_aide.add_separator()
menu_aide.add_command(label='V\u00E9rifier les mises \u00E0 jour',command=quitter.abt_maj)
menuBar.add_cascade(label='Aide',menu=menu_aide)

__main__.root.config(menu=menuBar)

__main__.root.bind('<Control-s>',sauvegarder.ctrl_s)
__main__.root.bind('<Control-o>',ouvrir.ctrl_o)
__main__.root.bind('<Control-q>',quitter.ctrl_q)