from tkinter import Tk,Label,Button,IntVar,Menu,messagebox
import __main__
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
    __main__.redemarrage=Tk()
    __main__.redemarrage.option_add('*Font','Arial 10')
    __main__.redemarrage.title('Avertissement')
    Label(__main__.redemarrage,text='Un red\u00E9marrage de l\u2019application est n\u00E9cessaire',width=50).grid(column=0,row=0)
    bouton_fermer=Button(__main__.redemarrage,text='Fermer',command=quitter.redemarrage_quit)
    bouton_fermer.grid(column=0,row=2)
    __main__.redemarrage.resizable(width=False,height=False)
    __main__.redemarrage.iconbitmap(r'avertissement.ico')
    __main__.redemarrage.mainloop()

def edit_ver_maj():
    file=open('preferences.py','r')
    list_of_lines=file.readlines()
    list_of_lines[0]='ver_maj='+str(ver_maj.get())+'\n'
    file=open('preferences.py','w')
    file.writelines(list_of_lines)
    file.close()

def edit_afficher_graphs():
    file=open('preferences.py','r')
    list_of_lines=file.readlines()
    list_of_lines[1]='afficher_graphs='+str(afficher_graphs.get())+'\n'
    file=open('preferences.py','w')
    file.writelines(list_of_lines)
    file.close()
    redemarrage()

menuBar=Menu(__main__.root)

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

menu_preference.add_checkbutton(label='V\u00E9rifier automatiquement les mises à jour',variable=ver_maj,command=edit_ver_maj)
menu_preference.add_checkbutton(label='Afficher les graphiques',variable=afficher_graphs,command=edit_afficher_graphs)

menu_edition.add_cascade(label='Pr\u00E9f\u00E9rences',menu=menu_preference)
menuBar.add_cascade(label='\u00C9dition',menu=menu_edition)

menu_aide=Menu(menuBar,tearoff=0)
menu_aide.add_command(label='\u00C0 propos',command=a_propos.main)
menu_aide.add_separator()
menu_aide.add_command(label='V\u00E9rifier les mises \u00E0 jour',command=quitter.abt_maj)
menuBar.add_cascade(label='Aide',menu=menu_aide)

__main__.root.config(menu=menuBar)

__main__.root.bind('<Control-s>',sauvegarder.main)
__main__.root.bind('<Control-o>',ouvrir.main)
__main__.root.bind('<Control-q>',quitter.close)
__main__.root.bind('<Control-E>',exporter.main)