# Simple A* implementation for grid graphs.
import heapq

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(start, goal, neighbors_fn, cost_fn=None):
    """Return path list from start (excluded) to goal (included)."""
    if start == goal:
        return []
    if cost_fn is None:
        cost_fn = lambda a, b: 1
    open_heap = []
    heapq.heappush(open_heap, (heuristic(start, goal), 0, start))
    came_from = {start: None}
    gscore = {start: 0}
    while open_heap:
        _, cur_g, current = heapq.heappop(open_heap)
        if current == goal:
            break
        for nb in neighbors_fn(*current):
            tentative_g = gscore[current] + cost_fn(current, nb)
            if nb not in gscore or tentative_g < gscore[nb]:
                gscore[nb] = tentative_g
                f = tentative_g + heuristic(nb, goal)
                heapq.heappush(open_heap, (f, tentative_g, nb))
                came_from[nb] = current
    if goal not in came_from:
        return []
    path = []
    cur = goal
    while cur != start:
        path.append(cur)
        cur = came_from[cur]
    path.reverse()
    return path
