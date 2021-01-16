import base64
import prgm

def main(path):
    prgm.rep[1]='<br/>'
    file_write=open(path,'w',encoding="utf-8")
    file_write.writelines('<!DOCTYPE html>\n<html>\n    <head>\n        <meta charset="utf-8" />\n        <link rel="icon" href="data:image/x-icon;base64,'+str(base64.b64encode((open(r'python.ico','rb')).read())).replace("b'","").replace("'","")+'"/>\n        <title>'+prgm.rep[0]+'</title>\n    </head>\n    <body>\n')
    file_write.close()
    for i in range(len(prgm.rep)):
        file_write=open(path,'a',encoding="utf-8")
        file_write.writelines('        <p style="font-family: Arial;">'+prgm.rep[i]+'</p>\n')
        file_write.close()
    file_write=open(path,'a',encoding="utf-8")
    file_write.writelines('    </body>\n</html>')
    file_write.close()
    prgm.rep[1]=''
