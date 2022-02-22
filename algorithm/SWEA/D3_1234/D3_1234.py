# 비밀번호
for tc in range(1, 11):
    N, arr = input().split()
    arr = list(arr)
    s = 0
    while s < len(arr): # 이전 값과 비교하여 없애고 없애면 하나 전 인덱스로 이동해 다시 확인
        if s and arr[s] == arr[s-1]:    # s가 0이 아닐 때 이전 값과 비교
            del arr[s], arr[s-1]    # 같을 땐 값을 지우고 이전 인덱스로 이동해 비교한다.
            s -= 1
        else:   # 다를 땐 다음 인덱스로 이동한다.
            s += 1
    print(f'#{tc} {"".join(arr)}')