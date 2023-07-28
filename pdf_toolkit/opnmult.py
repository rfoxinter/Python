from tkinter.filedialog import askopenfilenames

def main() -> str:
    return askopenfilenames(title='Select files',filetypes=[('Portable document format', '.pdf')],defaultextension='.pdf') 