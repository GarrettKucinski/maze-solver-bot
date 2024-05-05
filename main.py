from src.graphics import Window
from src.maze import Maze

def main():
  win = Window(1200, 1200)

  starting_coords = 10, 10
  grid = 20, 20 
  cell_size = 50, 50 

  maze = Maze(starting_coords, grid, cell_size, win, 10)

  print("maze created")
  is_solveable = maze.solve()
  if not is_solveable:
      print("maze can not be solved!")
  else:
      print("maze solved!")

  win.wait_for_close()

if __name__ == "__main__":
  main()
