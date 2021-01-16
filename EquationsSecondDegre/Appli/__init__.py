import prgm
import os
import sys

def mise_a_jour():
    import maj
    import importlib
    importlib.reload(maj)
    maj.down()
    os.execl(sys.executable,sys.executable,*sys.argv)

def mise_a_jour_quitter():
    import maj
    import importlib
    importlib.reload(maj)
    maj.down()
    quit()
