import prgm
from tkinter import Scale,Toplevel

def main(extension):
    root=Toplevel()
    police=prgm.font.Font(root,family='DejaVu Sans',size=10)
    root.option_add('*Font',police)
    qualite=prgm.IntVar(root)
    qualite.set(100)
    bar_qualite=Scale(root,from_=100,to=500,orient='horizontal',var=qualite,tickinterval=50,label='Résolution',length=325,resolution=5)
    bar_qualite.grid(column=0,row=0)
    prgm.Label(root,text='',width=50).grid(column=0,row=1)
    bouton_fermer=prgm.Button(root,text='Fermer',command=root.destroy)
    bouton_fermer.grid(column=0,row=2)
    root.title('Exporter en png')
    root.resizable(width=False,height=False)
    if prgm.os.name=='nt':
        root.iconbitmap('python.ico')
    prgm.root.wait_window(root)
    return qualite.get()
