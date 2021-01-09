from tkinter.filedialog import askopenfilename
import prgm
import entier
import fraction

def main(event=None):
    file=askopenfilename(title='S\u00E9lectionner un fichier à ouvrir',filetypes=[('Fichier \u00E9quation', '.eq')],defaultextension='.eq')
    lire=open(file,'r')
    lignes=len(lire.readlines())
    with open(file) as f:
        data = f.readlines()[0]
    if lignes<6:
        with open(file) as f:
            a=f.readlines()[0]
        with open(file) as f:
            b=f.readlines()[1]
        with open(file) as f:
            c=f.readlines()[2]
        prgm.ValeurA.set(a)
        prgm.ValeurB.set(b)
        prgm.ValeurC.set(b)
        entier.open_ent(int(a),int(b),int(c))
    else:
        with open(file) as f:
            a_num=f.readlines()[0]
        with open(file) as f:
            a_denom=f.readlines()[1]
        with open(file) as f:
            b_num=f.readlines()[2]
        with open(file) as f:
            b_denom=f.readlines()[3]
        with open(file) as f:
            c_num=f.readlines()[4]
        with open(file) as f:
            c_denom=f.readlines()[5]
        prgm.ValeurA_n.set(a_num)
        prgm.ValeurA_d.set(a_denom)
        prgm.ValeurB_n.set(b_num)
        prgm.ValeurB_d.set(b_denom)
        prgm.ValeurC_n.set(c_num)
        prgm.ValeurC_d.set(c_denom)
        fraction.open_frac(int(a_num),int(a_denom),int(b_num),int(b_denom),int(c_num),int(c_denom))
