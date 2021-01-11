from tkinter.filedialog import askopenfilename
import prgm
import entier
import fraction

def main(event=None):
    file=askopenfilename(title='S\u00E9lectionner un fichier à ouvrir',filetypes=[('Fichier \u00E9quation', '.eq')],defaultextension='.eq')
    lire=open(file,'r')
    lignes=lire.readlines()
    if len(lignes)<6:
        a=int(lignes[0])
        b=int(lignes[1])
        c=int(lignes[2])
        prgm.ValeurA.set(a)
        prgm.ValeurB.set(b)
        prgm.ValeurC.set(b)
        entier.open_ent(a,b,c)
    else:
        a_num=int(lignes[0])
        a_denom=int(lignes[1])
        b_num=int(lignes[2])
        b_denom=int(lignes[3])
        c_num=int(lignes[4])
        c_denom=int(lignes[5])
        prgm.ValeurA_n.set(a_num)
        prgm.ValeurA_d.set(a_denom)
        prgm.ValeurB_n.set(b_num)
        prgm.ValeurB_d.set(b_denom)
        prgm.ValeurC_n.set(c_num)
        prgm.ValeurC_d.set(c_denom)
        fraction.open_frac(int(a_num),int(a_denom),int(b_num),int(b_denom),int(c_num),int(c_denom))
