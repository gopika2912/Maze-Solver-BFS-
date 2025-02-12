from collections import deque

def bfs(maze, start, end):
    queue = deque([start])
    visited = set()
    visited.add(start)
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return True
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            new_pos = (x+dx, y+dy)
            if new_pos not in visited and maze.get(new_pos, 1) == 0:
                queue.append(new_pos)
                visited.add(new_pos)
    return False
