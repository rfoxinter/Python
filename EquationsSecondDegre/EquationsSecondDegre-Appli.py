from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from math import *

Fen=Tk()

def quitter():
    plt.close()
    Fen.destroy()

def main_ent():
    plt.close()
    for label in Fen.grid_slaves():
        if int(label.grid_info()["column"])==6:
            label.destroy()
    Col7=Label(Fen,width=40)
    Col7.grid(column=6,row=5)
    sec_ent(ValeurA.get(),ValeurB.get(),ValeurC.get())

def sec_ent(a,b,c):
    delta=b**2-4*a*c+(int(a/a)-1)
    alpha_num=-b
    alpha_denom=2*a
    beta_num=-delta
    beta_denom=4*a
    L1=Label(Fen,text='\u0394='+str(delta))
    L1.grid(column=6,row=0,sticky='w')
    if alpha_num%alpha_denom==0:
        alpha=alpha_num//alpha_denom
        L2=Label(Fen,text='\u03B1='+str(alpha))
        L2.grid(column=6,row=1,sticky='w')
    else:
        div_alpha=2
        while div_alpha<=abs(alpha_num) and div_alpha<=abs(alpha_denom):
            if alpha_num%div_alpha==0 and alpha_denom%div_alpha==0:
                alpha_num=alpha_num//div_alpha
                alpha_denom=alpha_denom//div_alpha
            else:
                div_alpha=div_alpha+1
        if alpha_num<0 and alpha_denom<0:
            L2=Label(Fen,text='\u03B1=('+str(int(-alpha_num))+')/('+str(int(-alpha_denom))+')='+str(alpha_num/alpha_denom))
            L2.grid(column=6,row=1,sticky='w')
        else:
            L2=Label(Fen,text='\u03B1=('+str(int(alpha_num))+')/('+str(int(alpha_denom))+')='+str(alpha_num/alpha_denom))
            L2.grid(column=6,row=1,sticky='w')
    if beta_num%beta_denom==0:
        beta=beta_num//beta_denom
        L3=Label(Fen,text='\u03B2='+str(beta))
        L3.grid(column=6,row=2,sticky='w')
    else:
        div_beta=2
        while div_beta<=abs(beta_num) and div_beta<=abs(beta_denom):
            if beta_num%div_beta==0 and beta_denom%div_beta==0:
                beta_num=beta_num//div_beta
                beta_denom=beta_denom//div_beta
            else:
                div_beta=div_beta+1
        if beta_num<0 and beta_denom<0:
            L3=Label(Fen,text='\u03B2=('+str(int(-beta_num))+')/('+str(int(-beta_denom))+')='+str(beta_num/beta_denom))
            L3.grid(column=6,row=2,sticky='w')
        else:
            L3=Label(Fen,text='\u03B2=('+str(int(beta_num))+')/('+str(int(beta_denom))+')='+str(beta_num/beta_denom))
            L3.grid(column=6,row=2,sticky='w')
    if delta<0:
        L4=Label(Fen,text='L\u2019\u00E9quation n\u2019admet pas de racine')
        L4.grid(column=6,row=3,sticky='w')
        pltxmin=alpha_num/alpha_denom-10
        pltxmax=alpha_num/alpha_denom+10
        ymax=0
        if a*(pltxmin)**2+b*(pltxmin)+c>a*(pltxmax)**2+b*(pltxmax)+c:
            if a*(pltxmin)**2+b*(pltxmin)+c>0:
                ymax=a*(pltxmin)**2+b*(pltxmin)+c
            else:
                ymax=a*(pltxmax)**2+b*(pltxmax)+c
        else:
            if a*(pltxmax)**2+b*(pltxmax)+c>0:
                ymax=a*(pltxmax)**2+b*(pltxmax)+c
            else:
                ymax=a*(pltxmin)**2+b*(pltxmin)+c
        x=np.linspace(pltxmin,pltxmax,1000)
        y=a*x**2+b*x+c
        plt.plot(x,y,c='blue')
        plt.scatter(alpha_num/alpha_denom,beta_num/beta_denom,c='red',marker='x',label="(\u03B1;\u03B2)")
        plt.xlabel("x")
        plt.ylabel("y=f(x)")
        pltymin=0
        pltymax=0
        if beta_num/beta_denom-ymax/100<ymax:
            pltymin=beta_num/beta_denom-ymax/100
            pltymax=ymax
        else:
            pltymin=ymax
            pltymax=beta_num/beta_denom-ymax/100
        plt.axis([pltxmin,pltxmax,pltymin,pltymax])
        plt.axhline(y=0,c='black')
        plt.axvline(x=0,c='black')
        plt.legend()
        plt.title('f(x)=('+str(a)+')x\u00B2+('+str(b)+')x+('+str(c)+')')
        plt.show()
    elif delta==0:
        x0_num=-b
        x0_denom=2*a
        if x0_num%x0_denom==0:
            x0=x0_num//x0_denom
            L4=Label(Fen,text='x\u2080='+str(int(x0)))
            L4.grid(column=6,row=3,sticky='w')
        else:
            div_x0=2
            while div_x0<=abs(x0_num) and div_x0<=abs(x0_denom):
                if x0_num%div_x0==0 and x0_denom%div_x0==0:
                    x0_num=x0_num//div_x0
                    x0_denom=x0_denom//div_x0
                else:
                    div_x0=div_x0+1
            if x0_num<0 and x0_denom<0:
                L4=Label(Fen,text='x\u2080=('+str(int(-x0_num))+')/('+str(int(-x0_denom))+')='+str(x0_num/x0_denom))
                L4.grid(column=6,row=3,sticky='w')
            else:
                L4=Label(Fen,text='x\u2080=('+str(int(x0_num))+')/('+str(int(x0_denom))+')='+str(x0_num/x0_denom))
                L4.grid(column=6,row=3,sticky='w')
        pltxmin=alpha_num/alpha_denom-10
        pltxmax=alpha_num/alpha_denom+10
        ymax=0
        if a*(pltxmin)**2+b*(pltxmin)+c>a*(pltxmax)**2+b*(pltxmax)+c:
            if a*(pltxmin)**2+b*(pltxmin)+c>0:
                ymax=a*(pltxmin)**2+b*(pltxmin)+c
            else:
                ymax=a*(pltxmax)**2+b*(pltxmax)+c
        else:
            if a*(pltxmax)**2+b*(pltxmax)+c>0:
                ymax=a*(pltxmax)**2+b*(pltxmax)+c
            else:
                ymax=a*(pltxmin)**2+b*(pltxmin)+c
        x=np.linspace(pltxmin,pltxmax,1000)
        y=a*x**2+b*x+c
        plt.plot(x,y,c='blue')
        plt.scatter(alpha_num/alpha_denom,beta_num/beta_denom,c='red',marker='x',label="x\u2080=(\u03B1;\u03B2)")
        plt.xlabel("x")
        plt.ylabel("y=f(x)")
        pltymin=0
        pltymax=0
        if beta_num/beta_denom-ymax/100<ymax:
            pltymin=beta_num/beta_denom-ymax/100
            pltymax=ymax
        else:
            pltymin=ymax
            pltymax=beta_num/beta_denom-ymax/100
        plt.axis([pltxmin,pltxmax,pltymin,pltymax])
        plt.axhline(y=0,c='black')
        plt.axvline(x=0,c='black')
        plt.legend()
        plt.title('f(x)=('+str(a)+')x\u00B2+('+str(b)+')x+('+str(c)+')')
        plt.show()
    else:
        x1_num=0
        x1_denom=0
        x2_num=0
        x2_denom=0
        if delta**0.5==int(delta**0.5):
            x1_num=-b-delta**0.5
            x1_denom=2*a
            if x1_num%x1_denom==0:
                x1=x1_num//x1_denom
                L4=Label(Fen,text='x\u2081='+str(int(x1)))
                L4.grid(column=6,row=3,sticky='w')
            else:
                div_x1=2
                while div_x1<=abs(x1_num) and div_x1<=abs(x1_denom):
                    if x1_num%div_x1==0 and x1_denom%div_x1==0:
                        x1_num=x1_num//div_x1
                        x1_denom=x1_denom//div_x1
                    else:
                        div_x1=div_x1+1
                if x1_num<0 and x1_denom<0:
                    L4=Label(Fen,text='x\u2081=('+str(int(-x1_num))+')/('+str(int(-x1_denom))+')='+str(x1_num/x1_denom))
                    L4.grid(column=6,row=3,sticky='w')
                else:
                    L4=Label(Fen,text='x\u2081=('+str(int(x1_num))+')/('+str(int(x1_denom))+')='+str(x1_num/x1_denom))
                    L4.grid(column=6,row=3,sticky='w')
        else:
            x1_num_int=-b
            x1_num_rt=delta
            x1_denom=2*a
            div_x1=2
            while div_x1<=abs(x1_num_int) and div_x1<=abs(x1_denom):
                if x1_num_int%div_x1==0 and x1_denom%div_x1==0 and x1_num_rt%div_x1**2==0:
                    x1_num_int=x1_num_int//div_x1
                    x1_denom=x1_denom//div_x1
                    x1_num_rt=x1_num_rt//div_x1**2
                else:
                    div_x1=div_x1+1
            if x1_num_int<0 and x1_denom<0:
                if abs(x1_denom)==1:
                    L4=Label(Fen,text='x\u2081='+str(int(-x1_num_int))+'+\u221A('+str(x1_num_rt)+')='+str(x1_num_int+x1_num_rt**0.5))
                    L4.grid(column=6,row=3,sticky='w')
                else:
                    L4=Label(Fen,text='x\u2081=('+str(int(-x1_num_int))+'+\u221A('+str(x1_num_rt)+'))/('+str(int(-x1_denom))+')='+str((x1_num_int+x1_num_rt**0.5)/x1_denom))
                    L4.grid(column=6,row=3,sticky='w')
            else:
                if abs(x1_denom)==1:
                    L4=Label(Fen,text='x\u2081='+str(int(x1_num_int))+'-\u221A('+str(x1_num_rt)+')='+str(x1_num_int-x1_num_rt**0.5))
                    L4.grid(column=6,row=3,sticky='w')
                else:
                    L4=Label(Fen,text='x\u2081=('+str(int(x1_num_int))+'-\u221A('+str(x1_num_rt)+'))/('+str(int(x1_denom))+')='+str((x1_num_int-x1_num_rt**0.5)/x1_denom))
                    L4.grid(column=6,row=3,sticky='w')
        if delta**0.5==int(delta**0.5):
            x2_num=-b+delta**0.5
            x2_denom=2*a
            if x2_num%x2_denom==0:
                x2=x2_num//x2_denom
                L5=Label(Fen,text='x\u2082='+str(int(x2)))
                L5.grid(column=6,row=4,sticky='w')
            else:
                div_x2=2
                while div_x2<=abs(x2_num) and div_x2<=abs(x2_denom):
                    if x2_num%div_x2==0 and x2_denom%div_x2==0:
                        x2_num=x2_num//div_x2
                        x2_denom=x2_denom//div_x2
                    else:
                        div_x2=div_x2+1
                if x2_num<0 and x2_denom<0:
                    L5=Label(Fen,text='x\u2082=('+str(int(-x2_num))+')/('+str(int(-x2_denom))+')='+str(x2_num/x2_denom))
                    L5.grid(column=6,row=4,sticky='w')
                else:
                    L5=Label(Fen,text='x\u2082=('+str(int(x2_num))+')/('+str(int(x2_denom))+')='+str(x2_num/x2_denom))
                    L5.grid(column=6,row=4,sticky='w')
        else:
            x2_num_int=-b
            x2_num_rt=delta
            x2_denom=2*a
            div_x2=2
            while div_x2<=abs(x2_num_int) and div_x2<=abs(x2_denom):
                if x2_num_int%div_x2==0 and x2_denom%div_x2==0 and x2_num_rt%div_x2**2==0:
                    x2_num_int=x2_num_int//div_x2
                    x2_denom=x2_denom//div_x2
                    x2_num_rt=x2_num_rt//div_x2**2
                else:
                    div_x2=div_x2+1
            if x2_num_int<0 and x2_denom<0:
                if abs(x2_denom)==1:
                    L5=Label(Fen,text='x\u2082='+str(int(-x2_num_int))+'-\u221A('+str(x2_num_rt)+')='+str(x2_num_int-x2_num_rt**0.5))
                    L5.grid(column=6,row=4,sticky='w')
                else:
                    L5=Label(Fen,text='x\u2082=('+str(int(-x2_num_int))+'-\u221A('+str(x2_num_rt)+'))/('+str(int(-x2_denom))+')='+str((x2_num_int-x2_num_rt**0.5)/x2_denom))
                    L5.grid(column=6,row=4,sticky='w')
            else:
                if abs(x2_denom)==1:
                    L5=Label(Fen,text='x\u2082='+str(int(x2_num_int))+'+\u221A('+str(x2_num_rt)+')='+str(x2_num_int+x2_num_rt**0.5))
                    L5.grid(column=6,row=4,sticky='w')
                else:
                    L5=Label(Fen,text='x\u2082=('+str(int(x2_num_int))+'+\u221A('+str(x2_num_rt)+'))/('+str(int(x2_denom))+')='+str((x2_num_int+x2_num_rt**0.5)/x2_denom))
                    L5.grid(column=6,row=4,sticky='w')
        pltxmin=alpha_num/alpha_denom-10
        pltxmax=alpha_num/alpha_denom+10
        ymax=0
        if a*(pltxmin)**2+b*(pltxmin)+c>a*(pltxmax)**2+b*(pltxmax)+c:
            if a*(pltxmin)**2+b*(pltxmin)+c>0:
                ymax=a*(pltxmin)**2+b*(pltxmin)+c
            else:
                ymax=a*(pltxmax)**2+b*(pltxmax)+c
        else:
            if a*(pltxmax)**2+b*(pltxmax)+c>0:
                ymax=a*(pltxmax)**2+b*(pltxmax)+c
            else:
                ymax=a*(pltxmin)**2+b*(pltxmin)+c
        x=np.linspace(pltxmin,pltxmax,1000)
        y=a*x**2+b*x+c
        plt.plot(x,y,c='blue')
        plt.scatter(alpha_num/alpha_denom,beta_num/beta_denom,c='red',marker='x',label="(\u03B1;\u03B2)")
        plt.scatter((-b-(delta**0.5))/(2*a),0,c='green',marker='x',label="x\u2081=(((-b-\u221A(\u0394))/2a);0)")
        plt.scatter((-b+(delta**0.5))/(2*a),0,c='violet',marker='x',label="x\u2082=(((-b+\u221A(\u0394))/2a);0)")
        plt.xlabel("x")
        plt.ylabel("y=f(x)")
        pltymin=0
        pltymax=0
        if beta_num/beta_denom-ymax/100<ymax:
            pltymin=beta_num/beta_denom-ymax/100
            pltymax=ymax
        else:
            pltymin=ymax
            pltymax=beta_num/beta_denom-ymax/100
        plt.axis([pltxmin,pltxmax,pltymin,pltymax])
        plt.axhline(y=0,c='black')
        plt.axvline(x=0,c='black')
        plt.legend()
        plt.title('f(x)=('+str(a)+')x\u00B2+('+str(b)+')x+('+str(c)+')')
        plt.show()

