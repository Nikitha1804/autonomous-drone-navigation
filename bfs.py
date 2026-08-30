from collections import deque


def bfs(grid, start, goal):
    """Find the shortest collision-free path using BFS."""

    queue = deque([start])
    came_from = {start: None}

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    while queue:
        current = queue.popleft()

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = came_from[current]

            return path[::-1]

        row, col = current

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if (
                0 <= new_row < len(grid)
                and 0 <= new_col < len(grid[0])
                and grid[new_row][new_col] == 0
            ):
                neighbor = (new_row, new_col)

                if neighbor not in came_from:
                    came_from[neighbor] = current
                    queue.append(neighbor)

    return []
