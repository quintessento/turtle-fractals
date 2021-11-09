import turtle
import math
import os


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

        half_width = self.width * 0.5
        half_height = self.height * 0.5
        angle_rad = (self.angle + 90) * math.pi / 180.0

        t.penup()
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

    def __init__(self, x, y, width, height, angle):
        self.children = []
        self.rectangles = []

        self.rectangles.append(Rectangle(x * 1.0, y * 1.0, width * 1.0, height * 1.0, angle * 1.0))
        # self.rectangles.append(Rectangle(
        #     x * 1.0 + width * -0.35, 
        #     y * 1.0 + height * 0.45, 
        #     width * 1.2, 
        #     height * 0.6, 
        #     angle + 360 * 0.04
        # ))
        # self.rectangles.append(Rectangle(
        #     x * 1.0 + width * 0.25, 
        #     y * 1.0 + height * 0.7,
        #     width * 0.9, 
        #     height * 0.6, 
        #     angle - 360 * 0.05
        # ))
        self.rectangles.append(Rectangle(
            x * 1.0 + width * -0.75, 
            y * 1.0 + height * 0.45, 
            width * 1.2, 
            height * 0.6, 
            angle + 360 * 0.04
        ))
        self.rectangles.append(Rectangle(
            x * 1.0 + width * 0.5, 
            y * 1.0 + height * 0.7,
            width * 0.9, 
            height * 0.6, 
            angle - 360 * 0.05
        ))

    def expand(self, depth):
        if depth > 0:
            for r in self.rectangles:
                self.children.append(Shape(r.x, r.y, r.width * 0.5, r.height * 0.5, r.angle))
            self.rectangles.clear()

            for s in self.children:
                s.expand(depth - 1)

    def apply_transform(self, translate_x, translate_y, scale_x, scale_y, rotate_z):
        pass
        # self.rect1.apply_transform(translate_x, translate_y, scale_x, scale_y, rotate_z)
        # self.rect2.apply_transform(translate_x, translate_y, scale_x, scale_y, rotate_z)
        # self.rect3.apply_transform(translate_x, translate_y, scale_x, scale_y, rotate_z)
        
    def draw(self, t):
        if not self.children:
            for r in self.rectangles:
                r.draw(t)

        for s in self.children:
            s.draw(t)


class IFS:
    
    def __init__(self):
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        turtle.tracer(30, 0)
        self.turtle.setheading(90)

        ts = self.turtle.getscreen()
        ts.screensize(4000, 4000)
        
        if os.name == 'nt':
            ts.setup(width=0.99, height=0.99, startx=None, starty=None)
        else:
            ts.setup(width=1.00, height=1.00, startx=None, starty=None)
    
    def generate(self):
        shape = Shape(0, 0, 400, 400, 0)
        shape.expand(5)
        shape.draw(self.turtle)
        
        turtle.mainloop()


def run_example_1():
    ifs = IFS()
    ifs.generate()

