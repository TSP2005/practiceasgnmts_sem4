from collections import deque
path=[]
def print_m(matrix):
    for row in matrix:
        for element in row:
            print(element, end="\t")
        print()
def findindex(m, a):
    k = []
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j] == a:
                k.append(i)
                k.append(j)
    return k
def graph(m, g, x, visited):
    q = deque()
    q.append(m)

    while q:
        t = q.pop()
        p = tuple(map(tuple, t))
        path.append(t)
        if t == x:
            return True

        b = findindex(t, 0)
        i = b[0]
        j = b[1]

        pm = [
            (i - 1, j),
            (i + 1, j),
            (i, j - 1),
            (i, j + 1)
        ]

        for move in pm:
            ni, nj = move
            if 0 <= ni < 3 and 0 <= nj < 3:
                k = [row[:] for row in t]
                k[ni][nj], k[i][j] = k[i][j], k[ni][nj]
                if tuple(map(tuple, k)) not in visited:
                    g[p] = k
                    visited.add(tuple(map(tuple, k)))
                    q.append(k)
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
p = graph(m, g, x, visited)
count=0
if p:
    print("Solution found.")
    for i in path:
        print_m(i)
        count+=1
        print()
    print("In ",count," moves")
else:
    print("Solution not found.")
