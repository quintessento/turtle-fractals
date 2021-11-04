import math
import random
from geom import Point2D


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

  def plot_random_point(self, turtle, step = 0.5, colors = ['red']):
    index = random.randint(0, len(self.vertices) - 1)
    vertex = self.vertices[index]
    color = colors[index % len(colors)]

    turtle_pos = Point2D(turtle.xcor(), turtle.ycor())
    pos = turtle_pos + (vertex - turtle_pos) * step

    turtle.setpos(pos.as_tuple())
    turtle.dot(2, color)
