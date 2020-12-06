import urllib.request
import __main__

filename=['entier','entier_deux_racines_plt','entier_pas_racine','entier_x0','entier_x1','entier_x2','fraction','fraction_deux_racines_plt','fraction_pas_racine','fraction_x0','fraction_x1','fraction_x1_delta_denom_entier','fraction_x1_delta_num_entier','fraction_x1_sinon','fraction_x2','main_maj','main_version','quitter']
for i in range(len(filename)):
    url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/'+filename[i]+'.py'
    urllib.request.urlretrieve(url, filename[i]+'.py')
url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/python.ico'
urllib.request.urlretrieve(url, 'python.ico')
__main__.root_maj.destroy()