import prgm

def main(root):
    doctext='''To add paper sizes, go to "File" -> "Edit paper sizes" and add a dimension with the format Dimension_name,Width,Height and with one per line.
The wdth and height are at 72 ppi, which corresponds to roughly 284 pixel per millimetre.
Add a ",True" at the end to have a landscape version of the dimension.
The dimension name should not contain spaces.
Landscape dimensions should start with "Land".

For page ranges, separate the page values with "," and use "-" for range values (bounds are included).
For example, to extract the first pages, pages 2 to 8 and page 10, the input will be "1,2-8,10".
The order of the pages can also be changed with this.

When merging PDFs, the files are imported in a random order. To order the files, provide their position in the final document according to the order given above.
For example, if the imported files are: bar.pdf, baz.pdf and foo.pdf (and they appear in this order), to have foo.pdf, then bar.pdf then baz.pdf, the input order is "2,3,1".

The files created by the program, such as the errors log or the file containing the added dimensions, are located in the "%APPDATA%\pdf_toolkit" folder.'''
    rt = prgm.Toplevel(root)
    rt.configure(bg='#333333')
    rt.focus_set()
    rt.transient(root)
    rt.geometry('500x500')
    rt.minsize(500,200)
    text_widget = prgm.Text(rt, wrap='word', font=('Segoe UI',12), bg="#333333", fg="#DDDDDD", width=50)
    text_widget.insert('end', doctext)
    text_widget.config(state='disabled', selectbackground="#333333", selectforeground="#DDDDDD", cursor='')
    text_widget.pack(side='left', fill='both', expand=True)
    text_widget.bind('<Control-c>', lambda _:'break')
    scrollbar = prgm.Scrollbar(rt, command=text_widget.yview)
    scrollbar.pack(side='right', fill='y')
    text_widget.configure(yscrollcommand=scrollbar.set)
    rt.title('Documentation')
    img=prgm.PhotoImage(data=prgm.icon)
    rt.tk.call('wm','iconphoto',rt._w,img)
    rt.mainloop()
