def sortx(m,n,matrix):
    x=[]
    for i in range(m):
        for j in range(n):
            x.append(matrix[i][j])
    x.sort()
    k=0
    matrixx=[]
    for i in range(m):
        a=[]
        for j in range(n):
            a.append(x[k])
            k+=1
        matrixx.append(a)
    return matrixx
def addarray(m,n,matrix1,matrix2):
    M=[]
    for i in range(m):
        for j in range(n):
            x=matrix1[i][j]+matrix2[i][j]
            M.append(x)
    return M
def subarray(m,n,matrix1,matrix2):
    M=[]
    for i in range(m):
        for j in range(n):
            x=matrix1[i][j]-matrix2[i][j]
            M.append(x)
    return M
def mullarray(m1,n1,m2,matrix1,matrix2):
    M = [[0 for _ in range(n2)] for _ in range(m1)]
    for i in range(m1):
        for j in range(n1):
            for k in range(n1):
                M[i][j] += matrix1[i][k] * matrix2[k][j]
    return M

matrix1=[]
m1 = int(input("Enter no.of rows:"))
n1 = int(input("Enter no.of columns:"))

for i in range(m1):
    a=[]
    for j in range(n1):
        b=int(input())
        a.append(b)
    matrix1.append(a)
print(matrix1)
matrix2=[]
m2 = int(input("Enter no.of rows:"))
n2 = int(input("Enter no.of columns:"))

for i in range(m2):
    a=[]
    for j in range(n2):
        b=int(input())
        a.append(b)
    matrix2.append(a)
print(matrix2)
x=matrix1+matrix2
print('Concatenate two arrays.',x)

matrix_1=sortx(m1,n1,matrix1)
matrix_2=sortx(m2,n2,matrix2)
print("sorted arrays are:",matrix_1,matrix_2)
if m1==n1 and m2==n2:
    M1=addarray(m1,n1,matrix1,matrix2)
    print("Addition:",M1)
    M2=subarray(m1,n1,matrix1,matrix2)
    print("Subtraction:",M2)
else:
    print("Addition and Substraction not possible")

if n1==m2:
    M3 = mullarray(m1, n1,m2, matrix1, matrix2)
    print("Multiplication:", M3)
else:
    print("Multiplication not possible")