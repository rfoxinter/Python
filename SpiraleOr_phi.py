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

phi=(1+5**0.5)/2

w=20
h=20

if f%2==0:
    w+=100+100/phi
    h+=100
else:
    w+=100
    h+=100+100/phi

svg="""<svg width="100%" height="100%" viewBox="0 0 """+str(w)+""" """+str(h)+"""" xmlns="http://www.w3.org/2000/svg">
    <style>
        /* <![CDATA[ */
        path {
            fill: none;
            stroke: black;
            stroke-width: """+width(str(max(w,h)/1000))+""";
        }
        /* ]]> */
    </style>
"""

w-=20
h-=20

d_w=0
d_h=0

for i in range(f):
    c_1=''
    c_2=''
    c_3=''
    if (f-i)%4==1:
        c_1=str(10+d_w)+','+str(10+d_h)
        c_2=str(w+10+d_w)+','+str(10+d_h)
        c_3=str(w+10+d_w)+','+str(100*(phi**(-i))+10+d_h)
        d_h+=100*(phi**(-i))
    elif (f-i)%4==2:
        c_1=str(10+d_w)+','+str(h+10+d_h)
        c_2=str(10+d_w)+','+str(10+d_h)
        c_3=str(100*(phi**(-i))+10+d_w)+','+str(10+d_h)
        d_w+=100*(phi**(-i))
    elif (f-i)%4==3:
        c_1=str(w+10+d_w)+','+str(h+10+d_h)
        c_2=str(10+d_w)+','+str(h+10+d_h)
        c_3=str(10+d_w)+','+str(h-100*(phi**(-i))+10+d_h)
    elif (f-i)%4==0:
        c_1=str(w+10+d_w)+','+str(10+d_h)
        c_2=str(w+10+d_w)+','+str(h+10+d_h)
        c_3=str(w-100*(phi**(-i))+10+d_w)+','+str(h+10+d_h)
    if i%2==0:
        w-=100*(phi**(-i))
    else:
        h-=100*(phi**(-i))
    svg+='    <path d="M'+c_1+' C'+c_1+' '+c_2+' '+c_3+'"></path>\n'

svg+='</svg>'

with open('SpiraleOr_phi.svg','w') as f:
    f.writelines(svg)
    f.close()
