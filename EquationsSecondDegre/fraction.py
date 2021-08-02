import prgm
import fraction_pas_racine
import fraction_x0
import fraction_x1
import fraction_x2
import fraction_deux_racines_plt
import preferences

def main_frac():
    if preferences.afficher_graphs==1:
        prgm.plt.close()
    for label in prgm.root.grid_slaves():
        if int(label.grid_info()['column'])==6:
            label.destroy()
    Col7=prgm.Label(prgm.root,width=100)
    Col7.grid(column=6,row=5)
    if prgm.ValeurA_n.get()!=0 and prgm.ValeurA_d.get()>0 and prgm.ValeurB_d.get()>0 and prgm.ValeurC_d.get()>0:
        prgm.latest='fraction'
        prgm.ValeurA_n.set(prgm.ValeurA_n.get())
        prgm.ValeurA_d.set(prgm.ValeurA_d.get())
        prgm.ValeurB_n.set(prgm.ValeurB_n.get())
        prgm.ValeurB_d.set(prgm.ValeurB_d.get())
        prgm.ValeurC_n.set(prgm.ValeurC_n.get())
        prgm.ValeurC_d.set(prgm.ValeurC_d.get())
        sec_frac(prgm.ValeurA_n.get(),prgm.ValeurA_d.get(),prgm.ValeurB_n.get(),prgm.ValeurB_d.get(),prgm.ValeurC_n.get(),prgm.ValeurC_d.get())
    else:
        i=0
        if prgm.ValeurA_n.get()==0:
            L1=prgm.Label(prgm.root,text='Erreur\u00A0:\u00A0a\u2208\u2124*')
            L1.grid(column=6,row=i,sticky='w')
            i=i+1
        if prgm.ValeurA_d.get()<=0 or prgm.ValeurB_d.get()<=0 or prgm.ValeurC_d.get()<=0:
            L1=prgm.Label(prgm.root,text='Erreur\u00A0:\u00A0D\u00E9nominateur\u2208\u2115*')
            L1.grid(column=6,row=i,sticky='w')
            i=i+1

def open_frac(a_num,a_denom,b_num,b_denom,c_num,c_denom):
    prgm.fraction_val[0]=a_num
    prgm.fraction_val[1]=a_denom
    prgm.fraction_val[2]=b_num
    prgm.fraction_val[3]=b_denom
    prgm.fraction_val[4]=c_num
    prgm.fraction_val[5]=c_denom
    if preferences.afficher_graphs==1:
        prgm.plt.close()
    for label in prgm.root.grid_slaves():
        if int(label.grid_info()['column'])==6:
            label.destroy()
    Col7=prgm.Label(prgm.root,width=100)
    Col7.grid(column=6,row=5)
    if prgm.ValeurA_n.get()!=0 and prgm.ValeurA_d.get()>0 and prgm.ValeurB_d.get()>0 and prgm.ValeurC_d.get()>0:
        prgm.latest='fraction'
        sec_frac(a_num,a_denom,b_num,b_denom,c_num,c_denom)
    else:
        i=0
        if prgm.ValeurA_n.get()==0:
            L1=prgm.Label(prgm.root,text='Erreur\u00A0:\u00A0a\u2208\u2124*')
            L1.grid(column=6,row=i,sticky='w')
            i=i+1
        if prgm.ValeurA_d.get()<=0 or prgm.ValeurB_d.get()<=0 or prgm.ValeurC_d.get()<=0:
            L1=prgm.Label(prgm.root,text='Erreur\u00A0:\u00A0D\u00E9nominateur\u2208\u2115*')
            L1.grid(column=6,row=i,sticky='w')
            i=i+1

