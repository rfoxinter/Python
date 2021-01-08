import __main__

def main(path):
    rep_0=__main__.rep[0]
    rep_2=__main__.rep[2]
    rep_3=__main__.rep[3]
    rep_4=__main__.rep[4]
    rep_5=__main__.rep[5]
    rep_6=__main__.rep[6]
    __main__.rep[0]=__main__.rep[0].replace("\u00B2","\u005C'b2")
    __main__.rep[2]=__main__.rep[2].replace("\u0394","\u005C'c4")
    __main__.rep[3]=__main__.rep[3].replace("\u03B1","\u005C'e1")
    __main__.rep[4]=__main__.rep[4].replace("\u03B2","\u005C'e2")
    __main__.rep[5]=__main__.rep[5].replace("\u2019","\u005Crquote ")
    __main__.rep[5]=__main__.rep[5].replace("\u00E9","\u005Cf1\u005C'e9\u005Cf0")
    __main__.rep[5]=__main__.rep[5].replace("\u2080","\u005Cf1\u005Cu8320\u003F\u005Cf0")
    __main__.rep[5]=__main__.rep[5].replace("\u2081","\u005Cf1\u005Cu8321\u003F\u005Cf0")
    __main__.rep[6]=__main__.rep[6].replace("\u2082","\u005Cf1\u005Cu8322\u003F\u005Cf0")
    for k in range(2):
        __main__.rep[k+5]=__main__.rep[k+5].replace("\u221A","\u005Cf1\u005Cu8730\u003F\u005Cf0")
    file_write=open(path,'w',encoding="utf-8")
    file_write.writelines('{\u005Crtf1\u005Cansi\u005Cdeff0{\u005Cfonttbl{\u005Cf0\u005Cfcharset161 Arial;}{\u005Cf1 Arial;}{\u005Cf2\u005Cfcharset1 Arial;}}\n')
    file_write.close()
    for i in range(len(__main__.rep)):
        file_write=open(path,'a',encoding="utf-8")
        file_write.writelines('\u005Cf0 '+__main__.rep[i]+'\u005Cpar\n')
        file_write.close()
    file_write=open(path,'a',encoding="utf-8")
    file_write.writelines('}')
    file_write.close()
    __main__.rep[0]=rep_0
    __main__.rep[2]=rep_2
    __main__.rep[3]=rep_3
    __main__.rep[4]=rep_4
    __main__.rep[5]=rep_5
    __main__.rep[6]=rep_6
