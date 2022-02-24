# 토너먼트 카드게임
def tournament(i, j):   # 대진 짜기
    if i == j:            # 1명 남았을 경우 => 가위바위보 하러 간다
        return i
    else:               # 조 편성하기
        left = tournament(i, (i+j)//2)
        right = tournament((i+j)//2+1, j)
        return win(left, right)


def win(i, j):              # 가위바위보
    if arr[i] == arr[j]:    # 비긴 경우
        return i
    elif arr[i] == 1:       # 가위를 낸 경우
        if arr[j] == 2:     # 가위 vs 바위
            return j
        else:               # 가위 vs 보
            return i
    elif arr[i] == 2:       # 바위를 낸 경우
        if arr[j] == 1:     # 바위 vs 가위
            return i
        else:               # 바위 vs 보
            return j
    else:                   # 보를 낸 경우
        if arr[j] == 1:     # 보 vs 가위
            return j
        else:               # 보 vs 바위
            return i


T = int(input())
for tc in range(1, 1 + T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    print(f'#{tc} {tournament(1, N)}')