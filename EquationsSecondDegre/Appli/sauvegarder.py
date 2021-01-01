from tkinter.filedialog import asksaveasfile
import __main__

def main():
    file=asksaveasfile(mode='w',title='Enregistrer l\u2019\u00E9quation',filetypes=[('Fichier \u00E9quation','*.eq')],defaultextension='*.eq')
    if file is None:
        return
    if __main__.latest=='entier':
        for l in range(len(__main__.entier_val)):
            file.writelines(str(__main__.entier_val[l])+'\n')
    elif __main__.latest=='fraction':
        for l in range(len(__main__.fraction_val)):
            file.writelines(str(__main__.fraction_val[l])+'\n')
    file.close()            

def ctrl_s(event):
    main()
