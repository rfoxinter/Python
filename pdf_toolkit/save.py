from tkinter.filedialog import asksaveasfilename

def main() -> str:
    return asksaveasfilename(title='Save as',filetypes=[('Portable document format', '.pdf')],defaultextension='.pdf')