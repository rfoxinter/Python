from tchar_py.numbers.rational import rat
from pypdf import PdfReader, PdfWriter, Transformation, PageObject, PaperSize

def main_fit(flnm: str, size: str, rettr: bool = False) -> PdfWriter:
    if rettr:
        trs = []
    else:
        out = PdfWriter()
    inp = PdfReader(flnm)
    pw = rat(getattr(PaperSize, size).width)
    ph = rat(getattr(PaperSize, size).height)
    for page in inp.pages:
        h = rat(page.mediabox.height)
        w = rat(page.mediabox.width)
        scale_factor = min(ph/h, pw/w)
        print("sf = " + str(scale_factor))
        tr = Transformation().scale(float(scale_factor), float(scale_factor)).translate(float((pw - w * scale_factor) / 2), float((ph - h * scale_factor) / 2))
        if rettr:
            trs.append(tr)
        else:
            npage = PageObject.create_blank_page(width = float(pw), height = float(ph))
            npage.merge_transformed_page(page, tr)
            out.add_page(npage)
    return (trs,inp, float(pw), float(ph)) if rettr else out


def main_crp(flnm: str, size: str, rettr: bool = False) -> PdfWriter:
    if rettr:
        trs = []
    else:
        out = PdfWriter()
    inp = PdfReader(flnm)
    pw = rat(getattr(PaperSize, size).width)
    ph = rat(getattr(PaperSize, size).height)
    for page in inp.pages:
        h = rat(page.mediabox.height)
        w = rat(page.mediabox.width)
        scale_factor = max(ph/h, pw/w)
        print("sf = " + str(scale_factor))
        tr = Transformation().scale(float(scale_factor), float(scale_factor)).translate(float((pw - w * scale_factor) / 2), float((ph - h * scale_factor) / 2))
        if rettr:
            trs.append(tr)
        else:
            npage = PageObject.create_blank_page(width = float(pw), height = float(ph))
            npage.merge_transformed_page(page, tr)
            out.add_page(npage)
    return (trs,inp, float(pw), float(ph)) if rettr else out

def save(flnm, outnm, size, crp):
    if crp:
        out = main_crp(flnm, size)
    else:
        out = main_fit(flnm, size)
    out.add_metadata({"/Producer": "PDF toolkit"})
    out.write(outnm)
    out.close()
