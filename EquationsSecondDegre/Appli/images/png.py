import prgm
from tkinter import Scale,Checkbutton,Toplevel

def main(extension):
    root=Toplevel()
    if 'DejaVu Sans' in list(prgm.font.families()):
        police=prgm.font.Font(root,family='DejaVu Sans',size=10)
        root.option_add('*Font',police)
    qualite=prgm.IntVar(root)
    qualite.set(100)
    transparent=prgm.IntVar(root)
    transparent.set(0)
    bar_qualite=Scale(root,from_=100,to=500,orient='horizontal',var=qualite,tickinterval=50,label='Résolution',length=325,resolution=5)
    bar_qualite.grid(column=0,row=0)
    bar_transparent=Checkbutton(root,text='Transparent',variable=transparent)
    bar_transparent.grid(column=0,row=1)
    prgm.Label(root,text='',width=50).grid(column=0,row=2)
    bouton_fermer=prgm.Button(root,text='Valider',command=root.destroy)
    bouton_fermer.grid(column=0,row=3)
    root.title('Exporter en png')
    root.resizable(width=False,height=False)
    if prgm.os.name=='nt':
        root.iconbitmap('python.ico')
    prgm.root.wait_window(root)
    return qualite.get(),transparent.get()
