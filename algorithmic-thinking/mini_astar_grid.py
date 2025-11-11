from heapq import heappush, heappop
Grid = list[list[int]]          # 0 = free, 1 = wall
Point = tuple[int, int]         # (row, col)

def neighbors(p: Point, grid: Grid) -> list[Point]:
    r, c = p
    H, W = len(grid), len(grid[0])
    cand = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
    out = []
    for rr, cc in cand:
        if 0 <= rr < H and 0 <= cc < W and grid[rr][cc] == 0:
            out.append((rr, cc))
    return out

def heuristic(a: Point, b: Point) -> int:
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def reconstruct_path(came_from: dict[Point, Point], start: Point, goal: Point) -> list[Point]:
    cur = goal
    path = [cur]
    while cur != start:
        cur = came_from[cur]
        path.append(cur)
    path.reverse()
    return path

def astar(grid: Grid, start: Point, goal: Point) -> list[Point] | None:
    frontier: list[tuple[int, Point]] = []
    heappush(frontier, (0, start))

    came_from: dict[Point, Point] = {}
    g_cost: dict[Point, int] = {start: 0}

    while frontier:
        _, current = heappop(frontier)
        if current == goal:
            return reconstruct_path(came_from, start, goal)

        for nxt in neighbors(current, grid):
            tentative = g_cost[current] + 1  # every move costs 1
            if nxt not in g_cost or tentative < g_cost[nxt]:
                g_cost[nxt] = tentative
                f = tentative + heuristic(nxt, goal)
                heappush(frontier, (f, nxt))
                came_from[nxt] = current

    return None  # no path

if __name__ == "__main__":
    # 0 = free, 1 = wall
    grid = [
        [0,0,0,0,0],
        [0,1,1,1,0],
        [0,0,0,1,0],
        [1,1,0,0,0],
        [0,0,0,1,0],
    ]
    start = (0, 0)
    goal  = (4, 4)

    path = astar(grid, start, goal)
    print("Path:", path)
    print("Length:", len(path) if path else None)

    # quick sanity check
    assert path is not None and path[0] == start and path[-1] == goal