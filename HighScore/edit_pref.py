import prgm

def main(var,val,line):
    file=open('preferences.py','r')
    list_of_lines=file.readlines()
    file.close()
    list_of_lines[line]=var+'='+val+'\n'
    file=open('preferences.py','w')
    file.writelines(list_of_lines)
    file.close()
    exec('prgm.'+var+'='+val)
    if line==2:
        for i in range(25):
            if not (i%5+1==i//5+1 or 4-i%5+1==i//5+1):
                eval('prgm.Val'+str(i%5+1)+str(i//5+1)).configure({'bg': prgm.rgb_hex((prgm.r,prgm.g,prgm.b))})
    elif line==5:
        for i in range(25):
            if (i%5+1==i//5+1 or 4-i%5+1==i//5+1):
                eval('prgm.Val'+str(i%5+1)+str(i//5+1)).configure({'bg': prgm.rgb_hex((prgm.r_d,prgm.g_d,prgm.b_d))})
