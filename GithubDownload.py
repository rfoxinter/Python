import urllib.request
from urllib.parse import quote
from os.path import exists
from os import mkdir

url=input('URL du dossier : ')
if not '/tree' in url:
    url=(url+'/tree/master').replace('//t','/t')
if url[len(url)-1]=='/':
    url=url[0:len(url)-1]
files=[]
folders=[]
folder=''
while url[len(url)-1-len(folder)]!='/':
    folder=url[len(url)-1-len(folder)]+folder
if not exists(folder):
    mkdir(folder)

def analyze(code):
    while True:
        _type=''
        href=''
        position=code.find('js-navigation-open Link--primary')
        if position==-1:
            break
        _type=code[code[position-1000:len(code)].find('aria-label')+12+position-1000]
        code=code[position:len(code)]
        while code[0:6]!='href="':
            code=code[1:len(code)]
        code=code[6:len(code)]
        while code[0]!='"':
            href=href+code[0]
            code=code[1:len(code)]
        if _type=='F':
            while href.find('%')!=-1:
                i=href.find('%')
                href=href[0:i]+chr(int(href[i+1:i+3],16))+href[i+3:len(href)]
            files.append('https://raw.githubusercontent.com'+href.replace('blob/',''))
        elif _type=='D':
            folders.append('https://github.com'+href)

analyze(urllib.request.urlopen(url).read().decode('utf-8'))

while len(folders)!=0:
    if not exists(folder+'/'+folders[0].replace(url+'/','')):
        mkdir(folder+'/'+folders[0].replace(url+'/',''))
    analyze(urllib.request.urlopen(folders[0]).read().decode('utf-8'))
    folders.pop(0)

path=url.replace('https://github.com','https://raw.githubusercontent.com')
path=path.replace('tree/','')

for i in files:
    i=(i.encode('latin1')).decode('utf-8')
    f=i
    f=quote(f)
    f=f.replace('%3A//','://')
    urllib.request.urlretrieve(f,folder+'/'+i.replace(path,''))
