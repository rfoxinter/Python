from os import listdir
from os.path import isdir,isfile,join
from platform import system
from sys import executable
from time import sleep
import zipfile

files=[]
folders=[]
module=input('Nom du module : ')

print('')

path=''
if system()=='Windows':
    path=join((executable.replace('python.exe','')).replace('pythonw.exe','')+'Lib/site-packages/'+module+'/')
elif system()=='Linux':
    from sys import path
    for i in path:
        if 'site-packages' in i:
            path=join(i+'/'+module+'/')
            break
elif system()=='Darwin':
    from sys import version_info
    version=str(version_info.major)+'.'+str(version_info.minor)
    path=join('/Library/Frameworks/Python.framework/Versions/'+version+'/lib/python'+version+'/site-packages/'+module+'/')
else:
    print('Système d\u2019exploitation non supporté')
    sleep(5)

def analyze_folder(f,p=''):
    if p!='':
        p=p+'/'
    for l in listdir(f):
        if isfile(join(f,l)):
            files.append(p+l)
        elif isdir(join(f,l)):
            if not l=='__pycache__':
                folders.append(p+l)

analyze_folder(path)

while len(folders)!=0:
    analyze_folder(path+folders[0]+'/',p=folders[0])
    folders.remove(folders[0])

file_write=zipfile.ZipFile(module+'.zip','w')
for f in files:
    print('Compression en cours ('+str(files.index(f)+1)+'/'+str(len(files))+')')
    file_write.write(join(path,f),f,zipfile.ZIP_DEFLATED)
file_write.close()

print('\nCompression terminée')
sleep(5)
