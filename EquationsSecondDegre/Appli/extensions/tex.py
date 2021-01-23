import prgm

def main(path):
    rep_0=prgm.rep[0]
    rep_2=prgm.rep[2]
    rep_3=prgm.rep[3]
    rep_4=prgm.rep[4]
    rep_5=prgm.rep[5]
    rep_6=prgm.rep[6]
    prgm.rep[0]=prgm.rep[0].replace("\u00B2","\u005E2")
    prgm.rep[1]=' '
    prgm.rep[2]=prgm.rep[2].replace("\u0394","\u005CDelta")
    prgm.rep[3]=prgm.rep[3].replace("\u03B1","\u005Calpha")
    prgm.rep[4]=prgm.rep[4].replace("\u03B2","\u005Cbeta")
    prgm.rep[5]=prgm.rep[5].replace(" ","\u005C:")
    prgm.rep[5]=prgm.rep[5].replace("\u00E9","\u005Cacute e")
    prgm.rep[5]=prgm.rep[5].replace("\u2080","_0")
    prgm.rep[5]=prgm.rep[5].replace("\u2081","_1")
    prgm.rep[6]=prgm.rep[6].replace("\u2082","_2")
    for k in range(2):
        for i in range(len(prgm.rep[k+5])):
            if prgm.rep[k+5][i]=="\u221A" :
                ifin=prgm.rep[k+5].find(")",i)
                prgm.rep[k+5]=prgm.rep[k+5].replace(prgm.rep[k+5][i:ifin+1],"\u005Csqrt{"+prgm.rep[k+5][i+2:ifin]+"}")
    for k in range(7):
        prgm.rep[k]=prgm.rep[k].replace(")/(","}{")
        prgm.rep[k]=prgm.rep[k].replace(")","}")
        prgm.rep[k]=prgm.rep[k].replace("(","\u005Cfrac{")
        prgm.rep[k]=prgm.rep[k].replace("\u005Cfrac{x}","(x)")
    if prgm.rep[6]=='':
        prgm.rep[6]=' '
    file_write=open(path,'w',encoding="utf-8")
    file_write.writelines('\u005Cdocumentclass\u005Ba4paper\u005D\u007Barticle\u007D\n\u005Cusepackage\u005Butf8\u005D\u007Binputenc\u007D\n\u005Csetlength\u007B\u005Cparindent\u007D\u007B0cm\u007D\n\u005Cbegin\u007Bdocument\u007D\n')
    file_write.close()
    for i in range(len(prgm.rep)):
        file_write=open(path,'a',encoding="utf-8")
        file_write.writelines('$'+prgm.rep[i]+'$\u005C\u005C\n')
        file_write.close()
    file_write=open(path,'a',encoding="utf-8")
    file_write.writelines('\u005Cend\u007Bdocument\u007D')
    file_write.close()
    prgm.rep[0]=rep_0
    prgm.rep[1]=''
    prgm.rep[2]=rep_2
    prgm.rep[3]=rep_3
    prgm.rep[4]=rep_4
    prgm.rep[5]=rep_5
    prgm.rep[6]=rep_6
