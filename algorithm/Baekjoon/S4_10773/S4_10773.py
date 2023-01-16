import sys
input = sys.stdin.readline

n = int(input())
stack = []
for i in range(n):
    x = int(input())
    if x:     # 0이 아닌 경우
        stack.append(x)
    else:       # 0인 경우
        stack.pop()

print(sum(stack))