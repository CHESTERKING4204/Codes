import copy
from heapq import heappush, heappop

initial = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
final = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

def calculate_heuristic(state, final_state):
    count = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] != final_state[i][j]:
                count += 1
    return count

class State:
    def __init__(self, state, cost, heuristic):
        self.state = state
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return self.cost + self.heuristic < other.cost + other.heuristic

def a_star(initial, final):
    row_offsets = [-1, 1, 0, 0]
    col_offsets = [0, 0, -1, 1]

    open_list = []
    closed_set = set()

    initial_cost = 0
    initial_heuristic = calculate_heuristic(initial, final)
    initial_state = State(initial, initial_cost, initial_heuristic)
    heappush(open_list, initial_state)

    while open_list:
        current_state = heappop(open_list)

        if current_state.state == final:
            return current_state

        closed_set.add(tuple(map(tuple, current_state.state)))

        for i in range(len(current_state.state)):
            for j in range(len(current_state.state[0])):
                if current_state.state[i][j] == 0:
                    for k in range(4):
                        new_i = i + row_offsets[k]
                        new_j = j + col_offsets[k]

                        if 0 <= new_i < len(current_state.state) and 0 <= new_j < len(current_state.state[0]):
                            new_state = copy.deepcopy(current_state.state)
                            new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]

                            if tuple(map(tuple, new_state)) not in closed_set:
                                new_cost = current_state.cost + 1
                                new_heuristic = calculate_heuristic(new_state, final)
                                new_state_obj = State(new_state, new_cost, new_heuristic)
                                heappush(open_list, new_state_obj)

    return None

result = a_star(initial, final)

if result:
    print("Goal state found!")
    print("Path to goal state:")
    for row in result.state:
        print(row)
else:
    print("Goal state not found.")
