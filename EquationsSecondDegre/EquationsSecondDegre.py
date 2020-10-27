def main_sec():
    reco=1
    while reco==1:
        dec=decimal()
        if dec==0:
            a=int(input('Entrer la valeur de a : '))
            b=int(input('Entrer la valeur de b : '))
            c=int(input('Entrer la valeur de c : '))
            sec_ent(a,b,c)
        else:
            a_num=int(input('Entrer la valeur du num\u00E9rateur de a : '))
            a_denom=int(input('Entrer la valeur du d\u00E9nominateur de a : '))
            b_num=int(input('Entrer la valeur du num\u00E9rateur de b : '))
            b_denom=int(input('Entrer la valeur du d\u00E9nominateur de b : '))
            c_num=int(input('Entrer la valeur du num\u00E9rateur de c : '))
            c_denom=int(input('Entrer la valeur du d\u00E9nominateur de c : '))
            sec_dec(a_num,a_denom,b_num,b_denom,c_num,c_denom)
        reco=recommencer()

def decimal():
    decVal=-1
    while decVal==-1:
        decimal_0_1=input('Les coefficients sont-ils des fractions [0/1] : ')
        if decimal_0_1=='1':
            decVal=1
        elif decimal_0_1=='0':
            decVal=0
        else:
            print('Entrer 0 ou 1')
    return decVal

def recommencer():
    recVal=-1
    while recVal==-1:
        recommencer_0_1=input('Recommencer [0/1] : ')
        if recommencer_0_1=='1':
            recVal=1
        elif recommencer_0_1=='0':
            recVal=0
        else:
            print('Entrer 0 ou 1')
    return recVal

