import prgm
import egalite

def main(a_num,a_denom,b_num,b_denom,delta_num,delta_denom):
    if delta_denom**0.5==int(delta_denom**0.5):
        x2_num=int((-b_num*(delta_denom**0.5)*a_denom)+((delta_num**0.5)*b_denom*a_denom))
        x2_denom=int(2*a_num*b_denom*(delta_denom**0.5))
        if x2_num%x2_denom==0:
            x2=x2_num//x2_denom
            L4=prgm.Label(prgm.root,text='x\u2082='+str(x2))
            L4.grid(column=6,row=4,sticky='w')
            prgm.rep[6]=L4.cget('text')
        else:
            div_x2=2
            while div_x2<=abs(x2_num) and div_x2<=abs(x2_denom):
                if x2_num%div_x2==0 and x2_denom%div_x2==0:
                    x2_num=x2_num//div_x2
                    x2_denom=x2_denom//div_x2
                else:
                    div_x2=div_x2+1
                
            if x2_num<0 and x2_denom<0:
                L4=prgm.Label(prgm.root,text='x\u2082=('+str(-x2_num)+')/('+str(-x2_denom)+')='+str(x2_num/x2_denom).replace('.',','))
                L4.grid(column=6,row=4,sticky='w')
                prgm.rep[6]=L4.cget('text')
            else:
                L4=prgm.Label(prgm.root,text='x\u2082=('+str(x2_num)+')/('+str(x2_denom)+')='+str(x2_num/x2_denom).replace('.',','))
                L4.grid(column=6,row=4,sticky='w')
                prgm.rep[6]=L4.cget('text')
    else:
        x2_num_int=int(b_denom*(delta_num**0.5)*a_denom)
        x2_num_rt_int=int(-b_num*a_denom)
        x2_num_rt=int(delta_denom)
        x2_denom_int=int(b_denom*2*a_num)
        x2_denom_rt=int(delta_denom)
        x2_num_rt_int_div=x2_num_rt_int
        x2_num_rt_div=x2_num_rt
        if x2_num_rt_int==0:
            x2_num_rt_int_div=x2_denom_int
            x2_num_rt_div=x2_denom_int
        div_x2=2
        while div_x2<=abs(x2_num_int) and (div_x2<=abs(x2_denom_int) or div_x2**2<=x2_denom_rt) and (div_x2<=abs(x2_num_rt_int_div) or div_x2**2<=x2_num_rt_div):
            if x2_num_int%div_x2==0 and (x2_denom_int%div_x2==0 or x2_denom_rt%div_x2**2==0) and (x2_num_rt_int%div_x2==0 or x2_num_rt%div_x2**2==0):
                x2_num_int=x2_num_int//div_x2
                if x2_denom_rt%div_x2**2==0:
                    x2_denom_rt=x2_denom_rt//div_x2**2
                else:
                    x2_denom_int=x2_denom_int//div_x2
                if x2_num_rt%div_x2**2==0:
                    x2_num_rt=x2_num_rt//div_x2**2
                else:
                    x2_num_rt_int=x2_num_rt_int//div_x2
                x2_num_rt_int_div=x2_num_rt_int_div//div_x2
                x2_num_rt_div=x2_num_rt_div//div_x2
            else:
                div_x2=div_x2+1
        x2_num_1=''
        x2_num_2=''
        x2_denom=''
        if x2_num_rt_int==0:
            x2_num_1=''
        elif x2_num_rt_int==1:
            x2_num_1='\u221A('+str(x2_num_rt)+')'
        elif x2_num_rt_int==-1:
            x2_num_1='-\u221A('+str(x2_num_rt)+')'
        else:
            x2_num_1=str(x2_num_rt_int)+'\u221A('+str(x2_num_rt)+')'
        if x2_num_int>0:
            x2_num_2='+'+str(x2_num_int)
        else:
            x2_num_2=str(x2_num_int)
        if x2_denom_int==0:
            x2_denom=''
        elif x2_denom_int==1:
            x2_denom='\u221A('+str(x2_denom_rt)+')'
        elif x2_denom_int==-1:
            x2_denom='-\u221A('+str(x2_denom_rt)+')'
        else:
            x2_denom=str(x2_denom_int)+'\u221A('+str(x2_denom_rt)+')'
        L4=prgm.Label(prgm.root,text='x\u2082=(('+x2_num_1+x2_num_2+')/('+x2_denom+'))'+egalite.main(((-b_num*a_denom*delta_denom**0.5)+(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5))+str(round(((-b_num*a_denom*delta_denom**0.5)+(a_denom*b_denom*delta_num**0.5))/(2*a_num*b_denom*delta_denom**0.5),10)).replace('.',','))
        L4.grid(column=6,row=4,sticky='w')
        prgm.rep[6]=L4.cget('text')