from copy import deepcopy
import numpy as np
import time

def misplaced_tiles(puzzle, goal):
    mscost = np.sum(puzzle != goal) - 1
    if mscost > 0:
        return mscost
    else:
        return 0

def coordinates(puzzle):
    pos = np.array(range(9))
    for p, q in enumerate(puzzle):
        pos[q] = p
    return pos
puzzle = []
print(" Input values from 0-8 for start state ")
for i in range(0, 9):
    x = int(input("Enter value: "))
    puzzle.append(x)

# User input of goal state
goal = []
print(" Input values from 0-8 for goal state ")
for i in range(0, 9):
    x = int(input("Enter value: "))
    goal.append(x)

start_time = time.time()
result = gbsf(puzzle, goal)
end_time = time.time()

print("Total states explored:", len(result))
print("Time taken:", end_time - start_time, "seconds")