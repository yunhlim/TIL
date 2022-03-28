import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr_a = list(map(int, input().split()))
arr_b = list(map(int, input().split()))
visited = [0 for _ in range(7)]
cnt = 0
for i in range(n):                  # arr_a의 값들 중 7로 나눈 나머지 값들의 존재 유무를 visited에 표시
    if visited[arr_a[i] % 7] == 0:
        visited[arr_a[i] % 7] = 1
        cnt += 1                    # 총 몇 개의 표시를 하는지 확인(최대 7개)
    if cnt == 7:                    # 일곱 개면 더 이상 확인 X
        break

ssum, check = 0, 0                  # 마지막에 더해줄 값, 7로 나누어떨어지는지 확인해줄 값
for i in range(m):
    temp = 7 - (check + arr_b[i]) % 7 if (check + arr_b[i]) % 7 != 0 else 0     # 더해서 7의 배수가 되는지 확인할 값
    if visited[temp]:       # 더해서 7의 배수가 되는데 현재 그 수가 존재하는 경우
        if cnt == 1:        # 배열의 원소가 다 제거되면 연산을 취소
            continue
        visited[temp] = 0   # 동일한 나머지를 가지는 값들을 제거하기 위해 방문 표시를 0으로 변경
        cnt -= 1            # visited에 표시된 개수가 하나 줄어들었다.
    check = (check + arr_b[i]) % 7
    ssum += arr_b[i]        # 값을 더해준다.
    ssum %= 1_000_000_007   # 값을 10 ** 9 + 7로 나눈다.(모듈러 성질)

result = []
for i in range(n):
    if visited[arr_a[i] % 7]:   # 현재 값이 삭제되지 않았으면
        result.append((arr_a[i] + ssum) % 1_000_000_007)    # arr_b에서 더한 값을 더해준 후 10 ** 9 + 7로 나눈다.
print(len(result))
print(*result)