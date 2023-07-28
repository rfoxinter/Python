import prgm
import opn, save, message
import error
from scripts import booklet
from os.path import splitext

global flnm, outnm, inpbl, outbl, btn
inpbl, outbl = False, False

def mainbooklet(flnm, outnm, size, flip, rt):
    try:
        booklet.main(flnm, outnm, size, flip)
        message.main('Booklet created successfully')
        rt.destroy()
    except Exception as e:
        file = open('errors.log', 'a')
        file.write(str(e) + '\n')
        file.close()
        error.main('Error when creating booklet file')

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

def main(root, sizes):
    flip = ['Short edge', 'Long edge']
    global flnm, outnm, btn
    rt = prgm.Toplevel(root)
    rt.configure(bg='#333333')
    rt.focus_set()
    flnm = prgm.StringVar()
    size = prgm.StringVar()
    outnm = prgm.StringVar()
    flp = prgm.StringVar()
    size.set('A4')
    flnm.set('')
    flp.set('Short edge')
    rt.transient(root)
    rt.geometry('500x500')
    prgm.tl(rt, text='File: ', anchor='e', width=34).grid(column=0, row=0)
    prgm.tbutton(rt, text='Open file', command=lambda:change_value(rt), width=34).grid(column=1, row=0)
    prgm.tl(rt, textvariable=flnm).grid(column=0, row=1, columnspan=2)
    prgm.tl(rt, text='Size: ', anchor='e', width=34).grid(column=0, row=2)
    prgm.tom(rt, size, *sizes).grid(column=1, row=2)
    prgm.tl(rt, text='Output: ', anchor='e', width=34).grid(column=0, row=3)
    prgm.tbutton(rt, text='Output file', command=lambda:change_out(rt), width=34).grid(column=1, row=3)
    prgm.tl(rt, textvariable=outnm).grid(column=0, row=4, columnspan=2)
    prgm.tl(rt, text='Flip: ', anchor='e', width=34).grid(column=0, row=5)
    prgm.tom(rt, flp, *flip).grid(column=1, row=5)
    btn = prgm.tbutton(rt, text='Make booklet', state='disabled', command=lambda:mainbooklet(flnm.get(), outnm.get(), size.get(), flp.get(), rt), width=34)
    btn.grid(column=0, row=6, columnspan=2)
    rt.title('PDF to Booklet')
    img=prgm.PhotoImage(data=prgm.icon)
    rt.tk.call('wm','iconphoto',rt._w,img)
    rt.resizable(width=False, height=False)
    rt.mainloop()
