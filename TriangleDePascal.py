def factorielle(n):
    f=1
    for i in range(2,n+1):
        f*=i
    return f

def produit(a,b):
    p=1
    for i in range(a,b+1):
        p=p*i
    return p

def combinatoire(k,n):
    if k>n:
        return ''
    return produit(max(k,n-k)+1,n)//factorielle(min(k,n-k))

def pascal(n):
    chars=str(max(len(str(combinatoire(round(n/2),n))),4)+1)
    h=''
    for i in range((int(chars)+1)*(n+2)+n+3):
        h+='—'
    print(h)
    print(str('|%'+chars+'s')%'n\k',end=' |')
    for i in range(n+1):
        print(str('%'+chars+'s')%str(i),end=' |')
    print('')
    print(h)
    for i in range(n+1):
        print(str('|%'+chars+'s')%str(i),end=' |')
        for j in range(n+1):
            print(str('%'+chars+'s')%str(combinatoire(j,i)),end=' |')
        print('')
        print(h)
