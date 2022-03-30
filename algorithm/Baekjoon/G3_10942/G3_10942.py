import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
palin = [[0] * n for _ in range(n)]     # 팰린드롬의 결과를 담을 배열
for i in range(n):          # 홀수일 때, i를 중심으로 한 칸씩 넓혀가며 팰린드롬인지 파악
    s = i
    e = i
    while s >= 0 and e < n:
        if arr[s] != arr[e]:    # 팰린드롬이 아니면 종료, i를 중심으로 하는 이후 값들도 무조건 팰린드롬이 아니다.
            break
        palin[s][e] = 1         # 팰린드롬이면 값을 넣어준다.
        s -= 1                  # 한 칸씩 양쪽으로 넓힌다.
        e += 1
for i in range(n):          # 짝수일 때, i + 0.5를 중심으로 한 칸씩 넓혀가며 팰린드롬인지 파악
    s = i
    e = i + 1
    while s >= 0 and e < n:
        if arr[s] != arr[e]:    # 팰린드롬이 아니면 종료
            break
        palin[s][e] = 1
        s -= 1                  # 한 칸씩 양쪽으로 넓힌다.
        e += 1
m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(palin[s - 1][e - 1])      # padding을 따로 넣지 않고 1씩 빼준 후 출력