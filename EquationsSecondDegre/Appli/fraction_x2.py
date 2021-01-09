from tkinter import Label
import prgm

def x2_frac(a_num,a_denom,b_num,b_denom,delta_num,delta_denom):
    L5=Label(prgm.root,text='x\u2082='+str(((-b_num*a_denom*delta_denom**0.5)+(b_denom*a_denom*delta_num**0.5))/(b_denom*2*a_num*delta_denom**0.5)))
    L5.grid(column=6,row=4,sticky='w')
    prgm.rep[6]=L5.cget('text')
