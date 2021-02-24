import prgm
from tkinter.filedialog import asksaveasfile
import pathlib
import preferences

def main(event=None):
    if preferences.export_graph==0:
        import edit_pref
        edit_pref.main('export_graph','1',3)
    file_list=[('Joint Photographic Experts Group','.jpg .jpeg'),('Portable Network Graphics','.png'),('Scalable Vector Graphics','.svg'),('Portable Document Format','.pdf')]
    file=asksaveasfile(title='Exporter le graphique',filetypes=file_list,defaultextension='.jpg')
    if file is None:
        return
    graph=''
    if prgm.latest=='entier':
        a=prgm.entier_val[0]
        b=prgm.entier_val[1]
        c=prgm.entier_val[2]
        if b**2-4*a*c<0:
            from entier_pas_racine import main
        elif b**2-4*a*c==0:
            from entier_x0 import main
        else:
            from entier_deux_racines_plt import main
    elif prgm.latest=='fraction':
        prgm.rep[0]='('+str(prgm.fraction_val[0])+')/('+str(prgm.fraction_val[1])+')x\u00B2+('+str(prgm.fraction_val[2])+')/('+str(prgm.fraction_val[3])+')x+('+str(prgm.fraction_val[4])+')/('+str(prgm.fraction_val[5])+')'
    if  pathlib.Path(file.name).suffix=='.jpg' or pathlib.Path(file.name).suffix=='.jpeg':
        if prgm.latest=='entier':
            if prgm.entier_val[1]**2-4*prgm.entier_val[0]*prgm.entier_val[2]<=0:
                main(prgm.entier_val[0],prgm.entier_val[1],prgm.entier_val[2],-prgm.entier_val[1],2*prgm.entier_val[0],-prgm.entier_val[1]**2+4*prgm.entier_val[0]*prgm.entier_val[2],4*prgm.entier_val[0],'jpg',file.name)
            else:
                main(prgm.entier_val[0],prgm.entier_val[1],prgm.entier_val[2],-prgm.entier_val[1],2*prgm.entier_val[0],-prgm.entier_val[1]**2+4*prgm.entier_val[0]*prgm.entier_val[2],4*prgm.entier_val[0],prgm.entier_val[1]**2-4*prgm.entier_val[0]*prgm.entier_val[2],'jpg',file.name)
    elif  pathlib.Path(file.name).suffix=='.png':
        if prgm.latest=='entier':
            if prgm.entier_val[1]**2-4*prgm.entier_val[0]*prgm.entier_val[2]<=0:
                main(prgm.entier_val[0],prgm.entier_val[1],prgm.entier_val[2],-prgm.entier_val[1],2*prgm.entier_val[0],-prgm.entier_val[1]**2+4*prgm.entier_val[0]*prgm.entier_val[2],4*prgm.entier_val[0],'png',file.name)
            else:
                main(prgm.entier_val[0],prgm.entier_val[1],prgm.entier_val[2],-prgm.entier_val[1],2*prgm.entier_val[0],-prgm.entier_val[1]**2+4*prgm.entier_val[0]*prgm.entier_val[2],4*prgm.entier_val[0],prgm.entier_val[1]**2-4*prgm.entier_val[0]*prgm.entier_val[2],'jpg',file.name)
    elif pathlib.Path(file.name).suffix=='.svg':
        if prgm.latest=='entier':
            if prgm.entier_val[1]**2-4*prgm.entier_val[0]*prgm.entier_val[2]<=0:
                main(prgm.entier_val[0],prgm.entier_val[1],prgm.entier_val[2],-prgm.entier_val[1],2*prgm.entier_val[0],-prgm.entier_val[1]**2+4*prgm.entier_val[0]*prgm.entier_val[2],4*prgm.entier_val[0],'svg',file.name)
            else:
                main(prgm.entier_val[0],prgm.entier_val[1],prgm.entier_val[2],-prgm.entier_val[1],2*prgm.entier_val[0],-prgm.entier_val[1]**2+4*prgm.entier_val[0]*prgm.entier_val[2],4*prgm.entier_val[0],prgm.entier_val[1]**2-4*prgm.entier_val[0]*prgm.entier_val[2],'jpg',file.name)
    elif pathlib.Path(file.name).suffix=='.pdf':
        if prgm.latest=='entier':
            if prgm.entier_val[1]**2-4*prgm.entier_val[0]*prgm.entier_val[2]<=0:
                main(prgm.entier_val[0],prgm.entier_val[1],prgm.entier_val[2],-prgm.entier_val[1],2*prgm.entier_val[0],-prgm.entier_val[1]**2+4*prgm.entier_val[0]*prgm.entier_val[2],4*prgm.entier_val[0],'pdf',file.name)
            else:
                main(prgm.entier_val[0],prgm.entier_val[1],prgm.entier_val[2],-prgm.entier_val[1],2*prgm.entier_val[0],-prgm.entier_val[1]**2+4*prgm.entier_val[0]*prgm.entier_val[2],4*prgm.entier_val[0],prgm.entier_val[1]**2-4*prgm.entier_val[0]*prgm.entier_val[2],'jpg',file.name)
    file.close()