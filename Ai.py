import heapq

grid = [
    ['S', '.', '.', '.'],
    ['#', '#', '.', '#'],
    ['.', '.', '.', 'G']
]

rows, cols = len(grid), len(grid[0])

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 'S':
            start = (i, j)
        if grid[i][j] == 'G':
            goal = (i, j)

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar():
    frontier = []
    heapq.heappush(frontier, (0, start))

    came_from = {}
    g_score = {start: 0}

    while frontier:
        current_f, current = heapq.heappop(frontier)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        x, y = current

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#':
                neighbor = (nx, ny)
                tentative_g = g_score[current] + 1

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f = tentative_g + manhattan(neighbor, goal)
                    heapq.heappush(frontier, (f, neighbor))

    return None

path = astar()
print("Path found by A*:", path)

def print_grid_with_path(path):
    display = [row[:] for row in grid]

    for x, y in path:
        if display[x][y] not in ['S', 'G']:
            display[x][y] = '*'

    for row in display:
        print(' '.join(row))

print("\nGrid with path:")
print_grid_with_path(path)
