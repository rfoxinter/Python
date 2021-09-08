try:
    from PIL import Image,ImageDraw,ImageFont
except ImportError:
    from os import system
    from sys import executable
    system('echo Ce programme doit installer pillow pour fonctionner & timeout 30 & '+executable+' -m pip install --upgrade pillow')
    from PIL import Image,ImageDraw,ImageFont

img=Image.new('RGBA',(3700,2600),color=(255,255,255,0))
tableau=[('1','Hydrog\u00E8ne','H','1,0','2,2'),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),('2','H\u00E9lium','He','4,0',''),
    ('3','Lithium','Li','6,9','1,0'),('4','B\u00E9ryllium','Be','9,0','1,6'),(),(),(),(),(),(),(),(),(),(),('5','Bore','B','10,8','2,0'),('6','Carbone','C','12,0','2,6'),('7','Azote','N','14,0','3,0'),('8','Oxyg\u00E8ne','O','16,0','3,4'),('9','Fluor','F','19,0','4,0'),('10','N\u00E9on','Ne','20,2',''),
    ('11','Sodium','Na','23,0','0,9'),('12','Magn\u00E9sium','Mg','24,3','1,3'),(),(),(),(),(),(),(),(),(),(),('13','Aluminium','Al','27,0','1,5'),('14','Silicium','Si','28,1','1,9'),('15','Phosphore','P','31,0','2,2'),('16','Soufre','S','32,1','2,5'),('17','Chlore','Cl','35,5','3,2'),('18','Argon','Ar','39,9',''),
    ('19','Potassium','K','39,1','0,8'),('20','Calcium','Ca','40,1','1,0'),('21','Scandium','Sc','45,0','1,4'),('22','Titane','Ti','47,9','1,5'),('23','Vanadium','V','50,9','1,6'),('24','Chrome','Cr','52,0','1,7'),('25','Mangan\u00E8se','Mn','54,9','1,6'),('26','Fer','Fe','55,8','1,8'),('27','Cobalt','Co','58,9','1,9'),('28','Nickel','Ni','58,7','1,9'),('29','Cuivre','Cu','63,5','1,9'),('30','Zinc','Zn','65,4','1,7'),('31','Gallium','Ga','69,7','1,8'),('32','Germanium','Ge','72,6','2,0'),('33','Arsenic','As','74,9','2,2'),('34','S\u00E9l\u00E9nium','Se','79,0','2,6'),('35','Brome','Br','79,9','3,0'),('36','Krypton','Kr','83,8',''),
    ('37','Rubidium','Rb','85,5','0,8'),('38','Strontium','Sr','87,6','1,0'),('39','Yttrium','Y','88,9','1,2'),('40','Zirconium','Zr','91,2','1,3'),('41','Niobium','Nb','92,9','1,5'),('42','Molybd\u00E8ne','Mo','95,9','2,2'),('43','Techn\u00E9tium','Tc','99','1,9'),('44','Ruth\u00E9nium','Ru','101,1','2,2'),('45','Rhodium','Rh','102,9','2,3'),('46','Palladium','Pd','106,4','2,2'),('47','Argent','Ag','107,9','1,9'),('48','Cadmium','Cd','112,4','1,7'),('49','Indium','In','114,8','1,8'),('50','\u00C9tain','Sn','118,7','2,0'),('51','Antimoine','Sb','121,7','2,1'),('52','Tellure','Te','127,6','2,1'),('53','Iode','I','126,9','2,7'),('54','X\u00E9non','Xe','131,3',''),
    ('55','C\u00E9sium','Cs','132,9','0,8'),('56','Baryum','Ba','137,3','0,9'),('57-71','Lathanides','','',''),('72','Hafnium','Hf','178,5','1,3'),('73','Tantale','Ta','180,9','1,5'),('74','Tungst\u00E8ne','W','183,9','2,4'),('75','Rh\u00E9nium','Re','186,2','1,9'),('76','Osmium','Os','190,2','2,2'),('77','Iridium','Ir','192,2','2,2'),('78','Platine','Pt','195,1','2,3'),('79','Or','Au','197,0','2,5'),('80','Mercure','Hg','200,6','2,0'),('81','Thallium','Tl','204,4','1,6'),('82','Plomb','Pb','207,2','2,3'),('83','Bismuth','Bi','209,0','2,0'),('84','Polonium','Po','209','2,0'),('85','Astate','At','210','2,2'),('86','Radon','Rn','222',''),
    ('87','Francium','Fr','223','0,7'),('88','Radium','Ra','226','0,9'),('89-103','Actinides','','',''),('104','Rutherfordium','Rf','261',''),('105','Dubnium','Db','262',''),('106','Seaborgium','Sg','266',''),('107','Bohrium','Bh','264',''),('108','Hassium','Hs','269',''),('109','Meitn\u00E9rium','Mt','268',''),('110','Darmstadtium','Ds','271',''),('111','Roentgenium','Rg','272',''),('112','Copernicium','Cn','285',''),('113','Nihonium','Nh','286',''),('114','Fl\u00E9rovium','Fl','289',''),('115','Moscovium','Mc','289',''),('116','Livermorium','Lv','293',''),('117','Tennesse','Ts','294',''),('118','Oganesson','Og','294',''),
    (),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),(),
    (),(),('57','Lanthane','La','138,9','1,1'),('58','C\u00E9rium','Ce','140,1','1,1'),('59','Pras\u00E9odyme','Pr','140,9','1,1'),('60','N\u00E9odyme','Nd','144,2','1,1'),('61','Prom\u00E9thium','Pm','145','1,1'),('62','Samarium','Sm','150,4','1,2'),('63','Europium','Eu','152,0','1,2'),('64','Gadolinium','Gd','157,3','1,2'),('65','Terbium','Tb','158,9','1,2'),('66','Dysprosium','Dy','162,5','1,2'),('67','Holmium','Ho','164,9','1,2'),('68','Erbium','Er','167,3','1,2'),('69','Thulium','Tm','168,9','1,3'),('70','Ytterbium','Yb','173,0','1,1'),('71','Lut\u00E9cium','Lu','175,0','1,3'),(),
    (),(),('89','Actinium','Ac','227','1,1'),('90','Thorium','Th','232','1,3'),('91','Protactinium','Pa','231','1,5'),('92','Uranium','U','238','1,4'),('93','Neptunium','Np','237','1,4'),('94','Plutonium','Pu','244','1,3'),('95','Am\u00E9ricium','Am','243','1,2'),('96','Curium','Cm','247','1,3'),('97','Berk\u00E9lium','Bk','247','1,3'),('98','Californium','Cf','251','1,3'),('99','Einsteinium','Es','252','1,3'),('100','Fermium','Fm','257','1,3'),('101','Mend\u00E9l\u00E9vium','Md','258','1,3'),('102','Nob\u00E9lium','No','259','1,3'),('103','Lawrencium','Lr','262','1,3'),()
]

draw=ImageDraw.Draw(img)
font=ImageFont.truetype('font.ttf',40)
font_symbol=ImageFont.truetype('font.ttf',60)
font_name=ImageFont.truetype('font.ttf',30)

def draw_symbol(x,y,no,name,symb,M,electro):
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
draw.text((425,2425),'Actinides \u2192',(0,0,0,255),anchor='rm',font=font_symbol)

img.save('TableauPeriodique.png',format='png')
