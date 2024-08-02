import random
def f(x):
    return -x ** 2 + 4 * x
def hill_climbing(f, x_min, x_max, step_size, max_iter):
    current_x = random.uniform(x_min, x_max)
    current_value = f(current_x)

    for _ in range(max_iter):
        next_x = current_x + random.uniform(-step_size, step_size)
        next_x = max(x_min, min(next_x, x_max))
        next_value = f(next_x)

        if next_value > current_value:
            current_x = next_x
            current_value = next_value
        else:
            break

    return current_x, current_value


initial_values = [-10, -5, 0, 5, 10]
step_sizes = [0.1, 0.5, 1.0]

for initial_value in initial_values:
    for step_size in step_sizes:
        max_x, max_value = hill_climbing(f, -10, 10, step_size, 1000)
        print("Initial Value: {}, Step Size: {}, Max Value: {}, at x = {}".format(initial_value, step_size, max_value, max_x))
