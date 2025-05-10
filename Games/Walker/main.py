height = 10
width = 30
x = 1
y = 1
import os, time, keyboard #DOWNLOAD KEYBOARD MODULE BY PIP (pip install keyboard) <-------------------

def update():
    os.system("cls")
    lines = list()
    for i in range(0, height):
        lines.append("@"*width)
    plr_line = list()
    for symbol in lines[x]: plr_line.append(symbol)
    plr_line[y] = " "
    lines[x] = "".join(plr_line)
    for line in lines:
        print(line)

def up(event):
    global x
    x -= 1
    try: update()
    except: x += 1; update()

def down(event):
    global x
    x += 1
    try: update()
    except: x -= 1; update()

def left(event):
    global y
    y -= 1
    try: update()
    except: y += 1; update()

def right(event):
    global y
    y += 1
    try: update()
    except: y -= 1; update()

keyboard.on_release_key("W", up)
keyboard.on_release_key("A", left)
keyboard.on_release_key("S", down)
keyboard.on_release_key("D", right)
while 1:
    pass
