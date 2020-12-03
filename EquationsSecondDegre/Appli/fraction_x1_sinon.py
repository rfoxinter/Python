from tkinter import *
import __main__

def main(a_num,a_denom,b_num,b_denom,delta_num,delta_denom):
    L4=Label(__main__.Fen,text='x\u2081='+str(((-b_num*a_denom*(delta_denom**0.5))-(a_denom*b_denom*(delta_num**0.5)))/(2*a_num*b_denom*(delta_denom**0.5))))
    L4.grid(column=6,row=3,sticky='w')