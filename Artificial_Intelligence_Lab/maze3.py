from collections import deque

def bfs(maze, start, end):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    queue = deque([start])
    visited = {start}
    parent = {}  # To reconstruct the path

    while queue:
        current = queue.popleft()
        if current == end:
            # Reconstruct path from end to start
            path = []
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path  # Return the full path

        for direction in directions:
            next_cell = (current[0] + direction[0], current[1] + direction[1])
            if (0 <= next_cell[0] < len(maze) and
                    0 <= next_cell[1] < len(maze[0]) and
                    maze[next_cell[0]][next_cell[1]] != '#' and
                    next_cell not in visited):
                queue.append(next_cell)
                visited.add(next_cell)
                parent[next_cell] = current

    return None  # No path found

# Maze where '#' is a wall, 'S' is start, and 'E' is end
maze = [
    ['S', '.', '.', '#', '.', '.', '.'],
    ['.', '#', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.'],
    ['.', '.', '#', '#', '#', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '#', '.', '#', '.'],
    ['.', '.', '.', '.', '.', '.', 'E'],
]

start = (0, 0)
end = (6, 6)

# Run BFS to find the path
path = bfs(maze, start, end)

if path:
    print("Path found:")
    for step in path:
        print(step)
else:
    print("No path exists.")


