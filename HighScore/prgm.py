from tkinter import Tk,messagebox,PhotoImage,Entry,IntVar,Menu,Label,Button,Frame
from os import name
import score

root=Tk()
root.geometry('800x750')

file=open('preferences.py','r')
for i in file.readlines():
    exec(i.replace('\n',''))
file.close()

import menu

global _S
_S=0

def rgb_hex(rgb):
    return "#%02x%02x%02x" % rgb 

def occurences(_list:list,val)->list:
    occ=[]
    for i in range(len(_list)):
        if _list[i]==val:
            occ.append(i)
    return occ

values = [str(i+1) for i in range (12)]
values.append('')
def check(value,row,col):
    if not value in values:
        return False
    else:
        if (eval('Val'+row+col+'.get()')=='' and value!='1') or (eval('Val'+row+col+'.get()')=='1' and value!=''):
            R[int(row)-1]+=1
            C[int(col)-1]+=1
            if row==col:
                D[0]+=1
            if str(6-int(row))==col:
                D[1]+=1
        elif (eval('Val'+row+col+'.get()')!='1' and value=='') or (eval('Val'+row+col+'.get()')!='' and value=='1'):
            R[int(row)-1]-=1
            C[int(col)-1]-=1
            if row==col:
                D[0]-=1
            if str(6-int(row))==col:
                D[1]-=1
        global _r,_d,_c
        o=occurences(R,5)
        if len(o)<_r:
            for i in score.diff([i for i in range(5)],o):
                eval('R'+str(i+1)+'_S').set('')
            _r-=1
        elif len(o)>_r:
            for i in o:
                eval('R'+str(i+1)+'_S').set(score.score([(int(eval('Val'+str(i+1)+str(j+1)).get()) if eval('Val'+str(i+1)+str(j+1)).get() in values[1:12] else int(value)) for j in range(5)]))
            _r+=1
        o=occurences(C,5)
        if len(o)<_c:
            for i in score.diff([i for i in range(5)],o):
                eval('C'+str(i+1)+'_S').set('')
            _c-=1
        elif len(o)>_c:
            for i in o:
                eval('C'+str(i+1)+'_S').set(score.score([(int(eval('Val'+str(j+1)+str(i+1)).get()) if eval('Val'+str(j+1)+str(i+1)).get() in values[1:12] else int(value)) for j in range(5)]))
            _c+=1
        o=occurences(D,5)
        if len(o)<_d:
            if D[0]<5:
                eval('D1_S').set('')
            if D[1]<5:
                eval('D2_S').set('')
            _d=len(o)
        elif len(o)>_d:
            if D[0]==5:
                eval('D1_S').set(2*score.score([(int(eval('Val'+str(j+1)+str(j+1)).get()) if eval('Val'+str(j+1)+str(j+1)).get() in values[1:12] else int(value)) for j in range(5)]))
            if D[1]==5:
                eval('D2_S').set(2*score.score([(int(eval('Val'+str(5-j)+str(j+1)).get()) if eval('Val'+str(5-j)+str(j+1)).get() in values[1:12] else int(value)) for j in range(5)]))
            _d=len(o)
        return True

def valider():
    global _S
    if _S==3:
        for i in range(3):
            eval('S'+str(i+1)+"_S").set('')
        eval('S_S').set('')
        _S=0
        Val['text']='Terminer la partie'
    else:
        if _r+_c+_d<12:
            messagebox.showwarning("Alerte", "La grille n\u2019est pas termin\u00E9e")
        else:
            _s=0
            for i in range(5):
                _s+=eval('R'+str(i+1)+"_S").get()
                _s+=eval('C'+str(i+1)+"_S").get()
                if i<2:
                    _s+=eval('D'+str(i+1)+"_S").get()
            exec('S'+str(_S+1)+'_S.set('+str(_s)+')')
            for i in range(5):
                for j in range(5):
                    eval('Valeur'+str(i+1)+str(j+1)).set('')
            _S+=1
            if _S==3:
                _s=0
                for i in range(3):
                    _s+=eval('S'+str(i+1)+"_S").get()
                S_S.set(_s)
                Val['text']='Recommencer le jeu'

