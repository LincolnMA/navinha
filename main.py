from tkinter import *
import random


##Functions
def update_screen():
    screen.delete("all")
    render_fire()
    #render_enemy_fire()
    render_player()
    render_enemies()
    detect_player_collision()
    #detect_fire_collision()
    screen.focus_set()
    if(game_over):
        screen.create_oval(x_player-20,y_player-20,x_player+20,y_player+20,outline = "red")
    else:
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
    out = -1
    render_enemies.frame_count += 1
    if render_enemies.frame_count >= delay_enemy.get():
        render_enemies.frame_count = 0
        x = random.randint(0,screensize_x)
        y = 50
        enemy_pos.append([x,y])
    for i in range(0,len(enemy_pos)):
        screen.create_image(enemy_pos[i][0],enemy_pos[i][1],image = heli,anchor = S)
        enemy_pos[i][1]+=speed_enemy.get()
        if(enemy_pos[i][1] >= screensize_y): out = i
    if(out > -1): del(enemy_pos[out])   
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
def detect_player_collision():
    global game_over
    for i in range(0,len(enemy_pos)):
        if(enemy_pos[i][0] - 49 <= x_player <= enemy_pos[i][0] + 49):
            if(enemy_pos[i][1] - 50 <= y_player <= enemy_pos[i][1]):
                game_over = True
                return

##Variables
window = Tk()
airplane = PhotoImage(file = "navinha.gif")
fire = PhotoImage(file = "fire.gif")
heli = PhotoImage(file = "heli.gif")
fire_pos = []
enemy_pos = []
render_enemies.frame_count = 0
x_player = 400
y_player = 600
delay_update = IntVar()
delay_update.set(500)
delay_enemy = IntVar()
delay_enemy.set(250)
speed_enemy = IntVar()
speed_enemy.set(1)
to_left = False
to_right = False
to_up = False
to_down = False
game_over = False
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
#Enemy Delay
sc2 = Scale(sidebar,from_ = 10,to = 500,
            label = "Enemy Delay(frames)",
            orient = HORIZONTAL,
            variable = delay_enemy,
            length = 150)
sc2.grid(row = 2,column = 0)
#Enemy Speed
sc3 = Scale(sidebar,from_ = 1,to = 10,
            label = "Enemy speed(frames)",
            orient = HORIZONTAL,
            variable = speed_enemy,
            length = 150)
sc3.grid(row = 3,column = 0)
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