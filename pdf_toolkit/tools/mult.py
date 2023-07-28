import prgm
import opn, save, message
import error
from scripts import mult
from os.path import splitext

global flnm, outnm

def mainbooklet(flnm, outnm, size, flip, pps, rt):
    try:
        mult.main(flnm, outnm, size, flip, pps)
        message.main('Disposition changed successfully')
        rt.destroy()
    except Exception as e:
        file = open('errors.log', 'a')
        file.write(str(e) + '\n')
        file.close()
        error.main('Error when changing disposition')

def change_value(root) -> None:
    global flnm
    flnm.set(opn.main())
    if flnm.get() == None:
        error.main()
    else:
        root.update_idletasks()

def change_out(root) -> None:
    global outnm
    outnm.set(save.main())
    if outnm.get() == '':
        error.main('Cannot write in destination')
    else:
        if splitext(outnm.get())[1] != '.pdf':
            outnm.set(outnm.get() + '.pdf')
        root.update_idletasks()

def main(root, sizes):
    flip = ['Short edge', 'Long edge']
    pps = [2,4]#,6,8]
    global flnm, outnm
    rt = prgm.Toplevel(root)
    rt.configure(bg='#333333')
    rt.focus_set()
    flnm = prgm.StringVar()
    size = prgm.StringVar()
    outnm = prgm.StringVar()
    flp = prgm.StringVar()
    nbr = prgm.IntVar()
    size.set('LandA4')
    flnm.set('')
    nbr.set(2)
    flp.set('Short edge')
    rt.transient(root)
    rt.geometry('500x500')
    prgm.tl(rt, text='File: ', anchor='e', width=34).grid(column=0, row=0)
    prgm.tbutton(rt, text='Open file', command=lambda:change_value(rt), width=34).grid(column=1, row=0)
    prgm.tl(rt, textvariable=flnm).grid(column=0, row=1, columnspan=2)
    prgm.tl(rt, text='Size: ', anchor='e', width=34).grid(column=0, row=2)
    prgm.tom(rt, size, *sizes).grid(column=1, row=2)
    prgm.tl(rt, text='Pages per sheet: ', anchor='e', width=34).grid(column=0, row=3)
    prgm.tom(rt, nbr, *pps).grid(column=1, row=3)
    prgm.tl(rt, text='Output: ', anchor='e', width=34).grid(column=0, row=4)
    prgm.tbutton(rt, text='Output file', command=lambda:change_out(rt), width=34).grid(column=1, row=4)
    prgm.tl(rt, textvariable=outnm).grid(column=0, row=5, columnspan=2)
    prgm.tl(rt, text='Flip: ', anchor='e', width=34).grid(column=0, row=6)
    prgm.tom(rt, flp, *flip).grid(column=1, row=6)
    prgm.tbutton(rt, text='Change disposition', command=lambda:mainbooklet(flnm.get(), outnm.get(), size.get(), flp.get(), nbr.get(), rt), width=34).grid(column=0, row=7, columnspan=2)
    rt.title('Change disposition')
    img=prgm.PhotoImage(data=prgm.icon)
    rt.tk.call('wm','iconphoto',rt._w,img)
    rt.resizable(width=False, height=False)
    rt.mainloop()
