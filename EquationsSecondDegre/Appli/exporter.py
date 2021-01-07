from tkinter.filedialog import asksaveasfile
import pathlib
import __main__

def main(event=None):
    file=asksaveasfile(title='Enregistrer l\u2019\u00E9quation',filetypes=[('Fichier texte','.txt .text'),('Rich Text Format','.rtf'),('Hypertext Markup Language','.html .htm')],defaultextension='.txt')
    if file is None:
        return
    if __main__.latest=='entier':
        __main__.rep[0]='('+str(__main__.entier_val[0])+')x\u00B2+('+str(__main__.entier_val[1])+')x+('+str(__main__.entier_val[2])+')'
    elif __main__.latest=='fraction':
        __main__.rep[0]='('+str(__main__.fraction_val[0])+'/'+str(__main__.fraction_val[1])+')x\u00B2+('+str(__main__.fraction_val[2])+'/'+str(__main__.fraction_val[3])+')x+('+str(__main__.fraction_val[4])+'/'+str(__main__.fraction_val[5])+')'
    if  pathlib.Path(file.name).suffix=='.rtf':
        from extensions import rtf
        rtf.main(file.name)
    elif pathlib.Path(file.name).suffix=='.html' or pathlib.Path(file.name).suffix=='.htm':
        from extensions import html
        html.main(file.name)
    else:
        from extensions import txt
        txt.main(file.name)
    file.close()