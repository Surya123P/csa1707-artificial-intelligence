import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = self.calculate_heuristic()

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def calculate_heuristic(self):
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        heuristic = 0
        for i in range(3):
            for j in range(3):
                if self.state[i][j] != 0:
                    goal_position = divmod(goal_state[i][j] - 1, 3)
                    current_position = divmod(self.state[i][j] - 1, 3)
                    heuristic += abs(goal_position[0] - current_position[0]) + abs(goal_position[1] - current_position[1])
        return heuristic

    def get_successors(self):
        successors = []
        zero_position = None
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    zero_position = (i, j)

        actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for action in actions:
            new_position = (zero_position[0] + action[0], zero_position[1] + action[1])
            if 0 <= new_position[0] < 3 and 0 <= new_position[1] < 3:
                new_state = [row.copy() for row in self.state]
                new_state[zero_position[0]][zero_position[1]] = self.state[new_position[0]][new_position[1]]
                new_state[new_position[0]][new_position[1]] = 0
                successors.append(PuzzleNode(new_state, parent=self, action=action, cost=self.cost + 1))

        return successors

def a_star_search(initial_state):
    initial_node = PuzzleNode(initial_state)
    open_set = [initial_node]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            return get_solution(current_node)

        closed_set.add(tuple(map(tuple, current_node.state)))

        successors = current_node.get_successors()
        for successor in successors:
            if tuple(map(tuple, successor.state)) not in closed_set:
                heapq.heappush(open_set, successor)

    return None

def get_solution(node):
    solution = []
    while node.parent is not None:
        solution.append((node.action, node.state))
        node = node.parent
    return solution[::-1]

def print_solution(solution):
    for step in solution:
        print("Move:", step[0])
        print_board(step[1])
        print("")

def print_board(state):
    for row in state:
        print(row)

if __name__ == "__main__":
    initial_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
    solution = a_star_search(initial_state)

    if solution:
        print_solution(solution)
    else:
        print("No solution found.")
