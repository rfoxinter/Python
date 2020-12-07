from tkinter import *
import fraction_x1_delta_num_entier
import fraction_x1_delta_denom_entier
import fraction_x1_sinon

#Define file to run depending on delta
def x1_frac(a_num,a_denom,b_num,b_denom,delta_num,delta_denom):
    if delta_num**0.5==int(delta_num**0.5):
        fraction_x1_delta_num_entier.main(a_num,a_denom,b_num,b_denom,delta_num,delta_denom)
    elif delta_denom**0.5==int(delta_denom**0.5):
        fraction_x1_delta_denom_entier.main(a_num,a_denom,b_num,b_denom,delta_num,delta_denom)
    else:
        fraction_x1_sinon.main(a_num,a_denom,b_num,b_denom,delta_num,delta_denom)
