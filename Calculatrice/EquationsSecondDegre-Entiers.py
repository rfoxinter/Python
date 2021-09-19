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
    alpha_n=-b
    alpha_d=2*a
    beta_n=-delta
    beta_d=4*a
    p_delta=str(delta)
    print('delta='+p_delta)
    if alpha_n%alpha_d==0:
        alpha=alpha_n//alpha_d
        p_alpha=str(alpha)
        print('alpha='+p_alpha)
    else:
        div_alpha=2
        while div_alpha<=abs(alpha_n) and div_alpha<=abs(alpha_d):
            if alpha_n%div_alpha==0 and alpha_d%div_alpha==0:
                alpha_n=alpha_n//div_alpha
                alpha_d=alpha_d//div_alpha
            else:
                div_alpha=div_alpha+1
        if alpha_n<0 and alpha_d<0:
            p_alpha_n=str(int(-alpha_n))
            p_alpha_d=str(int(-alpha_d))
            print('alpha=('+p_alpha_n+')/('+p_alpha_d+')')
        else:
            p_alpha_n=str(int(alpha_n))
            p_alpha_d=str(int(alpha_d))
            print('alpha=('+p_alpha_n+')/('+p_alpha_d+')')
    if beta_n%beta_d==0:
        beta=beta_n//beta_d
        p_beta=str(beta)
        print('beta='+p_beta)
    else:
        div_beta=2
        while div_beta<=abs(beta_n) and div_beta<=abs(beta_d):
            if beta_n%div_beta==0 and beta_d%div_beta==0:
                beta_n=beta_n//div_beta
                beta_d=beta_d//div_beta
            else:
                div_beta=div_beta+1
        if beta_n<0 and beta_d<0:
            p_beta_n=str(int(-beta_n))
            p_beta_d=str(int(-beta_d))
            print('beta=('+p_beta_n+')/('+p_beta_d+')')
        else:
            p_beta_n=str(int(beta_n))
            p_beta_d=str(int(beta_d))
            print('beta=('+p_beta_n+')/('+p_beta_d+')')
    if delta<0:
        print("L'équation n'admet pas de racine")
    if delta==0:
        x0_n=-b
        x0_d=2*a
        if x0_n%x0_d==0:
            x0=x0_n//x0_d
            p_x0=str(int(x0))
            print('x_0='+p_x0)
        else:
            div_x0=2
            while div_x0<=abs(x0_n) and div_x0<=abs(x0_d):
                if x0_n%div_x0==0 and x0_d%div_x0==0:
                    x0_n=x0_n//div_x0
                    x0_d=x0_d//div_x0
                else:
                    div_x0=div_x0+1
            if x0_n<0 and x0_d<0:
                p_x0_n=str(int(-x0_n))
                p_x0_d=str(int(-x0_d))
                print('x_0=('+p_x0_n+')/('+p_x0_d+')')
            else:
                p_x0_n=str(int(x0_n))
                p_x0_d=str(int(x0_d))
                print('x_0=('+p_x0_n+')/('+p_x0_d+')')
    if delta>0:
        if delta**0.5==int(delta**0.5):
            x1_n=-b-delta**0.5
            x1_d=2*a
            if x1_n%x1_d==0:
                x1=x1_n//x1_d
                p_x1=str(int(x1))
                print('x_1='+p_x1)
            else:
                div_x1=2
                while div_x1<=abs(x1_n) and div_x1<=abs(x1_d):
                    if x1_n%div_x1==0 and x1_d%div_x1==0:
                        x1_n=x1_n//div_x1
                        x1_d=x1_d//div_x1
                    else:
                        div_x1=div_x1+1
                if x1_n<0 and x1_d<0:
                    p_x1_n=str(int(-x1_n))
                    p_x1_d=str(int(-x1_d))
                    print('x_1=('+p_x1_n+')/('+p_x1_d+')')
                else:
                    p_x1_n=str(int(x1_n))
                    p_x1_d=str(int(x1_d))
                    print('x_1=('+p_x1_n+')/('+p_x1_d+')')
        else:
            x1_n_int=-b
            x1_n_rt=delta
            x1_d=2*a
            div_x1=2
            while div_x1<=abs(x1_n_int) and div_x1<=abs(x1_d):
                if x1_n_int%div_x1==0 and x1_d%div_x1==0 and x1_n_rt%div_x1**2==0:
                    x1_n_int=x1_n_int//div_x1
                    x1_d=x1_d//div_x1
                    x1_n_rt=x1_n_rt//div_x1**2
                else:
                    div_x1=div_x1+1
            p_x1_n_rt=str(x1_n_rt)
            if x1_n_int<0 and x1_d<0:
                p_x1_n_int=str(int(-x1_n_int))
                p_x1_d=str(int(-x1_d))
                if abs(x1_d)==1:
                    print('x_1='+p_x1_n_int+'+racine('+p_x1_n_rt+')')
                else:
                    print('x_1=('+p_x1_n_int+'+racine('+p_x1_n_rt+'))/('+p_x1_d+')')
            else:
                p_x1_n_int=str(int(x1_n_int))
                p_x1_d=str(int(x1_d))
                if abs(x1_d)==1:
                    print('x_1='+p_x1_n_int+'-racine('+p_x1_n_rt+')')
                else:
                    print('x_1=('+p_x1_n_int+'-racine('+p_x1_n_rt+'))/('+p_x1_d+')')
        if delta**0.5==int(delta**0.5):
            x2_n=-b+delta**0.5
            x2_d=2*a
            if x2_n%x2_d==0:
                x2=x2_n//x2_d
                p_x2=str(int(x2))
                print('x_2='+p_x2)
            else:
                div_x2=2
                while div_x2<=abs(x2_n) and div_x2<=abs(x2_d):
                    if x2_n%div_x2==0 and x2_d%div_x2==0:
                        x2_n=x2_n//div_x2
                        x2_d=x2_d//div_x2
                    else:
                        div_x2=div_x2+1
                if x2_n<0 and x2_d<0:
                    p_x2_n=str(int(-x2_n))
                    p_x2_d=str(int(-x2_d))
                    print('x_2=('+p_x2_n+')/('+p_x2_d+')')
                else:
                    p_x2_n=str(int(x2_n))
                    p_x2_d=str(int(x2_d))
                    print('x_2=('+p_x2_n+')/('+p_x2_d+')')
        else:
            x2_n_int=-b
            x2_n_rt=delta
            x2_d=2*a
            div_x2=2
            while div_x2<=abs(x2_n_int) and div_x2<=abs(x2_d):
                if x2_n_int%div_x2==0 and x2_d%div_x2==0 and x2_n_rt%div_x2**2==0:
                    x2_n_int=x2_n_int//div_x2
                    x2_d=x2_d//div_x2
                    x2_n_rt=x2_n_rt//div_x2**2
                else:
                    div_x2=div_x2+1
            p_x2_n_rt=str(x2_n_rt)
            if x2_n_int<0 and x2_d<0:
                p_x2_n_int=str(int(-x2_n_int))
                p_x2_d=str(int(-x2_d))
                if abs(x2_d)==1:
                    print('x_2='+p_x2_n_int+'-racine('+p_x2_n_rt+')')
                else:
                    print('x_2=('+p_x2_n_int+'-racine('+p_x2_n_rt+'))/('+p_x2_d+')')
            else:
                p_x2_n_int=str(int(x2_n_int))
                p_x2_d=str(int(x2_d))
                if abs(x2_d)==1:
                    print('x_2='+p_x2_n_int+'+racine('+p_x2_n_rt+')')
                else:
                    print('x_2=('+p_x2_n_int+'+racine('+p_x2_n_rt+'))/('+p_x2_d+')')
print('Résolution des équations du second degré')
main_sec()
