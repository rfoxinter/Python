from tchar_py.numbers.rational import r, itor
from pypdf import PdfReader, PdfWriter, Transformation, PageObject, PaperSize

def main(flnm: str, size: str, rettr: bool = False) -> PdfWriter:
    if rettr:
        trs = []
    else:
        out = PdfWriter()
    inp = PdfReader(flnm)
    pw = itor(getattr(PaperSize, size).width)
    ph = itor(getattr(PaperSize, size).height)
    for page in inp.pages:
        h = page.mediabox.height
        if isinstance(h, int):
            h = itor(h)
        else:
            d = 10 ** (len(str(h)) - len(str(int(h))) - 1)
            h = r(h * d, d)
            del d
        w = page.mediabox.width
        if isinstance(w, int):
            w = itor(w)
        else:
            d = 10 ** (len(str(w)) - len(str(int(w))) - 1)
            w = r(w * d, d)
            del d
        scale_factor = min(ph/h, pw/w)
        tr = Transformation().scale(float(scale_factor), float(scale_factor)).translate(float((pw - w * scale_factor) / 2), float((ph - h * scale_factor) / 2))
        if rettr:
            trs.append(tr)
        else:
            npage = PageObject.create_blank_page(width = float(pw), height = float(ph))
            npage.merge_transformed_page(page, tr)
            out.add_page(npage)
    return (trs,inp, float(pw), float(ph)) if rettr else out

def save(flnm, outnm, size):
    out = main(flnm, size)
    out.add_metadata({"/Producer": "PDF toolkit"})
    out.write(outnm)
    out.close()
