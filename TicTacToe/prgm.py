from tkinter import Tk,Canvas,messagebox,PhotoImage
from os import name
from random import getrandbits

root=Tk()
root.geometry('450x600')

x_play=bool(getrandbits(1))
boxes=[[True for i in range(3)]for j in range(3)]
board=[['' for i in range(3)]for j in range(3)]
xy_vals=[75,225,375]
winner=('player',False)
moves=[]
boxes_full=0
x_score=0
o_score=0

def clear(event=False):
    for i in range(len(xy_vals)):
        for j in range(len(xy_vals)):
            if not boxes[i][j]:
                canva.delete('button%s_%s'%(xy_vals[i],xy_vals[j]))
                boxes[i][j]=True
                board[i][j]=''
    global winner
    global x_play
    if winner[0]=='x':
        x_play=False
        global x_score
        x_score+=1
        score()
    elif winner[0]=='o':
        x_play=True
        global o_score
        o_score+=1
        score()
    else:
        x_play=bool(getrandbits(1))
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
        global x_play
        x_play=not x_play
        global boxes_full
        boxes_full=boxes_full-1
        player()

def coord_to_val(x):
    if x==75:
        return 1
    elif x==225:
        return 2
    else:
        return 3

def check_win(player):
    if (board[0][0]==player and board[0][1]==player and board[0][2]==player) or (board[1][0]==player and board[1][1]==player and board[1][2]==player) or (board[2][0]==player and board[2][1]==player and board[2][2]==player) or (board[0][0]==player and board[1][0]==player and board[2][0]==player) or (board[0][1]==player and board[1][1]==player and board[2][1]==player) or (board[0][2]==player and board[1][2]==player and board[2][2]==player) or (board[0][0]==player and board[1][1]==player and board[2][2]==player) or (board[0][2]==player and board[1][1]==player and board[2][0]==player):
        global winner
        winner=(player,True)
        messagebox.showinfo(title='Gagn\u00E9',message=player+' \u00E0 gagn\u00E9')

def plot_x(x,y,c='red'):
    canva.create_line(x-50,y-50,x+50,y+50,width=5,fill=c)
    canva.create_line(x+50,y-50,x-50,y+50,width=5,fill=c)
    canva.addtag_enclosed('button%s_%s'%(x,y),x-53,y-53,x+53,y+53)

def plot_o(x,y,c='blue'):
    canva.create_oval(x-50,y-50,x+50,y+50,width=5,outline=c)
    canva.addtag_enclosed('button%s_%s'%(x,y),x-53,y-53,x+53,y+53)

def plot_square(x,y):
    canva.create_rectangle(x-70,y-70,x+70,y+70,width=5,outline='yellow')
    canva.addtag_enclosed('sq',x-73,y-73,x+73,y+73)

def click_xy(xy):
    for i in range(len(xy_vals)):
        if abs(xy_vals[i]-xy)<75:
            return xy_vals[i],i

def player():
    if canva.find_withtag('sq')!=():
        canva.delete('button150_525')
        canva.delete('button300_525')
        canva.delete('sq')
    if x_play:
        plot_square(150,525)
        plot_x(150,525,'red')
        plot_o(300,525,'gray')
    else:
        plot_square(300,525)
        plot_x(150,525,'gray')
        plot_o(300,525,'blue')

def score():
    if canva.find_withtag('x_win')!=():
        canva.delete('x_win')
        canva.delete('o_win')
    x=str(x_score)
    canva.create_text(50,525,text=x,fill='red',anchor='center',font='50')
    canva.addtag_closest('x_win',50,525)
    o=str(o_score)
    canva.create_text(400,525,text=o,fill='blue',anchor='center',font='50')
    canva.addtag_closest('o_win',400,525)

def click(event):
    x=root.winfo_pointerx()-root.winfo_rootx()
    box_x,x_val=click_xy(x)
    y=root.winfo_pointery()-root.winfo_rooty()
    if y>=600:
        return
    box_y,y_val=click_xy(y)
    global boxes_full
    global x_play
    global winner
    if boxes[x_val][y_val]:
        boxes_full=boxes_full+1
        if x_play:
            plot_x(box_x,box_y)
            x_play=False
            board[x_val][y_val]='x'
            check_win('x')
        else:
            plot_o(box_x,box_y)
            x_play=True
            board[x_val][y_val]='o'
            check_win('o')
        boxes[x_val][y_val]=False
        moves.append((box_x,box_y))
    if winner[1]:
        clear()
    elif boxes_full==9:
        messagebox.showinfo(title='\u00C9galit\u00E9',message='\u00C9galit\u00E9')
        winner=('player',True)
        clear()
    else:
        player()

canva=Canvas(root,width=450,height=600)
canva.create_line(150,0,150,450,width=2)
canva.create_line(300,0,300,450,width=2)
canva.create_line(0,150,450,150,width=2)
canva.create_line(0,300,450,300,width=2)
canva.place(x=-1,y=-1)
player()
score()

root.bind('<Button-1>',click)
root.bind('<Escape>',clear)
root.bind('<BackSpace>',undo)
root.title('Tic tac toe')
if name=='nt':
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID('tictactoe')
img=PhotoImage(file='tictactoe.png')
root.tk.call('wm','iconphoto',root._w,img)
root.resizable(width=False,height=False)
root.mainloop()
