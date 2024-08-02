path = []

def print_m(matrix):
    for row in matrix:
        for element in row:
            print(element, end="\t")
        print()

def findindex(m, a):
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] == a:
                return i, j
    return -1, -1

def graph(m, g, x, visited):
    t = tuple(map(tuple, m))
    if t == x:
        return True
    b = findindex(m, 0)
    i = b[0]
    j = b[1]

    for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
        if 0 <= i + dx < 3 and 0 <= j + dy < 3:
            k = [row[:] for row in m]
            k[i + dx][j + dy], k[i][j] = k[i][j], k[i + dx][j + dy]
            g[t] = k
            if k == x:
                path.append(k)
                return True
            if tuple(map(tuple, k)) not in visited:
                g[t] = k
                visited.add(tuple(map(tuple, k)))
                if graph(k, g, x, visited):
                    return True
    return False

r = 3
c = 3
m = []

print("The numbers to solve (Give empty space as 0):")
for i in range(r):
    b = []
    for j in range(c):
        a = int(input())
        b.append(a)
    m.append(b)
    print('\n')

print("Initial Matrix is :")
print_m(m)

g = {}
x = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
visited = set([tuple(map(tuple, m))])
path = [m]
if graph(m, g, x, visited):
    print("Solution found")
    for i in path:
        print_m(i)
        print()
    print("In ", len(path)-1, " moves")
else:
    print("Solution not found")
