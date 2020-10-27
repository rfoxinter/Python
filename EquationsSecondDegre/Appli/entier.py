from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
from math import *
import __main__

def main_ent():
    __main__.plt.close()
    for label in __main__.Fen.grid_slaves():
        if int(label.grid_info()["column"])==6:
            label.destroy()
    Col7=Label(__main__.Fen,width=40)
    Col7.grid(column=6,row=5)
    sec_ent(__main__.ValeurA.get(),__main__.ValeurB.get(),__main__.ValeurC.get())

def sec_ent(a,b,c):
    delta=b**2-4*a*c+(int(a/a)-1)
    alpha_num=-b
    alpha_denom=2*a
    beta_num=-delta
    beta_denom=4*a
    L1=Label(__main__.Fen,text='\u0394='+str(delta))
    L1.grid(column=6,row=0,sticky='w')
    if alpha_num%alpha_denom==0:
        alpha=alpha_num//alpha_denom
        L2=Label(__main__.Fen,text='\u03B1='+str(alpha))
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
            L2=Label(__main__.Fen,text='\u03B1=('+str(int(-alpha_num))+')/('+str(int(-alpha_denom))+')='+str(alpha_num/alpha_denom))
            L2.grid(column=6,row=1,sticky='w')
        else:
            L2=Label(__main__.Fen,text='\u03B1=('+str(int(alpha_num))+')/('+str(int(alpha_denom))+')='+str(alpha_num/alpha_denom))
            L2.grid(column=6,row=1,sticky='w')
    if beta_num%beta_denom==0:
        beta=beta_num//beta_denom
        L3=Label(__main__.Fen,text='\u03B2='+str(beta))
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
            L3=Label(__main__.Fen,text='\u03B2=('+str(int(-beta_num))+')/('+str(int(-beta_denom))+')='+str(beta_num/beta_denom))
            L3.grid(column=6,row=2,sticky='w')
        else:
            L3=Label(__main__.Fen,text='\u03B2=('+str(int(beta_num))+')/('+str(int(beta_denom))+')='+str(beta_num/beta_denom))
            L3.grid(column=6,row=2,sticky='w')
    if delta<0:
        L4=Label(__main__.Fen,text='L\u2019\u00E9quation n\u2019admet pas de racine')
        L4.grid(column=6,row=3,sticky='w')
        __main__.pltxmin=alpha_num/alpha_denom-10
        __main__.pltxmax=alpha_num/alpha_denom+10
        ymax=0
        if a*(__main__.pltxmin)**2+b*(__main__.pltxmin)+c>a*(__main__.pltxmax)**2+b*(__main__.pltxmax)+c:
            if a*(__main__.pltxmin)**2+b*(__main__.pltxmin)+c>0:
                ymax=a*(__main__.pltxmin)**2+b*(__main__.pltxmin)+c
            else:
                ymax=a*(__main__.pltxmax)**2+b*(__main__.pltxmax)+c
        else:
            if a*(__main__.pltxmax)**2+b*(__main__.pltxmax)+c>0:
                ymax=a*(__main__.pltxmax)**2+b*(__main__.pltxmax)+c
            else:
                ymax=a*(__main__.pltxmin)**2+b*(__main__.pltxmin)+c
        x=np.linspace(__main__.pltxmin,__main__.pltxmax,1000)
        y=a*x**2+b*x+c
        __main__.plt.plot(x,y,c='blue')
        __main__.plt.scatter(alpha_num/alpha_denom,beta_num/beta_denom,c='red',marker='x',label="(\u03B1;\u03B2)")
        __main__.plt.xlabel("x")
        __main__.plt.ylabel("y=f(x)")
        __main__.pltymin=0
        __main__.pltymax=0
        if beta_num/beta_denom-ymax/100<ymax:
            __main__.pltymin=beta_num/beta_denom-ymax/100
            __main__.pltymax=ymax
        else:
            __main__.pltymin=ymax
            __main__.pltymax=beta_num/beta_denom-ymax/100
        __main__.plt.axis([__main__.pltxmin,__main__.pltxmax,__main__.pltymin,__main__.pltymax])
        __main__.plt.axhline(y=0,c='black')
        __main__.plt.axvline(x=0,c='black')
        __main__.plt.legend()
        __main__.plt.title('f(x)=('+str(a)+')x\u00B2+('+str(b)+')x+('+str(c)+')')
        __main__.plt.show()
    elif delta==0:
        x0_num=-b
        x0_denom=2*a
        if x0_num%x0_denom==0:
            x0=x0_num//x0_denom
            L4=Label(__main__.Fen,text='x\u2080='+str(int(x0)))
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
                L4=Label(__main__.Fen,text='x\u2080=('+str(int(-x0_num))+')/('+str(int(-x0_denom))+')='+str(x0_num/x0_denom))
                L4.grid(column=6,row=3,sticky='w')
            else:
                L4=Label(__main__.Fen,text='x\u2080=('+str(int(x0_num))+')/('+str(int(x0_denom))+')='+str(x0_num/x0_denom))
                L4.grid(column=6,row=3,sticky='w')
        __main__.pltxmin=alpha_num/alpha_denom-10
        __main__.pltxmax=alpha_num/alpha_denom+10
        ymax=0
        if a*(__main__.pltxmin)**2+b*(__main__.pltxmin)+c>a*(__main__.pltxmax)**2+b*(__main__.pltxmax)+c:
            if a*(__main__.pltxmin)**2+b*(__main__.pltxmin)+c>0:
                ymax=a*(__main__.pltxmin)**2+b*(__main__.pltxmin)+c
            else:
                ymax=a*(__main__.pltxmax)**2+b*(__main__.pltxmax)+c
        else:
            if a*(__main__.pltxmax)**2+b*(__main__.pltxmax)+c>0:
                ymax=a*(__main__.pltxmax)**2+b*(__main__.pltxmax)+c
            else:
                ymax=a*(__main__.pltxmin)**2+b*(__main__.pltxmin)+c
        x=np.linspace(__main__.pltxmin,__main__.pltxmax,1000)
        y=a*x**2+b*x+c
        __main__.plt.plot(x,y,c='blue')
        __main__.plt.scatter(alpha_num/alpha_denom,beta_num/beta_denom,c='red',marker='x',label="x\u2080=(\u03B1;\u03B2)")
        __main__.plt.xlabel("x")
        __main__.plt.ylabel("y=f(x)")
        __main__.pltymin=0
        __main__.pltymax=0
        if beta_num/beta_denom-ymax/100<ymax:
            __main__.pltymin=beta_num/beta_denom-ymax/100
            __main__.pltymax=ymax
        else:
            __main__.pltymin=ymax
            __main__.pltymax=beta_num/beta_denom-ymax/100
        __main__.plt.axis([__main__.pltxmin,__main__.pltxmax,__main__.pltymin,__main__.pltymax])
        __main__.plt.axhline(y=0,c='black')
        __main__.plt.axvline(x=0,c='black')
        __main__.plt.legend()
        __main__.plt.title('f(x)=('+str(a)+')x\u00B2+('+str(b)+')x+('+str(c)+')')
        __main__.plt.show()
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
                L4=Label(__main__.Fen,text='x\u2081='+str(int(x1)))
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
                    L4=Label(__main__.Fen,text='x\u2081=('+str(int(-x1_num))+')/('+str(int(-x1_denom))+')='+str(x1_num/x1_denom))
                    L4.grid(column=6,row=3,sticky='w')
                else:
                    L4=Label(__main__.Fen,text='x\u2081=('+str(int(x1_num))+')/('+str(int(x1_denom))+')='+str(x1_num/x1_denom))
                    L4.grid(column=6,row=3,sticky='w')
        else:
            x1_num_int=-b
            x1_num_rt=delta
            x1_denom=2*a
            x1_num_int_div=x1_num_int
            if x1_num_int_div==0:
                x1_num_int_div=x1_denom
            div_x1=2
            while div_x1<=abs(x1_num_int_div) and div_x1<=abs(x1_denom):
                if x1_num_int%div_x1==0 and x1_denom%div_x1==0 and x1_num_rt%div_x1**2==0:
                    x1_num_int=x1_num_int//div_x1
                    x1_denom=x1_denom//div_x1
                    x1_num_rt=x1_num_rt//div_x1**2
                    x1_num_int_div=x1_num_int_div//div_x1
                else:
                    div_x1=div_x1+1
            if x1_num_int==0:
                if abs(x1_denom)==1:
                    L4=Label(__main__.Fen,text='x\u2081=\u221A('+str(x1_num_rt)+')='+str(x1_num_rt**0.5))
                    L4.grid(column=6,row=3,sticky='w')
                else:
                    if x1_denom<0:
                        L4=Label(__main__.Fen,text='x\u2081=\u221A('+str(x1_num_rt)+')/('+str(int(-x1_denom))+')='+str((x1_num_rt**0.5)/-x1_denom))
                        L4.grid(column=6,row=3,sticky='w')
                    else:
                        L4=Label(__main__.Fen,text='x\u2081=-\u221A('+str(x1_num_rt)+')/('+str(int(x1_denom))+')='+str(-(x1_num_rt**0.5)/x1_denom))
                        L4.grid(column=6,row=3,sticky='w')
            elif x1_num_int<0 and x1_denom<0:
                if abs(x1_denom)==1:
                    L4=Label(__main__.Fen,text='x\u2081='+str(int(-x1_num_int))+'+\u221A('+str(x1_num_rt)+')='+str(x1_num_int+x1_num_rt**0.5))
                    L4.grid(column=6,row=3,sticky='w')
                else:
                    L4=Label(__main__.Fen,text='x\u2081=('+str(int(-x1_num_int))+'+\u221A('+str(x1_num_rt)+'))/('+str(int(-x1_denom))+')='+str((x1_num_int+x1_num_rt**0.5)/x1_denom))
                    L4.grid(column=6,row=3,sticky='w')
            else:
                if abs(x1_denom)==1:
                    L4=Label(__main__.Fen,text='x\u2081='+str(int(x1_num_int))+'-\u221A('+str(x1_num_rt)+')='+str(x1_num_int-x1_num_rt**0.5))
                    L4.grid(column=6,row=3,sticky='w')
                else:
                    L4=Label(__main__.Fen,text='x\u2081=('+str(int(x1_num_int))+'-\u221A('+str(x1_num_rt)+'))/('+str(int(x1_denom))+')='+str((x1_num_int-x1_num_rt**0.5)/x1_denom))
                    L4.grid(column=6,row=3,sticky='w')
        if delta**0.5==int(delta**0.5):
            x2_num=-b+delta**0.5
            x2_denom=2*a
            if x2_num%x2_denom==0:
                x2=x2_num//x2_denom
                L5=Label(__main__.Fen,text='x\u2082='+str(int(x2)))
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
                    L5=Label(__main__.Fen,text='x\u2082=('+str(int(-x2_num))+')/('+str(int(-x2_denom))+')='+str(x2_num/x2_denom))
                    L5.grid(column=6,row=4,sticky='w')
                else:
                    L5=Label(__main__.Fen,text='x\u2082=('+str(int(x2_num))+')/('+str(int(x2_denom))+')='+str(x2_num/x2_denom))
                    L5.grid(column=6,row=4,sticky='w')
        else:
            x2_num_int=-b
            x2_num_rt=delta
            x2_denom=2*a
            x2_num_int_div=x2_num_int
            if x2_num_int_div==0:
                x2_num_int_div=x2_denom
            div_x2=2
            while div_x2<=abs(x2_num_int_div) and div_x2<=abs(x2_denom):
                if x2_num_int%div_x2==0 and x2_denom%div_x2==0 and x2_num_rt%div_x2**2==0:
                    x2_num_int=x2_num_int//div_x2
                    x2_denom=x2_denom//div_x2
                    x2_num_rt=x2_num_rt//div_x2**2
                    x2_num_int_div=x2_num_int_div//div_x2
                else:
                    div_x2=div_x2+1
            if x2_num_int==0:
                if abs(x2_denom)==1:
                    L5=Label(__main__.Fen,text='x\u2082=-\u221A('+str(x2_num_rt)+')='+str(x2_num_int-x2_num_rt**0.5))
                    L5.grid(column=6,row=4,sticky='w')
                else:
                    if x2_denom<0:
                        L5=Label(__main__.Fen,text='x\u2082=-\u221A('+str(x2_num_rt)+')/('+str(int(-x2_denom))+')='+str(-(x2_num_rt**0.5)/-x2_denom))
                        L5.grid(column=6,row=4,sticky='w')
                    else:
                        L5=Label(__main__.Fen,text='x\u2082=\u221A('+str(x2_num_rt)+')/('+str(int(x2_denom))+')='+str((x2_num_rt**0.5)/x2_denom))
                        L5.grid(column=6,row=4,sticky='w')
            elif x2_num_int<0 and x2_denom<0:
                if abs(x2_denom)==1:
                    L5=Label(__main__.Fen,text='x\u2082='+str(int(-x2_num_int))+'-\u221A('+str(x2_num_rt)+')='+str(x2_num_int-x2_num_rt**0.5))
                    L5.grid(column=6,row=4,sticky='w')
                else:
                    L5=Label(__main__.Fen,text='x\u2082=('+str(int(-x2_num_int))+'-\u221A('+str(x2_num_rt)+'))/('+str(int(-x2_denom))+')='+str((x2_num_int-x2_num_rt**0.5)/x2_denom))
                    L5.grid(column=6,row=4,sticky='w')
            else:
                if abs(x2_denom)==1:
                    L5=Label(__main__.Fen,text='x\u2082='+str(int(x2_num_int))+'+\u221A('+str(x2_num_rt)+')='+str(x2_num_int+x2_num_rt**0.5))
                    L5.grid(column=6,row=4,sticky='w')
                else:
                    L5=Label(__main__.Fen,text='x\u2082=('+str(int(x2_num_int))+'+\u221A('+str(x2_num_rt)+'))/('+str(int(x2_denom))+')='+str((x2_num_int+x2_num_rt**0.5)/x2_denom))
                    L5.grid(column=6,row=4,sticky='w')
        __main__.pltxmin=alpha_num/alpha_denom-10
        __main__.pltxmax=alpha_num/alpha_denom+10
        ymax=0
        if a*(__main__.pltxmin)**2+b*(__main__.pltxmin)+c>a*(__main__.pltxmax)**2+b*(__main__.pltxmax)+c:
            if a*(__main__.pltxmin)**2+b*(__main__.pltxmin)+c>0:
                ymax=a*(__main__.pltxmin)**2+b*(__main__.pltxmin)+c
            else:
                ymax=a*(__main__.pltxmax)**2+b*(__main__.pltxmax)+c
        else:
            if a*(__main__.pltxmax)**2+b*(__main__.pltxmax)+c>0:
                ymax=a*(__main__.pltxmax)**2+b*(__main__.pltxmax)+c
            else:
                ymax=a*(__main__.pltxmin)**2+b*(__main__.pltxmin)+c
        x=np.linspace(__main__.pltxmin,__main__.pltxmax,1000)
        y=a*x**2+b*x+c
        __main__.plt.plot(x,y,c='blue')
        __main__.plt.scatter(alpha_num/alpha_denom,beta_num/beta_denom,c='red',marker='x',label="(\u03B1;\u03B2)")
        __main__.plt.scatter((-b-(delta**0.5))/(2*a),0,c='green',marker='x',label="x\u2081=(((-b-\u221A(\u0394))/2a);0)")
        __main__.plt.scatter((-b+(delta**0.5))/(2*a),0,c='violet',marker='x',label="x\u2082=(((-b+\u221A(\u0394))/2a);0)")
        __main__.plt.xlabel("x")
        __main__.plt.ylabel("y=f(x)")
        __main__.pltymin=0
        __main__.pltymax=0
        if beta_num/beta_denom-ymax/100<ymax:
            __main__.pltymin=beta_num/beta_denom-ymax/100
            __main__.pltymax=ymax
        else:
            __main__.pltymin=ymax
            __main__.pltymax=beta_num/beta_denom-ymax/100
        __main__.plt.axis([__main__.pltxmin,__main__.pltxmax,__main__.pltymin,__main__.pltymax])
        __main__.plt.axhline(y=0,c='black')
        __main__.plt.axvline(x=0,c='black')
        __main__.plt.legend()
        __main__.plt.title('f(x)=('+str(a)+')x\u00B2+('+str(b)+')x+('+str(c)+')')
        __main__.plt.show()
