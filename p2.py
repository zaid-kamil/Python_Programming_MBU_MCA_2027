from turtle import *
speed(-1) # fastest
side = 6
pensize(6)
colors = ['red','blue']
for i in range(side):
    for i in range(side):
        fd(50)
        for i in range(side):
            pencolor(colors[i%2])
            dot(2)
            fd(25)
            lt(360/side)
            circle(10, 42)
        lt(360/side)
    fd(100)
    lt(360/side)
hideturtle()
mainloop()