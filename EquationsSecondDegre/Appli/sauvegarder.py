from tkinter.filedialog import asksaveasfile
import prgm

def main(event=None):
    file=asksaveasfile(mode='w',title='Enregistrer l\u2019\u00E9quation',filetypes=[('Fichier \u00E9quation','.eq')],defaultextension='.eq')
    if file is None:
        return
    if prgm.latest=='entier':
        for l in range(len(prgm.entier_val)):
            file.writelines(str(prgm.entier_val[l])+'\n')
    elif prgm.latest=='fraction':
        for l in range(len(prgm.fraction_val)):
            file.writelines(str(prgm.fraction_val[l])+'\n')
    file.close()
