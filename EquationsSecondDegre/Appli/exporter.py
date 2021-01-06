from tkinter.filedialog import asksaveasfile
import pathlib
import __main__

def main(event=None):
    file=asksaveasfile(mode='w',title='Enregistrer l\u2019\u00E9quation',filetypes=[('Fichier texte','*.txt'),('Rich Text Format','*.rtf')],defaultextension='*.txt')
    if file is None:
        return
    if __main__.latest=='entier':
        __main__.rep[0]='('+str(__main__.entier_val[0])+')x\u00B2+('+str(__main__.entier_val[1])+')x+('+str(__main__.entier_val[2])+')'
    elif __main__.latest=='fraction':
        __main__.rep[0]='('+str(__main__.entier_val[0])+'/'+str(__main__.entier_val[1])+')x\u00B2+('+str(__main__.entier_val[2])+'/'+str(__main__.entier_val[3])+')x+('+str(__main__.entier_val[4])+'/'+str(__main__.entier_val[5])+')'
    if pathlib.Path(file.name).suffix=='.txt':
        file_write=open(file.name,'w',encoding="utf-8")
        file_write.writelines('')
        file_write.close()
        for i in range(len(__main__.rep)):
            file_write=open(file.name,'a',encoding="utf-8")
            file_write.writelines(__main__.rep[i]+'\n')
            file_write.close()
    elif pathlib.Path(file.name).suffix=='.rtf':
        __main__.rep[0]=__main__.rep[0].replace("\u00B2","\u005C'b2")
        __main__.rep[2]=__main__.rep[2].replace("\u0394","\u005C'c4")
        __main__.rep[3]=__main__.rep[3].replace("\u03B1","\u005C'e1")
        __main__.rep[4]=__main__.rep[4].replace("\u03B2","\u005C'e2")
        __main__.rep[5]=__main__.rep[5].replace("\u2019","\u005Crquote ")
        __main__.rep[5]=__main__.rep[5].replace("\u00E9","\u005Cf1\u005C'e9\u005Cf0")
        __main__.rep[5]=__main__.rep[5].replace("\u2080","\u005Cf1\u005Cu8320\u003F\u005Cf0")
        __main__.rep[5]=__main__.rep[5].replace("\u2081","\u005Cf1\u005Cu8321\u003F\u005Cf0")
        __main__.rep[6]=__main__.rep[6].replace("\u2082","\u005Cf1\u005Cu8322\u003F\u005Cf0")
        file_write=open(file.name,'w',encoding="utf-8")
        file_write.writelines('{\u005Crtf1\u005Cansi\u005Cdeff0{\u005Cfonttbl{\u005Cf0\u005Cfcharset161 Arial;}{\u005Cf1 Arial;}}\n')
        file_write.close()
        for i in range(len(__main__.rep)):
            file_write=open(file.name,'a',encoding="utf-8")
            file_write.writelines('\u005Cf0 '+__main__.rep[i]+'\u005Cpar\n')
            file_write.close()
        file_write=open(file.name,'a',encoding="utf-8")
        file_write.writelines('}')
        #file_write.encode('ansi')
        file_write.close()
    file.close()