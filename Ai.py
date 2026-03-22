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
    heapq.heappush(frontier, (manhattan(start, goal), 0, start))
    came_from = {}
    visited = set()

    while frontier:
        f, g, current = heapq.heappop(frontier)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        if current in visited:
            continue
        visited.add(current)

        x, y = current
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#':
                next_state = (nx, ny)
                if next_state not in visited:
                    new_g = g + 1
                    new_f = new_g + manhattan(next_state, goal)
                    heapq.heappush(frontier, (new_f, new_g, next_state))
                    came_from[next_state] = current

    return None

print("Path found by A*:", astar())
