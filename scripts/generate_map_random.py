"""
Random maze generator for development use.
Creates a simple grid maze using DFS backtracking.
"""

import random

W = 21
H = 17

def generate_maze():
    maze = [[1 for _ in range(W)] for _ in range(H)]
    stack = [(1,1)]
    maze[1][1] = 0

    while stack:
        x,y = stack[-1]
        dirs = [(2,0),(-2,0),(0,2),(0,-2)]
        random.shuffle(dirs)

        carved = False
        for dx,dy in dirs:
            nx, ny = x+dx, y+dy
            if 1 <= nx < W-1 and 1 <= ny < H-1 and maze[ny][nx] == 1:
                maze[ny][nx] = 0
                maze[y + dy//2][x + dx//2] = 0
                stack.append((nx,ny))
                carved = True
                break

        if not carved:
            stack.pop()

    return maze

if __name__ == "__main__":
    m = generate_maze()
    for row in m:
        print("".join(str(c) for c in row))
