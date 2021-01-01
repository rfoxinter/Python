from tkinter import *
import urllib.request
import __main__
import quitter

#Close app
def main():
    __main__.about_root=Tk()
    __main__.about_root.option_add('*Font', 'Arial 10')
    Label(__main__.about_root,text='Version actuelle\u00A0:\u00A0'+str(__main__.version)).grid(column=0,row=0,sticky='w')
    Label(__main__.about_root,text='-\u00A0Ajout d\u2019une option pour exporter les \u00E9quations.').grid(column=0,row=1,sticky='w')
    Label(__main__.about_root,text='-\u00A0Am\u00E9lioration de la fonction quitter.').grid(column=0,row=2,sticky='w')
    Label(__main__.about_root,width=50).grid(column=0,row=9)
    bouton_fermer=Button(__main__.about_root,text="Fermer",command=quitter.about_quit)
    bouton_fermer.grid(column=0,row=10)
    __main__.about_root.title("\u00C0 propos")
    __main__.about_root.resizable(width=False,height=False)
    __main__.about_root.iconbitmap(r'a_propos.ico')
    __main__.about_root.mainloop()