def sec_frac(a_num,a_denom,b_num,b_denom,c_num,c_denom):
    prgm.rep[6]=''
    prgm.fraction_val[0]=a_num
    prgm.fraction_val[1]=a_denom
    prgm.fraction_val[2]=b_num
    prgm.fraction_val[3]=b_denom
    prgm.fraction_val[4]=c_num
    prgm.fraction_val[5]=c_denom
    delta_num=int(b_num**2*a_denom*c_denom-4*a_num*c_num*b_denom**2)
    delta_denom=int(a_denom*b_denom**2*c_denom)
    if delta_num>0 and delta_denom<0:
        delta_num=-delta_num
        delta_denom=-delta_denom
    alpha_num=int(-b_num*a_denom)
    alpha_denom=int(2*a_num*b_denom)
    beta_num=int(-delta_num*a_denom)
    beta_denom=int(4*a_num*delta_denom)
    if delta_num%delta_denom==0:
        delta_num=delta_num//delta_denom
        delta_denom=1
        L1=prgm.Label(prgm.root,text='\u0394='+str(delta_num))
        L1.grid(column=6,row=0,sticky='w')
        prgm.rep[2]=L1.cget('text')
    else:
        div_delta=2
        while div_delta<=abs(delta_num) and div_delta<=abs(delta_denom):
            if delta_num%div_delta==0 and delta_denom%div_delta==0:
                delta_num=delta_num//div_delta
                delta_denom=delta_denom//div_delta
            else:
                div_delta=div_delta+1
        if delta_num<0 and delta_denom<0:
            L1=prgm.Label(prgm.root,text='\u0394='+str(int(-delta_num))+')/('+str(int(-delta_denom))+')='+str(delta_num/delta_denom).replace('.',','))
            L1.grid(column=6,row=0,sticky='w')
            prgm.rep[2]=L1.cget('text')
        else:
            L1=prgm.Label(prgm.root,text='\u0394=('+str(int(delta_num))+')/('+str(int(delta_denom))+')='+str(delta_num/delta_denom).replace('.',','))
            L1.grid(column=6,row=0,sticky='w')
            prgm.rep[2]=L1.cget('text')
    if alpha_num%alpha_denom==0:
        alpha=alpha_num//alpha_denom
        L2=prgm.Label(prgm.root,text='\u03B1='+str(alpha))
        L2.grid(column=6,row=1,sticky='w')
        prgm.rep[3]=L2.cget('text')
    else:
        div_alpha=2
        while div_alpha<=abs(alpha_num) and div_alpha<=abs(alpha_denom):
            if alpha_num%div_alpha==0 and alpha_denom%div_alpha==0:
                alpha_num=alpha_num//div_alpha
                alpha_denom=alpha_denom//div_alpha
            else:
                div_alpha=div_alpha+1
        if alpha_num<0 and alpha_denom<0:
            L2=prgm.Label(prgm.root,text='\u03B1=('+str(int(-alpha_num))+')/('+str(int(-alpha_denom))+')='+str(alpha_num/alpha_denom).replace('.',','))
            L2.grid(column=6,row=1,sticky='w')
            prgm.rep[3]=L2.cget('text')
        else:
            L2=prgm.Label(prgm.root,text='\u03B1=('+str(int(alpha_num))+')/('+str(int(alpha_denom))+')='+str(alpha_num/alpha_denom).replace('.',','))
            L2.grid(column=6,row=1,sticky='w')
            prgm.rep[3]=L2.cget('text')
    if beta_num%beta_denom==0:
        beta=beta_num//beta_denom
        L3=prgm.Label(prgm.root,text='\u03B2='+str(beta))
        L3.grid(column=6,row=2,sticky='w')
        prgm.rep[4]=L3.cget('text')
    else:
        div_beta=2
        while div_beta<=abs(beta_num) and div_beta<=abs(beta_denom):
            if beta_num%div_beta==0 and beta_denom%div_beta==0:
                beta_num=beta_num//div_beta
                beta_denom=beta_denom//div_beta
            else:
                div_beta=div_beta+1
        if beta_num<0 and beta_denom<0:
            L3=prgm.Label(prgm.root,text='\u03B2=('+str(int(-beta_num))+')/('+str(int(-beta_denom))+')='+str(beta_num/beta_denom).replace('.',','))
            L3.grid(column=6,row=2,sticky='w')
            prgm.rep[4]=L3.cget('text')
        else:
            L3=prgm.Label(prgm.root,text='\u03B2=('+str(int(beta_num))+')/('+str(int(beta_denom))+')='+str(beta_num/beta_denom).replace('.',','))
            L3.grid(column=6,row=2,sticky='w')
            prgm.rep[4]=L3.cget('text')
    if delta_num<0:
        fraction_pas_racine.main(a_num,a_denom,b_num,b_denom,c_num,c_denom,alpha_num,alpha_denom,beta_num,beta_denom,'','')
    elif delta_num==0:
        fraction_x0.main(a_num,a_denom,b_num,b_denom,c_num,c_denom,alpha_num,alpha_denom,beta_num,beta_denom,'','')
    else:
        fraction_x1.x1_frac(a_num,a_denom,b_num,b_denom,delta_num,delta_denom)
        fraction_x2.x2_frac(a_num,a_denom,b_num,b_denom,delta_num,delta_denom)
        if preferences.afficher_graphs==1:
            fraction_deux_racines_plt.main(a_num,a_denom,b_num,b_denom,c_num,c_denom,alpha_num,alpha_denom,beta_num,beta_denom,delta_num,delta_denom,'','')
