import __main__

def main(path):
    rep_0=__main__.rep[0]
    rep_2=__main__.rep[2]
    rep_3=__main__.rep[3]
    rep_4=__main__.rep[4]
    rep_5=__main__.rep[5]
    rep_6=__main__.rep[6]
    __main__.rep[0]=__main__.rep[0].replace("\u00B2","\u005E2")
    __main__.rep[1]=' '
    __main__.rep[2]=__main__.rep[2].replace("\u0394","\u005CDelta")
    __main__.rep[3]=__main__.rep[3].replace("\u03B1","\u005Calpha")
    __main__.rep[4]=__main__.rep[4].replace("\u03B2","\u005Cbeta")
    __main__.rep[5]=__main__.rep[5].replace(" ","\u005C:")
    __main__.rep[5]=__main__.rep[5].replace("\u00E9","\u005Cacute e")
    __main__.rep[5]=__main__.rep[5].replace("\u2080","_0")
    __main__.rep[5]=__main__.rep[5].replace("\u2081","_1")
    __main__.rep[6]=__main__.rep[6].replace("\u2082","_2")
    for k in range(2):
        for i in range(len(__main__.rep[k+5])):
            if __main__.rep[k+5][i]=="\u221A" :
                ifin=__main__.rep[k+5].find(")", i)
                __main__.rep[k+5]=__main__.rep[k+5].replace(__main__.rep[k+5][i:ifin],"\u005Csqrt{"+__main__.rep[k+5][i+2:ifin]+"}")
    if __main__.rep[6]=='':
        __main__.rep[6]=' '
    file_write=open(path,'w',encoding="utf-8")
    file_write.writelines('\u005Cdocumentclass\u005Ba4paper\u005D\u007Barticle\u007D\n\u005Cusepackage\u005Butf8\u005D\u007Binputenc\u007D\n\u005Csetlength\u007B\u005Cparindent\u007D\u007B0cm\u007D\n\u005Cbegin\u007Bdocument\u007D\n')
    file_write.close()
    for i in range(len(__main__.rep)):
        file_write=open(path,'a',encoding="utf-8")
        file_write.writelines('$'+__main__.rep[i]+'$\u005C\u005C\n')
        file_write.close()
    file_write=open(path,'a',encoding="utf-8")
    file_write.writelines('\u005Cend\u007Bdocument\u007D')
    file_write.close()
    __main__.rep[0]=rep_0
    __main__.rep[1]=''
    __main__.rep[2]=rep_2
    __main__.rep[3]=rep_3
    __main__.rep[4]=rep_4
    __main__.rep[5]=rep_5
    __main__.rep[6]=rep_6
