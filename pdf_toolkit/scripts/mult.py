from tchar_py.numbers.rational import r, itor
from pypdf import PdfReader, PdfWriter, Transformation, PageObject, PaperSize

def land(size):
    return size[4:len(size)] if len(size)>4 and size[0:4] == 'Land' else ('Land' + size)

def ord2(n: int) -> range:
    return range((n + 1) // 2 * 2)

def ord4(n: int) -> range:
    return range((n + 1) // 2)

def ord2land(n: int) -> range:
    def aux(x):
        if x % 4 == 1:
            return x + 1
        elif x % 4 == 2:
            return x - 1
        return x
    return [aux(i) for i in range((n + 3) // 4 * 4)]

def mult(inp: PdfReader, pgord: range, le: bool, pw: r, ph: r, l: int, island: bool) -> PdfWriter:
    out = PdfWriter()
    for pos, pg in enumerate(pgord):
        page = inp.pages[pg] if pg < l else PageObject.create_blank_page(width = float(pw), height = float(ph))
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
        if pw > ph:
            dx, dy, ppw, pph = pw / 2 * (pos % 2), 0, pw / 2, ph
        else:
            dx, dy, ppw, pph = 0, ph / 2 * ((pos + 1) % 2), pw, ph / 2
        sc = min(pph / h, ppw / w)
        nh = h * sc
        nw = w * sc
        tr = Transformation().scale(float(sc), float(sc)).translate(float(dx + (ppw - nw) / 2), float(dy + (pph - nh) / 2))
        if pos%2 == 0:
            npage = PageObject.create_blank_page(width = float(pw), height = float(ph))
            npage.merge_transformed_page(page, tr)
        else:
            npage.merge_transformed_page(page, tr)
            if le and pos % 4 == 3:
                npage.rotation = 180
            out.add_page(npage)
    return out

def mult2(flnm: str, size: str, flip: str):
    le = flip == 'Long edge'
    inp = PdfReader(flnm)
    l = len(inp.pages)
    pw = itor(getattr(PaperSize, size).width)
    ph = itor(getattr(PaperSize, size).height)
    return mult(inp, ord2(l), le, pw, ph, l, size[0:4] == 'Land')

def mult4(flnm: str, size: str, flip: str):
    le = flip == 'Long edge'
    inp = PdfReader(flnm)
    l = len(inp.pages)
    pw = itor(getattr(PaperSize, size).width)
    ph = itor(getattr(PaperSize, size).height)
    p2w = itor(getattr(PaperSize, land(size)).width)
    p2h = itor(getattr(PaperSize, land(size)).height)
    if p2w < p2h:
        pgord2 = ord2land(l)
    else:
        pgord2 = ord2(l)
    return mult(mult(inp, pgord2, False, p2w, p2h, l, size[0:4] == 'Land'), ord4(l), le, pw, ph, (l + 1) // 2 * 2, size[0:4] == 'Land')

def main(flnm: str, outnm: str, size: str, flip: str, pps: int):
    out = eval('mult' + str(pps) + '(\'' + flnm + '\',\'' + size + '\',\'' + flip + '\')')
    out.add_metadata({"/Producer": "PDF toolkit"})
    out.write(outnm)
    out.close()
