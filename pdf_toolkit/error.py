from tkinter.messagebox import showerror

def main(text: str = 'Impossible to open the file'):
    showerror(title='Error', message=text)