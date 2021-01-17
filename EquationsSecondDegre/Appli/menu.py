from tkinter import IntVar,Menu,messagebox
import os
import prgm
import quitter
import a_propos
import sauvegarder
import ouvrir
import preferences
import exporter
import edit_pref

ver_maj=IntVar()
ver_maj.set(preferences.ver_maj)
afficher_graphs=IntVar()
afficher_graphs.set(preferences.afficher_graphs)



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

menu_preference.add_checkbutton(label='V\u00E9rifier automatiquement les mises à jour',variable=ver_maj,command=lambda:edit_pref.main('ver_maj',str(ver_maj.get()),0))
menu_preference.add_checkbutton(label='Afficher les graphiques',variable=afficher_graphs,command=lambda:edit_pref.main('afficher_graphs',str(afficher_graphs.get()),1))

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