from tkinter import Tk,Label,Button,PhotoImage
import os
import sys

def main(package_name):
    if os.name=='posix':
        head,tail=os.path.split(sys.executable)
        pip_path=''
        if '3' in tail:
            pip_path=head+'/pip3'
        else:
            pip_path=head+'/pip'
        if not os.path.exists(pip_path):
            import packages_linux
            packages_linux.pip()
    python_path=sys.executable.replace('pythonw','python')
    root=Tk()
    root.option_add('*Font','Arial 10')
    Label(root,text='Ce programme \u00E0 besoin d\u2019installer '+package_name+' pour fonctionner.',width=50).grid(column=0,row=0)
    bouton_maj=Button(root,text='Installer '+package_name,command=lambda:os.system(python_path+' -m pip install --upgrade '+package_name))
    bouton_maj.grid(column=0,row=1)
    bouton_fermer=Button(root,text='Ne pas installer '+package_name,command=quit)
    bouton_fermer.grid(column=0,row=2)
    root.title(package_name)
    root.resizable(width=False,height=False)
    if os.name=='nt':
        root.iconbitmap(r'package.ico')
    else:
        img=PhotoImage(file='package.png')
        root.tk.call('wm','iconphoto',root._w,img)
    root.mainloop()
