import turtle, random
turtle.colormode(255)
class Hirst():

    def __init__(self, pen):
        self.pn = pen


    def dot_line(self, number_of_dots, distance_between_dots, number_of_lines, size_of_dot):
        self.pn.hideturtle()
        self.pn.penup()
        self.pn.speed('fastest')
        cnt = 0
        while cnt <= number_of_dots*number_of_lines - 1:
            self.pn.dot(size_of_dot, (random.randrange(0, 256, 20), random.randrange(0, 256, 20), random.randrange(0, 256, 20)))                    #We will use color of pen as the color of dot 
            self.pn.fd(distance_between_dots)
            cnt += 1
            if cnt % number_of_dots == 0:
                self.pn.left(90)
                self.pn.fd(distance_between_dots)
                self.pn.right(90)
                self.pn.bk(number_of_dots*distance_between_dots)


                
if __name__ == "__main__":
    pn = turtle.Turtle()
    pn.speed('fastest')
    scrn = turtle.Screen()
    scrn.setworldcoordinates(-1, -1, scrn.window_width() - 1, scrn.window_height() - 1)
    ob = Hirst(pn)
    #print('Enter no. of dots, distance between dots, number of lines, size of dots\n: ')
    #nd, dd, nl, sd = list(map(int, input().split()))
    ob.dot_line(34, 18, 34, 12); scrn.exitonclick()
    #number_of_dots, distance_between_dots, number_of_lines, size_of_dots
