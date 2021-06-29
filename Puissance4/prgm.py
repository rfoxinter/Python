from tkinter import Tk,Canvas,messagebox,PhotoImage
from os import name

root=Tk()
root.geometry('700x600')

x_play=True
boxes=[[True for i in range(7)]for j in range(6)]
board=[['' for i in range(7)]for j in range(6)]
xy_vals=[50,150,250,350,450,550,650]
winner=('player',False)
moves=[]
boxes_full=0

def clear(event=False):
    for i in range(len(xy_vals)-1):
        for j in range(len(xy_vals)):
            if not boxes[i][j]:
                globals()['button%s_%s'%(xy_vals[i],xy_vals[j])].delete('all')
                boxes[i][j]=True
                board[i][j]=''
                global x_play
                x_play=True
                global boxes_full
                boxes_full=0
                global winner
                winner=('player',False)

def undo(event=False):
    m=len(moves)
    globals()['button%s_%s'%(moves[m-1][0],moves[m-1][1])].delete("all")
    boxes[coord_to_val(moves[m-1][0])-1][coord_to_val(moves[m-1][1])-1]=True
    board[coord_to_val(moves[m-1][0])-1][coord_to_val(moves[m-1][1])-1]=''
    moves.pop()
    global x_play
    x_play=not x_play
    global boxes_full
    boxes_full=boxes_full-1

def coord_to_val(x):
    return int((x-50)/100+1)

def check_win(player,y,x):
    global winner
    print(y)
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

def plot_y(y,x):
    globals()['button%s_%s'%(y,x)]=Canvas(root,width=60,height=60,highlightthickness=0)
    globals()['button%s_%s'%(y,x)].create_oval(5,5,55,55,width=5,outline='yellow',fill='yellow')
    globals()['button%s_%s'%(y,x)].place(x=x-30,y=y-30)

def plot_r(y,x):
    globals()['button%s_%s'%(y,x)]=Canvas(root,width=60,height=60,highlightthickness=0)
    globals()['button%s_%s'%(y,x)].create_oval(5,5,55,55,width=5,outline='red',fill='red')
    globals()['button%s_%s'%(y,x)].place(x=x-30,y=y-30)

def click_xy(xy):
    for i in range(len(xy_vals)):
        if abs(xy_vals[i]-xy)<50:
            return xy_vals[i],i

def click(event):
    x=root.winfo_pointerx()-root.winfo_rootx()
    box_x,x_val=click_xy(x)
    global boxes_full
    boxes_full=boxes_full+1
    global x_play
    box_y,y_val=0,0
    for i in range(6):
        if boxes[5-i][x_val]:
            box_y=xy_vals[5-i]
            y_val=5-i
            break
    if boxes[y_val][x_val]:
        if x_play:
            plot_y(box_y,box_x)
            x_play=False
            board[y_val][x_val]='y'
            check_win('y',y_val,x_val)
        else:
            plot_r(box_y,box_x)
            x_play=True
            board[y_val][x_val]='r'
            check_win('r',y_val,x_val)
        boxes[y_val][x_val]=False
        moves.append((box_y,box_x))
    if winner[1]:
        clear()
    if boxes_full==42:
        messagebox.showinfo(title='\u00C9galit\u00E9',message='\u00C9galit\u00E9')
        clear()

canva=Canvas(root,width=700,height=600)
for i in xy_vals[0:6]:
    canva.create_line(i+50,0,i+50,800,width=2,fill='blue3')
for i in xy_vals[0:5]:
    canva.create_line(0,i+50,700,i+50,width=2,fill='blue3')
canva.place(x=0,y=0)

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
