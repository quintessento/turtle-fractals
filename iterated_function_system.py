import turtle


class IFS:
    
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.speed(10)
        self.turtle.setheading(90)

        ts = self.turtle.getscreen()
        ts.screensize(4000, 4000)
        ts.setup(width=1.0, height=1.0, startx=None, starty=None)
    
    def go_to_point(self, a, b, c, d, e, f):
        p = self.turtle.pos()
        
        x = a * p[0] + b * p[1] + e
        y = c * p[0] + d * p[1] + f
        
        self.turtle.goto(x, y)

#                    #set 1     set 2     set 3     set 4
#              #a     0.0100   -0.0100    0.4200    0.4200
#              #b     0.0000    0.0000   -0.4200    0.4200
#              #c     0.0000    0.0000    0.4200   -0.4200
#              #d     0.4500   -0.4500    0.4200    0.4200
#              #e     0.0000    0.0000    0.0000    0.0000
#              #f     0.0000    0.4000    0.4000    0.4000

def run_example_1():
    ifs = IFS()
    ifs.go_to_point(0.0100, 0.0000, 0.0000, 0.4500, 0.0000, 0.0000)
    turtle.mainloop()