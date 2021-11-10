import turtle
import math
import os


class Rectangle:
    
    def __init__(self, x, y, width, height, scale, angle):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.scale = scale
        self.angle = angle
        
        self.half_width = self.width * 0.5
        self.half_height = self.height * 0.5
        self.angle_rad = (self.angle + 90) * math.pi / 180.0

    def draw(self, t):


        t.penup()
        #t.setpos((self.x) * math.cos(self.angle_rad) - (self.y) * math.sin(self.angle_rad), 
                 #(self.x) * math.sin(self.angle_rad) + (self.y) * math.cos(self.angle_rad)) 
        t.setpos(self.x - self.half_width * math.cos(self.angle_rad), 
                 self.y - self.half_height * math.sin(self.angle_rad)) 
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

    def __init__(self, x, y, scale, angle):
        #self.width = width
        #self.height = height
        self.children = []
        self.rectangles = []
        
        angle1 = angle + 360 * 0.0
        angle1_rad = (angle1 + 90) * math.pi / 180.0
        self.rectangles.append(Rectangle(
            x,
            y,
            #x * math.cos(angle1_rad) - y * math.sin(angle1_rad), 
            #x * math.sin(angle1_rad) + y * math.cos(angle1_rad), 
            400 * 1.0 * scale, 
            400 * 1.0 * scale, 
            scale,
            angle1
        ))
        
        angle2 = angle * scale + 360 * 0.06
        angle2_rad = (angle2 + 90) * math.pi / 180.0
        self.rectangles.append(Rectangle(
            #x + 400 * -0.75 * scale,
            #y + 400 * 0.3 * scale,
            x * math.cos(angle2_rad) - y * math.sin(angle2_rad) + 400 * -0.75 * scale, 
            x * math.sin(angle2_rad) + y * math.cos(angle2_rad) + 400 * 0.3 * scale, 
            400 * 1.2 * scale, 
            400 * 0.6 * scale, 
            scale,
            angle2
        ))
        
        angle3 = angle * scale - 360 * 0.06
        angle3_rad = (angle3 + 90) * math.pi / 180.0
        self.rectangles.append(Rectangle(
            #x + 400 * 0.5 * scale,
            #y + 400 * 0.7 * scale,
            x * math.cos(angle3_rad) - y * math.sin(angle3_rad) + 400 * 0.5 * scale, 
            x * math.sin(angle3_rad) + y * math.cos(angle3_rad) + 400 * 0.7 * scale,
            400 * 0.9 * scale, 
            400 * 0.6 * scale, 
            scale,
            angle3
        ))

    def expand(self, depth):
        if depth > 0:
            for r in self.rectangles:
                self.children.append(Shape(r.x, r.y, r.scale * 0.5, r.angle))
            self.rectangles.clear()

            for s in self.children:
                s.expand(depth - 1)
        
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

        self.turtle.setheading(90)

        ts = self.turtle.getscreen()
        ts.screensize(4000, 4000)
        
        if os.name == 'nt':
            ts.setup(width=0.99, height=0.99, startx=None, starty=None)
            turtle.tracer(30, 0)
        else:
            ts.setup(width=1.00, height=1.00, startx=None, starty=None)
            turtle.tracer(1, 0)
    
    def generate(self):
        shape = Shape(0, 0, 1.0, 0)
        shape.expand(1)
        shape.draw(self.turtle)
        
        turtle.mainloop()


def run_example_1():
    ifs = IFS()
    ifs.generate()

