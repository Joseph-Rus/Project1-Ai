# Pacman Search Project - Running Instructions

This project has been updated to run with **Python 3** on macOS 15+.

## Prerequisites

- Python 3 (already installed on your Mac)
- No additional packages required!

## Quick Start

### 1. Basic Pacman Game (Manual Control)
```bash
python3 pacman.py
```
Use arrow keys or WASD to control Pacman.

### 2. Test Different Maze Layouts
```bash
# Small maze
python3 pacman.py -l tinyMaze

# Medium maze (default)
python3 pacman.py -l mediumMaze

# Large maze
python3 pacman.py -l bigMaze
```

### 3. Test Search Algorithms

The search algorithms need to be implemented in `search.py`. Currently they raise `NotImplementedError`.

Once implemented, you can test them:

```bash
# Test tiny maze with DFS (Depth First Search)
python3 pacman.py -l tinyMaze -p SearchAgent -a fn=depthFirstSearch

# Test with BFS (Breadth First Search)
python3 pacman.py -l mediumMaze -p SearchAgent -a fn=breadthFirstSearch

# Test with UCS (Uniform Cost Search)
python3 pacman.py -l mediumMaze -p SearchAgent -a fn=uniformCostSearch

# Test with A* Search
python3 pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
```

### 4. Run Autograder
```bash
# Test all questions
python3 autograder.py

# Test specific question
python3 autograder.py -q q1
```

### 5. Eight Puzzle
```bash
python3 eightpuzzle.py
```

## Common Command Options

- `-l LAYOUT` : Choose maze layout (tinyMaze, mediumMaze, bigMaze, etc.)
- `-p AGENT` : Choose pacman agent type (KeyboardAgent, SearchAgent, etc.)
- `-a OPTIONS` : Agent options (e.g., fn=bfs for search function)
- `-z ZOOM` : Zoom the display (0.5 = half size, 2 = double size)
- `--frameTime TIME` : Time between frames (lower = faster)
- `-n GAMES` : Number of games to play
- `-q` : Quiet mode (no graphics)
- `-t` : Text only display

## Example Commands from commands.txt

```bash
# Play with keyboard
python3 pacman.py

# Test the tinyMazeSearch function
python3 pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch

# Test BFS on medium maze
python3 pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

# Test corner problem
python3 pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

# Test A* with corners
python3 pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5

# Find closest dot
python3 pacman.py -l bigSearch -p ClosestDotSearchAgent -z .5
```

## Troubleshooting

1. **Graphics not working**: The code now works with Python 3's tkinter on macOS 15+

2. **Search algorithms not working**: You need to implement them in `search.py`:
   - `depthFirstSearch` (q1)
   - `breadthFirstSearch` (q2)
   - `uniformCostSearch` (q3)
   - `aStarSearch` (q4)
   
3. **"NotImplementedError"**: This means the search algorithm hasn't been implemented yet

4. **Slow performance**: Use `-z 0.5` to make display smaller and faster

## Implementation Status

Currently, the following need to be implemented in `search.py`:
- Line 75-95: `depthFirstSearch(problem)`
- Line 97-100: `breadthFirstSearch(problem)`
- Line 102-105: `uniformCostSearch(problem)`
- Line 107-110: `aStarSearch(problem, heuristic)`

The framework is ready - you just need to add the search algorithm implementations!