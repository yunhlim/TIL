# 종이붙이기
T = int(input())
memo = [0, 1, 3]    # 재귀 대신 DP 활용
for tc in range(1, T + 1):
    N = int(input()) // 10
    while N >= len(memo):   # 배열에 출력시킬 값이 없으면 출력시킬 수 있게 추가해준다.
        memo.append(memo[len(memo)-2] * 2 + memo[len(memo)-1])
    print(memo[N])