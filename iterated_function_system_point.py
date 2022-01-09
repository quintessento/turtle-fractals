import turtle
import math
import os
import random
import sys
from typing import Tuple

class IFSPoint:

    NX = 1000
    NY = 1000
    
    def __init__(self) -> None:
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        turtle.tracer(2000, 25)
        self.turtle.penup()
        self.prev_x = 0.0
        self.prev_y = 0.0

        # turtle.tracer(1, 0)

        ts = self.turtle.getscreen()
        ts.screensize(4000, 4000)
        
        if os.name == 'nt':
            ts.setup(width=0.99, height=0.99, startx=None, starty=None)
        else:
            ts.setup(width=1.00, height=1.00, startx=None, starty=None)


    def iterate(self, num_iterations = 10000):
        self.turtle.setpos(0, 0)

        xmin = sys.float_info.max
        ymin = sys.float_info.max
        xmax = sys.float_info.min
        ymax = sys.float_info.min

        x, y = self.turtle.pos()
        self.prev_x = x
        self.prev_y = y

        for j in range(2):
            for _ in range(num_iterations):
                roll = random.uniform(0, 1)
                coeffs = self.get_coefficients(roll)

                x = coeffs[0] * self.prev_x + coeffs[1] * self.prev_y + coeffs[4]
                y = coeffs[2] * self.prev_x + coeffs[3] * self.prev_y + coeffs[5]
                self.prev_x = x
                self.prev_y = y

                if x < xmin:
                    xmin = x
                if y < ymin:
                    ymin = y
                if x > xmax:
                    xmax = x
                if y > ymax:
                    ymax = y

                if j == 1:
                    scale = min(self.NX / (xmax - xmin), self.NY / (ymax - ymin))
                    xmid = (xmin + xmax) * 0.5
                    ymid = (ymin + ymax) * 0.5
                    tx = self.NX / 2 + (x - xmid) * scale
                    ty = self.NY / 2 + (y - ymid) * scale
                    self.turtle.setpos(tx, ty)
                    self.turtle.dot(2, 'black')

        turtle.mainloop()


    def get_coefficients(self, roll: float) -> Tuple:
        sets = [
            [0.0, 0.0, 0.0, 0.16, 0.0, 0.0],
            [0.2, -0.26, 0.26, 0.22, 0.0, 1.6],
            [-0.15, 0.28, 0.26, 0.24, 0.0, 0.44],
            [0.85, 0.04, -0.04, 0.85, 0.0, 1.6],
        ]

        return random.choices(sets, weights=(0.01, 0.07, 0.07, 0.85), k=1)[0]


def run_example_1():
    ifs = IFSPoint()
    ifs.iterate(10000)