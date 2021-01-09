from tkinter.filedialog import asksaveasfile
import pathlib
import __main__
from extensions import *

def main(event=None):
    file_list=[('Fichier texte','.txt .text'),('Fichier Rich Text Format','.rtf'),('Fichier Hypertext Markup Language','.html .htm'),('Fichier LaTeX','.tex'),('Tous les fichiers','.*')]
    file=asksaveasfile(title='Enregistrer l\u2019\u00E9quation',filetypes=file_list,defaultextension='.txt')
    if file is None:
        return
    if __main__.latest=='entier':
        if __main__.entier_val[0]==1:
            if __main__.entier_val[1]<-1:
                if __main__.entier_val[2]<0:
                    __main__.rep[0]='f(x)=x\u00B2-'+str(-__main__.entier_val[1])+'x-'+str(-__main__.entier_val[2])
                elif __main__.entier_val[2]==0:
                    __main__.rep[0]='f(x)=x\u00B2-'+str(-__main__.entier_val[1])+'x'
                else:
                    __main__.rep[0]='f(x)=x\u00B2-'+str(-__main__.entier_val[1])+'x+'+str(__main__.entier_val[2])
            elif __main__.entier_val[1]==0:
                if __main__.entier_val[2]<0:
                    __main__.rep[0]='f(x)=x\u00B2-'+str(-__main__.entier_val[2])
                elif __main__.entier_val[2]==0:
                    __main__.rep[0]='f(x)=x\u00B2'
                else:
                    __main__.rep[0]='f(x)=x\u00B2+'+str(__main__.entier_val[2])
            elif __main__.entier_val[1]==1:
                if __main__.entier_val[2]<0:
                    __main__.rep[0]='f(x)=x\u00B2+x-'+str(-__main__.entier_val[2])
                elif __main__.entier_val[2]==0:
                    __main__.rep[0]='f(x)=x\u00B2+x'
                else:
                    __main__.rep[0]='f(x)=x\u00B2+x+'+str(__main__.entier_val[2])
            elif __main__.entier_val[1]==-1:
                if __main__.entier_val[2]<0:
                    __main__.rep[0]='f(x)=x\u00B2-x-'+str(-__main__.entier_val[2])
                elif __main__.entier_val[2]==0:
                    __main__.rep[0]='f(x)=x\u00B2-x'
                else:
                    __main__.rep[0]='f(x)=x\u00B2-x+'+str(__main__.entier_val[2])
            else:
                if __main__.entier_val[2]<0:
                    __main__.rep[0]='f(x)=x\u00B2+'+str(__main__.entier_val[1])+'x-'+str(-__main__.entier_val[2])
                elif __main__.entier_val[2]==0:
                    __main__.rep[0]='f(x)=x\u00B2+'+str(__main__.entier_val[1])+'x'
                else:
                    __main__.rep[0]='f(x)=x\u00B2+'+str(__main__.entier_val[1])+'x+'+str(__main__.entier_val[2])
        elif __main__.entier_val[0]==-1:
            if __main__.entier_val[1]<-1:
                if __main__.entier_val[2]<0:
                    __main__.rep[0]='f(x)=-x\u00B2-'+str(-__main__.entier_val[1])+'x-'+str(-__main__.entier_val[2])
                elif __main__.entier_val[2]==0:
                    __main__.rep[0]='f(x)=-x\u00B2-'+str(-__main__.entier_val[1])+'x'
                else:
                    __main__.rep[0]='f(x)=-x\u00B2-'+str(-__main__.entier_val[1])+'x+'+str(__main__.entier_val[2])
            elif __main__.entier_val[1]==0:
                if __main__.entier_val[2]<0:
                    __main__.rep[0]='f(x)=-x\u00B2-'+str(-__main__.entier_val[2])
                elif __main__.entier_val[2]==0:
                    __main__.rep[0]='f(x)=-x\u00B2'
                else:
                    __main__.rep[0]='f(x)=-x\u00B2+'+str(__main__.entier_val[2])
            elif __main__.entier_val[1]==1:
                if __main__.entier_val[2]<0:
                    __main__.rep[0]='f(x)=-x\u00B2+x-'+str(-__main__.entier_val[2])
                elif __main__.entier_val[2]==0:
                    __main__.rep[0]='f(x)=-x\u00B2+x'
                else:
                    __main__.rep[0]='f(x)=-x\u00B2+x+'+str(__main__.entier_val[2])
            elif __main__.entier_val[1]==-1:
                if __main__.entier_val[2]<0:
                    __main__.rep[0]='f(x)=-x\u00B2-x-'+str(-__main__.entier_val[2])
                elif __main__.entier_val[2]==0:
                    __main__.rep[0]='f(x)=-x\u00B2-x'
                else:
                    __main__.rep[0]='f(x)=-x\u00B2-x+'+str(__main__.entier_val[2])
            else:
                if __main__.entier_val[2]<0:
                    __main__.rep[0]='f(x)=-x\u00B2+'+str(__main__.entier_val[1])+'x-'+str(-__main__.entier_val[2])
                elif __main__.entier_val[2]==0:
                    __main__.rep[0]='f(x)=-x\u00B2+'+str(__main__.entier_val[1])+'x'
                else:
                    __main__.rep[0]='f(x)=-x\u00B2+'+str(__main__.entier_val[1])+'x+'+str(__main__.entier_val[2])
        else:
            if __main__.entier_val[1]<-1:
                if __main__.entier_val[2]<0:
                    __main__.rep[0]='f(x)='+str(__main__.entier_val[0])+'x\u00B2-'+str(-__main__.entier_val[1])+'x-'+str(-__main__.entier_val[2])
                elif __main__.entier_val[2]==0:
                    __main__.rep[0]='f(x)='+str(__main__.entier_val[0])+'x\u00B2-'+str(-__main__.entier_val[1])+'x'
                else:
                    __main__.rep[0]='f(x)='+str(__main__.entier_val[0])+'x\u00B2-'+str(-__main__.entier_val[1])+'x+'+str(__main__.entier_val[2])
            elif __main__.entier_val[1]==0:
                if __main__.entier_val[2]<0:
                    __main__.rep[0]='f(x)='+str(__main__.entier_val[0])+'x\u00B2-'+str(-__main__.entier_val[2])
                elif __main__.entier_val[2]==0:
                    __main__.rep[0]='f(x)='+str(__main__.entier_val[0])+'x\u00B2'
                else:
                    __main__.rep[0]='f(x)='+str(__main__.entier_val[0])+'x\u00B2+'+str(__main__.entier_val[2])
            elif __main__.entier_val[1]==1:
                if __main__.entier_val[2]<0:
                    __main__.rep[0]='f(x)='+str(__main__.entier_val[0])+'x\u00B2+x-'+str(-__main__.entier_val[2])
                elif __main__.entier_val[2]==0:
                    __main__.rep[0]='f(x)='+str(__main__.entier_val[0])+'x\u00B2+x'
                else:
                    __main__.rep[0]='f(x)='+str(__main__.entier_val[0])+'x\u00B2+x+'+str(__main__.entier_val[2])
            elif __main__.entier_val[1]==-1:
                if __main__.entier_val[2]<0:
                    __main__.rep[0]='f(x)='+str(__main__.entier_val[0])+'x\u00B2-x-'+str(-__main__.entier_val[2])
                elif __main__.entier_val[2]==0:
                    __main__.rep[0]='f(x)='+str(__main__.entier_val[0])+'x\u00B2-x'
                else:
                    __main__.rep[0]='f(x)='+str(__main__.entier_val[0])+'x\u00B2-x+'+str(__main__.entier_val[2])
            else:
                if __main__.entier_val[2]<0:
                    __main__.rep[0]='f(x)='+str(__main__.entier_val[0])+'x\u00B2+'+str(__main__.entier_val[1])+'x-'+str(-__main__.entier_val[2])
                elif __main__.entier_val[2]==0:
                    __main__.rep[0]='f(x)='+str(__main__.entier_val[0])+'x\u00B2+'+str(__main__.entier_val[1])+'x'
                else:
                    __main__.rep[0]='f(x)='+str(__main__.entier_val[0])+'x\u00B2+'+str(__main__.entier_val[1])+'x+'+str(__main__.entier_val[2])
    elif __main__.latest=='fraction':
        __main__.rep[0]='('+str(__main__.fraction_val[0])+')/('+str(__main__.fraction_val[1])+')x\u00B2+('+str(__main__.fraction_val[2])+')/('+str(__main__.fraction_val[3])+')x+('+str(__main__.fraction_val[4])+')/('+str(__main__.fraction_val[5])+')'
    if  pathlib.Path(file.name).suffix=='.rtf':
        rtf.main(file.name)
    elif pathlib.Path(file.name).suffix=='.html' or pathlib.Path(file.name).suffix=='.htm':
        html.main(file.name)
    elif pathlib.Path(file.name).suffix=='.tex':
        tex.main(file.name)
    else:
        txt.main(file.name)
    file.close()