ch = root.register(check)

for i in range(25):
    exec('Valeur'+str(i%5+1)+str(i//5+1)+"=IntVar(root)")
    eval('Valeur'+str(i%5+1)+str(i//5+1)).set('')
    if i%5+1==i//5+1 or 4-i%5+1==i//5+1:
        exec('Val'+str(i%5+1)+str(i//5+1)+"=Entry(root,textvariable=Valeur"+str(i%5+1)+str(i//5+1)+",justify='center',width=10,font=('TkDefaultFont',50),bg=rgb_hex(("+str(r_d)+","+str(g_d)+","+str(b_d)+")),validate='key',validatecommand=(ch,'%P',"+str(i%5+1)+','+str(i//5+1)+"))")
    else:
        exec('Val'+str(i%5+1)+str(i//5+1)+"=Entry(root,textvariable=Valeur"+str(i%5+1)+str(i//5+1)+",justify='center',width=10,font=('TkDefaultFont',50),bg=rgb_hex(("+str(r)+","+str(g)+","+str(b)+")),validate='key',validatecommand=(ch,'%P',"+str(i%5+1)+','+str(i//5+1)+"))")
    eval('Val'+str(i%5+1)+str(i//5+1)).place(x=100*(i%5)+25,y=100*(i//5)+125,width=100,height=100)

for i in range(5):
    exec('R'+str(i+1)+"_S=IntVar(root)")
    eval('R'+str(i+1)+"_S").set('')
    exec('R'+str(i+1)+"=Label(root,textvariable=R"+str(i+1)+"_S,justify='center',width=10,font=('TkDefaultFont',50),bg=rgb_hex((150,150,150)),relief='groove')")
    eval('R'+str(i+1)).place(x=100*(i%5)+25,y=25,width=100,height=100)

for i in range(5):
    exec('C'+str(i+1)+"_S=IntVar(root)")
    eval('C'+str(i+1)+"_S").set('')
    exec('C'+str(i+1)+"=Label(root,textvariable=C"+str(i+1)+"_S,justify='center',width=10,font=('TkDefaultFont',50),bg=rgb_hex((150,150,150)),relief='groove')")
    eval('C'+str(i+1)).place(x=525,y=100*(i%5)+125,width=100,height=100)

for i in range(2):
    exec('D'+str(2-i)+"_S=IntVar(root)")
    eval('D'+str(2-i)+"_S").set('')
    exec('D'+str(2-i)+"=Label(root,textvariable=D"+str(2-i)+"_S,justify='center',width=10,font=('TkDefaultFont',50),bg=rgb_hex((150,150,150)),relief='groove')")
    eval('D'+str(2-i)).place(x=525,y=25+600*i,width=100,height=100)

for i in range(3):
    exec('S'+str(i+1)+"_S=IntVar(root)")
    eval('S'+str(i+1)+"_S").set('')
    exec('S'+str(i+1)+"=Label(root,textvariable=S"+str(i+1)+"_S,justify='center',width=10,font=('TkDefaultFont',40),bg=rgb_hex((150,150,150)),relief='groove')")
    eval('S'+str(i+1)).place(x=675,y=150*i+100,width=100,height=100)
    t='+'
    if i==2:
        t='='
    Label(root,text=t,anchor='center',font=('TkDefaultFont',40)).place(x=675,y=150*i+200,width=100,height=50)

S_S=IntVar(root)
S_S.set('')
S=Label(root,textvariable=S_S,justify='center',width=10,font=('TkDefaultFont',40),bg=rgb_hex((150,150,150)),relief='groove')
S.place(x=675,y=550,width=100,height=100)

Val=Button(root,text='Terminer la partie',command=valider,font=('TkDefaultFont',25))
Val.place(x=100,y=650,width=350,height=50)

R,C,D=[0 for i in range(5)],[0 for i in range(5)],[0 for i in range(2)]
global _r,_c,_d
_r,_c,_d=0,0,0

root.title('High score')
if name=='nt':
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('puissance4')
img=PhotoImage(file='highscore.png')
root.tk.call('wm','iconphoto',root._w,img)
root.resizable(width=False,height=False)
root.mainloop()
