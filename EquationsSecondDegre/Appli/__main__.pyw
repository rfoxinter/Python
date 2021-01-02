from tkinter import *
from math import inf
try:
    import matplotlib.pyplot as plt
    import numpy as np
except:
    import os
    import sys
    os.system(sys.executable+' -m pip install --upgrade matplotlib')
    import matplotlib.pyplot as plt
try:
    import numpy as np
except:
    import os
    import sys
    os.system(sys.executable+' -m pip install --upgrade numpy==1.19.3')
    import numpy as np
import quitter
import entier
import fraction
import a_propos
import sauvegarder
import ouvrir
import preferences

version=15

latest=''
entier_val=[0,0,0]
fraction_val=[0,0,0,0,0,0]

#Create main window
root=Tk()
root.option_add('*Font','Arial 10')

Label(root,text='Coefficients entiers').grid(column=0,row=0,columnspan=2)
Label(root,text='a=').grid(column=0,row=1,sticky='e')
Label(root,text='b=').grid(column=0,row=3,sticky='e')
Label(root,text='c=').grid(column=0,row=5,sticky='e')
ValeurA=IntVar(root)
ValeurB=IntVar(root)
ValeurC=IntVar(root)
ValA=Spinbox(root,textvariable=ValeurA,from_=-inf,to=inf,increment=1,width=10)
ValA.grid(column=1,row=1)
ValB=Spinbox(root,textvariable=ValeurB,from_=-inf,to=inf,increment=1,width=10)
ValB.grid(column=1,row=3)
ValC=Spinbox(root,textvariable=ValeurC,from_=-inf,to=inf,increment=1,width=10)
ValC.grid(column=1,row=5)
BoutonCalc=Button(root,text='Calculer',command=entier.main_ent)
BoutonCalc.grid(column=0,row=7,columnspan=2)

Label(root,text='Coefficients d\u00E9cimaux').grid(column=3,row=0,columnspan=2)
Label(root,text='Num\u00E9rateur de a=').grid(column=3,row=1,sticky='e')
Label(root,text='D\u00E9nominateur de a=').grid(column=3,row=2,sticky='e')
Label(root,text='Num\u00E9rateur de b=').grid(column=3,row=3,sticky='e')
Label(root,text='D\u00E9nominateur de b=').grid(column=3,row=4,sticky='e')
Label(root,text='Num\u00E9rateur de c=').grid(column=3,row=5,sticky='e')
Label(root,text='D\u00E9nominateur de c=').grid(column=3,row=6,sticky='e')
ValeurA_n=IntVar(root)
ValeurA_d=IntVar(root)
ValeurB_n=IntVar(root)
ValeurB_d=IntVar(root)
ValeurC_n=IntVar(root)
ValeurC_d=IntVar(root)
ValA_n=Spinbox(root,textvariable=ValeurA_n,from_=-inf,to=inf,increment=1,width=10)
ValA_n.grid(column=4,row=1)
ValA_d=Spinbox(root,textvariable=ValeurA_d,from_=1,to=inf,increment=1,width=10)
ValA_d.grid(column=4,row=2)
ValB_n=Spinbox(root,textvariable=ValeurB_n,from_=-inf,to=inf,increment=1,width=10)
ValB_n.grid(column=4,row=3)
ValB_d=Spinbox(root,textvariable=ValeurB_d,from_=1,to=inf,increment=1,width=10)
ValB_d.grid(column=4,row=4)
ValC_n=Spinbox(root,textvariable=ValeurC_n,from_=-inf,to=inf,increment=1,width=10)
ValC_n.grid(column=4,row=5)
ValC_d=Spinbox(root,textvariable=ValeurC_d,from_=1,to=inf,increment=1,width=10)
ValC_d.grid(column=4,row=6)
BoutonCalc=Button(root,text='Calculer',command=fraction.main_frac)
BoutonCalc.grid(column=3,row=7,columnspan=2)

BoutonQuit=Button(root,text='Quitter',command=quitter.close)
BoutonQuit.grid(column=7,row=10)

