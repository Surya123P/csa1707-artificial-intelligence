import heapq

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def a_star(start, goal, heuristic_func):
    open_set = [Node(start, None, 0, heuristic_func(start))]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal:
            path = []
            while current_node:
                path.insert(0, current_node.state)
                current_node = current_node.parent
            return path

        closed_set.add(current_node.state)

        for neighbor in get_neighbors(current_node.state):
            if neighbor not in closed_set:
                new_cost = current_node.cost + 1
                new_heuristic = heuristic_func(neighbor)
                new_node = Node(neighbor, current_node, new_cost, new_heuristic)

                if any(node.cost + node.heuristic < new_node.cost + new_node.heuristic for node in open_set):
                    continue

                heapq.heappush(open_set, new_node)

    return None

def heuristic(state):
    goal = (2, 2)
    return ((state[0] - goal[0])**2 + (state[1] - goal[1])**2)**0.5

def get_neighbors(state):
    x, y = state
    neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    return [(i, j) for i, j in neighbors if 0 <= i < 3 and 0 <= j < 3]  # Adjust this condition based on your problem

if __name__ == "__main__":
    start_state = (0, 0)
    goal_state = (2, 2)

    path = a_star(start_state, goal_state, heuristic)

    if path:
        print("Path found:", path)
    else:
        print("No path found.")
