class WaterJugProblem:
    def __init__(self, jug1_capacity, jug2_capacity, target_amount):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target_amount = target_amount
        self.visited_states = set()

    def is_valid_state(self, state):
        jug1, jug2 = state
        return 0 <= jug1 <= self.jug1_capacity and 0 <= jug2 <= self.jug2_capacity

    def is_goal_state(self, state):
        return state[0] == self.target_amount or state[1] == self.target_amount

    def get_successors(self, state):
        jug1, jug2 = state
        successors = []
        successors.append((self.jug1_capacity, jug2))

        successors.append((jug1, self.jug2_capacity))

        successors.append((0, jug2))

        successors.append((jug1, 0))
        pour_amount = min(jug1, self.jug2_capacity - jug2)
        successors.append((jug1 - pour_amount, jug2 + pour_amount))
        pour_amount = min(jug2, self.jug1_capacity - jug1)
        successors.append((jug1 + pour_amount, jug2 - pour_amount))

        return [s for s in successors if self.is_valid_state(s)]

    def solve(self):
        initial_state = (0, 0)
        if self.is_goal_state(initial_state):
            return [initial_state]

        stack = [(initial_state, [])]

        while stack:
            current_state, path = stack.pop()

            if current_state in self.visited_states:
                continue

            self.visited_states.add(current_state)

            if self.is_goal_state(current_state):
                return path + [current_state]

            successors = self.get_successors(current_state)
            for successor in successors:
                stack.append((successor, path + [current_state]))

        return None

def print_solution(solution):
    for step in solution:
        print(f"Jug 1: {step[0]}, Jug 2: {step[1]}")

if __name__ == "__main__":
    jug_problem = WaterJugProblem(jug1_capacity=4, jug2_capacity=3, target_amount=2)
    solution = jug_problem.solve()

    if solution:
        print("Solution:")
        print_solution(solution)
    else:
        print("No solution found.")  
