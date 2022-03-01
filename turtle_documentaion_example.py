import turtle


pn = turtle.Turtle()
spid = 'fastest'
length = 200
kalar = 'pink'
thickness = 2
pn.speed(spid)
pn.pensize(thickness)
pn.color(kalar)


while True:
    pn.fd(length)
    pn.left(170)
    if abs(pn.pos()) < 1:
        break

    
