# recursion error
from collections import deque
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def find_par(x, arr):
    if par[x] != x:
        arr.append(par[x])
        find_par(par[x], arr)


n = int(input())
par = [0 for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

par[1] = 1  # 루트
que = deque()
que.append(1)
while que:
    v = que.popleft()
    for node in graph[v]:
        if par[node]:
            continue
        par[node] = v
        que.append(node)

m = int(input())
for i in range(m):
    a, b = map(int, input().split())
    par_arr_a = [a]
    par_arr_b = [b]
    find_par(a, par_arr_a)
    find_par(b, par_arr_b)
    a_length = len(par_arr_a)
    b_length = len(par_arr_b)
    par_arr_a = par_arr_a[::-1]
    par_arr_b = par_arr_b[::-1]
    result = 1
    for i in range(min(a_length, b_length)):
        if par_arr_a[i] != par_arr_b[i]:
            break
        result = par_arr_a[i]
    print(result)
