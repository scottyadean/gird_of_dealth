""" 

Unit Test for solver.py

PROBLEM:
In a 100 by 100 2-D grid world, you are given a starting point A on one side of the grid, and an
ending point B on the other side of the grid. Your objective is to get from point A to point B.
Each grid space can be in a state of [“Blank”, “Speeder”, “Lava”, “Mud”]. You start out with 200
points of health and 450 moves. Below is a mapping of how much your health and moves are
affected by landing on a grid space.

[
“Blank”: {“Health”: 0, “Moves”: -1},
“Speeder”: {“Health”: -5, “Moves”: 0},
“Lava”: {“Health”: -50, “Moves”: -10},
“Mud”: {“Health”: -10, “Moves”: -5},
]

"""
import json
import unittest
from grid_game import GridGame

class TestGameGridSolver(unittest.TestCase):
    """ Class for testing solver of 2d NxN grid game board.  """
    def test_can_load_sample_data(self):
        """
        can we load sample level data as json and that it is a medium difficulty grid
        """
        with open ('./tests/data/level.json', "r", encoding="utf-8") as json_data:
            # read the level from the file
            level = json.loads(json_data.read())
            level_types = {}
            # all we are doing here is counting if the blank squares
            # out ratio the (lava, mud, speeder) types making the puzzle easier to solve
            for row in level:
                for col in row:
                    if col['type'] not in level_types:
                        level_types[col['type']] = 0
                    level_types[col['type']] += 1

        # medium difficulty board should contain a lot of blanks
        self.assertGreater(level_types['Blank'], 5000)
        # very few lava cells
        self.assertLess(level_types['Lava'], 1500)
        # few mud cells
        self.assertLess(level_types['Mud'], 2000)
        # few speeder cells
        self.assertLess(level_types['Speeder'], 2000)


    def test_can_solve_medium_difficulty_board(self):
        """
        test can consistently solve medium difficulty board
        """
        with open ('./tests/data/level.json', "r", encoding="utf-8") as json_data:
            # parse the json level data
            level = json.loads(json_data.read())
            # start at 0 0 on the game board with 200 health and 450 moves
            game = GridGame("easy", level)
            game.DEBUG = True
            result = game.solver(0, 0, game.DEFAULT_HEALTH, game.DEFAULT_MOVES)
            # An easy board with more blanks cells then
            # trap cells (lava, mud, speeder) we sould see the following output
            health = result[0]
            self.assertEqual( health, 5 )
            moves = result[1]
            self.assertEqual( moves, 23 )


    def test_can_not_solve_imposible_board(self):
        """ 
        test cannot solve impossible grid with moves and health allotted 
        """
        game = GridGame("hard")
        game.DEBUG = True
        # start at 0 0 on the game board with 100 health and 100 moves
        result = game.solver(0, 0, 100, 100)
        self.assertIs(result, None)