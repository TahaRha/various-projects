import turtle

mok = turtle.Turtle()
mok.speed("fastest")

mok.pu()
mok.goto(-100, 100)
mok.pd()

mok.fillcolor('red')
mok.begin_fill()
for i in range(2):
    mok.fd(350)
    mok.rt(90)
    mok.fd(250)
    mok.rt(90)
mok.end_fill()

mok.pu()
mok.goto(0,0)
mok.pd()

mok.fillcolor('green')
mok.begin_fill()

for i in range(5):
    mok.fd(150)
    mok.rt(144)
mok.end_fill()


def draw(x,y,color = 'red'):
    mok.pu()
    mok.goto(x, y)
    mok.pd()
    mok.fillcolor(color)
    mok.begin_fill()
    for i in range(8):
        mok.fd(50)
        mok.lt(45)
    mok.end_fill();
        
    
draw(-200, 0, "blue")
mok.pu()
mok.goto(-200, -250)
mok.pd()

mok.lt(75)
mok.fd(50)
mok.bk(20)
mok.lt(30)
mok.fd(20)
mok.pu()
mok.goto(0,0)
mok.pd()






