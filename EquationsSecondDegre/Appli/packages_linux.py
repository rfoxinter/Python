import os

def tkinter():
    print('Ce programme \u00E0 besoin d\u2019installer tkinter pour fonctionner')
    rep=input('Installer tkinter [y/n] ').upper()
    if rep=='Y' or rep=='YES':
        try:
            import linux_distribution
            linux_id_like=linux_distribution.id_like()
            if 'debian' in linux_id_like:
                os.system('sudo apt install python3-tk')
            elif 'arch' in linux_id_like:
                os.system('sudo pacman -S tk')
            elif ('suse' in linux_id_like) or ('sles' in linux_id_like):
                os.system('sudo zypper install python3-tk')
            elif 'rhel' in linux_id_like:
                os.system('sudo yum install python3-tkinter')
            elif 'fedora' in linux_id_like:
                linux_id=linux_distribution.id()
                if 'rhel' in linux_id:
                    os.system('sudo yum install python3-tkinter')
                else:
                    os.system('sudo dnf install python3-tkinter')
            else:
                print('Votre distribution de linux n\u2019est pas reconnue\nInstallez tkinter manuellement puis relancez le programme')
        except:
            print('Une erreur est survenue lors de l\u2019installation\nInstallez tkinter manuellement puis relancez le programme')
    else:
        quit()

def pip():
    print('Ce programme \u00E0 besoin d\u2019installer pip pour fonctionner')
    rep=input('Installer pip [y/n] ').upper()
    if rep=='Y' or rep=='YES':
        try:
            import linux_distribution
            linux_id_like=linux_distribution.id_like()
            if 'debian' in linux_id_like:
                os.system('sudo apt install python3-pip')
            elif 'arch' in linux_id_like:
                os.system('sudo pacman -S python-pip')
            elif ('suse' in linux_id_like) or ('sles' in linux_id_like):
                os.system('sudo zypper install python3-pip')
            elif 'rhel' in linux_id_like:
                os.system('sudo yum install epel-release')
                os.system('sudo yum install python3-pip')
            elif 'fedora' in linux_id_like:
                linux_id=linux_distribution.id()
                if 'rhel' in linux_id:
                    os.system('sudo yum install epel-release')
                    os.system('sudo yum install python3-pip')
            else:
                print('Votre distribution de linux n\u2019est pas reconnue\nInstallez pip manuellement puis relancez le programme')
        except:
            print('Une erreur est survenue lors de l\u2019installation\nInstallez pip manuellement puis relancez le programme')
    else:
        quit()