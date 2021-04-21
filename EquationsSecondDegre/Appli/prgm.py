import os
import sys
try:
    from tkinter import Tk,Label,Spinbox,Button,IntVar,PhotoImage,Menu,messagebox,font
except:
    if os.name=='posix':
        import packages_linux
        packages_linux.tkinter()
        from tkinter import Tk,Label,Spinbox,Button,IntVar,PhotoImage,Menu,messagebox,font
from math import inf
import preferences
try:
    from numpy import linspace
except:
    if preferences.afficher_graphs==1 or preferences.export_graph==1:
        import packages
        packages.main('numpy')
        from numpy import linspace
try:
    import matplotlib.pyplot as plt
except:
    if preferences.afficher_graphs==1 or preferences.export_graph==1:
        import packages
        packages.main('matplotlib')
        import matplotlib.pyplot as plt
import quitter
import entier
import fraction

if preferences.etat_maj!='':
    root=Tk()
    police=font.Font(family='DejaVu Sans',size=10)
    root.option_add('*Font',police)
    Label(root,text=preferences.etat_maj,width=50).grid(column=0,row=0)
    bouton_fermer=Button(root,text='Fermer',command=root.destroy)
    bouton_fermer.grid(column=0,row=1)
    root.title('Mise \u00E0 jour')
    root.resizable(width=False,height=False)
    if os.name=='nt':
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('equations')
    img=PhotoImage(file='python.png')
    root.tk.call('wm','iconphoto',root._w,img)
    root.mainloop()
    import edit_pref
    edit_pref.main('etat_maj',"''",2)

version=44

fonts=list(font.families())
if not 'DejaVu Sans' in fonts:
    import dejavusans
    dejavusans.main()

latest=''
entier_val=[0,0,0]
fraction_val=[0,0,0,0,0,0]
rep=['','','','','','','']

#Create main window
root=Tk()
police=font.Font(root,family='DejaVu Sans',size=10)
root.option_add('*Font',police)

import menu

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

Col7=Label(root,width=100)
Col7.grid(column=6,row=5)

root.protocol('WM_DELETE_WINDOW',quitter.close)
root.title('R\u00E9solution des \u00E9quations du second degr\u00E9 par Th\u00E9o')
root.resizable(width=False,height=False)
if os.name=='nt':
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('equations')
img=PhotoImage(file='python.png')
root.tk.call('wm','iconphoto',root._w,img)
root.mainloop()
