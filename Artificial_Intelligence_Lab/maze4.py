def dfs_with_path(maze, start, end):
    stack = [start]  # Initialize stack with start position
    visited = set()  # Track visited positions
    parent = {}      # Map to reconstruct the path

    while stack:
        position = stack.pop()
        x, y = position

        if position == end:
            # Reconstruct path from end to start using parent map
            path = []
            while position != start:
                path.append(position)
                position = parent[position]
            path.append(start)
            path.reverse()
            return True, path

        visited.add((x, y))

        # Explore neighbors (up, down, left, right)
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_x, new_y = x + dx, y + dy
            neighbor = (new_x, new_y)

            if (0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and
                    maze[new_x][new_y] == 0 and neighbor not in visited):
                stack.append(neighbor)
                parent[neighbor] = position  # Set parent for path reconstruction

    return False, []  # No path found

maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

found, path = dfs_with_path(maze, start, end)
print("Path found:", found)
print("Path:", path)

