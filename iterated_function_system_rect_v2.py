import turtle
import math
import os

from geom import Point2D


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
        center_x = self.center_x
        center_y = self.center_y
        t.setpos(center_x, center_y)
        t.color('red')
        t.dot(0.1 * min(self.scale_width, self.scale_height), 'red')

        width = self.scale_width
        height =self.scale_height

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


class RectangleLC:

    def __init__(self, bl_corner : Point2D, scale_width, scale_height, angle):
        self.bl_corner = bl_corner
        self.tl_corner = bl_corner
        self.br_corner = bl_corner
        self.tr_corner = bl_corner

        self.scale_width = scale_width
        self.scale_height = scale_height

        self.angle = angle
        
        self.angle_rad = math.radians(self.angle)

    def draw(self, t):
        t.penup()

        # mark the center
        start_x = self.bl_corner.x
        start_y = self.bl_corner.y
        t.setpos(start_x, start_y)
        t.color('red')
        t.dot(0.1 * min(self.scale_width, self.scale_height), 'red')

        width = self.scale_width
        height = self.scale_height

        # distance to the first point (lower left corner)
        # c = math.sqrt((width * 0.5) ** 2.0 + (height * 0.5) ** 2.0)

        # local angle
        # theta = math.atan2(height, width)

        # global shape angle + local rectangle angle
        # dx = c * math.cos(self.angle_rad + theta)
        # global shape angle + local rectangle angle
        # dy = c * math.sin(self.angle_rad + theta)
        
        print('Angle: ', self.angle)
        # print(c)
        # print('dx: ', dx, ', dy: ', dy)

        # t.setpos(center_x - dx, 
        #          center_y - dy) 
        t.setheading(90 + self.angle)
        t.pendown()

        t.color('black')
        t.forward(height)
        self.tl_corner = Point2D(t.xcor(), t.ycor())
        t.right(90)
        t.forward(width)
        self.tr_corner = Point2D(t.xcor(), t.ycor())
        t.right(90)
        t.forward(height)
        self.br_corner = Point2D(t.xcor(), t.ycor())
        t.right(90)
        t.forward(width)
        t.right(90)


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
        # shape = Shape(0, 0, 1.0, 1.0, 0)
        # shape.expand(0)
        # shape.draw(self.turtle)
        
        turtle.mainloop()


class PythagoreanTree:

    def __init__(self) -> None:
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

    def _draw_base_rect(self, pos : Point2D, size : int, angle : float) -> RectangleLC:
        base_size = size
        base_rect = RectangleLC(pos, base_size, base_size, angle)
        base_rect.draw(self.turtle)
        return base_rect

    def generate(self, pos : Point2D, size : int, angle : float, depth : int):

        base_rect = self._draw_base_rect(pos, size, angle)

        child_size = math.sqrt((size ** 2) * 0.5)

        if depth <= 0:
            return

        next_depth = depth - 1
        left_child_angle = angle + 45
        self.generate(base_rect.tl_corner, child_size, left_child_angle, next_depth)

        right_child_angle = angle - 45
        offset = Point2D(
            child_size * math.cos(math.radians(left_child_angle)), 
            child_size * math.sin(math.radians(left_child_angle)))
        right_child_pos = base_rect.tl_corner + offset
        self.generate(right_child_pos, child_size, right_child_angle, next_depth)


def run_example_1():
    tree = PythagoreanTree()
    tree.generate(Point2D(0, 0), 100, 0, 10)
    turtle.mainloop()
