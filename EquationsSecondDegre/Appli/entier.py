from tkinter import Label
import __main__
import entier_pas_racine
import entier_x0
import entier_x1
import entier_x2
import entier_deux_racines_plt
import preferences

def main_ent():
    if preferences.afficher_graphs==1:
        __main__.plt.close()
    for label in __main__.root.grid_slaves():
        if int(label.grid_info()['column'])==6:
            label.destroy()
    Col7=Label(__main__.root,width=100)
    Col7.grid(column=6,row=5)
    if __main__.ValeurA.get()!=0:
        __main__.latest='entier'
        sec_ent(__main__.ValeurA.get(),__main__.ValeurB.get(),__main__.ValeurC.get())
    else:
        L1=Label(__main__.root,text='Erreur\u00A0:\u00A0a\u22600')
        L1.grid(column=6,row=0,sticky='w')

def open_ent(a,b,c):
    if preferences.afficher_graphs==1:
        __main__.plt.close()
    for label in __main__.root.grid_slaves():
        if int(label.grid_info()['column'])==6:
            label.destroy()
    Col7=Label(__main__.root,width=100)
    Col7.grid(column=6,row=5)
    if __main__.ValeurA.get()!=0:
        __main__.latest='entier'
        __main__.entier_val[0]=a
        __main__.entier_val[1]=b
        __main__.entier_val[2]=c
        sec_ent(a,b,c)
    else:
        L1=Label(__main__.root,text='Erreur\u00A0:\u00A0a\u22600')
        L1.grid(column=6,row=0,sticky='w')

def sec_ent(a,b,c):
    __main__.rep[6]=''
    __main__.entier_val[0]=a
    __main__.entier_val[1]=b
    __main__.entier_val[2]=c
    delta=b**2-4*a*c+(int(a/a)-1)
    alpha_num=-b
    alpha_denom=2*a
    beta_num=-delta
    beta_denom=4*a
    L1=Label(__main__.root,text='\u0394='+str(delta))
    L1.grid(column=6,row=0,sticky='w')
    __main__.rep[2]=L1.cget('text')
    if alpha_num%alpha_denom==0:
        alpha=alpha_num//alpha_denom
        L2=Label(__main__.root,text='\u03B1='+str(alpha))
        L2.grid(column=6,row=1,sticky='w')
        __main__.rep[3]=L2.cget('text')
    else:
        div_alpha=2
        while div_alpha<=abs(alpha_num) and div_alpha<=abs(alpha_denom):
            if alpha_num%div_alpha==0 and alpha_denom%div_alpha==0:
                alpha_num=alpha_num//div_alpha
                alpha_denom=alpha_denom//div_alpha
            else:
                div_alpha=div_alpha+1
        if alpha_denom<0:
            L2=Label(__main__.root,text='\u03B1=('+str(int(-alpha_num))+')/('+str(int(-alpha_denom))+')='+str(alpha_num/alpha_denom).replace('.',','))
            L2.grid(column=6,row=1,sticky='w')
            __main__.rep[3]=L2.cget('text')
            __main__.rep[3]=L2.cget('text')
        else:
            L2=Label(__main__.root,text='\u03B1=('+str(int(alpha_num))+')/('+str(int(alpha_denom))+')='+str(alpha_num/alpha_denom).replace('.',','))
            L2.grid(column=6,row=1,sticky='w')
            __main__.rep[3]=L2.cget('text')
    if beta_num%beta_denom==0:
        beta=beta_num//beta_denom
        L3=Label(__main__.root,text='\u03B2='+str(beta))
        L3.grid(column=6,row=2,sticky='w')
        __main__.rep[4]=L3.cget('text')
    else:
        div_beta=2
        while div_beta<=abs(beta_num) and div_beta<=abs(beta_denom):
            if beta_num%div_beta==0 and beta_denom%div_beta==0:
                beta_num=beta_num//div_beta
                beta_denom=beta_denom//div_beta
            else:
                div_beta=div_beta+1
        if beta_denom<0:
            L3=Label(__main__.root,text='\u03B2=('+str(int(-beta_num))+')/('+str(int(-beta_denom))+')='+str(beta_num/beta_denom).replace('.',','))
            L3.grid(column=6,row=2,sticky='w')
            __main__.rep[4]=L3.cget('text')
        else:
            L3=Label(__main__.root,text='\u03B2=('+str(int(beta_num))+')/('+str(int(beta_denom))+')='+str(beta_num/beta_denom).replace('.',','))
            L3.grid(column=6,row=2,sticky='w')
            __main__.rep[4]=L3.cget('text')
    if delta<0:
        entier_pas_racine.main(a,b,c,alpha_num,alpha_denom,beta_num,beta_denom)
    elif delta==0:
        entier_x0.main(a,b,c,alpha_num,alpha_denom,beta_num,beta_denom)
    else:
        entier_x1.main(a,b,delta)
        entier_x2.main(a,b,delta)
        if preferences.afficher_graphs==1:
            entier_deux_racines_plt.main(a,b,c,alpha_num,alpha_denom,beta_num,beta_denom,delta)
