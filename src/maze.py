import random
from time import sleep
from .cell import Cell

class Maze():
  def __init__(self, coords, grid, cell_size, win=None, seed=None):
    self._win = win

    self._x1, self._y1 = coords
    self.num_cols, self.num_rows = grid
    self.cell_size_x, self.cell_size_y = cell_size

    self._cells = [[Cell(self._win) for _ in range(self.num_rows)] for _ in range(self.num_cols)]

    if seed:
      random.seed(seed)

    self._create_cells();
    self._break_entrance_and_exit()
    self._break_walls_r(0, 0)
    self._reset_cells_visited()

  def solve(self):
    return self._solve_r(0, 0)

  def _solve_r(self, i, j):
    self.__animate()

    current_cell = self._cells[i][j]
    current_cell.visited = True

    last_cell = self._cells[-1][-1]

    if current_cell == last_cell:
      return True

    moves = [(i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1)]

    for x, y in moves:
      possible_cell = self._get_cell(x, y)

      if possible_cell and not possible_cell.visited:
          if x < i and not current_cell.has_left_wall:
            current_cell.draw_move(possible_cell)
            if self._solve_r(x, y):
              return True
            current_cell.draw_move(possible_cell, undo=True)

          if x > i and not current_cell.has_right_wall:
            current_cell.draw_move(possible_cell)
            if self._solve_r(x, y):
              return True
            current_cell.draw_move(possible_cell, undo=True)

          if y < j and not current_cell.has_top_wall:
            current_cell.draw_move(possible_cell)
            if self._solve_r(x, y):
              return True
            current_cell.draw_move(possible_cell, undo=True)

          if y > j and not current_cell.has_bottom_wall:
            current_cell.draw_move(possible_cell)
            if self._solve_r(x, y):
              return True
            current_cell.draw_move(possible_cell, undo=True)

    
    return False


  def _create_cells(self):
    for i in range(self.num_rows):
      for j in range(self.num_cols):
        self.__draw_cell(i, j)
        self.__animate()

  def _break_entrance_and_exit(self):
    self._cells[0][0].has_top_wall = False
    self._cells[-1][-1].has_bottom_wall = False

    if self._win:
      self.__draw_cell(0, 0)
      self.__draw_cell(self.num_rows - 1, self.num_cols - 1)

  def _get_cell(self, i, j):
    try:
      return self._cells[i][j]
    except Exception:
      print("out of bounds")

  def _is_valid_cell(self, i, j, direction):
    directions = {
      "up": j > 0,
      "right": i <= self.num_cols - 1,
      "left": i > 0,
      "down": j <= self.num_rows - 1
    }

    return directions[direction]

  def _reset_cells_visited(self):
    for row in self._cells:
      for cell in row:
        cell.visited = False

  def _break_walls_r(self, i, j):
    current_cell = self._get_cell(i, j)
    current_cell.visited = True

    while True:
      to_visit = []

      left_coords = i - 1, j
      top_coords = i, j - 1
      right_coords = i + 1, j
      bottom_coords = i, j + 1

      if self._is_valid_cell(*top_coords, "up") and not self._get_cell(*top_coords).visited:
        to_visit.append(top_coords)

      if self._is_valid_cell(*left_coords, "left") and not self._get_cell(*left_coords).visited:
        to_visit.append(left_coords)

      if self._is_valid_cell(*bottom_coords, "down") and not self._get_cell(*bottom_coords).visited:
        to_visit.append(bottom_coords)

      if self._is_valid_cell(*right_coords, "right") and not self._get_cell(*right_coords).visited:
        to_visit.append(right_coords)

      if not len(to_visit):
        if self._win:
          self.__draw_cell(i, j)
        return

      random_coords_idx = random.randrange(0, len(to_visit))

      to = to_visit[random_coords_idx]
      to_visit.remove(to)

      if to == top_coords:
        current_cell.has_top_wall = False
        self._get_cell(*top_coords).has_bottom_wall = False
        if self._win:
          self.__draw_cell(*top_coords)
          self.__draw_cell(i, j)
      if to == bottom_coords:
        current_cell.has_bottom_wall = False
        self._get_cell(*bottom_coords).has_top_wall = False
        if self._win:
          self.__draw_cell(*bottom_coords)
          self.__draw_cell(i, j)
      if to == right_coords:
        current_cell.has_right_wall = False
        self._get_cell(*right_coords).has_left_wall = False
        if self._win:
          self.__draw_cell(*right_coords)
          self.__draw_cell(i, j)
      if to == left_coords:
        current_cell.has_left_wall = False
        self._get_cell(*left_coords).has_right_wall = False
        if self._win:
          self.__draw_cell(*left_coords)
          self.__draw_cell(i, j)

      self._break_walls_r(*to)

  def __draw_cell(self, i, j):
    distance_x = i * self.cell_size_x
    distance_y = j * self.cell_size_y
    x1 = distance_x + self._x1
    y1 = distance_y + self._y1
    x2 = x1 + self.cell_size_x
    y2 = y1 + self.cell_size_y

    self._cells[i][j].draw(x1, y1, x2, y2)
  
  def __animate(self):
    self._win.redraw()
    sleep(0.1)