def main_frac():
    plt.close()
    for label in Fen.grid_slaves():
        if int(label.grid_info()["column"])==6:
            label.destroy()
    Col7=Label(Fen,width=40)
    Col7.grid(column=6,row=5)
    L1=Label(Fen,text='Fonction actuellement indisponible.')
    L1.grid(column=6,row=0,sticky='w')

Label(Fen,text='Coefficients entiers').grid(column=0,row=0,columnspan=2)
Label(Fen,text='a=').grid(column=0,row=1,sticky='e')
Label(Fen,text='b=').grid(column=0,row=3,sticky='e')
Label(Fen,text='c=').grid(column=0,row=5,sticky='e')
ValeurA=IntVar(Fen)
ValeurB=IntVar(Fen)
ValeurC=IntVar(Fen)
ValA=Spinbox(Fen,textvariable=ValeurA,from_=-inf,to=inf,increment=1,width=10)
ValA.grid(column=1,row=1)
ValB=Spinbox(Fen,textvariable=ValeurB,from_=-inf,to=inf,increment=1,width=10)
ValB.grid(column=1,row=3)
ValC=Spinbox(Fen,textvariable=ValeurC,from_=-inf,to=inf,increment=1,width=10)
ValC.grid(column=1,row=5)
BoutonCalc=Button(Fen,text="Calculer",command=main_ent)
BoutonCalc.grid(column=0,row=7,columnspan=2)

