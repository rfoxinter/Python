def main_sec():
    reco=1   
    while reco==1:
        a=int(input('Entrer la valeur de a : '))
        b=int(input('Entrer la valeur de b : '))
        c=int(input('Entrer la valeur de c : '))
        sec_ent(a,b,c)
        reco=recommencer()

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
    p_delta=str(delta)
    print('delta='+p_delta)
    if alpha_num/alpha_denom==alpha_num//alpha_denom:
        alpha=alpha_num//alpha_denom
        p_alpha=str(alpha)
        print('alpha='+p_alpha)
    else:
        div_alpha=2
        while div_alpha<=abs(alpha_num) and div_alpha<=abs(alpha_denom):
            if alpha_num%div_alpha==0 and alpha_denom%div_alpha==0:
                alpha_num=alpha_num//div_alpha
                alpha_denom=alpha_denom//div_alpha
            else:
                div_alpha=div_alpha+1
        if alpha_num<0 and alpha_denom<0:
            p_alpha_num=str(int(-alpha_num))
            p_alpha_denom=str(int(-alpha_denom))
            print('alpha=('+p_alpha_num+')/('+p_alpha_denom+')')
        else:
            p_alpha_num=str(int(alpha_num))
            p_alpha_denom=str(int(alpha_denom))
            print('alpha=('+p_alpha_num+')/('+p_alpha_denom+')')
    if beta_num/beta_denom==beta_num//beta_denom:
        beta=beta_num//beta_denom
        p_beta=str(beta)
        print('beta='+p_beta)
    else:
        div_beta=2
        while div_beta<=abs(beta_num) and div_beta<=abs(beta_denom):
            if beta_num%div_beta==0 and beta_denom%div_beta==0:
                beta_num=beta_num//div_beta
                beta_denom=beta_denom//div_beta
            else:
                div_beta=div_beta+1
        if beta_num<0 and beta_denom<0:
            p_beta_num=str(int(-beta_num))
            p_beta_denom=str(int(-beta_denom))
            print('beta=('+p_beta_num+')/('+p_beta_denom+')')
        else:
            p_beta_num=str(int(beta_num))
            p_beta_denom=str(int(beta_denom))
            print('beta=('+p_beta_num+')/('+p_beta_denom+')')
    if delta<0:
        print("L'équation n'admet pas de racine")
    if delta==0:
        x0_num=-b
        x0_denom=2*a
        if x0_num/x0_denom==x0_num//x0_denom:
            x0=x0_num//x0_denom
            p_x0=str(int(x0))
            print('x_0='+p_x0)
        else:
            div_x0=2
            while div_x0<=abs(x0_num) and div_x0<=abs(x0_denom):
                if x0_num%div_x0==0 and x0_denom%div_x0==0:
                    x0_num=x0_num//div_x0
                    x0_denom=x0_denom//div_x0
                else:
                    div_x0=div_x0+1
            if x0_num<0 and x0_denom<0:
                p_x0_num=str(int(-x0_num))
                p_x0_denom=str(int(-x0_denom))
                print('L’équation admet une racine double en x_0=('+p_x0_num+')/('+p_x0_denom+')')
            else:
                p_x0_num=str(int(x0_num))
                p_x0_denom=str(int(x0_denom))
                print('L’équation admet une racine double en x_0=('+p_x0_num+')/('+p_x0_denom+')')
    if delta>0:
        if delta**0.5==int(delta**0.5):
            x1_num=-b-delta**0.5
            x1_denom=2*a
            if x1_num/x1_denom==x1_num//x1_denom:
                x1=x1_num//x1_denom
                p_x1=str(int(x1))
                print('x_1='+p_x1)
            else:
                div_x1=2
                while div_x1<=abs(x1_num) and div_x1<=abs(x1_denom):
                    if x1_num%div_x1==0 and x1_denom%div_x1==0:
                        x1_num=x1_num//div_x1
                        x1_denom=x1_denom//div_x1
                    else:
                        div_x1=div_x1+1
                if x1_num<0 and x1_denom<0:
                    p_x1_num=str(int(-x1_num))
                    p_x1_denom=str(int(-x1_denom))
                    print('x_1=('+p_x1_num+')/('+p_x1_denom+')')
                else:
                    p_x1_num=str(int(x1_num))
                    p_x1_denom=str(int(x1_denom))
                    print('x_1=('+p_x1_num+')/('+p_x1_denom+')')
        else:
            x1_num_int=-b
            x1_num_rt=delta
            x1_denom=2*a
            div_x1=2
            while div_x1<=abs(x1_num_int) and div_x1<=abs(x1_denom):
                if x1_num_int%div_x1==0 and x1_denom%div_x1==0 and x1_num_rt%div_x1**2==0:
                    x1_num_int=x1_num_int//div_x1
                    x1_denom=x1_denom//div_x1
                    x1_num_rt=x1_num_rt//div_x1**2
                else:
                    div_x1=div_x1+1
            p_x1_num_rt=str(x1_num_rt)
            if x1_num_int<0 and x1_denom<0:
                p_x1_num_int=str(int(-x1_num_int))
                p_x1_denom=str(int(-x1_denom))
                print('x_1=('+p_x1_num_int+'+racine('+p_x1_num_rt+'))/('+p_x1_denom+')')
            else:
                p_x1_num_int=str(int(x1_num_int))
                p_x1_denom=str(int(x1_denom))
                print('x_1=('+p_x1_num_int+'-racine('+p_x1_num_rt+'))/('+p_x1_denom+')')
        if delta**0.5==int(delta**0.5):
            x2_num=-b+delta**0.5
            x2_denom=2*a
            if x2_num/x2_denom==x2_num//x2_denom:
                x2=x2_num//x2_denom
                p_x2=str(int(x2))
                print('x_2='+p_x2)
            else:
                div_x2=2
                while div_x2<=abs(x2_num) and div_x2<=abs(x2_denom):
                    if x2_num%div_x2==0 and x2_denom%div_x2==0:
                        x2_num=x2_num//div_x2
                        x2_denom=x2_denom//div_x2
                    else:
                        div_x2=div_x2+1
                if x2_num<0 and x2_denom<0:
                    p_x2_num=str(int(-x2_num))
                    p_x2_denom=str(int(-x2_denom))
                    print('x_2=('+p_x2_num+')/('+p_x2_denom+')')
                else:
                    p_x2_num=str(int(x2_num))
                    p_x2_denom=str(int(x2_denom))
                    print('x_2=('+p_x2_num+')/('+p_x2_denom+')')
        else:
            x2_num_int=-b
            x2_num_rt=delta
            x2_denom=2*a
            div_x2=2
            while div_x2<=abs(x2_num_int) and div_x2<=abs(x2_denom):
                if x2_num_int%div_x2==0 and x2_denom%div_x2==0 and x2_num_rt%div_x2**2==0:
                    x2_num_int=x2_num_int//div_x2
                    x2_denom=x2_denom//div_x2
                    x2_num_rt=x2_num_rt//div_x2**2
                else:
                    div_x2=div_x2+1
            p_x2_num_rt=str(x2_num_rt)
            if x2_num_int<0 and x2_denom<0:
                p_x2_num_int=str(int(-x2_num_int))
                p_x2_denom=str(int(-x2_denom))
                print('x_2=('+p_x2_num_int+'-racine('+p_x2_num_rt+'))/('+p_x2_denom+')')
            else:
                p_x2_num_int=str(int(x2_num_int))
                p_x2_denom=str(int(x2_denom))
                print('x_2=('+p_x2_num_int+'+racine('+p_x2_num_rt+'))/('+p_x2_denom+')')

print('Calcul des équations du second degré par Théo')

main_sec()
