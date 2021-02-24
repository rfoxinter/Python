import prgm

def main(path):
    rep_0=prgm.rep[0]
    rep_2=prgm.rep[2]
    rep_3=prgm.rep[3]
    rep_4=prgm.rep[4]
    rep_5=prgm.rep[5]
    rep_6=prgm.rep[6]
    prgm.rep[0]=prgm.rep[0].replace("\u00B2","\u005C'b2")
    prgm.rep[2]=prgm.rep[2].replace("\u0394","\u005C'c4")
    prgm.rep[3]=prgm.rep[3].replace("\u03B1","\u005C'e1")
    prgm.rep[4]=prgm.rep[4].replace("\u03B2","\u005C'e2")
    prgm.rep[5]=prgm.rep[5].replace("\u2019","\u005Crquote ")
    prgm.rep[5]=prgm.rep[5].replace("\u00E9","\u005Cf1\u005C'e9\u005Cf0")
    prgm.rep[5]=prgm.rep[5].replace("\u2080","\u005Cf1\u005Cu8320\u003F\u005Cf0")
    prgm.rep[5]=prgm.rep[5].replace("\u2081","\u005Cf1\u005Cu8321\u003F\u005Cf0")
    prgm.rep[6]=prgm.rep[6].replace("\u2082","\u005Cf1\u005Cu8322\u003F\u005Cf0")
    for k in range(2):
        prgm.rep[k+5]=prgm.rep[k+5].replace("\u221A","\u005Cf1\u005Cu8730\u003F\u005Cf0")
    file_write=open(path,'w',encoding="utf-8")
    file_write.writelines('{\u005Crtf1\u005Cansi\u005Cdeff0{\u005Cfonttbl{\u005Cf0\u005Cfcharset161 DejaVu Sans;}{\u005Cf1 DejaVu Sans;}{\u005Cf2\u005Cfcharset1 DejaVu Sans;}}\n')
    file_write.close()
    for i in range(len(prgm.rep)):
        file_write=open(path,'a',encoding="utf-8")
        file_write.writelines('\u005Cf0 '+prgm.rep[i]+'\u005Cpar\n')
        file_write.close()
    file_write=open(path,'a',encoding="utf-8")
    file_write.writelines('}')
    file_write.close()
    prgm.rep[0]=rep_0
    prgm.rep[2]=rep_2
    prgm.rep[3]=rep_3
    prgm.rep[4]=rep_4
    prgm.rep[5]=rep_5
    prgm.rep[6]=rep_6
