import prgm

def main(path):
    file_write=open(path,'w',encoding="utf-8")
    file_write.writelines('')
    file_write.close()
    for i in range(len(prgm.rep)):
        file_write=open(path,'a',encoding="utf-8")
        file_write.writelines(prgm.rep[i]+'\n')
        file_write.close()
