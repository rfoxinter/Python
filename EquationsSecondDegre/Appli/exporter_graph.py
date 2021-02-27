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
    if prgm.latest=='entier':
        a=prgm.entier_val[0]
        b=prgm.entier_val[1]
        c=prgm.entier_val[2]
        if b**2-4*a*c<0:
            import entier_pas_racine
            entier_pas_racine.main(a,b,c,-b,2*a,-b**2+4*a*c,4*a,pathlib.Path(file.name).suffix.replace('.',''),file.name)
        elif b**2-4*a*c==0:
            import entier_x0
            entier_x0.main(a,b,c,-b,2*a,-b**2+4*a*c,4*a,pathlib.Path(file.name).suffix.replace('.',''),file.name)
        else:
            import entier_deux_racines_plt
            entier_deux_racines_plt.main(a,b,c,-b,2*a,-b**2+4*a*c,4*a,b**2-4*a*c,pathlib.Path(file.name).suffix.replace('.',''),file.name)
    elif prgm.latest=='fraction':
        prgm.rep[0]='('+str(prgm.fraction_val[0])+')/('+str(prgm.fraction_val[1])+')x\u00B2+('+str(prgm.fraction_val[2])+')/('+str(prgm.fraction_val[3])+')x+('+str(prgm.fraction_val[4])+')/('+str(prgm.fraction_val[5])+')'
    file.close()