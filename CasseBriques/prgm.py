from tkinter import Tk,Canvas,messagebox,PhotoImage
from math import cos,sin,pi
from os import name
from random import randint
from time import sleep
from threading import Thread

root=Tk()
root.geometry('600x400')

boxes=0
p_x=300
b_x=300
b_y=300
angle=randint(230,320)
speed=randint(125,175)

def clear(event=False):
    global boxes
    global p_x
    global b_x
    global b_y
    global angle
    global speed
    boxes=0
    p_x=300
    b_x=300
    b_y=300
    angle=randint(230,320)
    speed=randint(125,175)
    for x in (50,100,150,200,250,300,350,400,450,500):
        for y in (20,40,60,80,100):
            boxes+=1
            canva.create_rectangle(x+3,y+3,x+47,y+17,width=3,outline='black',fill='cyan')
            canva.addtag_closest('box%s_%s'%(x,y),x+25,y+10)
    plot_player(p_x)

def check_angle(angle):
    if angle<0:
        angle=360+angle
    elif angle>360:
        angle=360-angle
    if 180>=angle>160:
        return 160
    elif 180<angle<200:
        return 200
    elif 0<=angle<20:
        return 20
    elif 360>=angle>340:
        return 340
    else:
        return angle

def new_angle(i,j,x,y,angle):
    if (x<i-8 or x>i+58) and (y<j-8 or y>j+28):
        return angle-180+randint(-15,15)
    elif x<i-8 or x>i+58:
        return 180-angle+randint(-15,15)
    else:
        return 360-angle+randint(-15,15)

def check_touch(x,y):
    global angle
    global boxes
    global speed
    if y>=390:
        messagebox.showinfo(title='Perdu',message='Perdu')
        clear()
        return True
    elif x<=10:
        angle=180-angle
        angle=check_angle(angle)
        return
    elif x>=590:
        angle=180-angle
        angle=check_angle(angle)
        return
    elif 370>=y>=330 and abs(p_x-b_x)<60 and 180<angle<360:
        angle=360-angle-b_x+p_x+randint(-15,15)
        angle=check_angle(angle)
        speed+=1
        return
    elif y<=10:
        angle=360-angle
        speed+=1
        angle=check_angle(angle)
        return
    if 10<=y<=50:
        for i in (50,100,150,200,250,300,350,400,450,500):
            if x>=i-10 and x<=i+60 and canva.find_withtag('box%s_%s'%(i,20))!=():
                canva.delete('box%s_%s'%(i,20))
                boxes-=1
                angle=new_angle(i,20,x,y,angle)
                angle=check_angle(angle)
                speed+=1
                return
    elif 50<=y<=90:
        for i in (50,100,150,200,250,300,350,400,450,500):
            if x>=i-10 and x<=i+60 and canva.find_withtag('box%s_%s'%(i,60))!=():
                canva.delete('box%s_%s'%(i,60))
                boxes-=1
                angle=new_angle(i,60,x,y,angle)
                angle=check_angle(angle)
                speed+=1
                return
    elif 90<=y<=130:
        for i in (50,100,150,200,250,300,350,400,450,500):
            if x>=i-10 and x<=i+60 and canva.find_withtag('box%s_%s'%(i,100))!=():
                canva.delete('box%s_%s'%(i,100))
                boxes-=1
                angle=new_angle(i,100,x,y,angle)
                angle=check_angle(angle)
                speed+=1
                return
    if 30<=y<=70:
        for i in (50,100,150,200,250,300,350,400,450,500):
            if x>=i-10 and x<=i+60 and canva.find_withtag('box%s_%s'%(i,40))!=():
                canva.delete('box%s_%s'%(i,40))
                boxes-=1
                angle=new_angle(i,40,x,y,angle)
                angle=check_angle(angle)
                speed+=1
                return
    elif 70<=y<=110:
        for i in (50,100,150,200,250,300,350,400,450,500):
            if x>=i-10 and x<=i+60 and canva.find_withtag('box%s_%s'%(i,80))!=():
                canva.delete('box%s_%s'%(i,80))
                boxes-=1
                angle=new_angle(i,80,x,y,angle)
                angle=check_angle(angle)
                speed+=1
                return

def plot_ball(x,y):
    global b_x
    global b_y
    global speed
    clr=check_touch(x,y)
    if boxes==0:
        messagebox.showinfo(title='Gagn\u00E9',message='Gagn\u00E9')
        clear()
        clr=True
    x+=(0.01*speed)*cos(angle*pi/180)
    y-=(0.01*speed)*sin(angle*pi/180)
    canva.create_oval(x-10,y-10,x+10,y+10,width=0,fill='green')
    if canva.find_withtag('oval')!=():
        canva.delete('oval')
    canva.addtag_enclosed('oval',x-11,y-11,x+11,y+11)
    if not clr:
        b_x=x
        b_y=y
        speed+=0.01

def left(event=True):
    if p_x>50:
        plot_player(p_x-10)

def right(event=True):
    if p_x<550:
        plot_player(p_x+10)

def plot_player(x,y=350):
    global p_x
    try:
        canva.delete('player')
    except:
        pass
    canva.create_rectangle(x-47,y-7,x+47,y+7,width=3,outline='black',fill='red')
    canva.addtag_closest('player',x,y)
    p_x=x

canva=Canvas(root,width=600,height=400)
for x in (50,100,150,200,250,300,350,400,450,500):
    for y in (20,40,60,80,100):
        boxes+=1
        canva.create_rectangle(x+3,y+3,x+47,y+17,width=3,outline='black',fill='cyan')
        canva.addtag_closest('box%s_%s'%(x,y),x+25,y+10)
canva.place(x=-1,y=-1)

plot_player(p_x)

def ball():
    while True:
        plot_ball(b_x,b_y)
        sleep(0.005)

th=Thread(target=ball,daemon=True)

root.after_idle(th.start)
root.bind('<Left>',left)
root.bind('<Right>',right)
root.bind('<Escape>',clear)
root.title('Casse-briques')
if name=='nt':
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('cassebriques')
img=PhotoImage(file='cassebriques.png')
root.tk.call('wm','iconphoto',root._w,img)
root.resizable(width=False,height=False)
root.mainloop()