Col3_Row1=Label(root,width=5)
Col3_Row1.grid(column=2,row=0)
Col3_Row2=Label(root,width=5)
Col3_Row2.grid(column=2,row=1)
Col3_Row3=Label(root,width=5)
Col3_Row3.grid(column=2,row=2)
Col3_Row4=Label(root,width=5)
Col3_Row4.grid(column=2,row=3)
Col3_Row5=Label(root,width=5)
Col3_Row5.grid(column=2,row=4)
Col3_Row6=Label(root,width=5)
Col3_Row6.grid(column=2,row=5)
Col3_Row7=Label(root,width=5)
Col3_Row7.grid(column=2,row=6)
Col3_Row8=Label(root,width=5)
Col3_Row8.grid(column=2,row=7)
Col3_Row9=Label(root,width=5)
Col3_Row9.grid(column=2,row=8)
Col3_Row10=Label(root,width=5)
Col3_Row10.grid(column=2,row=9)
Col3_Row11=Label(root,width=5)
Col3_Row11.grid(column=2,row=10)

Col6_Row1=Label(root,width=5)
Col6_Row1.grid(column=5,row=0)
Col6_Row2=Label(root,width=5)
Col6_Row2.grid(column=5,row=1)
Col6_Row3=Label(root,width=5)
Col6_Row3.grid(column=5,row=5)
Col6_Row4=Label(root,width=5)
Col6_Row4.grid(column=5,row=3)
Col6_Row5=Label(root,width=5)
Col6_Row5.grid(column=5,row=4)
Col6_Row6=Label(root,width=5)
Col6_Row6.grid(column=5,row=5)
Col6_Row7=Label(root,width=5)
Col6_Row7.grid(column=5,row=6)
Col6_Row8=Label(root,width=5)
Col6_Row8.grid(column=5,row=7)
Col6_Row9=Label(root,width=5)
Col6_Row9.grid(column=5,row=8)
Col6_Row10=Label(root,width=5)
Col6_Row10.grid(column=5,row=9)
Col6_Row11=Label(root,width=5)
Col6_Row11.grid(column=5,row=10)

Col7=Label(root,width=100)
Col7.grid(column=6,row=5)

ver_maj=IntVar()
ver_maj.set(preferences.ver_maj)

def edit_ver_maj():
    file=open('preferences.py','r')
    list_of_lines =file.readlines()
    list_of_lines[0]='ver_maj='+str(ver_maj.get())
    file=open('preferences.py','w')
    file.writelines(list_of_lines)
    file.close()

menuBar=Menu(root)
menu_fichier=Menu(menuBar,tearoff=0)
menu_edition=Menu(menuBar,tearoff=0)
menu_preference=Menu(menu_edition,tearoff=0)
menu_aide=Menu(menuBar,tearoff=0)
menu_fichier.add_command(label='Enregistrer l\u2019\u00E9quation Ctrl+S',command=sauvegarder.main)
menu_fichier.add_command(label='Ouvrir une \u00E9quation Ctrl+O',command=ouvrir.main)
menuBar.add_cascade(label='Fichier',menu=menu_fichier)
menu_preference.add_checkbutton(label='V\u00E9rifier automatiquement les mises à jour',variable=ver_maj,command=edit_ver_maj)
menu_edition.add_cascade(label='Pr\u00E9f\u00E9rences',menu=menu_preference)
menuBar.add_cascade(label='\u00C9dition',menu=menu_edition)
menu_aide=Menu(menuBar,tearoff=0)
menu_aide.add_command(label='\u00C0 propos',command=a_propos.main)
menu_aide.add_separator()
menu_aide.add_command(label='V\u00E9rifier les mises \u00E0 jour',command=quitter.abt_maj)
menuBar.add_cascade(label='Aide',menu=menu_aide)
root.config(menu=menuBar)

root.bind('<Control-s>',sauvegarder.ctrl_s)
root.bind('<Control-o>',ouvrir.ctrl_o)

root.title('R\u00E9solution des \u00E9quations du second degr\u00E9 par Th\u00E9o')
root.resizable(width=False,height=False)
root.iconbitmap(r'python.ico')
root.mainloop()
