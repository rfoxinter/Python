from os import getcwd,mkdir
from os.path import exists,join
from platform import system
from sys import executable
from time import sleep
import zipfile

zip_path=''
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

if exists(module+'.zip'):
    zip_path=module+'.zip'
else:
    zip_path=input('Chemin absolu du fichier zip : ')

if not exists(path):
    mkdir(path)

file_read=zipfile.ZipFile(zip_path,'r')
files=file_read.namelist()
for f in files:
    print('Décompression en cours ('+str(files.index(f)+1)+'/'+str(len(files))+')')
    file_read.extract(f,path)


print('\nDécompression terminée')
sleep(5)
