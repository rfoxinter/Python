from tkinter import Label
import prgm

#Define x1 for f(x1)=0 when delta=0
def main(a_num,a_denom,b_num,b_denom,delta_num,delta_denom):
    x1_num_1=''
    x1_num_2=''
    x1_denom=''
    x1_num_int_1=int(-b_num*a_denom)
    x1_num_rt_1=int(delta_denom)
    x1_num_int_2=int(-b_denom*a_denom)
    x1_num_rt_2=int(delta_num)
    x1_denom_int=int(b_denom*2*a_num)
    x1_denom_rt=int(delta_denom)
    x1_num_int_1_div=x1_num_int_1
    x1_num_rt_1_div=x1_num_rt_1
    if x1_num_rt_1==0:
            x1_num_int_1=x1_denom_int
            x1_num_rt_1=x1_denom_int
    div_x1=2
    while (div_x1<=abs(x1_num_int_2) or div_x1**2<=x1_num_rt_2) and (div_x1<=abs(x1_denom_int) or div_x1**2<=x1_denom_rt) and (div_x1<=abs(x1_num_int_1_div) or div_x1**2<=x1_num_rt_1):
        if (x1_num_int_2%div_x1==0 or x1_num_rt_2%div_x1**2==0) and (x1_denom_int%div_x1==0 or x1_denom_rt%div_x1**2==0) and (x1_num_int_1%div_x1==0 or x1_num_rt_1%div_x1**2==0):
            if x1_num_rt_2%div_x1**2==0:
                x1_num_rt_2=x1_num_rt_2//div_x1**2
            else:
                x1_num_int_2=x1_num_int_2//div_x1
            if x1_denom_rt%div_x1**2==0:
                x1_denom_rt=x1_denom_rt//div_x1**2
            else:
                x1_denom_int=x1_denom_int//div_x1
            if x1_num_rt_1%div_x1**2==0:
                x1_num_rt_1=x1_num_rt_1//div_x1**2
            else:
                x1_num_rt_1=x1_num_rt_1//div_x1
            x1_num_int_1_div=x1_num_int_1_div//div_x1
            x1_num_rt_1_div=x1_num_rt_1_div//div_x1
        else:
            div_x1=div_x1+1
    print(x1_num_int_1)
    if x1_denom_int==1:
        x1_denom='\u221A('+str(x1_denom_rt)+')'
    elif x1_denom_int==-1:
        x1_denom='-\u221A('+str(x1_denom_rt)+')'
    else:
        x1_denom=str(x1_denom_int)+'\u221A('+str(x1_denom_rt)+')'
    if x1_num_int_1==1:
        x1_num_1='\u221A('+str(x1_num_rt_1)+')'
    elif x1_num_int_1==-1:
        x1_num_1='-\u221A('+str(x1_num_rt_1)+')'
    else:
        x1_num_1=str(x1_num_int_1)+'\u221A('+str(x1_num_rt_1)+')'
    if x1_num_int_2==1:
        x1_num_2='\u221A('+str(x1_num_rt_2)+')'
    elif x1_num_int_2==-1:
        x1_num_2='-\u221A('+str(x1_num_rt_2)+')'
    elif x1_num_int_2<0:
        x1_num_2=str(x1_num_int_2)+'\u221A('+str(x1_num_rt_2)+')'
    else:
        x1_num_2='+'+str(x1_num_int_2)+'\u221A('+str(x1_num_rt_2)+')'
    if x1_num_int_1==0:
        L4=Label(prgm.root,text='x\u2081=('+x1_num_2.replace('+','')+')/('+x1_denom+')='+str(((-b_num*a_denom*(delta_denom**0.5))-(a_denom*b_denom*(delta_num**0.5)))/(2*a_num*b_denom*(delta_denom**0.5))))
        L4.grid(column=6,row=3,sticky='w')
        prgm.rep[5]=L4.cget('text')
    else:
        L4=Label(prgm.root,text='x\u2081=('+x1_num_1+x1_num_2+')/('+x1_denom+')='+str(((-b_num*a_denom*(delta_denom**0.5))-(a_denom*b_denom*(delta_num**0.5)))/(2*a_num*b_denom*(delta_denom**0.5))))
        L4.grid(column=6,row=3,sticky='w')
        prgm.rep[5]=L4.cget('text')
"""    L4=Label(prgm.root,text='x\u2081='+str(((-b_num*a_denom*(delta_denom**0.5))-(a_denom*b_denom*(delta_num**0.5)))/(2*a_num*b_denom*(delta_denom**0.5))))
    L4.grid(column=6,row=3,sticky='w')
    "('('+str(x1_num_int_1)+'racine'+str(x1_num_rt_1+x1_num_int_2)+'racine'+str(x1_num_rt_2)+')/('+str(x1_denom_int)+'racine'+str(x1_denom_rt)+')')"
    prgm.rep[5]=L4.cget('text')"""