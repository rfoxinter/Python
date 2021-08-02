import prgm

def main():
    facteurs=[]
    a_num=prgm.fraction_val[0]
    a_denom=prgm.fraction_val[1]
    b_num=prgm.fraction_val[2]
    b_denom=prgm.fraction_val[3]
    c_num=prgm.fraction_val[4]
    c_denom=prgm.fraction_val[5]
    div_a=2
    while div_a<=abs(a_num) and div_a<=abs(a_denom):
        if a_num%div_a==0 and a_denom%div_a==0:
            a_num=a_num//div_a
            a_denom=a_denom//div_a
        else:
            div_a=div_a+1
    div_b=2
    while div_b<=abs(b_num) and div_b<=abs(b_denom):
        if b_num%div_b==0 and b_denom%div_b==0:
            b_num=b_num//div_b
            b_denom=b_denom//div_b
        else:
            div_b=div_b+1
    div_c=2
    while div_c<=abs(c_num) and div_c<=abs(c_denom):
        if c_num%div_c==0 and c_denom%div_c==0:
            c_num=c_num//div_c
            c_denom=c_denom//div_c
        else:
            div_c=div_c+1
    if a_denom==1:
        if a_num==1:
            facteurs.append('')
        elif a_num==-1:
            facteurs.append('-')
        else:
            facteurs.append(str(a_num))
    else:
        if a_num>0:
            facteurs.append('('+str(a_num)+')/('+str(a_denom)+')')
        else:
            facteurs.append('-('+str(-a_num)+')/('+str(a_denom)+')')
    if b_denom==1:
        if b_num==1:
            facteurs.append('+')
        elif b_num==-1:
            facteurs.append('-')
        elif b_num>0:
            facteurs.append('+'+str(b_num))
        else:
            facteurs.append(str(b_num))
    else:
        if b_num>0:
            facteurs.append('+('+str(b_num)+')/('+str(b_denom)+')')
        else:
            facteurs.append('-('+str(-b_num)+')/('+str(b_denom)+')')
    if c_denom==1:
        if c_num>0:
            facteurs.append('+'+str(c_num))
        else:
            facteurs.append(str(c_num))
    else:
        if c_num>0:
            facteurs.append('+('+str(c_num)+')/('+str(c_denom)+')')
        else:
            facteurs.append('-('+str(-c_num)+')/('+str(c_denom)+')')
    if b_num==0:
        if c_num==0:
            return 'f(x)='+facteurs[0]+'x\u00B2'
        else:
            return 'f(x)='+facteurs[0]+'x\u00B2'+facteurs[2]
    else:
        if c_num==0:
            return 'f(x)='+facteurs[0]+'x\u00B2'+facteurs[1]+'x'
        else:
            return 'f(x)='+facteurs[0]+'x\u00B2'+facteurs[1]+'x'+facteurs[2]