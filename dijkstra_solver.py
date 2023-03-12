""" 

https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

"""
import random
from heapq import * 

from colorama import init as colorama_init
from colorama import Fore
from colorama import Style


class GridGame:

    """
        GridGame Problem Overview: 
        In a 100 by 100 2-D grid world, you are given a starting point A on one side of the grid, and an
        ending point B on the other side of the grid. Your objective is to get from point A to point B.
        Each grid space can be in a state of [“Blank”, “Speeder”, “Lava”, “Mud”]. You start out with 200
        points of health and 450 moves. Below is a mapping of how much your health and moves are
        affected by landing on a grid space.
    """
    
    DEBUG=False
    
    def __init__(self):
        """ set up the grid """
        self.board=None
        self.moves = {"*":-1, "S": 0, "L": -10, "M": -5}
        self.health = {"*": 0, "S": -5, "L": -50, "M": -10}
    
    def log(self,msg:str)->None:
        """ Log a message """
        if self.DEBUG:
            print(msg)

    def make_grid(self, n:int=100, m:int=100)->None:
        """ generate board """
        board_char = [*"************LSM"]
        self.board = [["*"] * n for _ in range(m)]
        for i in range(n): 
            for j in range(m): 
                self.board[i][j] = random.choice(board_char)
                

    def print_grid(self):
        """ Display the nxn grid"""
        n_rows = len(self.board)
        n_cols = len(self.board[0])
        for i in range(n_rows): 
            for j in range(n_cols): 
                print(" " + self.board[i][j] + " ",end='')
            print()
        print()
        
        
    def find_shortest_path(self, x1, y1, x2, y2, moves, health): 
        """ Needs to check all paths not sortest"""
        
        def is_safe(x,y):
            if x < 0: return False 
            if y < 0: return False 
            if x >= len(self.board): return False 
            if y >= len(self.board[0]): return False 
            return True 
        
        max_heap = [(-(moves + self.moves[self.board[x1][y1]]),
                     -(health + self.health[self.board[x1][y1]]),
                     x1,
                     x1, 
                    [])]
        
        visited = set()
        
        while (x1 != x2 or y1 != y2) and max_heap: 
            curr_min = heappop(max_heap) 
            m,h,x1,y1,p = -curr_min[0], -curr_min[1], curr_min[2], curr_min[3], curr_min[4]
            if (x1, y1) not in visited: 
                visited.add((x1, y1))
                next_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                p = list(p)
                p.append((x1,y1))
                for next_move in next_moves:
                    i, j = next_move
                    if is_safe(x1+i, y1+j): 
                        heappush(max_heap,
                                 (-(m + self.moves[self.board[x1+i][y1+j]]), 
                                  -(h + self.health[self.board[x1+i][y1+j]]), 
                                  x1+i, y1+j, 
                                 p))
        
        n_rows = len(self.board)
        n_cols = len(self.board[0])
        path = [[False] * n_cols for _ in range(n_rows)]
        
        for ancestor in p: 
            x,y = ancestor[0], ancestor[1]
            path[x][y] = True
        
        for i in range(n_rows):
            for j in range(n_cols): 
                ch = "*" if path[i][j] else "."
                if ch == "*": 
                    print(f" {Style.DIM}{Fore.GREEN}{self.board[i][j]}{Style.RESET_ALL} ", end='')
                else:
                    print(f" {self.board[i][j]} ", end='')
            print()
            
        print()
        print("You Did It!")
        print(f"[moves]: {m}")
        print(f"[health]: {h}")
        print(f"path: {p}")

if __name__ == "__main__":
    test = GridGame()
    test.make_grid(32,32)
    test.print_grid()
    test.find_shortest_path(0,0,32,32,450,200) 