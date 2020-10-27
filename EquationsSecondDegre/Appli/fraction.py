from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import __main__
import fraction_x1
import fraction_x2

def main_frac():
    __main__.plt.close()
    for label in __main__.Fen.grid_slaves():
        if int(label.grid_info()["column"])==6:
            label.destroy()
    Col7=Label(__main__.Fen,width=40)
    Col7.grid(column=6,row=5)
    sec_frac(__main__.ValeurA_n.get(),__main__.ValeurA_d.get(),__main__.ValeurB_n.get(),__main__.ValeurB_d.get(),__main__.ValeurC_n.get(),__main__.ValeurC_d.get())

def sec_frac(a_num,a_denom,b_num,b_denom,c_num,c_denom):
    delta_num=b_num**2*a_denom*c_denom-4*a_num*c_num*b_denom**2+((a_num/a_num)-1)
    delta_denom=a_denom*b_denom**2*c_denom
    if delta_num>0 and delta_denom<0:
        delta_num=-delta_num
        delta_denom=-delta_denom
    alpha_num=-b_num*a_denom
    alpha_denom=2*a_num*b_denom
    beta_num=-delta_num*a_denom
    beta_denom=4*a_num*delta_denom
    if delta_num%delta_denom==0:
        delta_num=delta_num//delta_denom
        L1=Label(__main__.Fen,text='\u0394='+str(delta_num))
        L1.grid(column=6,row=0,sticky='w')
    else:
        div_delta=2
        while div_delta<=abs(delta_num) and div_delta<=abs(delta_denom):
            if delta_num%div_delta==0 and delta_denom%div_delta==0:
                delta_num=delta_num//div_delta
                delta_denom=delta_denom//div_delta
            else:
                div_delta=div_delta+1
        if delta_num<0 and delta_denom<0:
            L1=Label(__main__.Fen,text='\u0394='+str(int(-delta_num))+')/('+str(int(-delta_denom))+')='+str(delta_num/delta_denom))
            L1.grid(column=6,row=0,sticky='w')
        else:
            L1=Label(__main__.Fen,text='\u0394=('+str(int(delta_num))+')/('+str(int(delta_denom))+')='+str(delta_num/delta_denom))
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
            L3=Label(__main__.Fen,text='\u03B2=('+str(int(-beta_num))+')/('+str(int(-beta_denom))+')')
            L3.grid(column=6,row=2,sticky='w')
        else:
            L3=Label(__main__.Fen,text='\u03B2=('+str(int(beta_num))+')/('+str(int(beta_denom))+')')
            L3.grid(column=6,row=2,sticky='w')
    if delta_num<0:
        L4=Label(__main__.Fen,text='L\u2019\u00E9quation n\u2019admet pas de racine')
        L4.grid(column=6,row=3,sticky='w')
        pltxmin=alpha_num/alpha_denom-10
        pltxmax=alpha_num/alpha_denom+10
        ymax=0
        if (a_num/a_denom)*(pltxmin)**2+(b_num/b_denom)*(pltxmin)+(c_num/c_denom)>(a_num/a_denom)*(pltxmax)**2+(b_num/b_denom)*(pltxmax)+(c_num/c_denom):
            if (a_num/a_denom)*(pltxmin)**2+(b_num/b_denom)*(pltxmin)+(c_num/c_denom)>0:
                ymax=(a_num/a_denom)*(pltxmin)**2+(b_num/b_denom)*(pltxmin)+(c_num/c_denom)
            else:
                ymax=(a_num/a_denom)*(pltxmax)**2+(b_num/b_denom)*(pltxmax)+(c_num/c_denom)
        else:
            if (a_num/a_denom)*(pltxmax)**2+(b_num/b_denom)*(pltxmax)+(c_num/c_denom)>0:
                ymax=(a_num/a_denom)*(pltxmax)**2+(b_num/b_denom)*(pltxmax)+(c_num/c_denom)
            else:
                ymax=(a_num/a_denom)*(pltxmin)**2+(b_num/b_denom)*(pltxmin)+(c_num/c_denom)
        x=np.linspace(pltxmin,pltxmax,1000)
        y=(a_num/a_denom)*x**2+(b_num/b_denom)*x+(c_num/c_denom)
        __main__.plt.plot(x,y,c='blue')
        __main__.plt.scatter(alpha_num/alpha_denom,beta_num/beta_denom,c='red',marker='x',label="(\u03B1;\u03B2)")
        __main__.plt.xlabel("x")
        __main__.plt.ylabel("y=f(x)")
        pltymin=0
        pltymax=0
        if beta_num/beta_denom-ymax/100<ymax:
            pltymin=beta_num/beta_denom-ymax/100
            pltymax=ymax
        else:
            pltymin=ymax
            pltymax=beta_num/beta_denom-ymax/100
        __main__.plt.axis([pltxmin,pltxmax,pltymin,pltymax])
        __main__.plt.axhline(y=0,c='black')
        __main__.plt.axvline(x=0,c='black')
        __main__.plt.legend()
        __main__.plt.title('f(x)=('+str(a_num)+')/('+str(a_denom)+')x\u00B2+('+str(b_num)+')/('+str(b_denom)+')x+('+str(c_num)+')/('+str(c_denom)+')')
        __main__.plt.show()
    if delta_num==0:
        x0_num=-b_num*a_denom
        x0_denom=2*a_num*b_denom
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
        pltxmin=alpha_num/alpha_denom-10
        pltxmax=alpha_num/alpha_denom+10
        ymax=0
        if (a_num/a_denom)*(pltxmin)**2+(b_num/b_denom)*(pltxmin)+(c_num/c_denom)>(a_num/a_denom)*(pltxmax)**2+(b_num/b_denom)*(pltxmax)+(c_num/c_denom):
            if (a_num/a_denom)*(pltxmin)**2+(b_num/b_denom)*(pltxmin)+(c_num/c_denom)>0:
                ymax=(a_num/a_denom)*(pltxmin)**2+(b_num/b_denom)*(pltxmin)+(c_num/c_denom)
            else:
                ymax=(a_num/a_denom)*(pltxmax)**2+(b_num/b_denom)*(pltxmax)+(c_num/c_denom)
        else:
            if (a_num/a_denom)*(pltxmax)**2+(b_num/b_denom)*(pltxmax)+(c_num/c_denom)>0:
                ymax=(a_num/a_denom)*(pltxmax)**2+(b_num/b_denom)*(pltxmax)+(c_num/c_denom)
            else:
                ymax=(a_num/a_denom)*(pltxmin)**2+(b_num/b_denom)*(pltxmin)+(c_num/c_denom)
        x=np.linspace(pltxmin,pltxmax,1000)
        y=(a_num/a_denom)*x**2+(b_num/b_denom)*x+(c_num/c_denom)
        __main__.plt.plot(x,y,c='blue')
        __main__.plt.scatter(alpha_num/alpha_denom,beta_num/beta_denom,c='red',marker='x',label="x\u2080=(\u03B1;\u03B2)")
        __main__.plt.xlabel("x")
        __main__.plt.ylabel("y=f(x)")
        pltymin=0
        pltymax=0
        if beta_num/beta_denom-ymax/100<ymax:
            pltymin=beta_num/beta_denom-ymax/100
            pltymax=ymax
        else:
            pltymin=ymax
            pltymax=beta_num/beta_denom-ymax/100
        __main__.plt.axis([pltxmin,pltxmax,pltymin,pltymax])
        __main__.plt.axhline(y=0,c='black')
        __main__.plt.axvline(x=0,c='black')
        __main__.plt.legend()
        __main__.plt.title('f(x)=('+str(a_num)+')/('+str(a_denom)+')x\u00B2+('+str(b_num)+')/('+str(b_denom)+')x+('+str(c_num)+')/('+str(c_denom)+')')
        __main__.plt.show()
    if delta_num>0:
        fraction_x1.x1_frac(a_num,a_denom,b_num,b_denom,delta_num,delta_denom)
        fraction_x2.x2_frac(a_num,a_denom,b_num,b_denom,delta_num,delta_denom)

