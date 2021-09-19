def main_div():
    reco=1   
    while reco==1:
        dec=int(input('Entrer le nombre à décomposer : '))
        diviseurs(dec)
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
def diviseurs(nbr):
    n=nbr
    d=2
    diviseurs=[]
    while d<=n:
        div=0
        while n%d==0:
            n=n//d
            if div==0:
                diviseurs.append([d,1])
                div=1
            else:
                diviseurs[len(diviseurs)-1][1]+=1
        d+=1
    nombre=str(nbr)+'='
    for i in range(len(diviseurs)):
        if diviseurs[i][1]==1:
            nombre+=str(diviseurs[i][0])
        else:
            nombre+=str(diviseurs[i][0])
            p=str(diviseurs[i][1])
            for j in range(len(p)):
                if int(p[j])<4:
                    nombre+=chr(ord(p[j])+128)
                else:
                    nombre+=chr(ord(p[j])+8256)
        nombre+='×'
    nombre=nombre[0:len(nombre)-1]
    print(nombre)
print('Décompositions en facteurs premiers')
main_div()
