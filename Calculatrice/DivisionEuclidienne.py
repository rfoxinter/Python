def main_div():
    reco=1   
    while reco==1:
        de=int(eval(input('Entrer le dividende : ')))
        dr=int(eval(input('Entrer le diviseur : ')))
        diviseurs(de,dr)
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
def diviseurs(de,dr):
    print('Le quotient est : ',end='')
    print(de//dr)
    print('Le reste est : ',end='')
    print(de%dr)
print('Division euclidienne')
main_div()
