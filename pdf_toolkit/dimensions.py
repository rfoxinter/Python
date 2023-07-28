import prgm, error

def _land(size):
    return size[4:len(size)] if len(size)>4 and size[0:4] == 'Land' else ('Land' + size)

def load():
    try:
        f = open('dimensions.txt','r').readlines()
    except OSError:
        sizes = ['A'+str(k) for k in range(9)] + ['Letter', 'Legal']
        for s in range(len(sizes)):
            setattr(prgm.PaperSize, _land(sizes[s]), prgm.Dimensions(getattr(prgm.PaperSize, sizes[s]).height, getattr(prgm.PaperSize, sizes[s]).width))
            sizes.append(_land(sizes[s]))
        return sizes, False
    try:
        sizes = ['A'+str(k) for k in range(9)] + ['Letter', 'Legal']
        f = [l.split(',') for l in f]
        land = 0
        for l in f:
            if len(l) == 4 and l[3] == 'True':
                setattr(prgm.PaperSize, l[0], prgm.Dimensions(int(l[1]),int(l[2])))
                sizes.append(l[0])
            elif len(l) == 3 or (len(l) == 4 and l[3] == 'False'):
                setattr(prgm.PaperSize, l[0], prgm.Dimensions(int(l[1]),int(l[2])))
                sizes.append(l[0])
                land -= 1
            elif not (len(l) == 1 and prgm.sub(' ', '', l[0]) in ['\n', '']):
                raise Exception('Invlid dimension format')
        for s in range(len(sizes) + land):
            setattr(prgm.PaperSize, _land(sizes[s]), prgm.Dimensions(getattr(prgm.PaperSize, sizes[s]).height, getattr(prgm.PaperSize, sizes[s]).width))
            sizes.append(_land(sizes[s]))
        return sizes, True
    except Exception as e:
        file = open('errors.log', 'a')
        file.write(str(e) + '\n')
        file.close()
        sizes = ['A'+str(k) for k in range(9)] + ['Letter', 'Legal']
        for s in range(len(sizes)):
            setattr(prgm.PaperSize, _land(sizes[s]), prgm.Dimensions(getattr(prgm.PaperSize, sizes[s]).height, getattr(prgm.PaperSize, sizes[s]).width))
            sizes.append(_land(sizes[s]))
        return sizes, False

def write(root, text):
    f = open('dimensions.txt', 'w')
    f.write(text)
    f.close()
    prgm.sizes, success = load()
    if success:
        root.destroy()
    else:
        error.main('Invlid dimension format')

def main(root):
    rt = prgm.Toplevel(root)
    rt.configure(bg='#333333')
    rt.focus_set()
    rt.transient(root)
    rt.geometry('500x500')
    rt.minsize(500,200)
    text_widget = prgm.Text(rt, wrap='word', font=('Segoe UI',10), bg="#191919", fg="#DDDDDD", selectbackground="#1F6B8D", insertbackground='#EEEEEE', width=50)
    try:
        text_widget.insert('end', open('dimensions.txt','r').read())
    except OSError:
        pass
    text_widget.pack(side='left', fill='both', expand=True)
    scrollbar = prgm.Scrollbar(rt, command=text_widget.yview)
    scrollbar.pack(side='right', fill='y')
    text_widget.configure(yscrollcommand=scrollbar.set)
    rt.title('Edit dimensions')
    img=prgm.PhotoImage(data=prgm.icon)
    rt.tk.call('wm','iconphoto',rt._w,img)
    rt.protocol('WM_DELETE_WINDOW',lambda:write(rt, text_widget.get('1.0','end-1c')))
    rt.mainloop()