def sec_ent(a,b,c):
    delta=b**2-4*a*c
    alpha_num=-b
    alpha_denom=2*a
    beta_num=-delta
    beta_denom=4*a
    print('\u0394='+str(delta))
    if alpha_num%alpha_denom==0:
        alpha=alpha_num//alpha_denom
        print('\u03B1='+str(alpha))
    else:
        div_alpha=2
        while div_alpha<=abs(alpha_num) and div_alpha<=abs(alpha_denom):
            if alpha_num%div_alpha==0 and alpha_denom%div_alpha==0:
                alpha_num=alpha_num//div_alpha
                alpha_denom=alpha_denom//div_alpha
            else:
                div_alpha=div_alpha+1
        if alpha_num<0 and alpha_denom<0:
            print('\u03B1=('+str(int(-alpha_num))+')/('+str(int(-alpha_denom))+')='+str(alpha_num/alpha_denom))
        else:
            print('\u03B1=('+str(int(alpha_num))+')/('+str(int(alpha_denom))+')='+str(alpha_num/alpha_denom))
    if beta_num%beta_denom==0:
        beta=beta_num//beta_denom
        print('\u03B2='+str(beta))
    else:
        div_beta=2
        while div_beta<=abs(beta_num) and div_beta<=abs(beta_denom):
            if beta_num%div_beta==0 and beta_denom%div_beta==0:
                beta_num=beta_num//div_beta
                beta_denom=beta_denom//div_beta
            else:
                div_beta=div_beta+1
        if beta_num<0 and beta_denom<0:
            print('\u03B2=('+str(int(-beta_num))+')/('+str(int(-beta_denom))+')='+str(beta_num/beta_denom))
        else:
            print('\u03B2=('+str(int(beta_num))+')/('+str(int(beta_denom))+')='+str(beta_num/beta_denom))
    if delta<0:
        print('L\u2019\u00E9quation n\u2019admet pas de racine')
    elif delta==0:
        x0_num=-b
        x0_denom=2*a
        if x0_num%x0_denom==0:
            x0=x0_num//x0_denom
            print('L\u2019\u00E9quation admet une racine double en x\u2080='+str(int(x0)))
        else:
            div_x0=2
            while div_x0<=abs(x0_num) and div_x0<=abs(x0_denom):
                if x0_num%div_x0==0 and x0_denom%div_x0==0:
                    x0_num=x0_num//div_x0
                    x0_denom=x0_denom//div_x0
                else:
                    div_x0=div_x0+1
            if x0_num<0 and x0_denom<0:
                print('L\u2019\u00E9quation admet une racine double en x\u2080=('+str(int(-x0_num))+')/('+str(int(-x0_denom))+')='+str(x0_num/x0_denom))
            else:
                print('L\u2019\u00E9quation admet une racine double en x\u2080=('+str(int(x0_num))+')/('+str(int(x0_denom))+')='+str(x0_num/x0_denom))
    else:
        if delta**0.5==int(delta**0.5):
            x1_num=-b-delta**0.5
            x1_denom=2*a
            if x1_num%x1_denom==0:
                x1=x1_num//x1_denom
                print('L\u2019\u00E9quation admet une premi\u00E8re racine en x\u2081='+str(int(x1)))
            else:
                div_x1=2
                while div_x1<=abs(x1_num) and div_x1<=abs(x1_denom):
                    if x1_num%div_x1==0 and x1_denom%div_x1==0:
                        x1_num=x1_num//div_x1
                        x1_denom=x1_denom//div_x1
                    else:
                        div_x1=div_x1+1
                if x1_num<0 and x1_denom<0:
                    print('L\u2019\u00E9quation admet une premi\u00E8re racine en x\u2081=('+str(int(-x1_num))+')/('+str(int(-x1_denom))+')='+str(x1_num/x1_denom))
                else:
                    print('L\u2019\u00E9quation admet une premi\u00E8re racine en x\u2081=('+str(int(x1_num))+')/('+str(int(x1_denom))+')='+str(x1_num/x1_denom))
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
                    print('L\u2019\u00E9quation admet une premi\u00E8re racine en x\u2081=racine('+str(x1_num_rt)+')='+str(x1_num_rt**0.5))
                else:
                    if x1_denom<0:
                        print('L\u2019\u00E9quation admet une premi\u00E8re racine en x\u2081=racine('+str(x1_num_rt)+')/('+str(int(-x1_denom))+')='+str((x1_num_rt**0.5)/-x1_denom))
                    else:
                        print('L\u2019\u00E9quation admet une premi\u00E8re racine en x\u2081=-racine('+str(x1_num_rt)+')/('+str(int(x1_denom))+')='+str(-(x1_num_rt**0.5)/x1_denom))
            elif x1_num_int<0 and x1_denom<0:
                if abs(x1_denom)==1:
                    print('L\u2019\u00E9quation admet une premi\u00E8re racine en x\u2081='+str(int(-x1_num_int))+'+racine('+str(x1_num_rt)+')='+str(x1_num_int+x1_num_rt**0.5))
                else:
                    print('L\u2019\u00E9quation admet une premi\u00E8re racine en x\u2081=('+str(int(-x1_num_int))+'+racine('+str(x1_num_rt)+'))/('+str(int(-x1_denom))+')='+str((x1_num_int+x1_num_rt**0.5)/x1_denom))
            else:
                if abs(x1_denom)==1:
                    print('L\u2019\u00E9quation admet une premi\u00E8re racine en x\u2081='+str(int(x1_num_int))+'-racine('+str(x1_num_rt)+')='+str(x1_num_int-x1_num_rt**0.5))
                else:
                    print('L\u2019\u00E9quation admet une premi\u00E8re racine en x\u2081=('+str(int(x1_num_int))+'-racine('+str(x1_num_rt)+'))/('+str(int(x1_denom))+')='+str((x1_num_int-x1_num_rt**0.5)/x1_denom))
        if delta**0.5==int(delta**0.5):
            x2_num=-b+delta**0.5
            x2_denom=2*a
            if x2_num%x2_denom==0:
                x2=x2_num//x2_denom
                print('L\u2019\u00E9quation admet une deuxi\u00E8me racine en x\u2082='+str(int(x2)))
            else:
                div_x2=2
                while div_x2<=abs(x2_num) and div_x2<=abs(x2_denom):
                    if x2_num%div_x2==0 and x2_denom%div_x2==0:
                        x2_num=x2_num//div_x2
                        x2_denom=x2_denom//div_x2
                    else:
                        div_x2=div_x2+1
                if x2_num<0 and x2_denom<0:
                    print('L\u2019\u00E9quation admet une deuxi\u00E8me racine en x\u2082=('+str(int(-x2_num))+')/('+str(int(-x2_denom))+')='+str(x2_num/x2_denom))
                else:
                    print('L\u2019\u00E9quation admet une deuxi\u00E8me racine en x\u2082=('+str(int(x2_num))+')/('+str(int(x2_denom))+')='+str(x2_num/x2_denom))
        else:
            x2_num_int=-b
            x2_num_rt=delta
            x2_denom=2*a
            x2_num_int_div=x2_num_int
            if x2_num_int_div==0:
                x2_num_int_div=x2_denom
            div_x2=2
            while div_x2<=abs(x2_num_int_div) and div_x2<=abs(x2_denom):
                if x2_num_int%div_x2==0 and x2_denom%div_x2==0 and x2_num_rt%div_x2**2==0:
                    x2_num_int=x2_num_int//div_x2
                    x2_denom=x2_denom//div_x2
                    x2_num_rt=x2_num_rt//div_x2**2
                    x2_num_int_div=x2_num_int_div//div_x2
                else:
                    div_x2=div_x2+1
            if x2_num_int==0:
                if abs(x2_denom)==1:
                    print('L\u2019\u00E9quation admet une deuxi\u00E8me racine en x\u2082=-racine('+str(x2_num_rt)+')='+str(x2_num_rt**0.5))
                else:
                    if x2_denom<0:
                        print('L\u2019\u00E9quation admet une deuxi\u00E8me racine en x\u2082=-racine('+str(x2_num_rt)+')/('+str(int(-x2_denom))+')='+str(-(x2_num_rt**0.5)/-x2_denom))
                    else:
                        print('L\u2019\u00E9quation admet une deuxi\u00E8me racine en x\u2082=racine('+str(x2_num_rt)+')/('+str(int(x2_denom))+')='+str((x2_num_rt**0.5)/x2_denom))
            elif x2_num_int<0 and x2_denom<0:
                if abs(x2_denom)==1:
                    print('L\u2019\u00E9quation admet une deuxi\u00E8me racine en x\u2082='+str(int(-x2_num_int))+'-racine('+str(x2_num_rt)+')='+str(x2_num_int-x2_num_rt**0.5))
                else:
                    print('L\u2019\u00E9quation admet une deuxi\u00E8me racine en x\u2082=('+str(int(-x2_num_int))+'-racine('+str(x2_num_rt)+'))/('+str(int(-x2_denom))+')='+str((x2_num_int-x2_num_rt**0.5)/x2_denom))
            else:
                if abs(x2_denom)==1:
                    print('L\u2019\u00E9quation admet une deuxi\u00E8me racine en x\u2082='+str(int(x2_num_int))+'+racine('+str(x2_num_rt)+')='+str(x2_num_int+x2_num_rt**0.5))
                else:
                    print('L\u2019\u00E9quation admet une deuxi\u00E8me racine en x\u2082=('+str(int(x2_num_int))+'+racine('+str(x2_num_rt)+'))/('+str(int(x2_denom))+')='+str((x2_num_int+x2_num_rt**0.5)/x2_denom))

