import random

items = {'A': {'weight': 45, 'value': 3},
         'B': {'weight': 40, 'value': 5},
         'C': {'weight': 50, 'value': 8},
         'D': {'weight': 90, 'value': 10}}

population_size = 4
max_capacity = 100
mutation_order = ['D', 'C', 'B', 'A']

initial_population = ['1111', '1000', '1010', '1001']

def calculate_fitness(individual):
    total_weight = sum(items[item]['weight'] for bit, item in zip(individual, items.keys()) if bit == '1')
    total_value = sum(items[item]['value'] for bit, item in zip(individual, items.keys()) if bit == '1')
    if total_weight <= max_capacity:
        return total_value
    else:
        return 0

def one_point_crossover(parent1, parent2):
    crossover_point = len(parent1) // 2
    offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
    offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    return offspring1, offspring2

def mutate(individual):
    mutated_index = mutation_order.pop(0)
    mutation_order.append(mutated_index)
    index = list(items.keys()).index(mutated_index)
    individual = list(individual)
    individual[index] = '1' if individual[index] == '0' else '0'
    return ''.join(individual)

def select_fittest(population):
    sorted_population = sorted(population, key=calculate_fitness, reverse=True)
    return sorted_population[:2]

def genetic_algorithm(population):
    for _ in range(10):  
        selected_individuals = select_fittest(population)
        if len(selected_individuals) >= 4:
            offspring1, offspring2 = one_point_crossover(selected_individuals[2], selected_individuals[3])
            offspring1 = mutate(offspring1)
            new_population = selected_individuals[:2] + [offspring1, offspring2]
            population = new_population
    return population

final_population = genetic_algorithm(initial_population)

print("Final Population after 10 iterations:")
for individual in final_population:
    print(individual, "Fitness:", calculate_fitness(individual))
