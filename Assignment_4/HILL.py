import copy

n = 3

class State:
    def __init__(self, state, heuristic):
        self.state = state
        self.heuristic = heuristic

def calculateHeuristic(current, final) -> int:
    count = 0
    for i in range(n):
        for j in range(n):
            if current.state[i][j] != final[i][j]:
                count += 1
    return count

def generateNeighbors(current, final) -> list:
    neighbors = []
    x, y = 0, 0
    for i in range(n):
        for j in range(n):
            if current.state[i][j] == 0:
                x, y = i, j
                break

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            new_state = copy.deepcopy(current.state)
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            heuristic = calculateHeuristic(State(new_state, 0), final)
            neighbors.append(State(new_state, heuristic))

    return neighbors

def printMatrix(mat):
    for row in mat:
        print(row)

def hillClimbing(initial, final):
    current = State(initial, calculateHeuristic(State(initial, 0), final))

    while True:
        print("Current State:")
        printMatrix(current.state)
        print("Heuristic Value:", current.heuristic)

        if current.heuristic == 0:
            print("Goal state reached!")
            break

        neighbors = generateNeighbors(current, final)
        best_neighbor = min(neighbors, key=lambda x: x.heuristic)

        if best_neighbor.heuristic >= current.heuristic:
            print("Local Optimum Reached!")
            break

        current = best_neighbor

# Define initial state and final state
initial = [[2, 8, 3], [1, 5, 4], [7, 6, 0]]
final = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

# Solve the puzzle using Hill Climbing
hillClimbing(initial, final)
