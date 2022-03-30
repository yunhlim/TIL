import sys
input = sys.stdin.readline


def check(x):   # x이하의 정수들의 개수가 홀수인지 체크
    cnt = 0
    for a, c, b in arr:
        if a <= x:      # a보다 크거나 같은 경우만 있다.
            cnt += min((c - a), (x - a)) // b + 1       # 몫을 활용
    if cnt % 2:         # 홀수면 True
        return True
    else:
        return False

def counting(x):   # x의 개수를 찾는다.
    cnt = 0
    for a, c, b in arr:
        if x < a or x > c:
            continue
        if (x - a) % b == 0:    # 모듈러 연산으로 값이 있는지 확인
            cnt += 1
    return cnt

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

s, e = 1, 2_147_483_647
ans = -1
while s <= e:               # 이진탐색
    mid = (s + e) // 2
    if check(mid):          # x이하의 정수들의 개수 홀수인 것중 가장 작은 정수를 찾는다.
        ans = mid           # 매개변수 탐색
        e = mid - 1
    else:
        s = mid + 1
if ans == -1:               # 없으면 NOTHING 출력
    print('NOTHING')
else:
    print(ans, counting(ans))