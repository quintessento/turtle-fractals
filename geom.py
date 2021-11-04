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