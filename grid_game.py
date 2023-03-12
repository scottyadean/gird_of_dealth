import random

class GridGame:
  """
    GridGame Problem Overview: 
    In a 100 by 100 2-D grid world, you are given a starting point A on one side of the grid, and an
    ending point B on the other side of the grid. Your objective is to get from point A to point B.
    Each grid space can be in a state of [“Blank”, “Speeder”, “Lava”, “Mud”]. You start out with 200
    points of health and 450 moves. Below is a mapping of how much your health and moves are
    affected by landing on a grid space.
  """

  BLANK = { "name": "Blank", "health": 0, "moves": -1 }
  SPEEDER = {"name": "Speeder", "health": -5, "moves": 0}
  LAVA = {"name": "Lava", "health": -50, "moves": -10}
  MUD = {"name": "Mud", "health": -10, "moves": -5}
  
  DEFAULT_HEALTH = 200
  DEFAULT_MOVES = 450

  DEBUG = False

  def __init__(self, difficulty:str="medium", custom_grid:list=None)->None:
    self.difficulty = difficulty
    self.grid = custom_grid if custom_grid is not None else self.make_grid(100)
    self.visited = self.set_visited(self.grid)

  def log(self, msg:str) -> None:
     """ if debug == True print debug messages """
     if self.DEBUG:
        print(msg)

  def dealth_message(self) -> str:
    """ return a message if we cant solve the map """
    size = len(self.grid)
    diff = self.difficulty
    return f"""Died trying all routes on a {size} x {size} grid on {diff} mode"""

  def success_message(self, res) -> str:
    """ return a win message """
    diff = self.difficulty
    return f""" We Won! I found the best route health: {res[0]}, moves: {res[1]}, on {diff} mode"""

  def set_visited(self, grid)->list:
     """ Set a multi dim array that matches the grid to track visited cells """
     return [[False] * len(grid[0]) for _ in range(len(grid))]

  def make_grid(self, grid_size: int = 100) -> dict:
      """ Return a NxN grid with random world types and meta data  """
      grid = []

      if self.difficulty == "easy":
        level = self.easy_game_board()
      elif self.difficulty == "medium":
         level = self.medium_game_board()
      else:
         level = self.hard_game_board()
      
      for _row in range(grid_size):
          temp = []
          for _col in range(grid_size):
              temp.append( level[random.randrange( 0, len(level))]  )
          grid.append(temp)
      return grid
  
  def set_board_types(self, types:list)->list:
    """ return an array of cell types """
    level = []
    self.log(f"buidling a board with these types: {types}")
    for _ in range(10):
      cell = types[random.randrange(0, len(types))]
      level.append({"type": cell["name"], "health": cell["health"], "moves": cell["moves"]})
    return level
 
  def easy_game_board(self) -> list:
    """ return a board high probability of blanks"""
    types = [self.BLANK,
            self.LAVA,
            self.BLANK,
            self.BLANK,
            self.BLANK,
            self.SPEEDER,
            self.BLANK,
            self.BLANK,
            self.BLANK,
            self.MUD]
    return self.set_board_types(types)

  def medium_game_board(self) -> list:
    """ return a board with more probability of blanks"""
    types = [self.BLANK,
            self.SPEEDER,
            self.BLANK,
            self.BLANK,
            self.LAVA,
            self.BLANK,
            self.MUD,
            self.BLANK]
    return self.set_board_types(types)

  def hard_game_board(self) -> list:
    """ return a board equal probability of blanks """
    types = [self.BLANK,
            self.SPEEDER,
            self.LAVA,
            self.MUD]
    return self.set_board_types(types)
  

  def check_current_health(self, health:int, moves:int, cell:dict)->bool:
      """ If we dont have enough health to go on short-circuit the loop """
     
      # lava requires 50 health
      if cell["type"] == self.LAVA["name"] and health < self.LAVA["health"]:
          self.log("lava killed me")
          return False
      
      # mud requires 10 health
      if cell["type"] == self.MUD["name"] and health < self.MUD["health"]:
          self.log("mud killed me")
          return False

      # speeder requires 5 health
      if cell["type"] == self.SPEEDER["name"] and health < self.SPEEDER["health"]:
          self.log("speeder killed me")
          return False
      
      # No health no more moves
      if health + cell["health"] <= 0 or moves + cell["moves"] <= 0:
          self.log("trying new route")
          self.log(f"ran out of health: {health} or moves: {moves}")
          self.log(f"last cell: {cell}" )
          return False
      
      self.log(f"Still Alive: health: {health} | moves: {moves} ")
      return True
     

  def solver(self, x:int=0, y:int=0, health:int=0, moves:int=0)-> tuple:
      """ iterate over the grid, for each movement until the end cell is reached """
      
      # end of board exit
      if x < 0 or y < 0 or x >= len(self.grid[0]) or y >= len(self.grid):
          self.log("done parsing board!")
          return None
      
      # make this cell as visited
      if self.visited[y][x]:
          return None
      
      # get the current cell
      cell = self.grid[y][x]
      
      # make sure we have enough health to continue the path
      if self.check_current_health(health, moves, cell) is False:
         return None

      #set this cell to visited
      self.visited[y][x] = True
      
      # if row teversal complete
      if x == len(self.grid[0]) - 1 and y == (len(self.grid) - 1):
          return (health + cell["health"], moves + cell["moves"])
      
      # move across the board for each cell dimension
      results = [
          # right
          self.solver(x + 1, y, health + cell["health"], moves + cell["moves"]),
          # down
          self.solver(x, y + 1, health + cell["health"], moves + cell["moves"]),
          # left
          self.solver(x - 1, y, health + cell["health"], moves + cell["moves"]),
          # up
          self.solver(x, y - 1, health + cell["health"], moves + cell["moves"])
      ]


      self.log(f"x: {x}, y: {y} ")

      # Remove none values and return the best possible score
      res = max(filter(lambda x: x is not None, results), default=None)
      self.log(res)
      return res