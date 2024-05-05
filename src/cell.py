from .graphics import Line, Point

class Cell:
  def __init__(self, win):
    self.visited = False
    self.has_left_wall = True
    self.has_right_wall = True
    self.has_top_wall = True
    self.has_bottom_wall = True
    self._x1 = None
    self._x2 = None
    self._y1 = None
    self._y2 = None
    self._win = win

  def draw(self, x1, y1, x2, y2):
    self._x1 = x1
    self._x2 = x2
    self._y1 = y1
    self._y2 = y2

    left = Line(Point(x1, y1), Point(x1, y2))
    top = Line(Point(x1, y1), Point(x2, y1))
    right = Line(Point(x2, y1), Point(x2, y2))
    bottom = Line(Point(x1, y2), Point(x2, y2))

    if self.has_left_wall:
      self._win.draw_line(left)
    else:
      self._win.draw_line(left, "white")

    if self.has_top_wall:
      self._win.draw_line(top)
    else:
      self._win.draw_line(top, "white")

    if self.has_right_wall:
      self._win.draw_line(right)
    else:
      self._win.draw_line(right, "white")

    if self.has_bottom_wall:
      self._win.draw_line(bottom)
    else:
      self._win.draw_line(bottom, "white")

  def draw_move(self, to_cell, undo=False):
    line_color = "black" if undo else "red"

    half_of_length = abs(self._x2 - self._x1) // 2
    x1, y1 = self._x1 + half_of_length, self._y1 + half_of_length 

    half_of_length2 = abs(to_cell._x2 - to_cell._x1) // 2
    x2, y2 = to_cell._x1 + half_of_length2, to_cell._y1 + half_of_length2

    line = Line(Point(x1, y1), Point(x2, y2))
    self._win.draw_line(line, line_color)
