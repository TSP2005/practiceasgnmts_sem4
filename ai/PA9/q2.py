import numpy as np
import random
import math

# N students and k groups
N = 5
k = 2

# Mock student marks (replace with your own)
student_marks = np.array([80, 70, 85, 90, 75])

def objective_function(groups):
    """Calculate the diversity in groups."""
    mean_marks = [np.mean(group) for group in groups]
    diversity = np.std(mean_marks)
    return diversity

def simulated_annealing(initial_solution, temperature, cooling_rate, num_iterations):
    current_solution = initial_solution
    current_score = objective_function(current_solution)

    best_solution = current_solution
    best_score = current_score

    for i in range(num_iterations):
        new_solution = perturb_solution(current_solution)
        new_score = objective_function(new_solution)

        if new_score < current_score or random.random() < math.exp((current_score - new_score) / temperature):
            current_solution = new_solution
            current_score = new_score

        if new_score < best_score:
            best_solution = new_solution
            best_score = new_score

        temperature *= cooling_rate

    return best_solution, best_score

def perturb_solution(solution):
    """Swap two students between groups."""
    new_solution = solution.copy()
    i, j = random.sample(range(N), 2)
    new_solution[i], new_solution[j] = new_solution[j], new_solution[i]
    return new_solution

# Initialize with random grouping
initial_solution = np.random.choice(range(k), N)

# Set initial temperature and cooling rate
initial_temperature = 100.0
cooling_rate = 0.99
num_iterations = 1000

# Perform simulated annealing
best_solution, best_score = simulated_annealing(initial_solution, initial_temperature, cooling_rate, num_iterations)
print("Best grouping:", best_solution)
print("Diversity in best grouping:", best_score)
