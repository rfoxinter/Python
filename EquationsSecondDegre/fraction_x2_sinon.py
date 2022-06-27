import prgm
import egalite

def main(a_num,a_denom,b_num,b_denom,delta_num,delta_denom):
    x2_num_1=''
    x2_num_2=''
    x2_denom=''
    x2_num_int_1=int(-b_num*a_denom)
    x2_num_rt_1=int(delta_denom)
    x2_num_int_2=int(b_denom*a_denom)
    x2_num_rt_2=int(delta_num)
    x2_denom_int=int(b_denom*2*a_num)
    x2_denom_rt=int(delta_denom)
    x2_num_int_1_div=x2_num_int_1
    x2_num_rt_1_div=x2_num_rt_1
    if x2_num_rt_1==0:
            x2_num_int_1=x2_denom_int
            x2_num_rt_1=x2_denom_int
    div_x2=2
    while (div_x2<=abs(x2_num_int_2) or div_x2**2<=x2_num_rt_2) and (div_x2<=abs(x2_denom_int) or div_x2**2<=x2_denom_rt) and (div_x2<=abs(x2_num_int_1_div) or div_x2**2<=x2_num_rt_1):
        if (x2_num_int_2%div_x2==0 or x2_num_rt_2%div_x2**2==0) and (x2_denom_int%div_x2==0 or x2_denom_rt%div_x2**2==0) and (x2_num_int_1%div_x2==0 or x2_num_rt_1%div_x2**2==0):
            if x2_num_rt_2%div_x2**2==0:
                x2_num_rt_2=x2_num_rt_2//div_x2**2
            else:
                x2_num_int_2=x2_num_int_2//div_x2
            if x2_denom_rt%div_x2**2==0:
                x2_denom_rt=x2_denom_rt//div_x2**2
            else:
                x2_denom_int=x2_denom_int//div_x2
            if x2_num_rt_1%div_x2**2==0:
                x2_num_rt_1=x2_num_rt_1//div_x2**2
            else:
                x2_num_int_1=x2_num_int_1//div_x2
            x2_num_int_1_div=x2_num_int_1_div//div_x2
            x2_num_rt_1_div=x2_num_rt_1_div//div_x2
        else:
            div_x2=div_x2+1
    if x2_denom_int==1:
        x2_denom='\u221A('+str(x2_denom_rt)+')'
    elif x2_denom_int==-1:
        x2_denom='-\u221A('+str(x2_denom_rt)+')'
    else:
        x2_denom=str(x2_denom_int)+'\u221A('+str(x2_denom_rt)+')'
    if x2_num_int_1==1:
        x2_num_1='+\u221A('+str(x2_num_rt_1)+')'
    elif x2_num_int_1==-1:
        x2_num_1='-\u221A('+str(x2_num_rt_1)+')'
    else:
        x2_num_1=str(x2_num_int_1)+'\u221A('+str(x2_num_rt_1)+')'
    if x2_num_int_2==1:
        x2_num_2='+\u221A('+str(x2_num_rt_2)+')'
    elif x2_num_int_2==-1:
        x2_num_2='-\u221A('+str(x2_num_rt_2)+')'
    elif x2_num_int_2<0:
        x2_num_2=str(x2_num_int_2)+'\u221A('+str(x2_num_rt_2)+')'
    else:
        x2_num_2='+'+str(x2_num_int_2)+'\u221A('+str(x2_num_rt_2)+')'
    if x2_num_int_1==0:
        L4=prgm.Label(prgm.root,text='x\u2082=('+x2_num_2.replace('+','')+')/('+x2_denom+')'+egalite.main(((-b_num*a_denom*(delta_denom**0.5))+(a_denom*b_denom*(delta_num**0.5)))/(2*a_num*b_denom*(delta_denom**0.5)))+str(round(((-b_num*a_denom*(delta_denom**0.5))+(a_denom*b_denom*(delta_num**0.5)))/(2*a_num*b_denom*(delta_denom**0.5)),10)).replace('.',','))
        L4.grid(column=6,row=4,sticky='w')
        prgm.rep[6]=L4.cget('text')
    else:
        L4=prgm.Label(prgm.root,text='x\u2082=('+x2_num_1+x2_num_2+')/('+x2_denom+')'+egalite.main(((-b_num*a_denom*(delta_denom**0.5))+(a_denom*b_denom*(delta_num**0.5)))/(2*a_num*b_denom*(delta_denom**0.5)))+str(round(((-b_num*a_denom*(delta_denom**0.5))+(a_denom*b_denom*(delta_num**0.5)))/(2*a_num*b_denom*(delta_denom**0.5)),10)).replace('.',','))
        L4.grid(column=6,row=4,sticky='w')
        prgm.rep[6]=L4.cget('text')
