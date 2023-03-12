import random
import json 



#     health = 100
#     moves  = 100

#      0         1       2 
#   0 [m,0,0] [l,1,1] [b,0,2]
#   1 [s,1,0] [b,1,1] [m,1,2]
#   2 [m,2,0] [m,2,1] [b,2,2]
   
#   path1 (0 ,0) ( 1, 0 ) ( 2, 0 ) == h = 75 | m = 85
#   ** path2 (0 ,2) ( 1, 1 ) ( 2, 2 ) == h = 100 | m = 97
#   path3 (0 ,0) ( 1, 0 ) ( 2, 0 ) == h = 75 | m = 85


BLANK = {"h": 0, "m": -1, 'n': "Blank"}
SPEEDER = {"h": -5, "m": 0, 'n': "Speeder"}
LAVA = {"h": -50, "m": -10, 'n': "Lava"}
MUD = {"h": -10, "m": -5, 'n': "Mud"}


PATH = []

def grid_game(x, y, health, moves, visited, level):
    """ get  """
    
    # end of board
    if x < 0 or y < 0 or x >= len(level[0]) or y >= len(level):
        return None
    
    if visited[y][x]:
        return None

    cell = level[y][x]

    # lava requires 50 health
    if cell["type"] == LAVA["n"] and health < LAVA["h"]:
        print("lava kill me")
        return None
    
    # mud requires 10 health
    if cell["type"] == MUD["n"] and health < MUD["h"]:
        print("mud kill me")
        return None

    # speeder requires 5 health
    if cell["type"] == "Speeder" and health < SPEEDER["h"]:
        print("speeder kill me")
        return None

    # No health no more moves
    if health + cell["health"] <= 0 or moves + cell["moves"] <= 0:
        print("ran out of health:", cell )
        return None
    
    #set this cell to visited 
    visited[y][x] = True
    
    # grid teversal complete
    if x == len(level[0]) - 1 and y == len(level) - 1:
        return (health + cell["health"], moves + cell["moves"])
    
    # Try moving right, down, left, up
    results = [
        # right
        grid_game(x + 1, y, health + cell["health"], moves + cell["moves"], visited, level),
        # down
        grid_game(x, y + 1, health + cell["health"], moves + cell["moves"], visited, level),
        # left
        grid_game(x - 1, y, health + cell["health"], moves + cell["moves"], visited, level),
        # up
        grid_game(x, y - 1, health + cell["health"], moves + cell["moves"], visited, level)
    ]

    print(x,y )
    return min(filter(lambda x: x is not None, results), default=None)





LEVEL_TYPES = [ 
               {"type": BLANK["n"], "health": BLANK["h"], "moves": BLANK["m"]},   
               {"type": SPEEDER["n"], "health": SPEEDER["h"], "moves": SPEEDER["m"]},
               {"type": BLANK["n"], "health": BLANK["h"], "moves": BLANK["m"]},
               {"type": BLANK["n"], "health": BLANK["h"], "moves": BLANK["m"]},
               {"type": LAVA["n"], "health": LAVA["h"], "moves": LAVA["m"]},
               {"type": BLANK["n"], "health": BLANK["h"], "moves": BLANK["m"]},
               {"type": MUD["n"], "health": MUD["h"], "moves": MUD["m"]},
               {"type": BLANK["n"], "health": BLANK["h"], "moves": BLANK["m"]},]

def make_grid(grid_size: int = 100) -> dict:
    """ Return a 100x100 grid with random world types  """
    grid = []
    for _row in range(grid_size):
        temp = []
        for _col in range(grid_size):
            if _col > 0:
                print( temp[_col - 1]['type']  )
            temp.append(  LEVEL_TYPES[random.randrange( 0, len(LEVEL_TYPES))]  )

        grid.append(temp)
    return grid


# if __name__ == "__main__":


#     LEVEL = make_grid(100)

#     # print(LEVEL)
#     # print(len(LEVEL))

#     f = open("level.json", "w")
#     f.write(json.dumps(LEVEL))
#     f.close()



#     _visited = [[False] * len(LEVEL[0]) for _ in range(len(LEVEL))]

#     print(len(_visited))
#     result = grid_game(0, 0, 200, 450, _visited, LEVEL)
#     if result is None:
#         print("No path found.")
#     else:
#         print("Shortest path found", "Health", result[0], "Moves", result[1])
