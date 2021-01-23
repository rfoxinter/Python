from tkinter.filedialog import asksaveasfile
import pathlib
import prgm
from extensions import *

def main(event=None):
    file_list=[('Fichier texte','.txt .text'),('Fichier Rich Text Format','.rtf'),('Fichier Document Office Open XML','.docx'),('Fichier HyperText Markup Language','.html .htm'),('Fichier Extensible HyperText Markup Language','.xhtml'),('Fichier LaTeX','.tex'),('Tous les fichiers','.*')]
    file=asksaveasfile(title='Exporter l\u2019\u00E9quation',filetypes=file_list,defaultextension='.txt')
    if file is None:
        return
    facteurs=[]
    if prgm.latest=='entier':
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
                prgm.rep[0]='f(x)='+facteurs[0]+'x\u00B2'
            else:
                prgm.rep[0]='f(x)='+facteurs[0]+'x\u00B2'+facteurs[2]
        else:
            if prgm.entier_val[2]==0:
                prgm.rep[0]='f(x)='+facteurs[0]+'x\u00B2'+facteurs[1]+'x'
            else:
                prgm.rep[0]='f(x)='+facteurs[0]+'x\u00B2'+facteurs[1]+'x'+facteurs[2]
    elif prgm.latest=='fraction':
        prgm.rep[0]='('+str(prgm.fraction_val[0])+')/('+str(prgm.fraction_val[1])+')x\u00B2+('+str(prgm.fraction_val[2])+')/('+str(prgm.fraction_val[3])+')x+('+str(prgm.fraction_val[4])+')/('+str(prgm.fraction_val[5])+')'
    if  pathlib.Path(file.name).suffix=='.rtf':
        rtf.main(file.name)
    elif  pathlib.Path(file.name).suffix=='.docx':
        docx.main(file.name.replace(pathlib.Path(file.name).suffix,''))
    elif pathlib.Path(file.name).suffix=='.html' or pathlib.Path(file.name).suffix=='.htm':
        html.main(file.name)
    elif pathlib.Path(file.name).suffix=='.xhtml':
        xhtml.main(file.name)
    elif pathlib.Path(file.name).suffix=='.tex':
        tex.main(file.name)
    else:
        txt.main(file.name)
    file.close()