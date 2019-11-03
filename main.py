from tkinter import *


##Functions
def update_screen():
    screen.delete("all")
    render_fire()
    render_player()
    render_enemies()
    screen.focus_set()
    screen.after(delay_update.get(),update_screen)
def render_fire():
    out = -1
    global fire_pos
    for i in range(0,len(fire_pos)):
        screen.create_image(fire_pos[i][0],fire_pos[i][1],image = fire,anchor = N)
        fire_pos[i][1] = fire_pos[i][1] - 1
        if fire_pos[i][1] < 0: out = i
    if out > -1: del(fire_pos[out])

def render_player():
    global x_player
    global y_player
    if(to_left and x_player >= 0): x_player = x_player - 1
    if(to_right and x_player <= screensize_x): x_player = x_player + 1
    if(to_up and y_player >= 0): y_player = y_player - 1
    if(to_down and y_player <= screensize_y): y_player = y_player + 1
    screen.create_image(x_player,y_player,image = airplane,anchor = S)
def render_enemies():
    print("Render enemies!")
def to_left_on(x):
    global to_left
    to_left = True
def to_left_off(x):
    global to_left
    to_left = False
def to_right_on(x):
    global to_right
    to_right = True
def to_right_off(x):
    global to_right
    to_right = False
def to_up_on(x):
    global to_up
    to_up = True
def to_up_off(x):
    global to_up
    to_up = False
def to_down_on(x):
    global to_down
    to_down = True
def to_down_off(x):
    global to_down
    to_down = False
def new_fire(x):
    global fire_pos
    fire_pos.append([x_player,y_player])
##Variables
window = Tk()
airplane = PhotoImage(file = "navinha.gif")
fire = PhotoImage(file = "fire.gif")
fire_pos = []
x_player = 400
y_player = 600
delay_update = IntVar()
delay_update.set(500)
to_left = False
to_right = False
to_up = False
to_down = False
screensize_x = 800
screensize_y = 600
##SideBar
sidebar = Frame(window)
sidebar.grid(row = 0,column = 0)
#Tile
lb1 = Label(sidebar,text = "Controls")
lb1.grid(row = 0,column = 0)
#Update Delay
sc1 = Scale(sidebar,from_ = 1,to = 1000,
            label = "Update Delay(ms)",
            orient = HORIZONTAL,
            variable = delay_update,
            length = 150)
sc1.grid(row = 1,column = 0)
##Main Screen
screen = Canvas(window,bg = "white",height = screensize_y,width = screensize_x)
screen.grid(row = 0,column = 1)
screen.bind("<Key-a>",to_left_on)
screen.bind("<KeyRelease-a>",to_left_off)
screen.bind("<Key-d>",to_right_on)
screen.bind("<KeyRelease-d>",to_right_off)
screen.bind("<Key-w>",to_up_on)
screen.bind("<KeyRelease-w>",to_up_off)
screen.bind("<Key-s>",to_down_on)
screen.bind("<KeyRelease-s>",to_down_off)
screen.bind("<Key-space>",new_fire)

##Final
update_screen()
window.mainloop()