import random

items = {'A': {'weight': 2, 'value': 3},
         'B': {'weight': 3, 'value': 5},
         'C': {'weight': 4, 'value': 7},
         'D': {'weight': 5, 'value': 9}}

population_size = 4
max_weight = 9
mutation_order = ['C', 'A', 'D', 'B']

initial_population = ['1111', '1000', '1010', '1001']

def calculate_fitness(individual):
    total_weight = sum(items[item]['weight'] for bit, item in zip(individual, items.keys()) if bit == '1')
    total_value = sum(items[item]['value'] for bit, item in zip(individual, items.keys()) if bit == '1')
    if total_weight <= max_weight:
        return total_value, total_weight
    else:
        return 0, 0

def one_point_crossover(parent1, parent2):
    crossover_point = len(parent1) // 2
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    return offspring1, offspring2

def mutate(individual):
    mutated_index = mutation_order.pop(0)
    mutation_order.append(mutated_index)
    index = ord(mutated_index) - ord('A')
    individual = list(individual)
    individual[index] = '1' if individual[index] == '0' else '0'
    return ''.join(individual)

def select_fittest(population):
    sorted_population = sorted(population, key=lambda x: calculate_fitness(x)[0], reverse=True)
    return sorted_population[:2]

def genetic_algorithm(population):
    for _ in range(4):
        selected_individuals = select_fittest(population)
        if len(selected_individuals) >= 4:  # Check if selected_individuals has at least 4 elements
            offspring1, offspring2 = one_point_crossover(selected_individuals[2], selected_individuals[3])
            offspring1 = mutate(offspring1)
            new_population = selected_individuals[:2] + [offspring1, offspring2]
            population = new_population
    return population

final_population = genetic_algorithm(initial_population)

print("Final Population after four iterations:")
for individual in final_population:
    fitness, weight = calculate_fitness(individual)
    print(individual, "Fitness:", fitness, "Weight:", weight)
