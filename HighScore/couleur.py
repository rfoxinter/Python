import prgm
from tkinter import Scale,Toplevel
import edit_pref

def main(_diag=False):
    root=Toplevel()
    r,g,b=prgm.IntVar(root),prgm.IntVar(root),prgm.IntVar(root)
    def color(event=None):
        col.configure({'bg': prgm.rgb_hex((r.get(),g.get(),b.get()))})
    def valider():
        l=[r,g,b]
        l=['r','g','b']
        for i in range(3):
            if _diag:
                edit_pref.main(l[i]+'_d',str(eval(l[i]).get()),i+3)
            else:
                edit_pref.main(l[i],str(eval(l[i]).get()),i)
    if _diag:
        r.set(prgm.r_d)
        g.set(prgm.g_d)
        b.set(prgm.b_d)
    else:
        r.set(prgm.r)
        g.set(prgm.g)
        b.set(prgm.b)
    bar_r=Scale(root,from_=0,to=255,orient='horizontal',var=r,tickinterval=255,label='Rouge',length=256,command=color)
    bar_r.grid(column=0,row=0)
    bar_g=Scale(root,from_=0,to=255,orient='horizontal',var=g,tickinterval=255,label='Vert',length=256,command=color)
    bar_g.grid(column=0,row=1)
    bar_b=Scale(root,from_=0,to=255,orient='horizontal',var=b,tickinterval=255,label='Bleu',length=256,command=color)
    bar_b.grid(column=0,row=2)
    col=prgm.Frame(root,width=20,height=20,bg=prgm.rgb_hex((r.get(),g.get(),b.get())))
    col.grid(column=0,row=3)
    prgm.Label(root,text='',width=50).grid(column=0,row=4)
    bouton_fermer=prgm.Button(root,text='Valider',command=lambda:(valider(),root.destroy()))
    bouton_fermer.grid(column=0,row=5)
    if _diag:
        root.title('Couleur des diagonales')
    else:
        root.title('Couleur des cases')
    root.resizable(width=False,height=False)
    if prgm.name=='nt':
        root.tk.call('wm','iconphoto',root._w,prgm.img)
    prgm.root.wait_window(root)
    return r.get()
