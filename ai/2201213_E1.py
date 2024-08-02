from queue import PriorityQueue as pq

def valid(state):
    m, c, boat = state
    if m < 0 or m > 3 or c < 0 or c > 3:
        return False
    if m > 0 and m < c:
        return False
    if 3 - m < 3 - c and 3 - m > 0:
        return False
    return True

def successor_states(state):
    m, c, boat = state
    succ = []
    if boat:
        for i in range(3):
            for j in range(3):
                if 1 <= i + j <= 2:
                    next_state = (m - i, c - j, not boat)
                    if valid(next_state):
                        succ.append((next_state, i * 10 + 20 * j))
    else:
        for i in range(3):
            for j in range(3):
                if 1 <= i + j <= 2:
                    next_state = (m + i, c + j, not boat)
                    if valid(next_state):
                        succ.append((next_state, i * 10 + 20 * j))
    return succ

def UCS(goal_state):
    p = pq()
    start_state = (3, 3, True)
    visited = set()
    p.put((0, start_state))
    while not p.empty():
        cost, cstate = p.get()
        if cstate == goal_state:
            return cost
        visited.add(cstate)
        for next_state, c in successor_states(cstate):
            if next_state not in visited:
                p.put((cost + c, next_state))
    return -1

x = int(input("no.of missionaries: "))
y = int(input("no.of cannibals: "))
total_cost = UCS((x, y, False))
if total_cost == -1:
    print("Goal state can't be achieved.")
else:
    print("Minimum cost is:", total_cost)
