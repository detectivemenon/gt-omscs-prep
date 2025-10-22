# Minimal A* scaffold (fill in for practice)
from heapq import heappush, heappop

def a_star(start, goal_test, neighbors, h):
    frontier = []
    heappush(frontier, (h(start), 0, start, None))
    came_from = {}
    g = {start: 0}

    while frontier:
        f, g_cost, state, parent = heappop(frontier)
        if state not in came_from:
            came_from[state] = parent
            if goal_test(state):
                # Reconstruct path
                path = []
                s = state
                while s is not None:
                    path.append(s)
                    s = came_from[s]
                return list(reversed(path))
            for nxt, step_cost in neighbors(state):
                new_g = g_cost + step_cost
                if nxt not in g or new_g < g[nxt]:
                    g[nxt] = new_g
                    heappush(frontier, (new_g + h(nxt), new_g, nxt, state))
    return None