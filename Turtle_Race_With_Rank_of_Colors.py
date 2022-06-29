import turtle as T
import random
scrn = T.Screen()
colors = ['blue', 'green', 'yellow', 'brown', 'red']
start_positions = [180, 100, 0, -100, -180]
start_position = -300
start_x_positions = [start_position for _ in range(5)]
race_ends_x = 300


def rank_tester(lst):
    lst.sort(key = lambda x: -x.pos()[0])
    #print(lst)
    klr = [lst[i].pencolor() for i in range(len(lst))]
    return klr
    




players = []
for i in range(5):
    tim = T.Turtle('turtle')
    tim.penup()
    tim.color(colors[i])
    tim.goto(start_x_positions[i], start_positions[i])
    players.append(tim)

pn = T.Turtle()
pn.penup()
pn.goto(race_ends_x, 200)
pn.right(90)
pn.pendown()
pn.hideturtle()

pn.fd(400)

print(colors)
start = input('Enter the color of your turtle: ')
cond = True
if start in colors:
    while cond:
        for tim in players:
            tim.fd(random.randrange(5, 20))
            if tim.pos()[0] >= race_ends_x:
                cond = False
                if tim.pencolor() == start:
                    print(f"You won!")
                else:
                    print(f"You lost!, The winner is {tim.pencolor()}")
                    print("Your position in the race is = ", rank_tester(players).index(start) + 1)
else:
    print(f"No turtle of {start} found!")

scrn.exitonclick()
