import preferences
import prgm

#Plot graph when delta>0
def main(a,b,c,alpha_num,alpha_denom,beta_num,beta_denom,delta):
    if preferences.afficher_graphs==1:
        import matplotlib.pyplot as plt
        import numpy as np
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
    prgm.plt.scatter(alpha_num/alpha_denom,beta_num/beta_denom,c='red',marker='x',label='(\u03B1;\u03B2)')
    prgm.plt.scatter((-b-(delta**0.5))/(2*a),0,c='green',marker='x',label='x\u2081=(((-b-\u221A(\u0394))/2a);0)')
    prgm.plt.scatter((-b+(delta**0.5))/(2*a),0,c='violet',marker='x',label='x\u2082=(((-b+\u221A(\u0394))/2a);0)')
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
