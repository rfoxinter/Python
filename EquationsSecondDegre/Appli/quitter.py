import __main__

def main_quit():
    __main__.plt.close()
    __main__.root.destroy()filename=['main','maj']
    for i in range(len(filename)):
        url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/'+filename[i]+'.py'
        urllib.request.urlretrieve(url, filename[i]+'.py')

def maj_quit():
    __main__.root_maj.destroy()
