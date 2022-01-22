from re import S
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

        # print('Angle: ', self.angle)

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
    """ TODO: unfinished. """
    def __init__(self) -> None:
        self.turtle = turtle.Turtle()

        self.turtle.setheading(90)
        turtle.tracer(1, 0)

        ts = self.turtle.getscreen()
        ts.screensize(4000, 4000)
        
        if os.name == 'nt':
            ts.setup(width=0.99, height=0.99, startx=None, starty=None)
        else:
            ts.setup(width=1.00, height=1.00, startx=None, starty=None)

    def _draw_base_rect(self, pos : Point2D, size : tuple, angle : float) -> RectangleLC:
        size_x, size_y = size
        base_rect = RectangleLC(pos, size_x, size_y, angle)
        base_rect.draw(self.turtle)
        return base_rect

    def generate(self, pos : Point2D, scale : tuple, start_size : int, start_angle : float, depth : int):
        scale_x, scale_y = scale
        base_rect = self._draw_base_rect(pos, (start_size * scale_x, start_size * scale_y), start_angle)

        if depth <= 0:
            return

        angle = 30

        left_child_angle = start_angle + angle
        left_child_size = start_size * math.cos(math.radians(angle))

        right_child_angle = left_child_angle - 90
        right_child_size = start_size * math.sin(math.radians(angle))

        next_depth = depth - 1
        
        # left side
        left_child_offset = Point2D(
            start_size * math.cos(math.radians(start_angle)), 
            start_size * math.sin(math.radians(start_angle)))
        left_child_pos = base_rect.tl_corner + left_child_offset
        self.generate(left_child_pos, (1.2, 0.8), left_child_size, left_child_angle, next_depth)

        # right side
        right_child_offset = Point2D(
            left_child_size * math.cos(math.radians(left_child_angle)), 
            left_child_size * math.sin(math.radians(left_child_angle)))
        right_child_pos = base_rect.tl_corner + right_child_offset
        self.generate(right_child_pos, scale, right_child_size, right_child_angle, next_depth)


class PythagoreanTree:

    def __init__(self, start_angle: float = 45.0) -> None:
        self.start_angle = start_angle

        self.turtle = turtle.Turtle()

        self.turtle.setheading(90)
        turtle.tracer(1, 0)

        ts = self.turtle.getscreen()
        ts.screensize(4000, 4000)
        
        if os.name == 'nt':
            ts.setup(width=0.99, height=0.99, startx=None, starty=None)
        else:
            ts.setup(width=1.00, height=1.00, startx=None, starty=None)

    def _draw_base_rect(self, pos : Point2D, size : tuple, angle : float) -> RectangleLC:
        size_x, size_y = size
        base_rect = RectangleLC(pos, size_x, size_y, angle)
        base_rect.draw(self.turtle)
        return base_rect

    def generate(self, pos : Point2D, scale : tuple, start_size : int, start_angle : float, depth : int):
        scale_x, scale_y = scale
        base_rect = self._draw_base_rect(pos, (start_size * scale_x, start_size * scale_y), start_angle)

        if depth <= 0:
            return

        angle = self.start_angle

        left_child_angle = start_angle + angle
        left_child_size = start_size * math.cos(math.radians(angle))

        right_child_angle = left_child_angle - 90
        right_child_size = start_size * math.sin(math.radians(angle))

        next_depth = depth - 1
        
        # left side
        self.generate(base_rect.tl_corner, scale, left_child_size, left_child_angle, next_depth)

        offset = Point2D(
            left_child_size * math.cos(math.radians(left_child_angle)), 
            left_child_size * math.sin(math.radians(left_child_angle)))
        right_child_pos = base_rect.tl_corner + offset
        # right side
        self.generate(right_child_pos, scale, right_child_size, right_child_angle, next_depth)


def run_example_1(depth: int = 5):
    """ Pythagorean tree. """
    tree = PythagoreanTree()
    tree.generate(Point2D(0, 0), (1.0, 1.0), 100, 0, depth)
    turtle.mainloop()

def run_example_2(depth: int = 5):
    """ Pythagorean tree (inclined). """
    tree = PythagoreanTree(60)
    tree.generate(Point2D(0, 0), (1.0, 1.0), 100, 0, depth)
    turtle.mainloop()

def run_example_3(depth: int = 5):
    tree = IFSRect()
    tree.generate(Point2D(0, 0), (1.0, 1.0), 100, 0, depth)
    turtle.mainloop()
    
