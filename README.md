# Grid Of Dealth
The goal of this puzzle is to fill the grid with cells of type ("Blank", "Speeder", "Lava", "Mud") and traverse through without dying while finding the best route or determine if the grid is solvable.

### Python Verion:
3.9.10

### Set up
- git clone project
- cd grid_of_dealth
- pip install -r requirements.txt

### Running Tests
```
python  test_game.py
``` 
### Usage
```
python play_game.py
```
### Example Output
```
# unsolvable grid output: 
Died trying all routes on a 100 x 100 grid on easy mode
# success message output:
We Won! I found the best route health: 30, moves: 183, on easy mode
```
### Files
- `./play_game.py`: entry point
- `./grid_game.py`: grid class definition
- `./test_game.py`: test file

### Who to talk to
Scott Dean