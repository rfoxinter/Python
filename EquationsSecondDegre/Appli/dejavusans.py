from tkinter import Tk,Label,Button,PhotoImage
import urllib.request
import zipfile
import os

def install():
    data=urllib.request.urlopen('https://api.github.com/repos/dejavu-fonts/dejavu-fonts/releases/latest').read().decode('utf-8')
    data=(data.replace('false','False')).replace('null','"null"')
    data=eval(data)
    version=(data['tag_name'].replace('version_','')).replace('_','.')
    url='https://github.com/dejavu-fonts/dejavu-fonts/releases/download/'+data['tag_name']+'/dejavu-fonts-ttf-'+version+'.zip'
    urllib.request.urlretrieve(url,'DejaVu-'+version+'.zip')
    lire=zipfile.ZipFile('DejaVu-'+version+'.zip','r')
    lire.extractall('')
    os.chdir('dejavu-fonts-ttf-2.37')
    os.chdir('ttf')
    os.system('DejaVuSans.ttf')
    os.chdir('..')
    os.chdir('..')
    os.listdir()

def main():
    root=Tk()
    Label(root,text='Cette application a besions de la police DejaVu Sans pour fonctionner').grid(column=0,row=0,sticky='w')
    bouton_maj=Button(root,text='Installer DejaVu Sans',command=install)
    bouton_maj.grid(column=0,row=1)
    bouton_fermer=Button(root,text='Ne pas installer DejaVu Sans',command=quit)
    bouton_fermer.grid(column=0,row=2)
    root.title('DejaVu Sans')
    root.resizable(width=False,height=False)
    if os.name=='nt':
        import ctypes
        import prgm
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('equations')
    img=PhotoImage(file='python.png')
    root.tk.call('wm','iconphoto',root._w,img)
    root.mainloop()
