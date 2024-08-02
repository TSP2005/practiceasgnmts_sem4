import random
import math

distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
num_cities = len(distances)


def tour_distance(tour):
    total_distance = 0
    for i in range(num_cities):
        total_distance += distances[tour[i % num_cities]][tour[(i + 1) % num_cities]]
    return total_distance


def simulated_annealing(initial_solution, initial_temp, cooling_rate, num_iterations):
    current_solution = initial_solution
    current_cost = tour_distance(current_solution)
    best_solution = current_solution
    best_cost = current_cost
    temp = initial_temp

    for i in range(num_iterations):
        new_solution = current_solution[:]
        rand_index1, rand_index2 = random.sample(range(num_cities), 2)
        new_solution[rand_index1], new_solution[rand_index2] = new_solution[rand_index2], new_solution[rand_index1]

        new_cost = tour_distance(new_solution)
        delta_cost = new_cost - current_cost

        if delta_cost < 0 or random.random() < math.exp(-delta_cost / temp):
            current_solution = new_solution
            current_cost = new_cost

            if current_cost < best_cost:
                best_solution = current_solution
                best_cost = current_cost

        temp *= cooling_rate

    return best_solution, best_cost


initial_solution = list(range(num_cities))
initial_temp = 1000
cooling_rate = 0.99
num_iterations = 10000

best_solution, best_cost = simulated_annealing(initial_solution, initial_temp, cooling_rate, num_iterations)
print("Best Tour:", best_solution)
print("Best Cost:", best_cost)
