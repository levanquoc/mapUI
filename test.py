import collections
import numpy as np
def bfs(grid):
    start = (0, 0)
    queue = collections.deque([[start]])
    seen = set([start])
    width, height = len(grid[0]), len(grid)
    wall, clear, goal = 0, 1,9
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if grid[y][x] == goal:
            return path
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= x2 < width and 0 <= y2 < height and grid[y2][x2] != wall and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))

grid2 = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[9, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(type(grid2))
path = bfs(grid2)
print(type(grid2))
print(path)
print(len(path))
