from tkinter import Tk,Canvas,messagebox,PhotoImage
from os import name

root=Tk()
root.geometry('600x600')

x_play=True
boxes=[[True for i in range(3)]for j in range(3)]
board=[['' for i in range(3)]for j in range(3)]
xy_vals=[100,300,500]
winner=('player',False)
moves=[]
boxes_full=0

def clear(event=False):
    for i in range(len(xy_vals)):
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
    if x==100:
        return 1
    elif x==300:
        return 2
    else:
        return 3

def check_win(player):
    if (board[0][0]==player and board[0][1]==player and board[0][2]==player) or (board[1][0]==player and board[1][1]==player and board[1][2]==player) or (board[2][0]==player and board[2][1]==player and board[2][2]==player) or (board[0][0]==player and board[1][0]==player and board[2][0]==player) or (board[0][1]==player and board[1][1]==player and board[2][1]==player) or (board[0][2]==player and board[1][2]==player and board[2][2]==player) or (board[0][0]==player and board[1][1]==player and board[2][2]==player) or (board[0][2]==player and board[1][1]==player and board[2][0]==player):
        global winner
        winner=(player,True)
        messagebox.showinfo(title='Gagn\u00E9',message=player+' \u00E0 gagn\u00E9')

def plot_x(x,y):
    globals()['button%s_%s'%(x,y)]=Canvas(root,width=150,height=150,highlightthickness=0)
    globals()['button%s_%s'%(x,y)].create_line(25,25,125,125,width=5,fill='red')
    globals()['button%s_%s'%(x,y)].create_line(125,25,25,125,width=5,fill='red')
    globals()['button%s_%s'%(x,y)].place(x=x-75,y=y-75)

def plot_o(x,y):
    globals()['button%s_%s'%(x,y)]=Canvas(root,width=150,height=150,highlightthickness=0)
    globals()['button%s_%s'%(x,y)].create_oval(25,25,125,125,width=5,outline='blue')
    globals()['button%s_%s'%(x,y)].place(x=x-75,y=y-75)

def click_xy(xy):
    for i in range(len(xy_vals)):
        if abs(xy_vals[i]-xy)<100:
            return xy_vals[i],i

def click(event):
    x=root.winfo_pointerx()-root.winfo_rootx()
    box_x,x_val=click_xy(x)
    y=root.winfo_pointery()-root.winfo_rooty()
    box_y,y_val=click_xy(y)
    global boxes_full
    boxes_full=boxes_full+1
    global x_play
    if boxes[x_val][y_val]:
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
    if boxes_full==9:
        messagebox.showinfo(title='\u00C9galit\u00E9',message='\u00C9galit\u00E9')
        clear()

canva=Canvas(root,width=600,height=600)
canva.create_line(200,0,200,600,width=2)
canva.create_line(400,0,400,600,width=2)
canva.create_line(0,200,600,200,width=2)
canva.create_line(0,400,600,400,width=2)
canva.place(x=0,y=0)

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