from tkinter import IntVar,Menu,messagebox,PhotoImage
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

a_propos_image=PhotoImage(file='a_propos_menu.png')
exporter_image=PhotoImage(file='exporter_menu.png')
maj_image=PhotoImage(file='maj_menu.png')
ouvrir_image=PhotoImage(file='ouvrir_menu.png')
preferences_image=PhotoImage(file='preferences_menu.png')
quitter_image=PhotoImage(file='quitter_menu.png')
sauvegarder_image=PhotoImage(file='sauvegarder_menu.png')

menuBar=Menu(prgm.root)

menu_fichier=Menu(menuBar,tearoff=0)
menu_edition=Menu(menuBar,tearoff=0)
menu_preference=Menu(menu_edition,tearoff=0)
menu_aide=Menu(menuBar,tearoff=0)

menu_fichier.add_command(label='Enregistrer l\u2019\u00E9quation Ctrl+S',image=sauvegarder_image,compound='left',command=sauvegarder.main)
menu_fichier.add_command(label='Ouvrir une \u00E9quation Ctrl+O',image=ouvrir_image,compound='left',command=ouvrir.main)
menu_fichier.add_separator()
menu_fichier.add_command(label='Exporter l\u2019\u00E9quation Ctrl+Shift+E',image=exporter_image,compound='left',command=exporter.main)
menu_fichier.add_separator()
menu_fichier.add_command(label='Quitter Ctrl+q',image=quitter_image,compound='left',command=quitter.close)
menuBar.add_cascade(label='Fichier',menu=menu_fichier)

menu_preference.add_checkbutton(label='V\u00E9rifier automatiquement les mises à jour',variable=ver_maj,command=lambda:edit_pref.main('ver_maj',str(ver_maj.get()),0))
menu_preference.add_checkbutton(label='Afficher les graphiques',variable=afficher_graphs,command=lambda:edit_pref.main('afficher_graphs',str(afficher_graphs.get()),1))

menu_edition.add_cascade(label='Pr\u00E9f\u00E9rences',image=preferences_image,compound='left',menu=menu_preference)
menuBar.add_cascade(label='\u00C9dition',menu=menu_edition)

menu_aide=Menu(menuBar,tearoff=0)
menu_aide.add_command(label='\u00C0 propos',image=a_propos_image,compound='left',command=a_propos.main)
menu_aide.add_separator()
menu_aide.add_command(label='V\u00E9rifier les mises \u00E0 jour',image=maj_image,compound='left',command=quitter.abt_maj)
menuBar.add_cascade(label='Aide',menu=menu_aide)

prgm.root.config(menu=menuBar)

prgm.root.bind('<Control-s>',sauvegarder.main)
prgm.root.bind('<Control-o>',ouvrir.main)
prgm.root.bind('<Control-q>',quitter.close)
prgm.root.bind('<Control-E>',exporter.main)