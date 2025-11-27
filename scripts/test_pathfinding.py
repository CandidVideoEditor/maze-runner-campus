# Quick test script for BFS and A* pathfinding.
from game.pathfinding.bfs import bfs
from game.pathfinding.astar import astar

def neighbors(x,y):
    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
        yield (x+dx,y+dy)

print("BFS path:", bfs((0,0),(2,0), neighbors))
try:
    print("A* path:", astar((0,0),(2,0), neighbors))
except Exception as e:
    print("A* not configured for this neighbors API by default:", e)