Label(Fen,text='Coefficients entiers').grid(column=3,row=0,columnspan=2)
Label(Fen,text='Num\u00E9rateur de a=').grid(column=3,row=1,sticky='e')
Label(Fen,text='D\u00E9nominateur de a=').grid(column=3,row=2,sticky='e')
Label(Fen,text='Num\u00E9rateur de b=').grid(column=3,row=3,sticky='e')
Label(Fen,text='D\u00E9nominateur de b=').grid(column=3,row=4,sticky='e')
Label(Fen,text='Num\u00E9rateur de c=').grid(column=3,row=5,sticky='e')
Label(Fen,text='D\u00E9nominateur de c=').grid(column=3,row=6,sticky='e')
ValeurA_n=IntVar(Fen)
ValeurA_d=IntVar(Fen)
ValeurB_n=IntVar(Fen)
ValeurB_d=IntVar(Fen)
ValeurC_n=IntVar(Fen)
ValeurC_d=IntVar(Fen)
ValA_n=Spinbox(Fen,textvariable=ValeurA_n,from_=-inf,to=inf,increment=1,width=10)
ValA_n.grid(column=4,row=1)
ValA_d=Spinbox(Fen,textvariable=ValeurA_d,from_=1,to=inf,increment=1,width=10)
ValA_d.grid(column=4,row=2)
ValB_n=Spinbox(Fen,textvariable=ValeurB_n,from_=-inf,to=inf,increment=1,width=10)
ValB_n.grid(column=4,row=3)
ValB_d=Spinbox(Fen,textvariable=ValeurB_d,from_=1,to=inf,increment=1,width=10)
ValB_d.grid(column=4,row=4)
ValC_n=Spinbox(Fen,textvariable=ValeurC_n,from_=-inf,to=inf,increment=1,width=10)
ValC_n.grid(column=4,row=5)
ValC_d=Spinbox(Fen,textvariable=ValeurC_d,from_=1,to=inf,increment=1,width=10)
ValC_d.grid(column=4,row=6)
BoutonCalc=Button(Fen,text="Calculer",command=main_frac)
BoutonCalc.grid(column=3,row=7,columnspan=2)

