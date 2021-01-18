from tkinter import Tk,Label,Button
import os
import urllib.request
import prgm

#Close app
def main():
    prgm.about_root=Tk()
    prgm.about_root.option_add('*Font', 'Arial 10')
    Label(prgm.about_root,text='Version actuelle\u00A0:\u00A0'+str(prgm.version)).grid(column=0,row=0,sticky='w')
    Label(prgm.about_root,text='-\u00A0Correction de l\u2019icone Windows').grid(column=0,row=1,sticky='w')
    Label(prgm.about_root,text='-\u00A0Am\u00E9lioration de l\u2019exportation au format .docx').grid(column=0,row=2,sticky='w')
    Label(prgm.about_root,text='-\u00A0Am\u00E9lioration de la mise \u00E0 jour').grid(column=0,row=3,sticky='w')
    Label(prgm.about_root,width=50).grid(column=0,row=9)
    bouton_fermer=Button(prgm.about_root,text="Fermer",command=prgm.about_root.destroy)
    bouton_fermer.grid(column=0,row=10)
    prgm.about_root.title("\u00C0 propos")
    prgm.about_root.resizable(width=False,height=False)
    if os.name=='nt':
        prgm.about_root.iconbitmap(r'a_propos.ico')
    prgm.about_root.mainloop()
