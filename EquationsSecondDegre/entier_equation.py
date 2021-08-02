import prgm

def main():
    facteurs=[]
    if prgm.entier_val[0]==1:
        facteurs.append('')
    elif prgm.entier_val[0]==-1:
        facteurs.append('-')
    else:
        facteurs.append(str(prgm.entier_val[0]))
    if prgm.entier_val[1]==1:
        facteurs.append('+')
    elif prgm.entier_val[1]==-1:
        facteurs.append('-')
    elif prgm.entier_val[1]>0:
        facteurs.append('+'+str(prgm.entier_val[1]))
    else:
        facteurs.append(str(prgm.entier_val[1]))
    if prgm.entier_val[2]>0:
        facteurs.append('+'+str(prgm.entier_val[2]))
    else:
        facteurs.append(str(prgm.entier_val[2]))
    if prgm.entier_val[1]==0:
        if prgm.entier_val[2]==0:
            return 'f(x)='+facteurs[0]+'x\u00B2'
        else:
            return 'f(x)='+facteurs[0]+'x\u00B2'+facteurs[2]
    else:
        if prgm.entier_val[2]==0:
            return 'f(x)='+facteurs[0]+'x\u00B2'+facteurs[1]+'x'
        else:
            return 'f(x)='+facteurs[0]+'x\u00B2'+facteurs[1]+'x'+facteurs[2]