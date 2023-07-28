import prgm
import doc, dimensions

def main(root,font,quit_img,doc_img,dim_img):
    menu=prgm.Menu(root)

    flmenu=prgm.Menu(menu,tearoff=0)
    hlpmenu=prgm.Menu(menu,tearoff=0)

    flmenu.add_cascade(label='Edit paper sizes',image=dim_img,compound='left',command=lambda:dimensions.main(root),font=font)
    flmenu.add_separator()
    flmenu.add_command(label='Quit Ctrl+Q',image=quit_img,compound='left',command=prgm.exit,font=font)
    menu.add_cascade(label='File',menu=flmenu,font=font)

    hlpmenu.add_command(label='Documentation',image=doc_img,compound='left',command=lambda:doc.main(root),font=font)
    menu.add_cascade(label='Help',menu=hlpmenu,font=font)

    root.bind('<Control-q>',prgm.exit)
    root.config(menu=menu)