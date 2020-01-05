import turtle as t
wn = t.Screen()
wn.bgcolor("light blue")

color= ["blue","red","green","yellow"]
a = t.Turtle()
b = t.Turtle()


b.home()
b.pendown()
b.fillcolor("brown")
b.begin_fill()
b.goto(10,0)
b.right(90)
b.goto(10,-200)
b.right(90)
b.goto(-10,-200)
b.right(90)
b.goto(-10,0)
b.end_fill()
b.penup()

a.tracer(0)

def pinwheel(ang):
  a.pendown()
  a.left(ang)
  for x in range(4):
    a.fillcolor(color[x])
    a.begin_fill()
    a.circle(50,180)
    a.goto(0,0)
    a.left(90)
    a.end_fill()
  a.penup()


speed = 2
sp=1
# def pw_move(x,y):
#   a.goto(x,y)
#   pinwheel(20)
a.ht()
b.ht()
def speedup():
  global speed
  speed=speed+0.25
  #print speed

def slowdown():
  global speed
  speed=speed-0.25
  #print speed

wn.onkey(speedup,"Up")
wn.onkey(slowdown,"Down")
wn.listen()

while True:
  a.clear()
  sp=+speed
  pinwheel(sp)
  a.update() 
