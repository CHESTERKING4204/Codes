import random
import math

def evaluate_solution(solution, formula):
    clauses_satisfied = 0
    for clause in formula:
        if clause[0][0] == '~':
            var1 = not solution[ord(clause[0][1]) - ord('a')]
        else:
            var1 = solution[ord(clause[0]) - ord('a')]
        if clause[1][0] == '~':
            var2 = not solution[ord(clause[1][1]) - ord('a')]
        else:
            var2 = solution[ord(clause[1]) - ord('a')]
        if var1 or var2:
            clauses_satisfied += 1
    return clauses_satisfied

def generate_neighbor_solution(solution):
    index = random.randint(0, len(solution) - 1)
    new_solution = solution[:]
    new_solution[index] = not new_solution[index]
    return new_solution

def probability(delta_e, temperature):
    if temperature == 0:
        return 0
    else:
        return math.exp(delta_e / temperature)

def simulated_annealing(formula, initial_solution, T, cooling_rate, random_numbers):
    current_solution = initial_solution
    current_energy = evaluate_solution(current_solution, formula)
    best_solution = current_solution
    best_energy = current_energy

    for iteration in range(1, 101):  # Number of iterations
        T = max(T - cooling_rate, 0)

        new_solution = generate_neighbor_solution(current_solution)
        new_energy = evaluate_solution(new_solution, formula)

        delta_e = new_energy - current_energy

        if delta_e > 0:
            current_solution = new_solution
            current_energy = new_energy
            if current_energy > best_energy:
                best_solution = current_solution
                best_energy = current_energy
        else:
            if probability(delta_e, T) > random_numbers[iteration % 3]:
                current_solution = new_solution
                current_energy = new_energy

    return best_solution, best_energy

formula = [("~a", "d"), ("c", "b"), ("~c", "~d"), ("~d", "~b"), ("~a", "~d")]
initial_solution = [1, 1, 1, 1]
T = 500
cooling_rate = 50
random_numbers = [0.655, 0.254, 0.432]

best_solution, best_energy = simulated_annealing(formula, initial_solution, T, cooling_rate, random_numbers)
print(f"Best Solution: {best_solution}")
print(f"Number of Clauses Satisfied: {best_energy}")
