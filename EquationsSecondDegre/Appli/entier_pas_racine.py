from tkinter import Label
import preferences
if preferences.afficher_graphs==1:
    import matplotlib.pyplot as plt
    import numpy as np
import __main__

#Plot graph when delta<0
def main(a,b,c,alpha_num,alpha_denom,beta_num,beta_denom):
    L4=Label(__main__.root,text='L\u2019\u00E9quation n\u2019admet pas de racine.')
    L4.grid(column=6,row=3,sticky='w')
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
        __main__.plt.plot(x,y,c='blue')
        __main__.plt.scatter(alpha_num/alpha_denom,beta_num/beta_denom,c='red',marker='x',label='(\u03B1;\u03B2)')
        __main__.plt.xlabel('x')
        __main__.plt.ylabel('y=f(x)')
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
        __main__.plt.title('f(x)=('+str(a)+')x\u00B2+('+str(b)+')x+('+str(c)+')')
        __main__.plt.show()
