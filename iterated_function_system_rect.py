import turtle
import math
import os

#  *------------ +x
#  |
#  |
#  |
#  |
# +y

def min(a, b):
    if a > b:
        return b
    return a

origin_x = 0
origin_y = 0
default_size = 400

class Rectangle:
    
    def __init__(self, dx, dy, scale_width, scale_height, angle):
        self.center_x = dx
        self.center_y = dy
        self.scale_width = scale_width
        self.scale_height = scale_height
        self.angle = angle
        
        self.angle_rad = math.radians(self.angle)

    def draw(self, t):
        t.penup()

        # mark the center
        center_x = origin_x + self.center_x
        center_y = origin_y + self.center_y
        t.setpos(center_x, center_y)
        t.color('red')
        t.dot(10 * min(self.scale_width, self.scale_height), 'red')

        width = default_size * self.scale_width
        height = default_size * self.scale_height

        # distance to the first point (lower left corner)
        c = math.sqrt((width * 0.5) ** 2.0 + (height * 0.5) ** 2.0)

        # local angle
        theta = math.atan2(height, width)

        # global shape angle + local rectangle angle
        dx = c * math.cos(self.angle_rad + theta)
        # global shape angle + local rectangle angle
        dy = c * math.sin(self.angle_rad + theta)
        
        print('Angle: ', self.angle)
        # print(c)
        # print('dx: ', dx, ', dy: ', dy)

        t.setpos(center_x - dx, 
                 center_y - dy) 
        t.setheading(90 + self.angle)
        t.pendown()

        t.color('black')
        t.forward(height)
        t.right(90)
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
        t.forward(width)
        t.right(90)


class Shape:

    def __init__(self, x, y, scale_width, scale_height, angle):
        #self.width = width
        #self.height = height
        self.children = []
        self.rectangles = []
        
        angle1 = angle + 360 * 0.0
        # angle1_rad = (angle1 + 90) * math.pi / 180.0
        self.rectangles.append(Rectangle(
            x,
            y,
            #x * math.cos(angle1_rad) - y * math.sin(angle1_rad), 
            #x * math.sin(angle1_rad) + y * math.cos(angle1_rad), 
            # 400 * 1.0 * scale_width, 
            # 400 * 1.0 * scale_height, 
            scale_width,
            scale_height,
            angle1
        ))
        
        angle2 = angle * 1.0 + 360 * 0.06
        # angle2_rad = (angle2 + 90) * math.pi / 180.0
        self.rectangles.append(Rectangle(
            x + 400 * -0.55 * scale_width,
            y + 400 * 0.5 * scale_height,
            # x * math.cos(angle2_rad) - y * math.sin(angle2_rad) + 400 * -0.75 * scale, 
            # x * math.sin(angle2_rad) + y * math.cos(angle2_rad) + 400 * 0.3 * scale, 
            # 400 * 1.2 * scale_width, 
            # 400 * 0.6 * scale_height, 
            scale_width,
            scale_height,
            angle2
        ))
        
        angle3 = angle * 1.0 - 360 * 0.06
        angle3_rad = (angle3 + 90) * math.pi / 180.0
        self.rectangles.append(Rectangle(
            x + 400 * 0.5 * scale_width,
            y + 400 * 0.6 * scale_height,
            # x * math.cos(angle3_rad) - y * math.sin(angle3_rad) + 400 * 0.5 * scale, 
            # x * math.sin(angle3_rad) + y * math.cos(angle3_rad) + 400 * 0.7 * scale,
            # 400 * 0.9 * scale_width, 
            # 400 * 0.6 * scale_height, 
            scale_width,
            scale_height,
            angle3
        ))

    def expand(self, depth):
        if depth > 0:
            for r in self.rectangles:
                self.children.append(Shape(r.center_x, r.center_y, r.scale_width * 0.5, r.scale_height * 0.5, r.angle))
            self.rectangles.clear()

            for s in self.children:
                s.expand(depth - 1)
        
    def draw(self, t):
        if not self.children:
            for r in self.rectangles:
                r.draw(t)

        for s in self.children:
            s.draw(t)


class IFSRect:
    
    def __init__(self):
        self.turtle = turtle.Turtle()
        # self.turtle.hideturtle()

        self.turtle.setheading(90)
        turtle.tracer(1, 0)

        ts = self.turtle.getscreen()
        ts.screensize(4000, 4000)
        
        if os.name == 'nt':
            ts.setup(width=0.99, height=0.99, startx=None, starty=None)
        else:
            ts.setup(width=1.00, height=1.00, startx=None, starty=None)
            
    
    def generate(self):
        shape = Shape(0, 0, 1.0, 1.0, 0)
        shape.expand(0)
        shape.draw(self.turtle)
        
        turtle.mainloop()


def run_example_1():
    ifs = IFSRect()
    ifs.generate()

