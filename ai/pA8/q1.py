import numpy as np
import random

N = 100
k = 5
max_marks = 100

student_marks = np.random.randint(0, max_marks, N)

num_particles = 30
max_iterations = 100
w = 0.5
c1 = 1
c2 = 2


def diversity(groups):
    total_diversity = 0
    for group in groups:
        if len(group) > 0:
            mean_mark = np.mean(group)
            if not np.isnan(mean_mark):  # Check for NaN result
                diversity = np.sum(np.abs(group - mean_mark))
                total_diversity += diversity
    return total_diversity


particles_position = np.random.randint(0, k, (num_particles, N))
particles_velocity = np.zeros((num_particles, N))
particles_best_position = particles_position.copy()
global_best_position = None
global_best_fitness = float('inf')

for _ in range(max_iterations):
    for i in range(num_particles):
        fitness = diversity([student_marks[particles_position[i] == j] for j in range(k)])
        if fitness < diversity([student_marks[particles_best_position[i] == j] for j in range(k)]):
            particles_best_position[i] = particles_position[i].copy()
        if fitness < global_best_fitness:
            global_best_position = particles_position[i].copy()
            global_best_fitness = fitness

    for i in range(num_particles):
        r1 = random.random()
        r2 = random.random()
        cognitive_velocity = c1 * r1 * (particles_best_position[i] - particles_position[i])
        social_velocity = c2 * r2 * (global_best_position - particles_position[i])
        particles_velocity[i] = w * particles_velocity[i] + cognitive_velocity + social_velocity
        particles_position[i] = np.clip(particles_position[i] + particles_velocity[i], 0, k - 1)

group_assignment = [np.argmax([np.sum(particles_position[:, j] == i) for i in range(k)]) for j in range(N)]
group_diversity = [np.sum(np.abs(student_marks[group_assignment == i] - np.mean(student_marks[group_assignment == i])))
                   for i in range(k)]

print("Group assignment number of each student:", group_assignment)
print("Diversity value in each group:", group_diversity)
print("Global best fitness (total diversity):", global_best_fitness)
