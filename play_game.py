""" Sets up a grid and solves it with the built in class solver. 
    Run Cmd: python play_game.py
"""
from grid_game import GridGame

# GridGame class builds a 100x100 game grid
grid_game = GridGame("easy") # available modes: (easy, medium, hard)

# to view debug output set debug to true
grid_game.DEBUG = False

# use the solver to walk the grid
result = grid_game.solver(0, 0, grid_game.DEFAULT_HEALTH, grid_game.DEFAULT_MOVES)

# check if the solver found the lowest route.
if result is not None:
   print(grid_game.success_message(result))
else:
   print(grid_game.dealth_message())