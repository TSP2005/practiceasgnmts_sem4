matrix=[]
m = int(input("Enter no.of rows:"))
n = int(input("Enter no.of columns:"))

for i in range(m):
    a=[]
    for j in range(n):
        b=int(input())
        a.append(b)
    matrix.append(a)
print(matrix)
flatten = []
transpose= []
for i in range(m):
    a=[]
    for j in range(n):
        a.append(matrix[j][i])
    transpose.append(a)
print("transpose is :",transpose)
print("flatten matrix is:")
for i in matrix:
    for j in i:
        flatten.append(j)
print(flatten)