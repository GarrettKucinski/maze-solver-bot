import unittest

from src.maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        starting_coords = 0, 0
        grid = 10, 12
        cell_size = 10, 10

        m1 = Maze(starting_coords, grid, cell_size)

        self.assertEqual(len(m1._cells), grid[0])
        self.assertEqual(len(m1._cells[0]), grid[1])

    def test_break_entrance_and_exit(self):
        starting_coords = 0, 0
        grid = 10, 12
        cell_size = 10, 10

        m1 = Maze(starting_coords, grid, cell_size)
        m1._break_entrance_and_exit()

        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[grid[0] - 1][grid[1] - 1].has_bottom_wall)

    def test_reset_cells_visited(self):
        starting_coords = 0, 0
        grid = 10, 12
        cell_size = 10, 10

        m1 = Maze(starting_coords, grid, cell_size)
        m1._break_walls_r(0, 0)
        m1._reset_cells_visited()

        for row in m1._cells:
            for cell in row:
                self.assertFalse(cell.visited)


if __name__ == "__main__":
  unittest.main()
