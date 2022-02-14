from my_math import fibo_suite

def width(x):
    if 'e+' in x:
        n=int(x[x.find('e+')+2:len(x)])
        x=x[0:x.find('e+')]
        print(x)
        for i in range(n):
            x+='*10'
        x='calc('+x+')'
    return x

f=int(input('Nombre de côtés : '))
s=fibo_suite(f)

w=20
h=20

if f%2==0:
    w+=100*(s[len(s)-2]+s[len(s)-1])/s[len(s)-2]
    h+=100*(s[len(s)-1])/s[len(s)-2]
else:
    w+=100*(s[len(s)-1])/s[len(s)-2]
    h+=100*(s[len(s)-2]+s[len(s)-1])/s[len(s)-2]

fact=(s[len(s)-1]/s[len(s)-2])

svg="""<?xml version="1.0" standalone="no"?>
<svg width="100%" height="100%" viewBox="0 0 """+str(w)+""" """+str(h)+"""" version="1.1" xmlns="http://www.w3.org/2000/svg">
    <style>
        /* <![CDATA[ */
        path {
            fill: none;
            stroke: black;
            stroke-width: """+width(str((max(w,h)/1000)*fact))+""";
        }
        /* ]]> */
    </style>
"""

w-=20
h-=20

d_w=0
d_h=0

for i in range(len(s)-1,0,-1):
    c_1=''
    c_2=''
    c_3=''
    if i%4==1:
        c_1=str(10+d_w)+','+str(10+d_h)
        c_2=str(w+10+d_w)+','+str(10+d_h)
        c_3=str(w+10+d_w)+','+str(w+10+d_h)
        d_h+=w
    elif i%4==2:
        c_1=str(10+d_w)+','+str(h+10+d_h)
        c_2=str(10+d_w)+','+str(10+d_h)
        c_3=str(h+10+d_w)+','+str(10+d_h)
        d_w+=h
    elif i%4==3:
        c_1=str(w+10+d_w)+','+str(h+10+d_h)
        c_2=str(10+d_w)+','+str(h+10+d_h)
        c_3=str(10+d_w)+','+str(h-w+10+d_h)
    elif i%4==0:
        c_1=str(w+10+d_w)+','+str(10+d_h)
        c_2=str(w+10+d_w)+','+str(h+10+d_h)
        c_3=str(w-h+10+d_w)+','+str(h+10+d_h)
    if i%2==0:
        w=abs(w-h)
    else:
        h=abs(h-w)
    svg+='    <path d="M'+c_1+' C'+c_1+' '+c_2+' '+c_3+'"/>\n'

svg+='</svg>'

with open('SpiraleOr.svg','w') as f:
    f.writelines(svg)
    f.close()
