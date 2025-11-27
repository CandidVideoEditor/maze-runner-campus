from collections import deque

def bfs(start, goal, neighbors_fn):
    """Return path list from start (excluded) to goal (included)."""
    if start == goal:
        return []
    q = deque([start])
    prev = {start: None}
    while q:
        cur = q.popleft()
        if cur == goal:
            break
        for n in neighbors_fn(*cur):
            if n not in prev:
                prev[n] = cur
                q.append(n)
    if goal not in prev:
        return []
    path = []
    cur = goal
    while cur != start:
        path.append(cur)
        cur = prev[cur]
    path.reverse()
    return path
