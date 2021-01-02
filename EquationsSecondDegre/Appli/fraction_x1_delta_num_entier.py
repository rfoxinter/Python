from tkinter import Label
import __main__

#Define x1 for f(x1)=0 when delta=0
def main(a_num,a_denom,b_num,b_denom,delta_num,delta_denom):
    if delta_denom**0.5==int(delta_denom**0.5):
        x1_num=int((-b_num*(delta_denom**0.5)*a_denom)-((delta_num**0.5)*b_denom*a_denom))
        x1_denom=int(2*a_num*b_denom*(delta_denom**0.5))
        if x1_num%x1_denom==0:
            x1=x1_num//x1_denom
            L4=Label(__main__.root,text='x\u2081='+str(x1))
            L4.grid(column=6,row=3,sticky='w')
        else:
            div_x1=2
            while div_x1<=abs(x1_num) and div_x1<=abs(x1_denom):
                if x1_num%div_x1==0 and x1_denom%div_x1==0:
                    x1_num=x1_num//div_x1
                    x1_denom=x1_denom//div_x1
                else:
                    div_x1=div_x1+1
                
            if x1_num<0 and x1_denom<0:
                L4=Label(__main__.root,text='x\u2081=('+str(-x1_num)+')/('+str(-x1_denom)+')='+str(x1_num/x1_denom))
                L4.grid(column=6,row=3,sticky='w')
            else:
                L4=Label(__main__.root,text='x\u2081=('+str(x1_num)+')/('+str(x1_denom)+')='+str(x1_num/x1_denom))
                L4.grid(column=6,row=3,sticky='w')
    else:
        x1_num_int=int(-b_denom*(delta_num**0.5)*a_denom)
        x1_num_rt_int=int(-b_num*a_denom)
        x1_num_rt=int(delta_denom)
        x1_denom_int=int(b_denom*2*a_num)
        x1_denom_rt=int(delta_denom)
        x1_num_rt_int_div=x1_num_rt_int
        x1_num_rt_div=x1_num_rt
        if x1_num_rt_int==0:
            x1_num_rt_int_div=x1_denom_int
            x1_num_rt_div=x1_denom_int
        div_x1=2
        while div_x1<=abs(x1_num_int) and (div_x1<=abs(x1_denom_int) or div_x1**2<=x1_denom_rt) and (div_x1<=abs(x1_num_rt_int_div) or div_x1**2<=x1_num_rt_div):
            if x1_num_int%div_x1==0 and (x1_denom_int%div_x1==0 or x1_denom_rt%div_x1**2==0) and (x1_num_rt_int%div_x1==0 or x1_num_rt%div_x1**2==0):
                x1_num_int=x1_num_int//div_x1
                if x1_denom_rt%div_x1**2==0:
                    x1_denom_rt=x1_denom_rt//div_x1**2
                else:
                    x1_denom_int=x1_denom_int//div_x1
                if x1_num_rt%div_x1**2==0:
                    x1_num_rt=x1_num_rt//div_x1**2
                else:
                    x1_num_rt_int=x1_num_rt_int//div_x1
                x1_num_rt_int_div=x1_num_rt_int_div//div_x1
                x1_num_rt_div=x1_num_rt_div//div_x1
            else:
                div_x1=div_x1+1
        if x1_num_rt_int==0:
            if x1_num_int<0 and x1_denom_int<0:
                if x1_denom_int==-1:
                    L4=Label(__main__.root,text='x\u2081=('+str(-x1_num_int)+')/(\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                    L4.grid(column=6,row=3,sticky='w')
                else:
                    L4=Label(__main__.root,text='x\u2081=('+str(-x1_num_int)+')/('+str(-x1_denom_int)+'\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                    L4.grid(column=6,row=3,sticky='w')
            else:
                if x1_denom_int==1:
                    L4=Label(__main__.root,text='x\u2081=('+str(x1_num_int)+')/(\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                    L4.grid(column=6,row=3,sticky='w')
                elif x1_denom_int==-1:
                    L4=Label(__main__.root,text='x\u2081=('+str(-x1_num_int)+')/(\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                    L4.grid(column=6,row=3,sticky='w')
                else:
                    L4=Label(__main__.root,text='x\u2081=('+str(x1_num_int)+')/('+str(x1_denom_int)+'\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                    L4.grid(column=6,row=3,sticky='w')
        elif x1_denom_int<0 and (x1_num_int<0 or x1_num_rt_int<0):
            if x1_num_int>0:
                if x1_denom_int==-1:
                    if x1_num_rt_int==1:
                        L4=Label(__main__.root,text='x\u2081=(\u221A('+str(x1_num_rt)+')-'+str(-x1_num_int)+')/(-\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                    elif x1_num_rt_int==-1:
                        L4=Label(__main__.root,text='x\u2081=(\u221A('+str(x1_num_rt)+')+'+str(-x1_num_int)+')/(\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                    else:
                        L4=Label(__main__.root,text='x\u2081=('+str(-x1_num_rt_int)+'\u221A('+str(x1_num_rt)+')+'+str(-x1_num_int)+')/(\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                else:
                    if x1_num_rt_int==1:
                        L4=Label(__main__.root,text='x\u2081=(\u221A('+str(x1_num_rt)+')-'+str(-x1_num_int)+')/('+str(x1_denom_int)+'\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                    elif x1_num_rt_int==-1:
                        L4=Label(__main__.root,text='x\u2081=(\u221A('+str(x1_num_rt)+')+'+str(-x1_num_int)+')/(-\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                    else:
                        L4=Label(__main__.root,text='x\u2081=('+str(-x1_num_rt_int)+'\u221A('+str(x1_num_rt)+')+'+str(-x1_num_int)+')/(-\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
            else:
                if x1_denom_int==-1:
                    if x1_num_rt_int==1:
                        L4=Label(__main__.root,text='x\u2081=(\u221A('+str(x1_num_rt)+')+'+str(x1_num_int)+')/(-\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                    elif x1_num_rt_int==-1:
                        L4=Label(__main__.root,text='x\u2081=(\u221A('+str(x1_num_rt)+')-'+str(x1_num_int)+')/(\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                    else:
                        L4=Label(__main__.root,text='x\u2081=('+str(-x1_num_rt_int)+'\u221A('+str(x1_num_rt)+')-'+str(x1_num_int)+')/(\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                else:
                    if x1_num_rt_int==1:
                        L4=Label(__main__.root,text='x\u2081=(\u221A('+str(x1_num_rt)+')+'+str(x1_num_int)+')/('+str(x1_denom_int)+'\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                    elif x1_num_rt_int==-1:
                        L4=Label(__main__.root,text='x\u2081=(\u221A('+str(x1_num_rt)+')-'+str(x1_num_int)+')/(-\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                    else:
                        L4=Label(__main__.root,text='x\u2081=('+str(-x1_num_rt_int)+'\u221A('+str(x1_num_rt)+')-'+str(x1_num_int)+')/(-\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
        else:
            if x1_num_int>0:
                if x1_denom_int==1:
                    if x1_num_rt_int==1:
                        L4=Label(__main__.root,text='x\u2081=(\u221A('+str(x1_num_rt)+')+'+str(x1_num_int)+')/(\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                    elif x1_num_rt_int==-1:
                        L4=Label(__main__.root,text='x\u2081=(-\u221A('+str(x1_num_rt)+')+'+str(x1_num_int)+')/(\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                    else:
                        L4=Label(__main__.root,text='x\u2081=('+str(x1_num_rt_int)+'\u221A('+str(x1_num_rt)+')+'+str(x1_num_int)+')/(\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                elif x1_denom_int==-1:
                    if x1_num_rt_int==1:
                        L4=Label(__main__.root,text='x\u2081=(\u221A('+str(x1_num_rt)+')+'+str(x1_num_int)+')/(-\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                    elif x1_num_rt_int==-1:
                        L4=Label(__main__.root,text='x\u2081=(-\u221A('+str(x1_num_rt)+')+'+str(x1_num_int)+')/(-\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                    else:
                        L4=Label(__main__.root,text='x\u2081=('+str(x1_num_rt_int)+'\u221A('+str(x1_num_rt)+')+'+str(x1_num_int)+')/(-\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                else:
                    if x1_num_rt_int==1:
                        L4=Label(__main__.root,text='x\u2081=(\u221A('+str(x1_num_rt)+')+'+str(x1_num_int)+')/('+str(x1_denom_int)+'\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                    elif x1_num_rt_int==-1:
                        L4=Label(__main__.root,text='x\u2081=(-\u221A('+str(x1_num_rt)+')+'+str(x1_num_int)+')/('+str(x1_denom_int)+'\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                    else:
                        L4=Label(__main__.root,text='x\u2081=('+str(x1_num_rt_int)+'\u221A('+str(x1_num_rt)+')+'+str(x1_num_int)+')/('+str(x1_denom_int)+'\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
            else:
                if x1_denom_int==1:
                    if x1_num_rt_int==1:
                        L4=Label(__main__.root,text='x\u2081=(\u221A('+str(x1_num_rt)+')-'+str(-x1_num_int)+')/(\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                    elif x1_num_rt_int==-1:
                        L4=Label(__main__.root,text='x\u2081=(-\u221A('+str(x1_num_rt)+')-'+str(-x1_num_int)+')/(\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                    else:
                        L4=Label(__main__.root,text='x\u2081=('+str(x1_num_rt_int)+'\u221A('+str(x1_num_rt)+')-'+str(-x1_num_int)+')/(\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                elif x1_denom_int==-1:
                    if x1_num_rt_int==1:
                        L4=Label(__main__.root,text='x\u2081=(\u221A('+str(x1_num_rt)+')-'+str(-x1_num_int)+')/(-\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                    elif x1_num_rt_int==-1:
                        L4=Label(__main__.root,text='x\u2081=(-\u221A('+str(x1_num_rt)+')-'+str(-x1_num_int)+')/(-\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                    else:
                        L4=Label(__main__.root,text='x\u2081=('+str(x1_num_rt_int)+'\u221A('+str(x1_num_rt)+')-'+str(-x1_num_int)+')/(-\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                else:
                    if x1_num_rt_int==1:
                        L4=Label(__main__.root,text='x\u2081=(\u221A('+str(x1_num_rt)+')-'+str(-x1_num_int)+')/('+str(x1_denom_int)+'\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                    elif x1_num_rt_int==-1:
                        L4=Label(__main__.root,text='x\u2081=(-\u221A('+str(x1_num_rt)+')-'+str(-x1_num_int)+')/('+str(x1_denom_int)+'\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
                    else:
                        L4=Label(__main__.root,text='x\u2081=('+str(x1_num_rt_int)+'\u221A('+str(x1_num_rt)+')-'+str(-x1_num_int)+')/('+str(x1_denom_int)+'\u221A('+str(x1_denom_rt)+'))='+str(((-b_num*a_denom*delta_denom**0.5)-(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5)))
                        L4.grid(column=6,row=3,sticky='w')
