import prgm
import opnmult, save, message
import error
from scripts import merge
from os.path import splitext
from re import sub

global flnm, flnms, outnm, inpbl, outbl, btn
inpbl, outbl = False, False

def mainmerge(flnms, outnm, bl, size, rt):
    if flnms != None:
        try:
            merge.main(flnms, outnm, bl, size)
            message.main('PDF merged successfully')
            rt.destroy()
        except Exception as e:
            file = open('errors.log', 'a')
            file.write(str(e) + '\n')
            file.close()
            error.main('Error when merging files')

def getfls(flnms: list[str], pgs: str) -> list[str]:
    if pgs == '':
        return flnms
    try:
        pgs = pgs.split(',')
        pg = []
        for p in pgs:
            pg += [int(p) - 1]
        return [flnms[p] for p in pg]
    except:
        error.main('Invalid order')
        return None

def change_value(root) -> None:
    flnmstmp = opnmult.main()
    if flnmstmp != '' and len(flnmstmp) > 1:
        global flnm, flnms, inpbl, outbl, btn
        flnms = list(flnmstmp)
        flnm.set(sub(', ', '\n' ,sub('\'', '' ,str(flnms))).replace('[', '').replace(']', ''))
        inpbl = True
        if inpbl and outbl:
            btn.configure(state='normal')
        root.update_idletasks()
    elif len(flnmstmp) == 1:
        error.main('Select more than one file')

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
    global flnm, flnms, outnm, btn
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
    prgm.tl(rt, textvariable=flnm, wraplength=500, justify='center').grid(column=0, row=1, columnspan=2)
    prgm.tl(rt, text='Change order (default given above): ', anchor='e', width=34).grid(column=0, row=2)
    prgm.te(rt, textvariable=pgs, width=40).grid(column=1, row=2)
    om = prgm.tom(rt, size, *sizes)
    prgm.tcb(rt, text='Resize', variable=res, command=lambda:resizeom(om)).grid(column=0, row=3, columnspan=2)
    prgm.tl(rt, text='Size: ', anchor='e', width=34).grid(column=0, row=4)
    om.configure(state='disabled')
    om.grid(column=1, row=4)
    prgm.tl(rt, text='Output: ', anchor='e', width=34).grid(column=0, row=5)
    prgm.tbutton(rt, text='Output file', command=lambda:change_out(rt), width=34).grid(column=1, row=5)
    prgm.tl(rt, textvariable=outnm).grid(column=0, row=6, columnspan=2)
    btn = prgm.tbutton(rt, text='Merge', state='disabled', command=lambda:mainmerge(getfls(flnms, pgs.get()), outnm.get(), bool(res.get()), size.get(), rt), width=34)
    btn.grid(column=0, row=7, columnspan=2)
    rt.title('Merge PDF')
    img=prgm.PhotoImage(data=prgm.icon)
    rt.tk.call('wm','iconphoto',rt._w,img)
    rt.resizable(width=False, height=False)
    rt.mainloop()
