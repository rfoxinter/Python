import prgm
import entier_equation

def main(a,b,c,alpha_num,alpha_denom,beta_num,beta_denom,extension,path):
    if extension!='':
        prgm.plt.figure(300)
    if prgm.afficher_graphs==1 or extension!='':
        prgm.plt.rcParams['pdf.fonttype']=42
        prgm.plt.rcParams['font.family']='DejaVu Sans'
        prgm.plt.rcParams['font.size']='10'
    L4=prgm.Label(prgm.root,text='L\u2019\u00E9quation n\u2019admet pas de racine dans \u211D.')
    L4.grid(column=6,row=3,sticky='w')
    prgm.rep[5]=L4.cget('text')
    if prgm.afficher_graphs==1 or extension!='':
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
        x=prgm.linspace(pltxmin,pltxmax,1000)
        y=a*x**2+b*x+c
        prgm.plt.plot(x,y,c='blue')
        prgm.plt.scatter(alpha_num/alpha_denom,beta_num/beta_denom,c='red',marker='x',label='(\u03B1;\u03B2)')
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
        prgm.plt.title(entier_equation.main())
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
