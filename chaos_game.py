import turtle
from polygons import RegularPolygon


class ChaosGame:

  def __init__(self, colors):
    self.colors = colors
    self.turtle = turtle.Turtle()
    self.turtle.hideturtle()
    self.turtle.speed(0)
    turtle.tracer(100, 0)

    ts = self.turtle.getscreen()
    ts.screensize(4000, 4000)

    self.turtle.penup()

  def play_polygon(self, num_vertices, size, include_mid_points = False, num_iterations = 10000, step = 0.5, draw_outline = False):
    polygon = RegularPolygon(num_vertices, size, include_mid_points)
    if draw_outline:
      polygon.plot_perimeter(self.turtle)
    self.turtle.setpos(polygon.get_starting_point().as_tuple())

    for i in range(num_iterations):
      polygon.plot_random_point(self.turtle, step, self.colors)

    turtle.mainloop()


def run_example_1(iterations: int = 50000):
  """ Pentagon. """
  colors = ['red', 'green', 'blue', 'magenta']
  chaos_game = ChaosGame(colors)
  chaos_game.play_polygon(5, 300, include_mid_points = False, num_iterations = iterations, step = (1.0 / 2.0), draw_outline = False)

def run_example_2(iterations: int = 50000):
  """ Sierpinski carpet. """
  colors = ['red', 'green', 'blue', 'magenta']
  chaos_game = ChaosGame(colors)
  chaos_game.play_polygon(4, 300, include_mid_points = True, num_iterations = iterations, step = (2.0 / 3.0), draw_outline = False)

def run_example_3(iterations: int = 50000):
  """ Sierpinski triangle. """
  colors = ['red', 'green', 'blue', 'magenta']
  chaos_game = ChaosGame(colors)
  chaos_game.play_polygon(3, 300, include_mid_points = False, num_iterations = iterations, step = (1.0 / 2.0), draw_outline = False)