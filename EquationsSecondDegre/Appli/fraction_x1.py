from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import __main__

def x1_frac(a_num,a_denom,b_num,b_denom,delta_num,delta_denom):
    if delta_num**0.5==int(delta_num**0.5):
        if delta_denom**0.5==int(delta_denom**0.5):
            x1_num=(-b_num-(delta_num**0.5))*a_denom
            x1_denom=2*a_num*b_denom*(delta_denom**0.5)
            p_x1_num=str(x1_num)
            p_x1_denom=str(x1_denom)
            print('L\u2019\u00E9quation admet une premi\u00E8re racine en x\u2081=('+p_x1_num+')/('+p_x1_denom+').')
        else:
            print('racine 1')
    else:
        print('racine 1')
