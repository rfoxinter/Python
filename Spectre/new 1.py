try:
    from PIL import Image,ImageDraw,ImageFont
except ImportError:
    from os import system
    from sys import executable
    system('echo Ce programme doit installer pillow pour fonctionner & timeout 30 & '+executable+' -m pip install --upgrade pillow')

img = Image.new('RGBA',(80060,500),color=(255,255,255,255))

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
    
    return int(red),int(green),int(blue)

draw=ImageDraw.Draw(img)
#font=ImageFont.truetype('font.ttf',40)
#font_symbol=ImageFont.truetype('font.ttf',60)
#font_name=ImageFont.truetype('font.ttf',30)

"""def draw_symbol(x,y,no,name,symb,M,electro):
    draw.rectangle((x,y,x+200,y+250),fill=(255,255,255,0),outline=(0,0,0,255))
    draw.text((x+10,y+10),no,(255,0,255,255),anchor='lt',font=font)
    draw.text((x+190,y+10),electro,(0,255,0,255),anchor='rt',font=font)
    draw.text((x+100,y+105),symb,(0,0,0,255),anchor='mm',font=font_symbol)
    draw.text((x+100,y+155),name,(0,0,255,255),anchor='mm',font=font_name)
    draw.text((x+100,y+240),M,(50,200,200,255),anchor='mb',font=font)

for i in range(len(tableau)):
    if tableau[i]!=():
        x=(i%18)*200+50
        y=(i//18)*250+50
        draw_symbol(x,y,tableau[i][0],tableau[i][1],tableau[i][2],tableau[i][3].replace('.',','),tableau[i][4].replace('.',','))

draw_symbol(1350,300,'Z','Nom','X','M','\u03C7')
draw.text((425,2175),'Lathanides \u2192',(0,0,0,255),anchor='rm',font=font_symbol)
draw.text((425,2425),'Actinides \u2192',(0,0,0,255),anchor='rm',font=font_symbol)"""

for i in range(7600,15600+1):
    x = 10*(i-7600)+20
    print(i,x)
    r,g,b=wl2rgb(i/20)
    draw.rectangle((x,20,x+20,480),fill=(r,g,b,255))

img.save('Spectre.png',format='png')