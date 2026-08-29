import heapq


def heuristic(a, b):
    """Calculate Manhattan distance between two grid cells."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_neighbors(grid, node):
    """Return valid neighboring cells."""
    rows = len(grid)
    cols = len(grid[0])

    row, col = node

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    neighbors = []

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if (
            0 <= new_row < rows
            and 0 <= new_col < cols
            and grid[new_row][new_col] == 0
        ):
            neighbors.append((new_row, new_col))

    return neighbors


def astar(grid, start, goal):
    """Find the shortest collision-free path using A*."""

    open_set = []

    heapq.heappush(
        open_set,
        (0, start)
    )

    came_from = {}

    g_score = {
        start: 0
    }

    while open_set:

        _, current = heapq.heappop(open_set)

        if current == goal:

            path = []

            while current in came_from:
                path.append(current)
                current = came_from[current]

            path.append(start)

            return path[::-1]

        for neighbor in get_neighbors(grid, current):

            tentative_g = g_score[current] + 1

            if (
                neighbor not in g_score
                or tentative_g < g_score[neighbor]
            ):

                came_from[neighbor] = current
                g_score[neighbor] = tentative_g

                f_score = (
                    tentative_g
                    + heuristic(neighbor, goal)
                )

                heapq.heappush(
                    open_set,
                    (f_score, neighbor)
                )

    return []
