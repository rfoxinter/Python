import prgm

def main(a,b,delta):
    if delta**0.5==int(delta**0.5):
        x1_num=-b-delta**0.5
        x1_denom=2*a
        if x1_num%x1_denom==0:
            x1=x1_num//x1_denom
            L4=prgm.Label(prgm.root,text='x\u2081='+str(int(x1)))
            L4.grid(column=6,row=3,sticky='w')
            prgm.rep[5]=L4.cget('text')
        else:
            div_x1=2
            while div_x1<=abs(x1_num) and div_x1<=abs(x1_denom):
                if x1_num%div_x1==0 and x1_denom%div_x1==0:
                    x1_num=x1_num//div_x1
                    x1_denom=x1_denom//div_x1
                else:
                    div_x1=div_x1+1
            if x1_num<0 and x1_denom<0:
                L4=prgm.Label(prgm.root,text='x\u2081=('+str(int(-x1_num))+')/('+str(int(-x1_denom))+')='+str(x1_num/x1_denom).replace('.',','))
                L4.grid(column=6,row=3,sticky='w')
                prgm.rep[5]=L4.cget('text')
            else:
                L4=prgm.Label(prgm.root,text='x\u2081=('+str(int(x1_num))+')/('+str(int(x1_denom))+')='+str(x1_num/x1_denom).replace('.',','))
                L4.grid(column=6,row=3,sticky='w')
                prgm.rep[5]=L4.cget('text')
    else:
        x1_num_int=-b
        x1_num_rt=delta
        x1_denom=2*a
        x1_num_int_div=x1_num_int
        if x1_num_int_div==0:
            x1_num_int_div=x1_denom
        div_x1=2
        while div_x1<=abs(x1_num_int_div) and div_x1<=abs(x1_denom):
            if x1_num_int%div_x1==0 and x1_denom%div_x1==0 and x1_num_rt%div_x1**2==0:
                x1_num_int=x1_num_int//div_x1
                x1_denom=x1_denom//div_x1
                x1_num_rt=x1_num_rt//div_x1**2
                x1_num_int_div=x1_num_int_div//div_x1
            else:
                div_x1=div_x1+1
        if x1_num_int==0:
            if abs(x1_denom)==1:
                L4=prgm.Label(prgm.root,text='x\u2081=\u221A('+str(x1_num_rt)+')='+str(x1_num_rt**0.5).replace('.',','))
                L4.grid(column=6,row=3,sticky='w')
                prgm.rep[5]=L4.cget('text')
            else:
                if x1_denom<0:
                    L4=prgm.Label(prgm.root,text='x\u2081=\u221A('+str(x1_num_rt)+')/('+str(int(-x1_denom))+')='+str((x1_num_rt**0.5)/-x1_denom).replace('.',','))
                    L4.grid(column=6,row=3,sticky='w')
                    prgm.rep[5]=L4.cget('text')
                else:
                    L4=prgm.Label(prgm.root,text='x\u2081=-\u221A('+str(x1_num_rt)+')/('+str(int(x1_denom))+')='+str(-(x1_num_rt**0.5)/x1_denom).replace('.',','))
                    L4.grid(column=6,row=3,sticky='w')
                    prgm.rep[5]=L4.cget('text')
        elif x1_num_int<0 and x1_denom<0:
            if abs(x1_denom)==1:
                L4=prgm.Label(prgm.root,text='x\u2081='+str(int(-x1_num_int))+'+\u221A('+str(x1_num_rt)+')='+str(x1_num_int+x1_num_rt**0.5).replace('.',','))
                L4.grid(column=6,row=3,sticky='w')
                prgm.rep[5]=L4.cget('text')
            else:
                L4=prgm.Label(prgm.root,text='x\u2081=('+str(int(-x1_num_int))+'+\u221A('+str(x1_num_rt)+'))/('+str(int(-x1_denom))+')='+str((x1_num_int+x1_num_rt**0.5)/x1_denom).replace('.',','))
                L4.grid(column=6,row=3,sticky='w')
                prgm.rep[5]=L4.cget('text')
        else:
            if abs(x1_denom)==1:
                L4=prgm.Label(prgm.root,text='x\u2081='+str(int(x1_num_int))+'-\u221A('+str(x1_num_rt)+')='+str(x1_num_int-x1_num_rt**0.5).replace('.',','))
                L4.grid(column=6,row=3,sticky='w')
                prgm.rep[5]=L4.cget('text')
            else:
                L4=prgm.Label(prgm.root,text='x\u2081=('+str(int(x1_num_int))+'-\u221A('+str(x1_num_rt)+'))/('+str(int(x1_denom))+')='+str((x1_num_int-x1_num_rt**0.5)/x1_denom).replace('.',','))
                L4.grid(column=6,row=3,sticky='w')
                prgm.rep[5]=L4.cget('text')
