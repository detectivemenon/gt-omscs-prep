"""
Uniform Cost Search (UCS) Scaffold
----------------------------------
Goal:
  - Implement a pathfinding algorithm that expands the least-cost node first.

Concepts:
  - Priority queue (min-heap)
  - Frontier vs. explored set
  - Cumulative path cost (g)
"""

from heapq import heappush, heappop

def uniform_cost_search(start, goal_test, neighbors):
    """
    Parameters:
        start        – the initial state
        goal_test    – function(state) → bool, returns True when goal found
        neighbors    – function(state) → list of (neighbor, cost)

    Returns:
        path (list): the least-cost path from start to goal, if one exists
    """
    frontier = []
    heappush(frontier, (0, start, None))  # (cumulative cost, state, parent)
    came_from = {}
    cost_so_far = {start: 0}

    while frontier:
        current_cost, state, parent = heappop(frontier)

        # Record parent (first time we see the node)
        if state not in came_from:
            came_from[state] = parent

            if goal_test(state):
                # Reconstruct path
                path = []
                while state is not None:
                    path.append(state)
                    state = came_from[state]
                return list(reversed(path))

            for neighbor, step_cost in neighbors(state):
                new_cost = current_cost + step_cost
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    heappush(frontier, (new_cost, neighbor, state))

    return None  # Goal not found


# Example usage (optional for testing)
if __name__ == "__main__":
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": []
    }

    def neighbors(n): return graph[n]
    def goal_test(n): return n == "D"

    path = uniform_cost_search("A", goal_test, neighbors)
    print("Least-cost path:", path)