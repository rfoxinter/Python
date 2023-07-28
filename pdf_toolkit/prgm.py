from tkinter import Tk, Canvas, Frame, Scrollbar, Button, Label, Text, OptionMenu, Checkbutton, Entry, Toplevel, IntVar, StringVar, PhotoImage, Menu, font
from tkinter.filedialog import askopenfilename, askopenfilenames, asksaveasfile
from tkinter.messagebox import showerror, showinfo
from os import name, chdir, getenv, mkdir
from os.path import splitext, exists
from tools import booklet, extract, merge, mult, resize
from icon import icon, quiticon, docicon, dimicon
from pypdf import PdfReader, PdfWriter, Transformation, PageObject, PaperSize
from pypdf.papersizes import Dimensions
from tchar_py.numbers.rational import r, itor
from re import sub
from sys import exit
import menu, dimensions

global rw
rw = 0

def te(*args, **kwargs) -> Entry:
    return Entry(*args, **kwargs, bg="#191919", fg="#DDDDDD", highlightbackground="#1F6B8D")

def tl(*args, **kwargs) -> Label:
    return Label(*args, **kwargs, bg="#333333", fg="#DDDDDD")

def tcb(*args, **kwargs) -> Checkbutton:
    return Checkbutton(*args, **kwargs, indicatoron=0, bg="#333333", fg="#DDDDDD", activebackground="#1F6B8D", activeforeground="#FFF", selectcolor="#2A4868", offrelief="solid", borderwidth=1)

def tom(*args, **kwargs) -> OptionMenu:
    om = OptionMenu(*args, **kwargs)
    om.config(bg="#2A4868", fg="#DDDDDD", activebackground="#1F6B8D", activeforeground="#FFF", disabledforeground="#AAAAAA", highlightthickness=0)
    return om

def tbutton(*args, **kwargs) -> Button:
    return Button(*args, **kwargs, bg="#2A4868", fg="#DDDDDD", activebackground="#1F6B8D", activeforeground="#FFF", disabledforeground="#AAAAAA")

def button(*args, **kwargs):
    global rw
    Button(*args, **kwargs, borderwidth = 5, bg="#2A4868", fg="#DDDDDD", activebackground="#1F6B8D", activeforeground="#FFF").grid(column=0,row=rw,padx=10,pady=10)
    rw += 1

def on_mousewheel(canvas, event = None):
    canvas.update()
    _, y0, _, y1 = canvas.bbox('all')
    yview = canvas.yview()
    if event.delta > 0 and yview[0] <= 0:
        return
    if event.delta < 0 and yview[1] >= 1 and y1 <= canvas.winfo_height():
        return
    canvas.yview_scroll(int(-1 * (event.delta / 120)), 'units')

def on_resize(canvas, root, w):
    canvas.update()
    canvas.configure(scrollregion=canvas.bbox('all'))
    canvas.itemconfigure('1', width=canvas.winfo_width())
    canvas.move('1', (root.winfo_width() - w)/2, 0)
    root.update_idletasks()

def main():
    root = Tk()
    root.configure(bg='#333333')
    font=('Segoe UI',10)
    root.option_add('*Font',font)
    canvas = Canvas(root, highlightthickness=0)
    canvas.configure(bg='#333333')
    frm = Frame(canvas, highlightthickness=0)
    frm.configure(bg='#333333')
    canvas.create_window(0, 0, window=frm, anchor='center')
    scrollbar = Scrollbar(root, orient='vertical', command=canvas.yview)
    canvas.config(yscrollcommand=scrollbar.set)
    scrollbar.pack(side='right', fill='y')
    canvas.pack(side='top', fill='both', expand=True)
    if name=='nt':
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('pdftk')
    img=PhotoImage(data=icon)
    quitimg=PhotoImage(data=quiticon)
    docimg=PhotoImage(data=docicon)
    dimimg=PhotoImage(data=dimicon)
    root.tk.call('wm','iconphoto',root._w, img)
    button(frm, text='Resize PDF', command=lambda:resize.main(root=root, sizes=sizes))
    button(frm, text='Merge PDF', command=lambda:merge.main(root=root, sizes=sizes))
    button(frm, text='Extract PDF pages', command=lambda:extract.main(root=root, sizes=sizes))
    button(frm, text='Change disposition', command=lambda:mult.main(root=root, sizes=sizes))
    button(frm, text='Make booklet', command=lambda:booklet.main(root=root, sizes=sizes))
    frm.update()
    w = frm.winfo_width() + 16
    root.minsize(w, 100)
    root.bind('<Configure>', lambda event:on_resize(canvas=canvas, root=root, w=w))
    canvas.bind_all("<MouseWheel>", lambda event:on_mousewheel(canvas=canvas, event = event))
    root.state('zoomed')
    root.title('PDF toolkit')
    menu.main(root,font,quitimg,docimg, dimimg)
    root.mainloop()

if __name__ == '__main__':
    if not exists(getenv('APPDATA') + '\\pdf_toolkit'):
        mkdir(getenv('APPDATA') + '\\pdf_toolkit')
    chdir(getenv('APPDATA') + '\\pdf_toolkit')
    PaperSize.Letter = Dimensions(612, 792)
    PaperSize.Legal = Dimensions(612, 1008)
    sizes, _ = dimensions.load()
    main()