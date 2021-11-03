import turtle
import random
import math

class Point2D:

  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __str__(self):
    return "(" + str(self.x) + ", " + str(self.y) + ")"

  def __add__(self, other):
    return Point2D(self.x + other.x, self.y + other.y)

  def __sub__(self, other):
    return Point2D(self.x - other.x, self.y - other.y)

  def __mul__(self, scalar):
    return Point2D(self.x * scalar, self.y * scalar)

  def as_tuple(self):
    return (self.x, self.y)


class RegularPolygon:

  def __init__(self, num_vertices, side_length, include_mid_points = False, starting_vertex = Point2D(0, 0)):
    self.vertices = [starting_vertex]

    angle = math.radians(180 - 360 / num_vertices)
   
    inter_angle = 0
    for i in range(num_vertices - 1):
      prev_point = self.vertices[i]

      inter_angle -= (math.pi - angle)

      point = Point2D(
        prev_point.x + side_length * math.cos(inter_angle),
        prev_point.y + side_length * math.sin(inter_angle)
      )

      self.vertices.append(point)

    mid_points = []
    if include_mid_points:
      for i in range(0, num_vertices - 1):
        mid_points.append((self.vertices[i] + self.vertices[i + 1]) * 0.5)
      mid_points.append((self.vertices[0] + self.vertices[len(self.vertices) - 1]) * 0.5)

      self.vertices += mid_points

  def plot_perimeter(self, turtle):
    turtle.setpos(self.vertices[0].as_tuple())
    turtle.pendown()
    turtle.color('red')
    for i in range(1, len(self.vertices)):
      turtle.goto(self.vertices[i].as_tuple())
    turtle.goto(self.vertices[0].as_tuple())
    turtle.penup()

  def get_starting_point(self):
    return self.vertices[0]

  def plot_random_point(self, turtle, step = 0.5, colors=['red']):
    index = random.randint(0, len(self.vertices) - 1)
    vertex = self.vertices[index]
    color = colors[index % len(colors)]

    turtle_pos = Point2D(turtle.xcor(), turtle.ycor())
    pos = turtle_pos + (vertex - turtle_pos) * step

    turtle.setpos(pos.as_tuple())
    turtle.dot(1, color)


class ChaosGame:

  def __init__(self, colors):
    self.colors = colors
    self.turtle = turtle.Turtle()
    self.turtle.hideturtle()
    turtle.tracer(2000, 25)
    self.turtle.penup()

  def play_polygon(self, num_vertices, size, include_mid_points = False, num_iterations = 10000, step = 0.5, draw_outline = False):
    polygon = RegularPolygon(num_vertices, size, include_mid_points)
    if draw_outline:
      polygon.plot_perimeter(self.turtle)
    self.turtle.setpos(polygon.get_starting_point().as_tuple())

    for i in range(num_iterations):
      polygon.plot_random_point(self.turtle, step, self.colors)


class LSystem:

  def __init__(self, depth = 1, rules = {}, axiom = "", length = 30, angle = 0, actions = {}):
    self.depth = depth
    self.rules = rules
    self.axiom = axiom
    self.length = length
    self.angle = angle
    self.actions = actions

    self.turtle = turtle.Turtle()
    self.turtle.speed(10)
    self.turtle.setheading(90)

    ts = self.turtle.getscreen()
    ts.screensize(4000, 4000)
    ts.setup(width=1.0, height=1.0, startx=None, starty=None)

  def draw(self):
    instruction = self.axiom
    print(instruction)

    # http://paulbourke.net/fractals/lsys/

    for current_depth in range(self.depth):
      
      inst_length = len(instruction)
      c_index = 0
      while c_index < inst_length:

        c = instruction[c_index]
        if (c in self.rules):
          replacement_inst = self.rules[c]
   
          instruction = instruction[:c_index] + \
                        replacement_inst + \
                        instruction[(c_index + 1):]

          inst_length = len(instruction)
          c_index += (len(replacement_inst))
        else:
          c_index += 1

    print("Final: ", instruction)

    saved_states = []

    for command in instruction:
      if command in self.actions:
        self.actions[command](self.turtle, self.length, self.angle, saved_states)

    # call mainloop to let the graphics window stay open after the turtle has finished drawing
    turtle.mainloop()


def forward(t, length, angle, saved_states):
  t.color('black')
  t.forward(length)

def leaf(t, length, angle, saved_states):
  t.color('red')
  t.forward(length)

def turn_left(t, length, angle, saved_states):
  t.left(angle)

def turn_right(t, length, angle, saved_states):
  t.right(angle)

def push(t, length, angle, saved_states):
  saved_states.append((t.pos(), t.heading()))

def pop(t, length, angle, saved_states):
  pos, angle = saved_states.pop()
  t.penup()
  t.setpos(pos)
  t.setheading(angle)
  t.pendown()

def push_and_turn_left(t, length, angle, saved_states):
  push(t, length, angle, saved_states)
  turn_left(t, length, angle, saved_states)

def pop_and_turn_right(t, length, angle, saved_states):
  pop(t, length, angle, saved_states)
  turn_right(t, length, angle, saved_states)

# variables : 0, 1
# constants: “[”, “]”
# axiom  : 0
# rules  : (1 → 11), (0 → 1[0]0)

# tree_system = \
#   LSystem(depth = 5, rules = { "1" : "11", "0" : "1[0]0" }, axiom = "0", angle = 45, length = 30,
#     actions = { "1" : forward, "0" : leaf, "[" : push_and_turn_left, "]" : pop_and_turn_right }
#   )

# axiom = FX
# X -> [-FX]+FX
# angle = 40

# tree_system = LSystem(depth = 2, rules = { "X" : "[-FX]+FX" }, axiom = "FX", angle = 40, actions = { "F" : forward, "X" : leaf })

# axiom = X
# F -> FF
# X -> F[+X]F[-X]+X
# angle = 20

# tree_system = LSystem(depth = 5, rules = { "F" : "FF", "X" : "F[+X]F[-X]+X" }, axiom = "X", length = 30, angle = 20, 
#   actions = { "F" : forward, "X" : leaf, "-" : turn_left, "+" : turn_right, "[" : push, "]" : pop })

tree_system = LSystem(depth = 2, rules = { "F" : "F+F-F-FF+F+F-F" }, axiom = "F+F+F+F", length = 30, angle = 90,
  actions = { "F" : forward, "-" : turn_left, "+" : turn_right })


tree_system.draw()

# F[-F[-FX]+FX]+F[-FX]+FX

# colors = ['red', 'green', 'blue', 'magenta']
# chaos_game = ChaosGame(colors)
# chaos_game.play_polygon(5, 200, include_mid_points = False, num_iterations = 50000, step = (1.0 / 2.0), draw_outline = False)