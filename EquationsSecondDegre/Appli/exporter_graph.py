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
        a_n=prgm.fraction_val[0]
        a_d=prgm.fraction_val[1]
        b_n=prgm.fraction_val[2]
        b_d=prgm.fraction_val[3]
        c_n=prgm.fraction_val[4]
        c_d=prgm.fraction_val[5]
        delta_num=int(b_n**2*a_d*c_d-4*a_n*c_n*b_d**2+((a_n/a_n)-1))
        delta_denom=int(a_d*b_d**2*c_d)
        if delta_num>0 and delta_denom<0:
            delta_num=-delta_num
            delta_denom=-delta_denom
        if delta_num/delta_denom<0:
            import fraction_pas_racine
            fraction_pas_racine.main(a_n,a_d,b_n,b_d,c_n,c_d,int(-b_n*a_d),int(2*a_n*b_d),int(-delta_num*a_d),int(4*a_n*delta_denom),pathlib.Path(file.name).suffix.replace('.',''),file.name)
        elif delta_num==0:
            import fraction_x0
            fraction_x0.main(a_n,a_d,b_n,b_d,c_n,c_d,int(-b_n*a_d),int(2*a_n*b_d),int(-delta_num*a_d),int(4*a_n*delta_denom),pathlib.Path(file.name).suffix.replace('.',''),file.name)
        else:
            import fraction_deux_racines_plt
            fraction_deux_racines_plt.main(a_n,a_d,b_n,b_d,c_n,c_d,int(-b_n*a_d),int(2*a_n*b_d),int(-delta_num*a_d),int(4*a_n*delta_denom),delta_num,delta_denom,pathlib.Path(file.name).suffix.replace('.',''),file.name)
    file.close()