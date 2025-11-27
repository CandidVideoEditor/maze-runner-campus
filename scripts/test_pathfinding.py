"""
Test BFS / A* pathfinding on ASCII maps.
"""

from game.pathfinding.bfs import bfs

sample_map = [
    "11111",
    "10001",
    "10101",
    "10001",
    "11111",
]

def neighbors(x,y):
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx,ny = x+dx,y+dy
        if sample_map[ny][nx] == "0":
            yield (nx,ny)

if __name__ == "__main__":
    path = bfs((1,1),(3,3),neighbors)
    print("Path:", path)
