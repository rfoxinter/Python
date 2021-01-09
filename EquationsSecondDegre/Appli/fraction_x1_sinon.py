from tkinter import Label
import __main__

#Define x1 for f(x1)=0 when delta=0
def main(a_num,a_denom,b_num,b_denom,delta_num,delta_denom):
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
    L4=Label(__main__.root,text='x\u2081='+str(((-b_num*a_denom*(delta_denom**0.5))-(a_denom*b_denom*(delta_num**0.5)))/(2*a_num*b_denom*(delta_denom**0.5))))
    L4.grid(column=6,row=3,sticky='w')
    "('('+str(x1_num_int_1)+'racine'+str(x1_num_rt_1+x1_num_int_2)+'racine'+str(x1_num_rt_2)+')/('+str(x1_denom_int)+'racine'+str(x1_denom_rt)+')')"
    __main__.rep[5]=L4.cget('text')