from tkinter import *
import __main__

def x1_frac(a_num,a_denom,b_num,b_denom,delta_num,delta_denom):
    if delta_num**0.5==int(delta_num**0.5):
        if delta_denom**0.5==int(delta_denom**0.5):
            x1_num=int((-b_num-(delta_num**0.5))*a_denom)
            x1_denom=int(2*a_num*b_denom*(delta_denom**0.5))
            if x1_num%x1_denom==0:
                x1=x1_num//x1_denom
                L4=Label(__main__.Fen,text='x\u2081='+str(x1))
                L4.grid(column=6,row=3,sticky='w')
            else:
                div_x1=2
                while div_x1<=abs(x1_num) and div_x1<=abs(x1_denom):
                    if x1_num%div_x1==0 and x1_denom%div_x1==0:
                        x1_num=x1_num//div_x1
                        x1_denom=x1_denom//div_x1
                    else:
                        div_x1=div_x1+1
                L4=Label(__main__.Fen,text='x\u2081=('+str(x1_num)+')/('+str(x1_denom)+')='+str(x1_num/x1_denom))
                L4.grid(column=6,row=3,sticky='w')
        else:
            L5=Label(__main__.Fen,text='x\u2081='+str(((-b_num*a_denom*delta_denom**0.5)-(b_denom*a_denom*delta_num**0.5))/(b_denom*2*a_num*delta_denom**0.5)))
            L5.grid(column=6,row=3,sticky='w')
    else:
        L5=Label(__main__.Fen,text='x\u2081='+str(((-b_num*a_denom*delta_denom**0.5)-(b_denom*a_denom*delta_num**0.5))/(b_denom*2*a_num*delta_denom**0.5)))
        L5.grid(column=6,row=3,sticky='w')
