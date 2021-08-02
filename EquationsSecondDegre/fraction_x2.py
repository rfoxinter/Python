import prgm
import fraction_x2_delta_num_entier
import fraction_x2_delta_denom_entier
import fraction_x2_sinon

def x2_frac(a_num,a_denom,b_num,b_denom,delta_num,delta_denom):
    if delta_num**0.5==int(delta_num**0.5):
        fraction_x2_delta_num_entier.main(a_num,a_denom,b_num,b_denom,delta_num,delta_denom)
    elif delta_denom**0.5==int(delta_denom**0.5):
        fraction_x2_delta_denom_entier.main(a_num,a_denom,b_num,b_denom,delta_num,delta_denom)
    else:
        fraction_x2_sinon.main(a_num,a_denom,b_num,b_denom,delta_num,delta_denom)