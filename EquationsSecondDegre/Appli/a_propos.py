from tkinter import Tk,Label,Button
import os
import urllib.request
import prgm
import quitter

#Close app
def main():
    prgm.about_root=Tk()
    prgm.about_root.option_add('*Font', 'Arial 10')
    Label(prgm.about_root,text='Version actuelle\u00A0:\u00A0'+str(prgm.version)).grid(column=0,row=0,sticky='w')
    Label(prgm.about_root,text='-\u00A0Compatibile avec Linux.').grid(column=0,row=1,sticky='w')
    Label(prgm.about_root,width=50).grid(column=0,row=9)
    bouton_fermer=Button(prgm.about_root,text="Fermer",command=quitter.about_quit)
    bouton_fermer.grid(column=0,row=10)
    prgm.about_root.title("\u00C0 propos")
    prgm.about_root.resizable(width=False,height=False)
    if os.name=='nt':
        prgm.about_root.iconbitmap(r'a_propos.ico')
    prgm.about_root.mainloop()
