from tkinter import Label
import preferences
import prgm

#Define x for f(x)=0 when delta=0
#Plot graph when delta=0
def main(a,b,c,alpha_num,alpha_denom,beta_num,beta_denom):
    if preferences.afficher_graphs==1:
        import matplotlib.pyplot as plt
        import numpy as np
    x0_num=-b
    x0_denom=2*a
    if x0_num%x0_denom==0:
        x0=x0_num//x0_denom
        L4=Label(prgm.root,text='x\u2080='+str(int(x0)))
        L4.grid(column=6,row=3,sticky='w')
        prgm.rep[5]=L4.cget('text')
    else:
        div_x0=2
        while div_x0<=abs(x0_num) and div_x0<=abs(x0_denom):
            if x0_num%div_x0==0 and x0_denom%div_x0==0:
                x0_num=x0_num//div_x0
                x0_denom=x0_denom//div_x0
            else:
                div_x0=div_x0+1
        if x0_num<0 and x0_denom<0:
            L4=Label(prgm.root,text='x\u2080=('+str(int(-x0_num))+')/('+str(int(-x0_denom))+')='+str(x0_num/x0_denom).replace('.',','))
            L4.grid(column=6,row=3,sticky='w')
            prgm.rep[5]=L4.cget('text')
        else:
            L4=Label(prgm.root,text='x\u2080=('+str(int(x0_num))+')/('+str(int(x0_denom))+')='+str(x0_num/x0_denom).replace('.',','))
            L4.grid(column=6,row=3,sticky='w')
            prgm.rep[5]=L4.cget('text')
    
    if preferences.afficher_graphs==1:
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
        prgm.plt.plot(x,y,c='blue')
        prgm.plt.scatter(alpha_num/alpha_denom,beta_num/beta_denom,c='red',marker='x',label='x\u2080=(\u03B1;\u03B2)')
        prgm.plt.xlabel('x')
        prgm.plt.ylabel('y=f(x)')
        pltymin=0
        pltymax=0
        if beta_num/beta_denom-ymax/100<ymax:
            pltymin=beta_num/beta_denom-ymax/100
            pltymax=ymax
        else:
            pltymin=ymax
            pltymax=beta_num/beta_denom-ymax/100
        prgm.plt.axis([pltxmin,pltxmax,pltymin,pltymax])
        prgm.plt.axhline(y=0,c='black')
        prgm.plt.axvline(x=0,c='black')
        prgm.plt.legend()
        prgm.plt.title('f(x)=('+str(a)+')x\u00B2+('+str(b)+')x+('+str(c)+')')
        prgm.plt.show()
