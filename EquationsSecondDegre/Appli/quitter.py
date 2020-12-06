import urllib.request
import __main__

def main_quit():
    __main__.plt.close()
    __main__.root.destroy()
    url='https://raw.githubusercontent.com/rfoxinter/Python/master/EquationsSecondDegre/Appli/main_version.py'
    urllib.request.urlretrieve(url, 'main_version.py')
    print(str(__main__.version))
    import main_version
    if main_version.version>__main__.version:
        print(hello)

def maj_quit():
    __main__.root_maj.destroy()
