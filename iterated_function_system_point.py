import turtle
import math
import os
import random
import sys
from typing import Tuple


WIDTH = 1000
HEIGHT = 1000

# Values as seen here:
# http://paulbourke.net/fractals/ifs/

FERN = [
    [0.0, 0.0, 0.0, 0.16, 0.0, 0.0],
    [0.2, -0.26, 0.26, 0.22, 0.0, 1.6],
    [-0.15, 0.28, 0.26, 0.24, 0.0, 0.44],
    [0.85, 0.04, -0.04, 0.85, 0.0, 1.6],
]
FERN_WEIGHTS = (0.01, 0.07, 0.07, 0.85)

MAPLE_LEAF = [
    [0.14, 0.01, 0.00, 0.51, -0.08, -1.31],
    [0.43, 0.52, -0.45, 0.50, 1.49, -0.75],
    [0.45, -0.49, 0.47, 0.47, -1.62, -0.74],
    [0.49, 0.00, 0.00, 0.51, 0.02, 1.62]
]
MAPLE_LEAF_WEIGHTS = (0.25, 0.25, 0.25, 0.25)

TREE = [
    [0.01, 0.00, 0.00, 0.45, 0.00, 0.00],
    [-0.1, 0.00, 0.00, -0.45, 0.00, 0.40],
    [0.42, -0.42, 0.42, 0.42, 0.00, 0.40],
    [0.42, 0.42, -0.42, 0.42, 0.00, 0.40]
]
TREE_WEIGHTS = (0.25, 0.25, 0.25, 0.25)

SNOWFLAKE = [
    [0.3820, 0.0000, 0.0000, 0.3820, 0.3090, 0.5700],
    [0.1180, -0.3633, 0.3633, 0.1180, 0.3633, 0.3306],
    [0.1180, 0.3633, -0.3633, 0.1180, 0.5187, 0.6940],
    [-0.3090, -0.2245, 0.2245, -0.3090, 0.6070, 0.3090],
    [-0.3090, 0.2245, -0.2245, -0.3090, 0.7016, 0.5335],
    [0.3820, 0.0000, 0.0000, -0.3820, 0.3090, 0.6770]
]
SNOWFLAKE_WEIGHTS = (1/6, 1/6, 1/6, 1/6, 1/6, 1/6)


class IFSPoint:
    
    def __init__(self, coefficient_set, coefficient_weights):
        self.coefficient_set = coefficient_set
        self.coefficient_weights = coefficient_weights
        
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
                    scale = min(WIDTH / (xmax - xmin), HEIGHT / (ymax - ymin))
                    xmid = (xmin + xmax) * 0.5
                    ymid = (ymin + ymax) * 0.5
                    tx = WIDTH / 2 + (x - xmid) * scale
                    ty = HEIGHT / 2 + (y - ymid) * scale
                    self.turtle.setpos(tx, ty)
                    self.turtle.dot(2, 'black')

        turtle.mainloop()


    def get_coefficients(self, roll: float) -> Tuple:
        return random.choices(self.coefficient_set, weights=self.coefficient_weights, k=1)[0]


def run_example_1():
    ifs = IFSPoint(FERN, FERN_WEIGHTS)
    ifs.iterate(100000)
    
def run_example_2():
    ifs = IFSPoint(MAPLE_LEAF, MAPLE_LEAF_WEIGHTS)
    ifs.iterate(100000)
    
def run_example_3():
    ifs = IFSPoint(TREE, TREE_WEIGHTS)
    ifs.iterate(100000)
    
def run_example_4():
    ifs = IFSPoint(SNOWFLAKE, SNOWFLAKE_WEIGHTS)
    ifs.iterate(1000000)
    
