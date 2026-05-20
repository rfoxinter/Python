from tchar_py.numbers.rational import rat
from pypdf import PdfReader, PdfWriter, Transformation, PageObject, PaperSize

def pgord(n: int) -> list[int]:
    N = (n + 3) // 4 * 4
    pg = []
    for k in range(N, N//2, -1):
        if k%2:
            pg.append(N-k)
            pg.append(k-1)
        else:
            pg.append(k-1)
            pg.append(N-k)
    return pg

def main(flnm: str, outnm: str, size: str, flip: str):
    le = flip == 'Long edge'
    out = PdfWriter()
    inp = PdfReader(flnm)
    l = len(inp.pages)
    pw = rat(getattr(PaperSize, size).width)
    ph = rat(getattr(PaperSize, size).height)
    for pos, pg in enumerate(pgord(l)):
        page = inp.pages[pg] if pg < l else PageObject.create_blank_page(width = float(pw), height = float(ph))
        h = rat(page.mediabox.height)
        w = rat(page.mediabox.width)
        sc = min(pw / h, ph / (2 * w))
        nh = h * sc
        nw = w * sc
        dx = ph / 2 * (pos % 2)
        tr = Transformation().scale(float(sc), float(sc)).translate(float(dx + (ph / 2 - nw) / 2), float((pw - nh) / 2))
        if pos%2 == 0:
            npage = PageObject.create_blank_page(width = float(ph), height = float(pw))
            npage.merge_transformed_page(page, tr)
        else:
            npage.merge_transformed_page(page, tr)
            if le and pos % 4 == 3:
                npage.rotation = 180
            out.add_page(npage)
    out.add_metadata({"/Producer": "PDF toolkit"})
    out.write(outnm)
    out.close()
