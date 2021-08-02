from tkinter import Tk,Canvas,messagebox,PhotoImage
from os import name
from random import getrandbits

root=Tk()
root.geometry('700x700')

y_play=bool(getrandbits(1))
boxes=[[True for i in range(7)]for j in range(6)]
board=[['' for i in range(7)]for j in range(6)]
xy_vals=[50,150,250,350,450,550,650]
winner=('player',False)
moves=[]
boxes_full=0
y_score=0
r_score=0

def clear(event=False):
    for i in range(len(xy_vals)-1):
        for j in range(len(xy_vals)):
            if not boxes[i][j]:
                canva.delete('button%s_%s'%(xy_vals[i],xy_vals[j]))
                boxes[i][j]=True
                board[i][j]=''
    global winner
    global y_play
    if winner[0]=='y':
        y_play=False
        global y_score
        y_score+=1
        score()
    elif winner[0]=='r':
        y_play=True
        global r_score
        r_score+=1
        score()
    else:
        y_play=bool(getrandbits(1))
    global boxes_full
    boxes_full=0
    old_winner=winner
    winner=('player',False)
    global moves
    moves=[]
    player()

def undo(event=False):
    m=len(moves)
    if m>0:
        canva.delete('button%s_%s'%(moves[m-1][0],moves[m-1][1]))
        boxes[coord_to_val(moves[m-1][0])-1][coord_to_val(moves[m-1][1])-1]=True
        board[coord_to_val(moves[m-1][0])-1][coord_to_val(moves[m-1][1])-1]=''
        moves.pop()
        global y_play
        y_play=not y_play
        global boxes_full
        boxes_full=boxes_full-1
        player()

def coord_to_val(x):
    return int((x-50)/100+1)

def check_win(player,y,x):
    global winner
    if y<=2 and board[y+1][x]==player and board[y+2][x]==player and board[y+3][x]==player:
        winner=(player,True)
    elif x>=3 and board[y][x-3]==player and board[y][x-2]==player and board[y][x-1]==player:
        winner=(player,True)
    elif x>=2 and x<=5 and board[y][x-2]==player and board[y][x-1]==player and board[y][x+1]==player:
        winner=(player,True)
    elif x>=1 and x<=4 and board[y][x-1]==player and board[y][x+1]==player and board[y][x+2]==player:
        winner=(player,True)
    elif x<=3 and board[y][x+1]==player and board[y][x+2]==player and board[y][x+3]==player:
        winner=(player,True)
    elif x>=3 and y>=3 and board[y-1][x-1]==player and board[y-2][x-2]==player and board[y-3][x-3]==player:
        winner=(player,True)
    elif x>=2 and x<=5 and y>=2 and y<=4 and board[y+1][x+1]==player and board[y-1][x-1]==player and board[y-2][x-2]==player:
        winner=(player,True)
    elif x>=1 and x<=4 and y>=1 and y<=3 and board[y+2][x+2]==player and board[y+1][x+1]==player and board[y-1][x-1]==player:
        winner=(player,True)
    elif x<=3 and y<=2 and board[y+3][x+3]==player and board[y+2][x+2]==player and board[y+1][x+1]==player:
        winner=(player,True)
    elif x>=3 and y<=2 and board[y+1][x-1]==player and board[y+2][x-2]==player and board[y+3][x-3]==player:
        winner=(player,True)
    elif x>=2 and x<=5 and y>=1 and y<=3 and board[y-1][x+1]==player and board[y+1][x-1]==player and board[y+2][x-2]==player:
        winner=(player,True)
    elif x>=1 and x<=4 and y>=2 and y<=4 and board[y-2][x+2]==player and board[y-1][x+1]==player and board[y+1][x-1]==player:
        winner=(player,True)
    elif x<=3 and y>=3 and board[y-3][x+3]==player and board[y-2][x+2]==player and board[y-1][x+1]==player:
        winner=(player,True)
    if winner[1]:
        if winner[0]=='y':
            messagebox.showinfo(title='Gagn\u00E9',message='Jaune \u00E0 gagn\u00E9')
        else:
            messagebox.showinfo(title='Gagn\u00E9',message='Rouge \u00E0 gagn\u00E9')

def plot_y(y,x,c='gold'):
    canva.create_oval(x-25,y-25,x+25,y+25,width=5,outline=c,fill=c)
    canva.addtag_enclosed('button%s_%s'%(y,x),x-28,y-28,x+28,y+28)

def plot_r(y,x,c='red'):
    canva.create_oval(x-25,y-25,x+25,y+25,width=5,outline=c,fill=c)
    canva.addtag_enclosed('button%s_%s'%(y,x),x-28,y-28,x+28,y+28)

def plot_square(y,x):
    canva.create_rectangle(x-35,y-35,x+35,y+35,width=5,outline='lime green')
    canva.addtag_enclosed('sq',x-38,y-38,x+38,y+38)

def click_xy(xy):
    for i in range(len(xy_vals)):
        if abs(xy_vals[i]-xy)<50:
            return xy_vals[i],i

def player():
    if canva.find_withtag('sq')!=():
        canva.delete('button650_200')
        canva.delete('button650_500')
        canva.delete('sq')
    if y_play:
        plot_square(650,200)
        plot_y(650,200,'gold')
        plot_r(650,500,'gray')
    else:
        plot_square(650,500)
        plot_y(650,200,'gray')
        plot_r(650,500,'red')

def score():
    if canva.find_withtag('y_win')!=():
        canva.delete('y_win')
        canva.delete('r_win')
    y=str(y_score)
    canva.create_text(100,650,text=y,fill='gold',anchor='center',font='50')
    canva.addtag_closest('y_win',100,650)
    r=str(r_score)
    canva.create_text(600,650,text=r,fill='red',anchor='center',font='50')
    canva.addtag_closest('r_win',600,650)

def click(event):
    x=root.winfo_pointerx()-root.winfo_rootx()
    box_x,x_val=click_xy(x)
    if root.winfo_pointery()-root.winfo_rooty()>=600:
        return
    global y_play
    global winner
    box_y,y_val=0,0
    for i in range(6):
        if boxes[5-i][x_val]:
            box_y=xy_vals[5-i]
            y_val=5-i
            break
    if boxes[y_val][x_val]:
        global boxes_full
        boxes_full=boxes_full+1
        if y_play:
            plot_y(box_y,box_x)
            y_play=False
            board[y_val][x_val]='y'
            check_win('y',y_val,x_val)
        else:
            plot_r(box_y,box_x)
            y_play=True
            board[y_val][x_val]='r'
            check_win('r',y_val,x_val)
        boxes[y_val][x_val]=False
        moves.append((box_y,box_x))
    if winner[1]:
        clear()
    elif boxes_full==42:
        messagebox.showinfo(title='\u00C9galit\u00E9',message='\u00C9galit\u00E9')
        winner=('player',True)
        clear()
    else:
        player()

canva=Canvas(root,width=700,height=700)
for i in xy_vals[0:6]:
    canva.create_line(i+50,0,i+50,600,width=2,fill='blue2')
for i in xy_vals[0:5]:
    canva.create_line(0,i+50,700,i+50,width=2,fill='blue2')
canva.create_line(0,600,700,600,width=2,fill='blue2')
canva.place(x=-1,y=-1)
player()
score()

root.bind('<Button-1>',click)
root.bind('<Escape>',clear)
root.bind('<BackSpace>',undo)
root.title('Puissance 4')
if name=='nt':
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('puissance4')
img=PhotoImage(file='puissance4.png')
root.tk.call('wm','iconphoto',root._w,img)
root.resizable(width=False,height=False)
root.mainloop()
