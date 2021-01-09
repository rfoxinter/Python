from tkinter import Tk,Label,Button,IntVar,Menu,messagebox
import prgm
import quitter
import a_propos
import sauvegarder
import ouvrir
import preferences
import exporter

ver_maj=IntVar()
ver_maj.set(preferences.ver_maj)
afficher_graphs=IntVar()
afficher_graphs.set(preferences.afficher_graphs)

def redemarrage():
    try:
        import matplotlib.pyplot as plt
    except:
        prgm.redemarrage=Tk()
        prgm.redemarrage.option_add('*Font','Arial 10')
        prgm.redemarrage.title('Avertissement')
        Label(prgm.redemarrage,text='Un red\u00E9marrage de l\u2019application est n\u00E9cessaire',width=50).grid(column=0,row=0)
        bouton_fermer=Button(prgm.redemarrage,text='Fermer',command=quitter.redemarrage_quit)
        bouton_fermer.grid(column=0,row=2)
        prgm.redemarrage.resizable(width=False,height=False)
        prgm.redemarrage.iconbitmap(r'avertissement.ico')
        prgm.redemarrage.mainloop()

def edit_pref(var,val,line):
    file=open('preferences.py','r')
    list_of_lines=file.readlines()
    list_of_lines[line]=var+'='+val+'\n'
    file=open('preferences.py','w')
    file.writelines(list_of_lines)
    file.close()
    import importlib
    importlib.reload(preferences)
    if var=='afficher_graphs':
        redemarrage()

menuBar=Menu(prgm.root)

menu_fichier=Menu(menuBar,tearoff=0)
menu_edition=Menu(menuBar,tearoff=0)
menu_preference=Menu(menu_edition,tearoff=0)
menu_aide=Menu(menuBar,tearoff=0)

menu_fichier.add_command(label='Enregistrer l\u2019\u00E9quation Ctrl+S',command=sauvegarder.main)
menu_fichier.add_command(label='Ouvrir une \u00E9quation Ctrl+O',command=ouvrir.main)
menu_fichier.add_separator()
menu_fichier.add_command(label='Exporter l\u2019\u00E9quation Ctrl+Shift+E',command=exporter.main)
menu_fichier.add_separator()
menu_fichier.add_command(label='Quitter Ctrl+q',command=quitter.close)
menuBar.add_cascade(label='Fichier',menu=menu_fichier)

menu_preference.add_checkbutton(label='V\u00E9rifier automatiquement les mises à jour',variable=ver_maj,command=lambda:edit_pref('ver_maj',str(ver_maj.get()),0))
menu_preference.add_checkbutton(label='Afficher les graphiques',variable=afficher_graphs,command=lambda:edit_pref('afficher_graphs',str(afficher_graphs.get()),1))

menu_edition.add_cascade(label='Pr\u00E9f\u00E9rences',menu=menu_preference)
menuBar.add_cascade(label='\u00C9dition',menu=menu_edition)

menu_aide=Menu(menuBar,tearoff=0)
menu_aide.add_command(label='\u00C0 propos',command=a_propos.main)
menu_aide.add_separator()
menu_aide.add_command(label='V\u00E9rifier les mises \u00E0 jour',command=quitter.abt_maj)
menuBar.add_cascade(label='Aide',menu=menu_aide)

prgm.root.config(menu=menuBar)

prgm.root.bind('<Control-s>',sauvegarder.main)
prgm.root.bind('<Control-o>',ouvrir.main)
prgm.root.bind('<Control-q>',quitter.close)
prgm.root.bind('<Control-E>',exporter.main)