from tkinter.filedialog import askopenfilename

def main() -> str:
    return askopenfilename(title='Select a file',filetypes=[('Portable document format', '.pdf')],defaultextension='.pdf') 