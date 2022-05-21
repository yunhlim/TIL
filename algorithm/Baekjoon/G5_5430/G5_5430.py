t = int(input())
for _ in range(t):
    p = input()
    n = int(input())
    arr = input()[1:-1].split(',')      # 배열로 바꾼다.
    
    s = 0   # 시작 인덱스
    e = n   # 마지막 인덱스
    r = 0   # 회전(홀짝 판별)
    for x in p:
        if x == 'R':
            r ^= 1
        else:
            if r:   # 홀수번 회전 뒤를 지운다.
                e -= 1
            else:       # 짝수번 회전 앞을 지운다.
                s += 1
    if s > e:      # 숫자 개수보다 더 지운 경우
        print('error')
    elif r:
        print('[' + ','.join(arr[s:e][::-1]) + ']')     # 원하는 출력형태로 변경
    else:
        print('[' + ','.join(arr[s:e]) + ']')