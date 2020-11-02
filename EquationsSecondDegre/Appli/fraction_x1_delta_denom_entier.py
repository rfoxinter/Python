from tkinter import *
import __main__

def main(a_num,a_denom,b_num,b_denom,delta_num,delta_denom):
    x1_num_int=int(-b_num*(delta_denom**0.5)*a_denom)
    x1_num_rt_int=int(-b_denom*a_denom)
    x1_num_rt=int(delta_num)
    x1_denom=int(b_denom*2*a_num*(delta_denom**0.5))
    x1_num_int_div=x1_num_int
    if x1_num_int==0:
        x1_num_int_div=x1_denom
    div_x1=2
    while div_x1<=abs(x1_num_int_div) and div_x1<=abs(x1_denom) and (div_x1<=abs(x1_num_rt_int) or div_x1**2<=x1_num_rt):
        if x1_num_int%div_x1==0 and x1_denom%div_x1==0 and (x1_num_rt_int%div_x1==0 or x1_num_rt%div_x1**2==0):
            x1_num_int=x1_num_int//div_x1
            x1_denom=x1_denom//div_x1
            if x1_num_rt%div_x1**2==0:
                x1_num_rt=x1_num_rt//div_x1**2
            else:
                x1_num_rt_int=x1_num_rt_int//div_x1
            x1_num_int_div=x1_num_int_div//div_x1
        else:
            div_x1=div_x1+1
    if x1_num_int==0:
        if x1_num_rt_int<0 and x1_denom<0:
            if x1_num_rt_int==1:
                L4=Label(__main__.Fen,text='x\u2081=(-\u221A('+str(x1_num_rt)+'))/('+str(-x1_denom)+')='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                L4.grid(column=6,row=3,sticky='w')
            elif x1_num_rt_int==-1:
                L4=Label(__main__.Fen,text='x\u2081=(\u221A('+str(x1_num_rt)+'))/('+str(-x1_denom)+')='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                L4.grid(column=6,row=3,sticky='w')
            else:
                L4=Label(__main__.Fen,text='x\u2081=('+str(-x1_num_rt_int)+'\u221A('+str(x1_num_rt)+'))/('+str(-x1_denom)+')='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                L4.grid(column=6,row=3,sticky='w')
        else:
            if x1_num_rt_int==1:
                L4=Label(__main__.Fen,text='x\u2081=(\u221A('+str(x1_num_rt)+'))/('+str(x1_denom)+')='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                L4.grid(column=6,row=3,sticky='w')
            elif x1_num_rt_int==-1:
                L4=Label(__main__.Fen,text='x\u2081=(-\u221A('+str(x1_num_rt)+'))/('+str(x1_denom)+')='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                L4.grid(column=6,row=3,sticky='w')
            else:
                L4=Label(__main__.Fen,text='x\u2081=('+str(x1_num_rt_int)+'\u221A('+str(x1_num_rt)+'))/('+str(x1_denom)+')='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                L4.grid(column=6,row=3,sticky='w')
    elif x1_denom<0 and (x1_num_int<0 or x1_num_rt_int<0):
        if x1_num_int>0:
            if x1_num_rt_int==1:
                L4=Label(__main__.Fen,text='x\u2081=(-\u221A('+str(x1_num_rt)+')-'+str(x1_num_int)+')/('+str(-x1_denom)+')='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                L4.grid(column=6,row=3,sticky='w')
            elif x1_num_rt_int==-1:
                L4=Label(__main__.Fen,text='x\u2081=(\u221A('+str(x1_num_rt)+')-'+str(x1_num_int)+')/('+str(-x1_denom)+')='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                L4.grid(column=6,row=3,sticky='w')
            else:
                L4=Label(__main__.Fen,text='x\u2081=('+str(-x1_num_rt_int)+'\u221A('+str(x1_num_rt)+')-'+str(x1_num_int)+')/('+str(-x1_denom)+')='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                L4.grid(column=6,row=3,sticky='w')
        else:
            if x1_num_rt_int==1:
                L4=Label(__main__.Fen,text='x\u2081=(-\u221A('+str(x1_num_rt)+')+'+str(-x1_num_int)+')/('+str(-x1_denom)+')='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                L4.grid(column=6,row=3,sticky='w')
            elif x1_num_rt_int==-1:
                L4=Label(__main__.Fen,text='x\u2081=(\u221A('+str(x1_num_rt)+')+'+str(-x1_num_int)+')/('+str(-x1_denom)+')='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                L4.grid(column=6,row=3,sticky='w')
            else:
                L4=Label(__main__.Fen,text='x\u2081=('+str(-x1_num_rt_int)+'\u221A('+str(x1_num_rt)+')+'+str(-x1_num_int)+')/('+str(-x1_denom)+')='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                L4.grid(column=6,row=3,sticky='w')
    else:
        if x1_num_int>0:
            if x1_num_rt_int==1:
                L4=Label(__main__.Fen,text='x\u2081=(\u221A('+str(x1_num_rt)+')+'+str(x1_num_int)+')/('+str(x1_denom)+')='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                L4.grid(column=6,row=3,sticky='w')
            else:
                L4=Label(__main__.Fen,text='x\u2081=('+str(x1_num_rt_int)+'\u221A('+str(x1_num_rt)+')+'+str(x1_num_int)+')/('+str(x1_denom)+')='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                L4.grid(column=6,row=3,sticky='w')
        else:
            if x1_num_rt_int==1:
                L4=Label(__main__.Fen,text='x\u2081=(\u221A('+str(x1_num_rt)+')-'+str(-x1_num_int)+')/('+str(x1_denom)+')='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                L4.grid(column=6,row=3,sticky='w')
            else:
                L4=Label(__main__.Fen,text='x\u2081=('+str(x1_num_rt_int)+'\u221A('+str(x1_num_rt)+')-'+str(-x1_num_int)+')/('+str(x1_denom)+')='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                L4.grid(column=6,row=3,sticky='w')