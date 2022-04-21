import sys
input = sys.stdin.readline


t = int(input())
dic = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10}
for _ in range(t):
    n = int(input())
    arr = [input().rstrip() for _ in range(n)]
    matrix = [[0] * 11 for _ in range(11)]
    for i in range(n):
        matrix[dic[arr[i][0]]][dic[arr[i][1]]] += 1
    total = 0
    for i in range(11):
        for j in range(11):
            if matrix[i][j] > 0:
                for i2 in range(i + 1, 11):
                    total += matrix[i][j] * matrix[i2][j]
                for j2 in range(j + 1, 11):
                    total += matrix[i][j] * matrix[i][j2]
    print(total)