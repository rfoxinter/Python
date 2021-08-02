import prgm
from tkinter.filedialog import asksaveasfile
import pathlib
import entier_equation
import fraction_equation
from extensions import *

def main(event=None):
    file_list=[('Fichier texte','.txt .text'),('Fichier Rich Text Format','.rtf'),('Fichier Document Office Open XML','.docx'),('Fichier HyperText Markup Language','.html .htm'),('Fichier Extensible HyperText Markup Language','.xhtml'),('Fichier LaTeX','.tex'),('Tous les fichiers','.*')]
    file=asksaveasfile(title='Exporter l\u2019\u00E9quation',filetypes=file_list,defaultextension='.txt')
    if file is None:
        return
    if prgm.latest=='entier':
        prgm.rep[0]=entier_equation.main()
    elif prgm.latest=='fraction':
        prgm.rep[0]=fraction_equation.main()
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