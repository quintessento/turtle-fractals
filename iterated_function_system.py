import turtle
import math


class Rectangle:
    
    def __init__(self, x, y, width, height, angle):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle
    
    def apply_transform(self, translate_x, translate_y, scale_x, scale_y, rotate_z):
        pass
    
    def draw(self, t):
        t.penup()
        
        half_width = self.width * 0.5
        half_height = self.height * 0.5
        angle_rad = (self.angle + 90) * math.pi / 180.0
        t.setpos(self.x - half_width * math.cos(angle_rad), self.y - half_height * math.sin(angle_rad))
        t.setheading(self.angle + 90)
        t.pendown()
        t.forward(self.height)
        t.right(90)
        t.forward(self.width)
        t.right(90)
        t.forward(self.height)
        t.right(90)
        t.forward(self.width)
        t.right(90)


class Shape:
    
    def __init__(self):
        self.rect1 = Rectangle(0, 0, 100, 100, 0)
        self.rect2 = Rectangle(-70, 40, 120, 60, 15)
        self.rect3 = Rectangle(60, 65, 90, 60, -20)
        
    def apply_transform(self, translate_x, translate_y, scale_x, scale_y, rotate_z):
        self.rect1.apply_transform(translate_x, translate_y, scale_x, scale_y, rotate_z)
        self.rect2.apply_transform(translate_x, translate_y, scale_x, scale_y, rotate_z)
        self.rect3.apply_transform(translate_x, translate_y, scale_x, scale_y, rotate_z)
        
    def draw(self, t):
        self.rect1.draw(t)
        self.rect2.draw(t)
        self.rect3.draw(t)


class IFS:
    
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.speed(10)
        self.turtle.setheading(90)

        ts = self.turtle.getscreen()
        ts.screensize(4000, 4000)
        ts.setup(width=1.0, height=1.0, startx=None, starty=None)
    
    def generate(self):
        shape = Shape()
        shape.draw(self.turtle)
        
        turtle.mainloop()

#                    #set 1     set 2     set 3     set 4
#              #a     0.0100   -0.0100    0.4200    0.4200
#              #b     0.0000    0.0000   -0.4200    0.4200
#              #c     0.0000    0.0000    0.4200   -0.4200
#              #d     0.4500   -0.4500    0.4200    0.4200
#              #e     0.0000    0.0000    0.0000    0.0000
#              #f     0.0000    0.4000    0.4000    0.4000

def run_example_1():
    ifs = IFS()
    ifs.generate()

