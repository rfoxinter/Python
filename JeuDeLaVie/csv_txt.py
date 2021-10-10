name=input('Nom du fichier : ')
f=open(name+'.csv','r')
r=f.readlines()
f.close()
l='['

for i in range(len(r)):
    l=l+'['+(r[i].replace('\n','],')).replace('\n','')

l=l+']'
l=l.replace('],]',']]')

file_write=open(name+'.txt','w',encoding="utf-8")
file_write.writelines(l)
file_write.close()