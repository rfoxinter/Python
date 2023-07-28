from scripts.resize import main as rmain
from pypdf import PdfWriter, PageObject, PdfReader

def main(file: str, outnm: str, pages: list[int], res: bool, size: str):
    out = PdfWriter()
    if res:
        trs, inp, pw, ph = rmain(file, size, True)
        for page in pages:
            npage = PageObject.create_blank_page(width = pw, height = ph)
            npage.merge_transformed_page(inp.pages[page], trs[page])
            out.add_page(npage)
    else:
        inp = PdfReader(file)
        for page in pages:
            out.add_page(inp.pages[page])
    out.add_metadata({"/Producer": "PDF toolkit"})
    out.write(outnm)
    out.close()