BoutonQuit=Button(Fen,text="Quitter",command=quitter)
BoutonQuit.grid(column=7,row=10)

Col3_Row1=Label(Fen,width=5)
Col3_Row1.grid(column=2,row=0)
Col3_Row2=Label(Fen,width=5)
Col3_Row2.grid(column=2,row=1)
Col3_Row3=Label(Fen,width=5)
Col3_Row3.grid(column=2,row=2)
Col3_Row4=Label(Fen,width=5)
Col3_Row4.grid(column=2,row=3)
Col3_Row5=Label(Fen,width=5)
Col3_Row5.grid(column=2,row=4)
Col3_Row6=Label(Fen,width=5)
Col3_Row6.grid(column=2,row=5)
Col3_Row7=Label(Fen,width=5)
Col3_Row7.grid(column=2,row=6)
Col3_Row8=Label(Fen,width=5)
Col3_Row8.grid(column=2,row=7)
Col3_Row9=Label(Fen,width=5)
Col3_Row9.grid(column=2,row=8)
Col3_Row10=Label(Fen,width=5)
Col3_Row10.grid(column=2,row=9)
Col3_Row11=Label(Fen,width=5)
Col3_Row11.grid(column=2,row=10)

Col6_Row1=Label(Fen,width=5)
Col6_Row1.grid(column=5,row=0)
Col6_Row2=Label(Fen,width=5)
Col6_Row2.grid(column=5,row=1)
Col6_Row3=Label(Fen,width=5)
Col6_Row3.grid(column=5,row=5)
Col6_Row4=Label(Fen,width=5)
Col6_Row4.grid(column=5,row=3)
Col6_Row5=Label(Fen,width=5)
Col6_Row5.grid(column=5,row=4)
Col6_Row6=Label(Fen,width=5)
Col6_Row6.grid(column=5,row=5)
Col6_Row7=Label(Fen,width=5)
Col6_Row7.grid(column=5,row=6)
Col6_Row8=Label(Fen,width=5)
Col6_Row8.grid(column=5,row=7)
Col6_Row9=Label(Fen,width=5)
Col6_Row9.grid(column=5,row=8)
Col6_Row10=Label(Fen,width=5)
Col6_Row10.grid(column=5,row=9)
Col6_Row11=Label(Fen,width=5)
Col6_Row11.grid(column=5,row=10)

Col7=Label(Fen,width=40)
Col7.grid(column=6,row=5)

Fen.title("R\u00E9solution des \u00E9quations du second degr\u00E9 par Th\u00E9o")
Fen.resizable(width=False,height=False)
Fen.mainloop()
