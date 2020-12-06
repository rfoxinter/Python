import urllib.request

filename=['maj','main']
for i in range(len(filename)):
	url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/'+filename[i]+'.py'
	urllib.request.urlretrieve(url, filename[i]+'.py')