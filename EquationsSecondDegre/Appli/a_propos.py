import prgm

def main():
    prgm.about_root=prgm.Tk()
    police=prgm.font.Font(prgm.about_root,family='DejaVu Sans',size=10)
    prgm.about_root.option_add('*Font',police)
    prgm.Label(prgm.about_root,text='Version actuelle\u00A0:\u00A0'+str(prgm.version)).grid(column=0,row=0,sticky='w')
    prgm.Label(prgm.about_root,text='-\u00A0Modification de la police').grid(column=0,row=1,sticky='w')
    prgm.Label(prgm.about_root,text='-\u00A0Optimisations').grid(column=0,row=2,sticky='w')
    prgm.Label(prgm.about_root,width=50).grid(column=0,row=9)
    bouton_fermer=prgm.Button(prgm.about_root,text="Fermer",command=prgm.about_root.destroy)
    bouton_fermer.grid(column=0,row=10)
    prgm.about_root.title("\u00C0 propos")
    prgm.about_root.resizable(width=False,height=False)
    if prgm.os.name=='nt':
        prgm.about_root.iconbitmap('a_propos.ico')
    prgm.about_root.mainloop()
