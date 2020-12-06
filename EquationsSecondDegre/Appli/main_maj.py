import urllib.request

filename=['__main__','maj']
for i in range(len(filename)):
	url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/'+filename[i]+'.py'
	urllib.request.urlretrieve(url, filename[i]+'.py')