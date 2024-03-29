import prgm
import egalite

def main(a,b,delta):
    x2_num=-b+delta**0.5
    x2_denom=2*a
    if delta**0.5==int(delta**0.5):
        if x2_num%x2_denom==0:
            x2=x2_num//x2_denom
            L5=prgm.Label(prgm.root,text='x\u2082='+str(int(x2)))
            L5.grid(column=6,row=4,sticky='w')
            prgm.rep[6]=L5.cget('text')
        else:
            div_x2=2
            while div_x2<=abs(x2_num) and div_x2<=abs(x2_denom):
                if x2_num%div_x2==0 and x2_denom%div_x2==0:
                    x2_num=x2_num//div_x2
                    x2_denom=x2_denom//div_x2
                else:
                    div_x2=div_x2+1
            if x2_num<0 and x2_denom<0:
                L5=prgm.Label(prgm.root,text='x\u2082=('+str(int(-x2_num))+')/('+str(int(-x2_denom))+')'+egalite.main(x2_num/x2_denom)+str(round(x2_num/x2_denom,10)).replace('.',','))
                L5.grid(column=6,row=4,sticky='w')
                prgm.rep[6]=L5.cget('text')
            else:
                L5=prgm.Label(prgm.root,text='x\u2082=('+str(int(x2_num))+')/('+str(int(x2_denom))+')'+egalite.main(x2_num/x2_denom)+str(round(x2_num/x2_denom,10)).replace('.',','))
                L5.grid(column=6,row=4,sticky='w')
                prgm.rep[6]=L5.cget('text')
    else:
        x2_num_int=-b
        x2_num_rt=delta
        x2_denom_c=2*a
        x2_num_int_div=x2_num_int
        if x2_num_int_div==0:
            x2_num_int_div=x2_denom_c
        div_x2=2
        while div_x2<=abs(x2_num_int_div) and div_x2<=abs(x2_denom_c):
            if x2_num_int%div_x2==0 and x2_denom_c%div_x2==0 and x2_num_rt%div_x2**2==0:
                x2_num_int=x2_num_int//div_x2
                x2_denom_c=x2_denom_c//div_x2
                x2_num_rt=x2_num_rt//div_x2**2
                x2_num_int_div=x2_num_int_div//div_x2
            else:
                div_x2=div_x2+1
        if x2_num_int==0:
            if abs(x2_denom_c)==1:
                L5=prgm.Label(prgm.root,text='x\u2082=-\u221A('+str(x2_num_rt)+')'+egalite.main(x2_num/x2_denom)+str(round(x2_num/x2_denom,10)).replace('.',','))
                L5.grid(column=6,row=4,sticky='w')
                prgm.rep[6]=L5.cget('text')
            else:
                if x2_denom_c<0:
                    L5=prgm.Label(prgm.root,text='x\u2082=-\u221A('+str(x2_num_rt)+')/('+str(int(-x2_denom_c))+')'+egalite.main(x2_num/x2_denom)+str(round(x2_num/x2_denom,10)).replace('.',','))
                    L5.grid(column=6,row=4,sticky='w')
                    prgm.rep[6]=L5.cget('text')
                else:
                    L5=prgm.Label(prgm.root,text='x\u2082=\u221A('+str(x2_num_rt)+')/('+str(int(x2_denom_c))+')'+egalite.main(x2_num/x2_denom)+str(round(x2_num/x2_denom,10)).replace('.',','))
                    L5.grid(column=6,row=4,sticky='w')
                    prgm.rep[6]=L5.cget('text')
        elif x2_num_int<0 and x2_denom_c<0:
            if abs(x2_denom_c)==1:
                L5=prgm.Label(prgm.root,text='x\u2082='+str(int(-x2_num_int))+'-\u221A('+str(x2_num_rt)+')'+egalite.main(x2_num/x2_denom)+str(round(x2_num/x2_denom,10)).replace('.',','))
                L5.grid(column=6,row=4,sticky='w')
                prgm.rep[6]=L5.cget('text')
            else:
                L5=prgm.Label(prgm.root,text='x\u2082=('+str(int(-x2_num_int))+'-\u221A('+str(x2_num_rt)+'))/('+str(int(-x2_denom_c))+')'+egalite.main(x2_num/x2_denom)+str(round(x2_num/x2_denom,10)).replace('.',','))
                L5.grid(column=6,row=4,sticky='w')
                prgm.rep[6]=L5.cget('text')
        else:
            if abs(x2_denom_c)==1:
                L5=prgm.Label(prgm.root,text='x\u2082='+str(int(x2_num_int))+'+\u221A('+str(x2_num_rt)+')'+egalite.main(x2_num/x2_denom)+str(round(x2_num/x2_denom,10)).replace('.',','))
                L5.grid(column=6,row=4,sticky='w')
                prgm.rep[6]=L5.cget('text')
            else:
                L5=prgm.Label(prgm.root,text='x\u2082=('+str(int(x2_num_int))+'+\u221A('+str(x2_num_rt)+'))/('+str(int(x2_denom_c))+')'+egalite.main(x2_num/x2_denom)+str(round(x2_num/x2_denom,10)).replace('.',','))
                L5.grid(column=6,row=4,sticky='w')
                prgm.rep[6]=L5.cget('text')
