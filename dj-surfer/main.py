import mido
import turtle
import time 

sc = turtle.Screen()
sc.bgcolor("black")
screenTk = sc.getcanvas().winfo_toplevel()
screenTk.attributes("-fullscreen", True)
sc.setup(width=1.0, height=1.0)

bounds = turtle.Turtle()
bounds.speed(0)
bounds.shape("square")
bounds.color("white")
bounds.shapesize(stretch_wid=50, stretch_len=1)
bounds.penup()
bounds.goto(150, 0)

bounds2 = turtle.Turtle()
bounds2.speed(0)
bounds2.shape("square")
bounds2.color("white")
bounds2.shapesize(stretch_wid=50, stretch_len=1)
bounds2.penup()
bounds2.goto(-150, 0)

outerbounds = turtle.Turtle()
outerbounds.speed(0)
outerbounds.shape("square")
outerbounds.color("white")
outerbounds.shapesize(stretch_wid=50, stretch_len=1)
outerbounds.penup()
outerbounds.goto(450, 0)

outerbounds2 = turtle.Turtle()
outerbounds2.speed(0)
outerbounds2.shape("square")
outerbounds2.color("white")
outerbounds2.shapesize(stretch_wid=50, stretch_len=1)
outerbounds2.penup()
outerbounds2.goto(-450, 0)

player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("white")
player.penup()
player.goto(0, -400)

hurdle = turtle.Turtle()
hurdle.speed(3)
hurdle.shape("square")
hurdle.shapesize(stretch_wid=4, stretch_len=10)
hurdle.color("white")
hurdle.penup()
hurdle.goto(0, -400)

def __init__ spawnhurdle(self)
    

    

# Initialize the score
score = 0

#time.sleep(10)
# Displays the score
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("white")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 450)
sketch.write(
    "Score:" score,
    align="center",
    font=("Terminal", 24, "normal"),
)

pyg = mido.Backend('mido.backends.pygame')
inport = pyg.open_input('Xponent MIDI 1') ##for Linux
#inport = mido.open_input("Xponent Audio   0")  ##for Windows
numCol = 0
inactivity = 0
inactive = False
level = 1
playerx=0
sumx=0
while True:
    for msg in inport.iter_pending():
        if msg.type == "control_change" and msg.control == 22:
            if (msg.channel % 5) == 1:
                sumx += 64-msg.value
                if sumx > 100:
                    playerx +=1
                    sumx=0
                    if playerx == 1:
                        player.goto(225, -400)
                    elif playerx == 0:
                        player.goto(0, -400)
                if sumx < -100:
                    playerx -=1
                    sumx=0
                    if playerx == 0:
                        player.goto(0, -400)
                    elif playerx == -1:
                        player.goto(-225, -400)
                if playerx > 1:
                    playerx =1
                if playerx < -1:
                    playerx = -1
    time.sleep(0.1)
    score +=1 
        elif msg.type == "note_on" and msg.note == 18:
            exit()