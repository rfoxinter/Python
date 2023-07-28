import prgm
import opn, save, message
import error
from scripts import extract
from os.path import splitext

global flnm, outnm, inpbl, outbl, btn
inpbl, outbl = False, False

def mainextract(flnm, outnm, pgs, bl, size, rt):
    if pgs != None:
        try:
            extract.main(flnm, outnm, pgs, bl, size)
            message.main('Pages extracted successfully')
            rt.destroy()
        except Exception as e:
            file = open('errors.log', 'a')
            file.write(str(e) + '\n')
            file.close()
            error.main('Error when extracting pages')

def getpages(pgs: str) -> list[int]:
    try:
        pgs = pgs.split(',')
        pg = []
        for p in pgs:
            if '-' in p:
                start, end = p.split('-')
                pg += list(range(int(start) - 1, int(end)))
            else:
                pg += [int(p) - 1]
        return pg
    except:
        error.main('Invalid pages range')
        return None

def change_value(root) -> None:
    fl = opn.main()
    if fl != '':
        global flnm, inpbl, outbl, btn
        flnm.set(fl)
        inpbl = True
        if inpbl and outbl:
            btn.configure(state='normal')
        root.update_idletasks()

def change_out(root) -> None:
    out = save.main()
    if out != '':
        global outnm, inpbl, outbl, btn
        outnm.set(out)
        outbl = True
        if inpbl and outbl:
            btn.configure(state='normal')
        if splitext(outnm.get())[1] != '.pdf':
            outnm.set(outnm.get() + '.pdf')
        root.update_idletasks()

def resizeom(om):
    if str(om['state']) == 'disabled':
        om.configure(state='normal')
    else:
        om.configure(state='disabled')

def main(root, sizes):
    global flnm, outnm, btn
    rt = prgm.Toplevel(root)
    rt.configure(bg='#333333')
    rt.focus_set()
    flnm = prgm.StringVar()
    size = prgm.StringVar()
    outnm = prgm.StringVar()
    pgs = prgm.StringVar()
    res = prgm.IntVar()
    size.set('A4')
    flnm.set('')
    pgs.set('')
    res.set(0)
    rt.transient(root)
    rt.geometry('500x500')
    prgm.tl(rt, text='Files: ', anchor='e', width=34).grid(column=0, row=0)
    prgm.tbutton(rt, text='Open files', command=lambda:change_value(rt), width=34).grid(column=1, row=0)
    prgm.tl(rt, textvariable=flnm).grid(column=0, row=1, columnspan=2)
    om = prgm.tom(rt, size, *sizes)
    prgm.tcb(rt, text='Resize', variable=res, command=lambda:resizeom(om)).grid(column=0, row=2, columnspan=2)
    prgm.tl(rt, text='Size: ', anchor='e', width=34).grid(column=0, row=3)
    om.configure(state='disabled')
    om.grid(column=1, row=3)
    prgm.tl(rt, text='Pages: ', anchor='e', width=34).grid(column=0, row=4)
    prgm.te(rt, textvariable=pgs, width=40).grid(column=1, row=4)
    prgm.tl(rt, text='Output: ', anchor='e', width=34).grid(column=0, row=5)
    prgm.tbutton(rt, text='Output file', command=lambda:change_out(rt), width=34).grid(column=1, row=5)
    prgm.tl(rt, textvariable=outnm).grid(column=0, row=6, columnspan=2)
    btn = prgm.tbutton(rt, text='Extract', state='disabled', command=lambda:mainextract(flnm.get(), outnm.get(), getpages(pgs.get()), bool(res.get()), size.get(), rt), width=34)
    btn.grid(column=0, row=7, columnspan=2)
    rt.title('Extract PDF pages')
    img=prgm.PhotoImage(data=prgm.icon)
    rt.tk.call('wm','iconphoto',rt._w,img)
    rt.resizable(width=False, height=False)
    rt.mainloop()
