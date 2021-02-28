import prgm

def main(a_num,a_denom,b_num,b_denom,c_num,c_denom,alpha_num,alpha_denom,beta_num,beta_denom,delta_num,delta_denom,extension,path):
    if extension!='':
        prgm.plt.figure(300)
    prgm.plt.rcParams['pdf.fonttype']=42
    prgm.plt.rcParams['font.family']='DejaVu Sans'
    prgm.plt.rcParams['font.size']='10'
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
    x=prgm.linspace(pltxmin,pltxmax,1000)
    y=(a_num/a_denom)*x**2+(b_num/b_denom)*x+(c_num/c_denom)
    prgm.plt.plot(x,y,c='blue')
    prgm.plt.scatter(alpha_num/alpha_denom,beta_num/beta_denom,c='red',marker='x',label='(\u03B1;\u03B2)')
    prgm.plt.scatter((-(b_num/b_denom)-((delta_num/delta_denom)**0.5))/(2*(a_num/a_denom)),0,c='green',marker='x',label='x\u2081=(((-b-\u221A(\u0394))/2a);0)')
    prgm.plt.scatter((-(b_num/b_denom)+((delta_num/delta_denom)**0.5))/(2*(a_num/a_denom)),0,c='violet',marker='x',label='x\u2082=(((-b+\u221A(\u0394))/2a);0)')
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
    prgm.plt.title('f(x)=('+str(a_num)+')/('+str(a_denom)+')x\u00B2+('+str(b_num)+')/('+str(b_denom)+')x+('+str(c_num)+')/('+str(c_denom)+')')
    if extension=='pdf':
        from matplotlib.backends.backend_pdf import PdfPages
        prgm.plt.savefig(path)
        prgm.plt.show(block=False)
        prgm.plt.close(300)
    elif extension!='':
        if extension=='png':
            from images import png
            prgm.plt.rcParams['savefig.dpi'],prgm.plt.rcParams['savefig.transparent']=png.main(extension)
        elif extension=='jpg':
            from images import jpg
            prgm.plt.rcParams['savefig.dpi']=jpg.main(extension)
        prgm.plt.savefig(path)
        prgm.plt.show(block=False)
        prgm.plt.close(300)
    else:
        prgm.plt.show()
