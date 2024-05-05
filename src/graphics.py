from tkinter import Tk, BOTH, Canvas

class Point():
  def __init__(self, x, y):
    self.x = x
    self.y = y


class Line():
  def __init__(self, point_one, point_two):
    self.p1 = point_one
    self.p2 = point_two

  def draw(self, canvas, fill):
    canvas.create_line(
      self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill, width=2
    )


class Window():
  def __init__(self, width, height):
    self.__root = Tk()
    self.__root.title('Maze Solver')
    self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
    self.__canvas.pack(fill=BOTH, expand=1)
    self.__running = False
    self.__root.protocol("WM_DELETE_WINDOW", self.close)

  def draw_line(self, line, fill="black"):
    line.draw(self.__canvas, fill)

  def redraw(self):
    self.__root.update()
    self.__root.update_idletasks()

  def wait_for_close(self):
    self.__running = True
    while self.__running:
      self.redraw()

  def close(self):
    self.__running = False
