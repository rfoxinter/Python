import prgm

def redemarrage():
    try:
        prgm.plt
    except:
        prgm.redemarrage=prgm.Tk()
        if 'DejaVu Sans' in list(prgm.font.families()):
            police=prgm.font.Font(family='DejaVu Sans',size=10)
            prgm.redemarrage.option_add('*Font',police)
        prgm.redemarrage.title('Avertissement')
        prgm.Label(prgm.redemarrage,text='Un red\u00E9marrage de l\u2019application est n\u00E9cessaire',width=50).grid(column=0,row=0)
        bouton_redemarrer=prgm.Button(prgm.redemarrage,text='Red\u00E9marrer l\u2019application',command=lambda:prgm.os.execl(prgm.sys.executable,prgm.sys.executable,*prgm.sys.argv))
        bouton_redemarrer.grid(column=0,row=1)
        bouton_fermer=prgm.Button(prgm.redemarrage,text='Red\u00E9marrer plus tard',command=prgm.redemarrage.destroy)
        bouton_fermer.grid(column=0,row=2)
        prgm.redemarrage.resizable(width=False,height=False)
        if prgm.os.name=='nt':
            prgm.redemarrage.iconbitmap('avertissement.ico')
        prgm.redemarrage.mainloop()

def main(var,val,line,restart=True):
    file=open('preferences.py','r')
    list_of_lines=file.readlines()
    file.close()
    list_of_lines[line]=var+'='+val+'\n'
    file=open('preferences.py','w')
    file.writelines(list_of_lines)
    file.close()
    exec('prgm.'+var+'='+val)
    if ((var=='afficher_graphs' and val=='1') or (var=='export_graph' and val=='1')) and restart:
        redemarrage()