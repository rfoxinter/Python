from tkinter import Tk,Canvas,Toplevel,Label,Button,Spinbox,IntVar,StringVar,font,OptionMenu,PhotoImage
from tkinter.filedialog import askopenfilename
from os import listdir,name
from random import getrandbits
from time import sleep
from threading import Thread

board=[]
gen=0
pop=0

t=Tk()
if 'DejaVu Sans' in list(font.families()):
    police=font.Font(t,family='DejaVu Sans',size=10)
    t.option_add('*Font',police)
l=IntVar(t)
l.set(10)
c=IntVar(t)
c.set(10)
options=['al\u00E9atoire','fichier']
for i in listdir('.'):
    if '.txt' in i:
        options.append(i.replace('.txt',''))
f=StringVar(t)
f.set(options[0])

def fichier():
    global c,l,board
    if l.get()>100:
        l.set(100)
    elif l.get()<5:
        l.set(5)
    if c.get()>100:
        c.set(100)
    elif c.get()<5:
        c.set(5)
    if f.get()=='fichier':
        file=askopenfilename(title='S\u00E9lectionner un fichier à ouvrir',filetypes=[('Fichier texte', '.txt')],defaultextension='.txt')
        lire=open(file,'r')
        lignes=lire.readlines()
        board=eval(lignes[0])
        l=len(board)
        c=len(board[0])
    elif f.get()!='al\u00E9atoire':
        lire=open(f.get()+'.txt','r')
        lignes=lire.readlines()
        board=eval(lignes[0])
        l=len(board)
        c=len(board[0])
    t.destroy()

def debut():
    Label(t,text='Lignes\u00A0:\u00A0').grid(column=0,row=0,sticky='e')
    Spinbox(t,textvariable=l,from_=1,to=100,increment=1,width=10).grid(column=1,row=0,sticky='w')
    Label(t,text='Colonnes\u00A0:\u00A0').grid(column=0,row=1,sticky='e')
    Spinbox(t,textvariable=c,from_=1,to=100,increment=1,width=10).grid(column=1,row=1,sticky='w')
    Label(t,text='Grille\u00A0:\u00A0').grid(column=0,row=2,sticky='e')
    m=OptionMenu(t,f,*options)
    m.config(width=15)
    m.grid(column=1,row=2,sticky='w')
    Label(t,text='',width=35).grid(column=0,row=3,columnspan=2)
    Button(t,text='Valider',command=fichier).grid(column=0,row=4,columnspan=2)
    if name=='nt':
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('jeudelavie')
    img=PhotoImage(file='jeudelavie.png')
    t.protocol('WM_DELETE_WINDOW',quit)
    t.tk.call('wm','iconphoto',t._w,img)
    t.resizable(width=False,height=False)
    t.title('Taille de la grille')
    t.mainloop()

debut()

root=Tk()

h=(root.winfo_screenheight())
w=(root.winfo_screenwidth())
if board==[]:
    l=l.get()
    c=c.get()
size_h=20 if h/l>20 else int(h/l)
size_w=20 if w/c>20 else int(w/c)
size=0
if size_h<size_w:
    size=size_h
elif size_w<size_h:
    size=size_w
else:
    size=20
del h,w,size_h,size_w
if board==[]:
    board=[[int(getrandbits(1)+getrandbits(1)+getrandbits(1)+getrandbits(1)>2) for i in range(c)] for j in range(l)]
root.geometry('%sx%s'%(size*c,size*l+2*size))

def damier():
    for i in range(1,l):
        canva.create_line(0,size*i,size*c,size*i,width=2,fill='gray')
    for j in range(1,c):
        canva.create_line(size*j,0,size*j,size*l,width=2,fill='gray')

def cases():
    global pop
    pop=0
    for i in range(c):
        for j in range(l):
            if board[j][i]==1:
                canva.create_rectangle(i*size+2,j*size+2,i*size+size-2,j*size+size-2,width=0,fill='black')
                canva.addtag_enclosed('case',i*size,j*size,i*size+size,j*size+size)
                pop+=1

def voisins():
    v=[[0 for i in range(c)] for j in range(l)]
    for i in range(c):
        for j in range(l):
            v[j][i]=board[(j-1)%l][(i-1)%c]+board[(j-1)%l][i]+board[(j-1)%l][(i+1)%c]+board[j][(i-1)%c]+board[j][(i+1)%c]+board[(j+1)%l][(i-1)%c]+board[(j+1)%l][i]+board[(j+1)%l][(i+1)%c]
    for i in range(c):
        for j in range(l):
            if v[j][i]==3:
                board[j][i]=1
            elif v[j][i]<2 or v[j][i]>3:
                board[j][i]=0

canva=Canvas(root,width=size*c,height=size*l+2*size)
canva.place(x=-1,y=-1)
damier()

def jeu():
    global gen
    x=size*c/2
    g_y=size*(l+1/2)
    p_y=size*(l+3/2)
    while True:
        canva.delete('case')
        cases()
        voisins()
        gen+=1
        if canva.find_withtag('g')!=():
            canva.delete('g')
            canva.delete('p')
        g='G\u00E9n\u00E9rations\u00A0:\u00A0'+str(gen)
        canva.create_text(x,g_y,text=g,fill='black',anchor='center',font=('',12))
        canva.addtag_closest('g',x,g_y)
        p='Population\u00A0:\u00A0'+str(pop)
        canva.create_text(x,p_y,text=p,fill='black',anchor='center',font=('',12))
        canva.addtag_closest('p',x,p_y)
        sleep(0.25)

th=Thread(target=jeu,daemon=True)

root.after_idle(th.start)
if name=='nt':
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('jeudelavie')
img=PhotoImage(file='jeudelavie.png')
root.tk.call('wm','iconphoto',root._w,img)
root.resizable(width=False,height=False)
root.title('Jeu de la vie')
root.mainloop()
