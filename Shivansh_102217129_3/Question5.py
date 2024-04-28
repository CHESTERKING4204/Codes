def find_minimum_cost(graph, cost, goal, start):
    min_costs = [float('inf')] * len(goal)
    frontier = [(0, start)]
    visited = {}
    goal_count = 0

    while frontier:
        current_cost, current_node = frontier.pop(0)
        current_cost *= -1

        if current_node in goal:
            index = goal.index(current_node)
            if min_costs[index] == float('inf'):
                goal_count += 1
            if min_costs[index] > current_cost:
                min_costs[index] = current_cost
            frontier.pop(0) 
            if goal_count == len(goal):
                return min_costs

        if current_node not in visited:
            for neighbor in graph[current_node]:
                new_cost = (cost[(current_node, neighbor)] + current_cost) * -1
                frontier.append((new_cost, neighbor))

            visited[current_node] = 1

    return min_costs


graph = {
    0: [1, 3],
    3: [1, 6, 4],
    1: [6],
    4: [2, 5],
    2: [1],
    5: [2, 6],
    6: [4]
}

costs = {
    (0, 1): 2,
    (0, 3): 5,
    (1, 6): 1,
    (3, 1): 5,
    (3, 6): 6,
    (3, 4): 2,
    (2, 1): 4,
    (4, 2): 4,
    (4, 5): 3,
    (5, 2): 6,
    (5, 6): 3,
    (6, 4): 7
}

goal_nodes = [6]
start = 0
result = find_minimum_cost(graph, costs, goal_nodes, start)
print("Minimum cost from start to goal is =", result[0])
