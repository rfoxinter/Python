import svgwrite

dwg=svgwrite.Drawing(filename='example.svg')

def wl2rgb(wavelength):
    Gamma = 0.80
    IntensityMax = 255
    factor, red, green, blue = 0.0,0.0,0.0,0.0
    if((wavelength >= 380) and (wavelength<440)):
        red = -(wavelength - 440) / (440 - 380)
        green = 0.0
        blue = 1.0
    elif((wavelength >= 440) and (wavelength<490)):
        red = 0.0
        green = (wavelength - 440) / (490 - 440)
        blue = 1.0
    elif((wavelength >= 490) and (wavelength<510)):
        red = 0.0
        green = 1.0
        blue = -(wavelength - 510) / (510 - 490)
    elif((wavelength >= 510) and (wavelength<580)):
        red = (wavelength - 510) / (580 - 510)
        green = 1.0
        blue = 0.0
    elif((wavelength >= 580) and (wavelength<645)):
        red = 1.0
        green = -(wavelength - 645) / (645 - 580)
        blue = 0.0
    elif((wavelength >= 645) and (wavelength<781)):
        red = 1.0
        green = 0.0
        blue = 0.0
    else:
        red = 0.0
        green = 0.0
        blue = 0.0

    if((wavelength >= 380) and (wavelength<420)):
        factor = 0.3 + 0.7*(wavelength - 380) / (420 - 380)
    elif((wavelength >= 420) and (wavelength<701)):
        factor = 1.0
    elif((wavelength >= 701) and (wavelength<781)):
        factor = 0.3 + 0.7*(780 - wavelength) / (780 - 700)
    else:
        factor = 0.0
    
    if (red != 0):
        red = IntensityMax * (red * factor)**Gamma
    
    if (green != 0):
        green = IntensityMax * (green * factor)**Gamma
    
    if (blue != 0):
        blue = IntensityMax * (blue * factor)**Gamma
    
    return red,green,blue

def draw_text_b(i):
    dwg.add(dwg.text('↑',insert=(10*(i-7600)+25,10851.5),fill=svgwrite.rgb(0,0,0,'rgb'),stroke_width=2,style="text-anchor:middle",font_size='1200px',font_family="CMU Serif"))
    dwg.add(dwg.text(str(int(i/20))+' nm',insert=(10*(i-7600)+25,11951.5),fill=svgwrite.rgb(0,0,0,'rgb'),stroke_width=2,style="text-anchor:middle",font_size='1200px',font_family="CMU Serif"))

def draw_text_t(i):
    dwg.add(dwg.text('↑',insert=(10*(i-7600)+25,1788.5),fill=svgwrite.rgb(0,0,0,'rgb'),stroke_width=2,style="text-anchor:middle",font_size='1200px',font_family="CMU Serif"))
    dwg.add(dwg.text(str(int(i/20))+' nm',insert=(10*(i-7600)+25,951.5),fill=svgwrite.rgb(0,0,0,'rgb'),stroke_width=2,style="text-anchor:middle",font_size='1200px',font_family="CMU Serif"))

def plot_rect(i,width):
    x = 10*(i-7600)+20
    r,g,b=wl2rgb(i/20)
    c=svgwrite.rgb(r,g,b,'rgb')
    dwg.add(dwg.rect((x,2020),(width,8000),stroke='none',fill=c))
    if i/20 in [420,485,560,610,660]:
        draw_text_t(i)

for i in range(7600,15600):
    plot_rect(i,15)
    if i%1000==0:
        draw_text_b(i)
        #dwg.add(dwg.text('↑',insert=(10*(i-7600)+25,1820),fill=svgwrite.rgb(0,0,0,'rgb'),stroke_width=2,style="text-anchor:middle",font_size='1200px',font_family="CMU Serif"))
        #dwg.add(dwg.text(str(int(i/20))+' nm',insert=(10*(i-7600)+25,2920),fill=svgwrite.rgb(0,0,0,'rgb'),stroke_width=2,style="text-anchor:middle",font_size='1200px',font_family="CMU Serif"))

plot_rect(15600,10)

dwg.save()