def sec_dec(a_num,a_denom,b_num,b_denom,c_num,c_denom):
    delta_num=b_num**2*a_denom*c_denom-4*a_num*c_num*b_denom**2
    delta_denom=a_denom*b_denom**2*c_denom
    if delta_num>0 and delta_denom<0:
        delta_num=-delta_num
        delta_denom=-delta_denom
    alpha_num=-b_num*a_denom
    alpha_denom=2*a_num*b_denom
    beta_num=-delta_num*a_denom
    beta_denom=4*a_num*delta_denom
    if delta_num%delta_denom==0:
        delta_num=delta_num//delta_denom
        print('\u0394='+str(delta_num))
    else:
        div_delta=2
        while div_delta<=abs(delta_num) and div_delta<=abs(delta_denom):
            if delta_num%div_delta==0 and delta_denom%div_delta==0:
                delta_num=delta_num//div_delta
                delta_denom=delta_denom//div_delta
            else:
                div_delta=div_delta+1
        if delta_num<0 and delta_denom<0:
            print('\u0394=('+str(int(-delta_num))+')/('+str(int(-delta_denom))+')='+str(delta_num/delta_denom))
        else:
            print('\u0394=('+str(int(delta_num))+')/('+str(int(delta_denom))+')='+str(delta_num/delta_denom))
    if alpha_num%alpha_denom==0:
        alpha=alpha_num//alpha_denom
        print('\u03B1='+str(alpha))
    else:
        div_alpha=2
        while div_alpha<=abs(alpha_num) and div_alpha<=abs(alpha_denom):
            if alpha_num%div_alpha==0 and alpha_denom%div_alpha==0:
                alpha_num=alpha_num//div_alpha
                alpha_denom=alpha_denom//div_alpha
            else:
                div_alpha=div_alpha+1
        if alpha_num<0 and alpha_denom<0:
            print('\u03B1=('+str(int(-alpha_num))+')/('+str(int(-alpha_denom))+')='+str(alpha_num/alpha_denom))
        else:
            print('\u03B1=('+str(int(alpha_num))+')/('+str(int(alpha_denom))+')='+str(alpha_num/alpha_denom))
    if beta_num%beta_denom==0:
        beta=beta_num//beta_denom
        print('\u03B2='+str(beta))
    else:
        div_beta=2
        while div_beta<=abs(beta_num) and div_beta<=abs(beta_denom):
            if beta_num%div_beta==0 and beta_denom%div_beta==0:
                beta_num=beta_num//div_beta
                beta_denom=beta_denom//div_beta
            else:
                div_beta=div_beta+1
        if beta_num<0 and beta_denom<0:
            print('\u03B2=('+str(int(-beta_num))+')/('+str(int(-beta_denom))+')')
        else:
            print('\u03B2=('+str(int(beta_num))+')/('+str(int(beta_denom))+')')
    if delta_num<0:
        print('L\u2019\u00E9quation n\u2019admet pas de racine.')
    if delta_num==0:
        x0_num=-b_num*a_denom
        x0_denom=2*a_num*b_denom
        if x0_num%x0_denom==0:
            x0=x0_num//x0_denom
            print('L\u2019\u00E9quation admet une racine double en x\u2080='+str(int(x0)))
        else:
            div_x0=2
            while div_x0<=abs(x0_num) and div_x0<=abs(x0_denom):
                if x0_num%div_x0==0 and x0_denom%div_x0==0:
                    x0_num=x0_num//div_x0
                    x0_denom=x0_denom//div_x0
                else:
                    div_x0=div_x0+1
            if x0_num<0 and x0_denom<0:
                print('L\u2019\u00E9quation admet une racine double en x\u2080=('+str(int(-x0_num))+')/('+str(int(-x0_denom))+')')
            else:
                print('L\u2019\u00E9quation admet une racine double en x\u2080=('+str(int(x0_num))+')/('+str(int(x0_denom))+')')
    if delta_num>0:
        x1_dec(a_num,a_denom,b_num,b_denom,delta_num,delta_denom)
        x2_dec(a_num,a_denom,b_num,b_denom,delta_num,delta_denom)

def x1_dec(a_num,a_denom,b_num,b_denom,delta_num,delta_denom):
    if delta_num**0.5==int(delta_num**0.5):
        if delta_denom**0.5==int(delta_denom**0.5):
            x1_num=(-b_num-(delta_num**0.5))*a_denom
            x1_denom=2*a_num*b_denom*(delta_denom**0.5)
            p_x1_num=str(x1_num)
            p_x1_denom=str(x1_denom)
            print('L\u2019\u00E9quation admet une premi\u00E8re racine en x\u2081=('+p_x1_num+')/('+p_x1_denom+').')
    else:
        print('racine 1')

def x2_dec(a_num,a_denom,b_num,b_denom,delta_num,delta_denom):
    print('racine 2')

print('R\u00E9solution des \u00E9quations du second degr\u00E9 par Th\u00E9o')

main_sec()
