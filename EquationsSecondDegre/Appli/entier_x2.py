from tkinter import *
import __main__

def main(a,b,delta):
    if delta**0.5==int(delta**0.5):
        x2_num=-b+delta**0.5
        x2_denom=2*a
        if x2_num%x2_denom==0:
            x2=x2_num//x2_denom
            L5=Label(__main__.Fen,text='x\u2082='+str(int(x2)))
            L5.grid(column=6,row=4,sticky='w')
        else:
            div_x2=2
            while div_x2<=abs(x2_num) and div_x2<=abs(x2_denom):
                if x2_num%div_x2==0 and x2_denom%div_x2==0:
                    x2_num=x2_num//div_x2
                    x2_denom=x2_denom//div_x2
                else:
                    div_x2=div_x2+1
            if x2_num<0 and x2_denom<0:
                L5=Label(__main__.Fen,text='x\u2082=('+str(int(-x2_num))+')/('+str(int(-x2_denom))+')='+str(x2_num/x2_denom))
                L5.grid(column=6,row=4,sticky='w')
            else:
                L5=Label(__main__.Fen,text='x\u2082=('+str(int(x2_num))+')/('+str(int(x2_denom))+')='+str(x2_num/x2_denom))
                L5.grid(column=6,row=4,sticky='w')
    else:
        x2_num_int=-b
        x2_num_rt=delta
        x2_denom=2*a
        x2_num_int_div=x2_num_int
        if x2_num_int_div==0:
            x2_num_int_div=x2_denom
        div_x2=2
        while div_x2<=abs(x2_num_int_div) and div_x2<=abs(x2_denom):
            if x2_num_int%div_x2==0 and x2_denom%div_x2==0 and x2_num_rt%div_x2**2==0:
                x2_num_int=x2_num_int//div_x2
                x2_denom=x2_denom//div_x2
                x2_num_rt=x2_num_rt//div_x2**2
                x2_num_int_div=x2_num_int_div//div_x2
            else:
                div_x2=div_x2+1
        if x2_num_int==0:
            if abs(x2_denom)==1:
                L5=Label(__main__.Fen,text='x\u2082=-\u221A('+str(x2_num_rt)+')='+str(x2_num_int-x2_num_rt**0.5))
                L5.grid(column=6,row=4,sticky='w')
            else:
                if x2_denom<0:
                    L5=Label(__main__.Fen,text='x\u2082=-\u221A('+str(x2_num_rt)+')/('+str(int(-x2_denom))+')='+str(-(x2_num_rt**0.5)/-x2_denom))
                    L5.grid(column=6,row=4,sticky='w')
                else:
                    L5=Label(__main__.Fen,text='x\u2082=\u221A('+str(x2_num_rt)+')/('+str(int(x2_denom))+')='+str((x2_num_rt**0.5)/x2_denom))
                    L5.grid(column=6,row=4,sticky='w')
        elif x2_num_int<0 and x2_denom<0:
            if abs(x2_denom)==1:
                L5=Label(__main__.Fen,text='x\u2082='+str(int(-x2_num_int))+'-\u221A('+str(x2_num_rt)+')='+str(x2_num_int-x2_num_rt**0.5))
                L5.grid(column=6,row=4,sticky='w')
            else:
                L5=Label(__main__.Fen,text='x\u2082=('+str(int(-x2_num_int))+'-\u221A('+str(x2_num_rt)+'))/('+str(int(-x2_denom))+')='+str((x2_num_int-x2_num_rt**0.5)/x2_denom))
                L5.grid(column=6,row=4,sticky='w')
        else:
            if abs(x2_denom)==1:
                L5=Label(__main__.Fen,text='x\u2082='+str(int(x2_num_int))+'+\u221A('+str(x2_num_rt)+')='+str(x2_num_int+x2_num_rt**0.5))
                L5.grid(column=6,row=4,sticky='w')
            else:
                L5=Label(__main__.Fen,text='x\u2082=('+str(int(x2_num_int))+'+\u221A('+str(x2_num_rt)+'))/('+str(int(x2_denom))+')='+str((x2_num_int+x2_num_rt**0.5)/x2_denom))
                L5.grid(column=6,row=4,sticky='w')
