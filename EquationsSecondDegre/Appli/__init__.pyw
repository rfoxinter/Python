import maj
import prgm
import os
import sys

def mise_a_jour():
    maj.down()
    prgm.root.destroy()
    os.execl(sys.executable,sys.executable,*sys.argv)

def mise_a_jour_quitter():
    maj.down()
    quit()
