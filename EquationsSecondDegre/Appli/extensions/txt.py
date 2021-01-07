import __main__

def main(path):
    file_write=open(path,'w',encoding="utf-8")
    file_write.writelines('')
    file_write.close()
    for i in range(len(__main__.rep)):
        file_write=open(path,'a',encoding="utf-8")
        file_write.writelines(__main__.rep[i]+'\n')
        file_write.close()
