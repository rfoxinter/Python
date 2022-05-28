import prgm

def main():
    if prgm.afficher_graphs==1:
        prgm.plt.close()
    for label in prgm.root.grid_slaves():
        if int(label.grid_info()['column'])==6:
            label.destroy()
    Col7=prgm.Label(prgm.root,width=100)
    Col7.grid(column=6,row=5)
    L1=prgm.Label(prgm.root,text='Une erreur est survenue lors de l\u2019ouverture du fichier')
    L1.grid(column=6,row=0,sticky='w')