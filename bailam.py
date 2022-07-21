from tkinter import *
import random

root = Tk()
root.title("..................................................")
width = 450
height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="white")

player_fire = PhotoImage(file='D:/VHien/học web/Ai/btvn1/fire.png').subsample(1)
player_water = PhotoImage(file='D:/VHien/học web/Ai/btvn1/water.png').subsample(1)
player_earth = PhotoImage(file='D:/VHien/học web/Ai/btvn1/earth.png').subsample(1)
player_metal = PhotoImage(file='D:/VHien/học web/Ai/btvn1/metal.png').subsample(5)
player_wood = PhotoImage(file='D:/VHien/học web/Ai/btvn1/wood.png').subsample(1)
comp_fire = PhotoImage(file='D:/VHien/học web/Ai/btvn1/fire.png').subsample(1)
comp_water = PhotoImage(file='D:/VHien/học web/Ai/btvn1/water.png').subsample(1)
comp_earth = PhotoImage(file='D:/VHien/học web/Ai/btvn1/earth.png').subsample(1)
comp_metal = PhotoImage(file='D:/VHien/học web/Ai/btvn1/metal.png').subsample(5)
comp_wood = PhotoImage(file='D:/VHien/học web/Ai/btvn1/wood.png').subsample(1)
start = PhotoImage(file='img/start.png').subsample(5)
win = PhotoImage(file='img/win.png').subsample(5)
draw = PhotoImage(file='img/draw.png').subsample(5)
lose = PhotoImage(file='img/lose.png').subsample(5)

player_img = Label(root, image=player_fire, bg='white')
player_img.grid(row=2, column=1, padx=30, pady=20)
comp_img = Label(root, image=comp_fire, bg='white')
comp_img.grid(row=2, column=3, padx=30, pady=20)

# Lbl Player
lbl_player = Label(root, font=("Arial", 15), text='Player', bg='white', fg='black')
lbl_player.grid(row=1, column=1)

# Lbl Comp
lbl_comp = Label(root, font=("Arial", 15), text='Comp', bg='white', fg='black')
lbl_comp.grid(row=1, column=3)

# Score
player_score = Label(root, text='0', font=('Arial', 30), bg='white', fg='black')
breaklbl = Label(root, text='-', font=('Arial', 30), bg='white', fg='black')
comp_score = Label(root, text='0', font=('Arial', 30), bg='white', fg='black')
player_score.grid(row=3, column=1)
breaklbl.grid(row=3, column=2)
comp_score.grid(row=3, column=3)

# Message
msg = Label(root, font=('Arial', 30), bg='white', fg='#CC9900')
msg.grid(row=2, column=2)
msg.configure(image=start)

# Update Player Score
def updatePlayerScore():
    score = int(player_score['text'])
    score += 1
    player_score['text'] = score

# Update Computer Score
def updateCompScore():
    score = int(comp_score['text'])
    score += 1
    comp_score['text'] = score

# Logic
def fire():
    global player_choice
    player_choice = 1 
    player_img.configure(image=player_fire)
    MatchProcess()

def water():
    global player_choice
    player_choice = 2
    player_img.configure(image=player_water)
    MatchProcess()

def earth():
    global player_choice
    player_choice = 3
    player_img.configure(image=player_earth)
    MatchProcess()

def metal():
    global player_choice
    player_choice = 4
    player_img.configure(image=player_metal)
    MatchProcess()    

def wood():
    global player_choice
    player_choice = 4
    player_img.configure(image=player_wood)
    MatchProcess()  

def MatchProcess():
    comp_choice = random.randint(1, 3) 
    if comp_choice == 1:
        comp_img.configure(image=comp_fire)
        Computerfire()
    elif comp_choice == 2:
        comp_img.configure(image=comp_water)
        Computerwater()
    elif comp_choice == 3:
        comp_img.configure(image=comp_earth)
        Computerearth()
    elif comp_choice == 4:
        comp_img.configure(image=comp_metal)
        Computermetal()
    else:
        comp_img.configure(image=comp_wood)
        Computerwood()

def Computerfire():
    if player_choice == 1:
        msg.configure(image=draw)
        
    elif player_choice == 2:
        msg.configure(image=win)
        updatePlayerScore()
    elif player_choice == 3:
        msg.configure(image=win)
        updatePlayerScore()
    elif player_choice == 4:
        msg.configure(image=win)
        updatePlayerScore()
    else:
        msg.configure(image=win)
        updatePlayerScore()

def Computerwater():
    if player_choice == 1:
        msg.configure(image=win)
        updatePlayerScore()
    elif player_choice == 2:
        msg.configure(image=draw)

    elif player_choice == 3:
        msg.configure(image=lose)
        updateCompScore()
    elif player_choice == 4:
        msg.configure(image=win)
        updatePlayerScore()
    else:
        msg.configure(image=win)
        updatePlayerScore()


def Computerearth():
    if player_choice == 1:
        msg.configure(image=win)
        updatePlayerScore()
    elif player_choice == 2:
        msg.configure(image=win)
        updatePlayerScore()
    elif player_choice == 3:
        msg.configure(image=draw)

    elif player_choice == 4:
        msg.configure(image=draw)

    else:
        msg.configure(image=draw)


def Computermetal():
    if player_choice == 1:
        msg.configure(image=win)
        updatePlayerScore()
    elif player_choice == 2:
        msg.configure(image=win)
        updatePlayerScore()
    elif player_choice == 3:
        msg.configure(image=draw)

    elif player_choice == 4:
        msg.configure(image=draw)

    else:
        msg.configure(image=draw)

def Computerwood():
    if player_choice == 1:
        msg.configure(image=lose)
        updateCompScore()
    elif player_choice == 2:
        msg.configure(image=lose)
        updateCompScore()
    elif player_choice == 3:
        msg.configure(image=draw)

    elif player_choice == 4:
        msg.configure(image=draw)

    else:
        msg.configure(image=draw)

sm_player_fire = player_fire.subsample(2)
fire = Button(root, image=sm_player_fire, command=fire, bg='yellow')
fire.grid(row=4, column=1)

sm_player_water = player_water.subsample(2)
water = Button(root, image=sm_player_water, command=water, bg='yellow')
water.grid(row=4, column=2)

sm_player_earth = player_earth.subsample(2)
earth = Button(root, image=sm_player_earth, command=earth, bg='yellow')
earth.grid(row=4, column=3)

sm_player_metal = player_metal.subsample(2)
metal = Button(root, image=sm_player_metal, command=metal, bg='yellow')
metal.grid(row=5, column=3)

sm_player_wood = player_wood.subsample(2)
wood = Button(root, image=sm_player_wood, command=wood, bg='yellow')
wood.grid(row=5, column=1)

root.mainloop()