from scripts.resize import main as rmain
from pypdf import PdfWriter, PageObject

def main(files: list[str], outnm: str, res: bool, size: str):
    out = PdfWriter()
    for file in files:
        if res:
            trs, inp, pw, ph = rmain(file, size, True)
            for page in range(len(inp.pages)):
                npage = PageObject.create_blank_page(width = pw, height = ph)
                npage.merge_transformed_page(inp.pages[page], trs[page])
                out.add_page(npage)
        else:
            out.append(open(file, 'rb'))
    out.add_metadata({"/Producer": "PDF toolkit"})
    out.write(outnm)
    out.close()
