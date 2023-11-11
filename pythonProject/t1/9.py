from random import randrange
def mean(matrix,n):
    for i in range(n):
        matrix[i][i]='*'

def sr(matrix,n):
    for i in range(n):
        matrix[n//2][i]='*'

def sur(matrix,n):
    for i in range(n):
        for j in range(n):
            if(i==n-j-1):
                matrix[i][j]='*'

def srr(matrix,n):
    for i in range(n):
        matrix[i][n//2]='*'

def solve(matrix,n):
    mean(matrix,n)
    sr(matrix,n)
    sur(matrix,n)
    srr(matrix,n)
n = randrange(5, 20, 2)
matrix=[]
for i in range(0,n):
    matrix.append([])
    for j in range(0,n):
        matrix[i].append('.')

solve(matrix,n)
for i in range(len(matrix)):
    print(''.join(matrix[i]))